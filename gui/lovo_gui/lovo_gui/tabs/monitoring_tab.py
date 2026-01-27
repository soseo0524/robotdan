"""
Monitoring 탭
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel
from PyQt6.QtCore import Qt, QTimer


class MonitoringTab(QWidget):
    """Monitoring 탭 - 시스템 모니터링 맵"""
    
    def __init__(self, comm_manager, parent=None):
        super().__init__(parent)
        self.comm_manager = comm_manager
        self.robot_markers = {} # {robot_role: QLabel}
        
        self._setup_ui()
        
        # 주기적 업데이트 타이머 (1초)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_map)
        self.timer.start(1000)
    
    def update_map(self):
        """API 서버에서 데이터를 가져와 지도 위 로봇 위치 업데이트"""
        robots_data = self.comm_manager.fetch_robots()
        
        for r_data in robots_data:
            # 운송 로봇만 지도에 표시 (좌표가 있는 경우)
            if r_data.get('robot_kind') == 'PINKY':
                role = r_data.get('robot_role')
                x = r_data.get('pose_x', 0)
                y = r_data.get('pose_y', 0)
                
                # 마커가 없으면 생성
                if role not in self.robot_markers:
                    marker = QLabel(self.map_frame)
                    marker.setFixedSize(30, 30)
                    marker.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    marker.setText("🤖")
                    marker.setStyleSheet("""
                        background-color: #2196F3;
                        color: white;
                        border-radius: 15px;
                        font-size: 16px;
                    """)
                    marker.show()
                    self.robot_markers[role] = marker
                
                # 위치 업데이트 (0~100 좌표계를 800x600 픽셀로 변환)
                # 예: x=10 -> 80px, y=20 -> 120px
                pixel_x = int(x * 7.5) + 25 # 약간의 오프셋
                pixel_y = int(y * 5.5) + 25
                self.robot_markers[role].move(pixel_x, pixel_y)

    def _setup_ui(self):
        """UI 구성"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 모니터링 맵 프레임
        self.map_frame = QFrame()
        self.map_frame.setFixedSize(800, 600) # 가시성을 위해 현실적인 크기로 조정
        self.map_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
            }
        """)
        
        # 맵 배경 그리드 레이블 (임시)
        bg_label = QLabel("Factory Floor Map", self.map_frame)
        bg_label.setGeometry(0, 0, 800, 30)
        bg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bg_label.setStyleSheet("color: #adb5bd; font-weight: bold;")
        
        layout.addWidget(self.map_frame, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
