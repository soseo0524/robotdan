"""
카메라 뷰 위젯
"""
import time
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap


class CameraWidget(QWidget):
    """카메라 뷰 위젯"""
    
    def __init__(self, robot_name, parent=None):
        super().__init__(parent)
        self.robot_name = robot_name
        self.camera_controller = None
        
        self._setup_ui()
    
    def _setup_ui(self):
        """UI 구성"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        vision_group = QGroupBox(f"📷 {self.robot_name} Camera")
        vision_layout = QVBoxLayout()
        
        # 카메라 뷰
        self.cam_view = QLabel("카메라 대기 중...")
        self.cam_view.setFixedSize(640, 480)
        self.cam_view.setStyleSheet("background-color: black; color: white; border: 2px solid #555; border-radius: 4px;")
        self.cam_view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vision_layout.addWidget(self.cam_view)
        
        # 컨트롤 버튼
        btn_layout = QHBoxLayout()
        
        self.btn_connect = QPushButton("🔌 CONNECT")
        self.btn_connect.setFixedHeight(40)
        self.btn_connect.clicked.connect(self._camera_connect)
        btn_layout.addWidget(self.btn_connect)
        
        self.btn_disconnect = QPushButton("❌ DISCONNECT")
        self.btn_disconnect.setFixedHeight(40)
        self.btn_disconnect.setEnabled(False)
        self.btn_disconnect.clicked.connect(self._camera_disconnect)
        btn_layout.addWidget(self.btn_disconnect)
        
        self.btn_capture = QPushButton("📸 CAPTURE")
        self.btn_capture.setFixedHeight(40)
        self.btn_capture.setEnabled(False)
        self.btn_capture.clicked.connect(self._camera_capture)
        btn_layout.addWidget(self.btn_capture)
        
        vision_layout.addLayout(btn_layout)
        vision_group.setLayout(vision_layout)
        layout.addWidget(vision_group)
        layout.addStretch()
    
    def set_camera_controller(self, camera_controller):
        """카메라 컨트롤러 설정 및 Signal 연결"""
        self.camera_controller = camera_controller
        
        if camera_controller:
            camera_controller.frame_updated.connect(self.update_camera_frame)
            camera_controller.connection_changed.connect(self.on_camera_connection_changed)
    
    def _camera_connect(self):
        """카메라 연결"""
        if self.camera_controller:
            self.camera_controller.start()
    
    def _camera_disconnect(self):
        """카메라 연결 해제"""
        if self.camera_controller:
            self.camera_controller.stop()
    
    def _camera_capture(self):
        """카메라 캡처"""
        if self.camera_controller:
            filename = f"capture_{self.robot_name}_{int(time.time())}.jpg"
            self.camera_controller.capture(filename)
            print(f"📸 캡처 저장: {filename}")
    
    def update_camera_frame(self, frame):
        """카메라 프레임 업데이트"""
        import cv2
        
        # OpenCV BGR → RGB 변환
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        
        # QImage 생성
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        
        # QLabel 크기에 맞게 스케일링
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(
            self.cam_view.width(), 
            self.cam_view.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        
        self.cam_view.setPixmap(scaled_pixmap)
    
    def on_camera_connection_changed(self, connected):
        """카메라 연결 상태 변경"""
        if connected:
            self.btn_connect.setEnabled(False)
            self.btn_disconnect.setEnabled(True)
            self.btn_capture.setEnabled(True)
            self.cam_view.setText("")
        else:
            self.btn_connect.setEnabled(True)
            self.btn_disconnect.setEnabled(False)
            self.btn_capture.setEnabled(False)
            self.cam_view.clear()
            self.cam_view.setText("카메라 연결 끊김")
