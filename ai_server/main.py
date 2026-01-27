from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import numpy as np
import time
import socket
import threading
import cv2

app = FastAPI(title="LOVO AI Analysis Server")

# --- UDP Video Receiver Logic ---
class VideoState:
    def __init__(self):
        self.latest_frame = None
        self.lock = threading.Lock()
        self.robot_ip = "192.168.0.48" # From user metadata
        self.udp_port = 9540
        self.command_port = 9541

video_state = VideoState()

def udp_receiver_task():
    """Background task to receive UDP JPEG frames on port 9540."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", video_state.udp_port))
    sock.settimeout(2.0)
    
    # Send START command to robot (Matches GUI logic)
    print(f"Sending START to {video_state.robot_ip}:{video_state.command_port}")
    try:
        cmd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cmd_sock.sendto(b"START", (video_state.robot_ip, video_state.command_port))
    except Exception as e:
        print(f"Failed to send START: {e}")

    print(f"UDP Video Receiver listening on port {video_state.udp_port}...")
    
    while True:
        try:
            data, addr = sock.recvfrom(65507)
            
            # Simple direct JPEG decoding (Matches GUI CameraController)
            nparr = np.frombuffer(data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if frame is not None:
                with video_state.lock:
                    video_state.latest_frame = frame
        except socket.timeout:
            continue 
        except Exception as e:
            print(f"UDP Receiver Error: {e}")

# Start the UDP thread on startup
@app.on_event("startup")
async def startup_event():
    thread = threading.Thread(target=udp_receiver_task, daemon=True)
    thread.start()

def generate_video_stream():
    """Generator for MJPEG stream."""
    while True:
        with video_state.lock:
            if video_state.latest_frame is None:
                # Send a blank placeholder if no frame yet
                img = np.zeros((480, 640, 3), dtype=np.uint8)
                cv2.putText(img, "Waiting for Robot 2...", (150, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                placeholder = img
            else:
                placeholder = video_state.latest_frame
        
        _, jpeg = cv2.imencode('.jpg', placeholder)
        if jpeg is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        time.sleep(0.03) # ~30 FPS

@app.get("/api/video/feed")
async def video_feed():
    """Endpoint for MJPEG stream."""
    return StreamingResponse(generate_video_stream(), media_type="multipart/x-mixed-replace; boundary=frame")


# --- Original AI Logic ---
class InferenceRequest(BaseModel):
    data: List[float]
    model_type: str = "demand_forecast"

class InferenceResponse(BaseModel):
    prediction: List[float]
    latency_ms: float
    model_version: str

@app.get("/")
def read_root():
    return {"message": "LOVO AI Server is running"}

@app.post("/predict", response_model=InferenceResponse)
def predict(request: InferenceRequest):
    start_time = time.time()
    input_array = np.array(request.data)
    prediction = (input_array * 1.1).tolist()
    latency = (time.time() - start_time) * 1000
    return InferenceResponse(
        prediction=prediction,
        latency_ms=latency,
        model_version="1.0.0-alpha"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
