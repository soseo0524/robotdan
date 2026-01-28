from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional, Dict
import numpy as np
import time
import socket
import threading
import cv2
from collections import deque
from ultralytics import YOLO

app = FastAPI(title="LOVO Multi-Robot AI Analysis Server")

# --- Model & Robot Configuration ---
ROBOT_CONFIG = {
    "robot1": {"port": 9511, "model": "Model_A", "name": "상차 로봇"},
    "robot2": {"port": 9521, "model": "Model_A", "name": "하차 로봇"},
    "robot3": {"port": 9541, "model": "Model_B", "name": "청소 로봇 (Pinky)"},
}

# --- State Management ---
class RobotState:
    def __init__(self, robot_id, config):
        self.robot_id = robot_id
        self.name = config["name"]
        self.port = config["port"]
        self.model_type = config["model"]
        
        self.latest_frame = None
        self.processed_frame = None
        self.inference_result = {"status": "Waiting for data"}
        self.lock = threading.Lock()
        
        # Performance Metrics
        self.receive_count = 0
        self.inference_count = 0
        self.receive_fps = 0.0
        self.inference_fps = 0.0
        self.latency_ms = 0.0
        
        self.last_receive_time = time.time()
        self.last_inference_time = time.time()
        self.fps_calc_time = time.time()

    def update_receive_stats(self):
        self.receive_count += 1
        now = time.time()
        if now - self.fps_calc_time > 1.0:
            self.receive_fps = self.receive_count / (now - self.fps_calc_time)
            self.inference_fps = self.inference_count / (now - self.fps_calc_time)
            self.receive_count = 0
            self.inference_count = 0
            self.fps_calc_time = now

class RobotManager:
    def __init__(self, configs):
        self.robots: Dict[str, RobotState] = {
            rid: RobotState(rid, cfg) for rid, cfg in configs.items()
        }
        # Load Models
        self.model_a = YOLO("models/yolov8n.pt")      # 상차/하차용
        self.model_b = YOLO("models/yolov8n-seg.pt")  # 핑키 세그멘테이션용
        print("YOLO Models loaded successfully.")

    def get_robot(self, robot_id) -> Optional[RobotState]:
        return self.robots.get(robot_id)

manager = RobotManager(ROBOT_CONFIG)

# --- UDP Receiver Task ---
def udp_receiver_task(robot_state: RobotState):
    """Independent UDP Receiver for each robot port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(("0.0.0.0", robot_state.port))
        sock.settimeout(1.0)
        print(f"Receiver started for {robot_state.robot_id} on port {robot_state.port}")
    except Exception as e:
        print(f"Error binding port {robot_state.port} for {robot_state.robot_id}: {e}")
        return

    while True:
        try:
            data, addr = sock.recvfrom(65507)
            nparr = np.frombuffer(data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if frame is not None:
                with robot_state.lock:
                    robot_state.latest_frame = frame
                robot_state.update_receive_stats()
        except socket.timeout:
            continue
        except Exception as e:
            print(f"UDP Error ({robot_state.robot_id}): {e}")

# --- Inference Worker Task ---
def inference_worker_task():
    """Central scheduler for inference with load control."""
    INFERENCE_FPS_CAP = 10.0
    MIN_INTERVAL = 1.0 / INFERENCE_FPS_CAP

    while True:
        for robot_id, state in manager.robots.items():
            now = time.time()
            # 1. Load Control: Check if enough time has passed for this robot
            if now - state.last_inference_time < MIN_INTERVAL:
                continue

            # 2. Get latest frame
            frame_to_process = None
            with state.lock:
                if state.latest_frame is not None:
                    # In real app, we might check if this frame is "new"
                    frame_to_process = state.latest_frame.copy()
            
            if frame_to_process is not None:
                start_time = time.time()
                
                # 3. Actual YOLO Inference
                try:
                    target_model = manager.model_a if state.model_type == "Model_A" else manager.model_b
                    # Run inference (stream=False, we process one by one here)
                    results = target_model.predict(frame_to_process, verbose=False, conf=0.3)
                    
                    if results and len(results) > 0:
                        processed_frame = results[0].plot() # Annotated frame
                        
                        # Extract classes/names
                        names = results[0].names
                        detected_objects = []
                        if results[0].boxes is not None:
                            for box in results[0].boxes:
                                cls_id = int(box.cls[0])
                                conf = float(box.conf[0])
                                detected_objects.append({"class": names[cls_id], "conf": round(conf, 2)})
                    else:
                        processed_frame = frame_to_process.copy()
                        detected_objects = []

                except Exception as e:
                    print(f"Inference Error on {robot_id}: {e}")
                    processed_frame = frame_to_process.copy()
                    detected_objects = ["Error"]

                # 4. Save results independently
                with state.lock:
                    state.processed_frame = processed_frame
                    state.inference_result = {
                        "robot": state.robot_id,
                        "model": state.model_type,
                        "objects": detected_objects,
                        "timestamp": time.time()
                    }
                
                state.inference_count += 1
                state.latency_ms = (time.time() - start_time) * 1000
                state.last_inference_time = time.time()
        
        time.sleep(0.01) # Yield CPU

# --- App Lifecycle ---
@app.on_event("startup")
async def startup_event():
    # Start receivers for all robots
    for robot_id, state in manager.robots.items():
        t = threading.Thread(target=udp_receiver_task, args=(state,), daemon=True)
        t.start()
    
    # Start inference scheduler
    t_inf = threading.Thread(target=inference_worker_task, daemon=True)
    t_inf.start()

# --- API Routes ---
def generate_mjpeg_stream(robot_id, use_overlay=False):
    """Generator for MJPEG stream (Raw or Processed)."""
    while True:
        state = manager.get_robot(robot_id)
        if not state: break
        
        display_frame = None
        with state.lock:
            if use_overlay:
                display_frame = state.processed_frame if state.processed_frame is not None else state.latest_frame
            else:
                display_frame = state.latest_frame
        
        if display_frame is None:
            # Placeholder
            display_frame = np.zeros((480, 640, 3), dtype=np.uint8)
            cv2.putText(display_frame, f"No Signal: {robot_id}", (150, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        _, jpeg = cv2.imencode('.jpg', display_frame)
        if jpeg is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        time.sleep(0.05) # ~20 FPS display limit

@app.get("/api/video/{robot_id}")
async def video_feed(robot_id: str):
    if robot_id not in manager.robots:
        raise HTTPException(status_code=404, detail="Robot not found")
    return StreamingResponse(generate_mjpeg_stream(robot_id, use_overlay=False), 
                             media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/api/video/{robot_id}/overlay")
async def video_overlay_feed(robot_id: str):
    if robot_id not in manager.robots:
        raise HTTPException(status_code=404, detail="Robot not found")
    return StreamingResponse(generate_mjpeg_stream(robot_id, use_overlay=True), 
                             media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/api/infer/{robot_id}/latest")
async def get_latest_inference(robot_id: str):
    state = manager.get_robot(robot_id)
    if not state:
        raise HTTPException(status_code=404, detail="Robot not found")
    return state.inference_result

@app.get("/api/status")
async def get_status():
    """Full system status monitor."""
    status = {}
    for rid, s in manager.robots.items():
        status[rid] = {
            "name": s.name,
            "port": s.port,
            "model": s.model_type,
            "receive_fps": round(s.receive_fps, 2),
            "inference_fps": round(s.inference_fps, 2),
            "latency_ms": round(s.latency_ms, 2),
            "is_active": (time.time() - s.last_receive_time) < 5.0
        }
    return status

@app.get("/")
def read_root():
    return {"message": "LOVO Multi-Robot AI Server is running", "robots": list(ROBOT_CONFIG.keys())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
