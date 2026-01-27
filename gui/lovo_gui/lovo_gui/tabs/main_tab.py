"""
Main 탭
"""
from PyQt6.QtWidgets import (
    QWidget, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit,
    QGridLayout, QPushButton, QSizePolicy
)
from PyQt6.QtCore import Qt, QTimer
from lovo_gui.constants import MAIN_SYSTEM_MAP, MAIN_ORDER_LOG, MAIN_ROBOT_GRID, MAIN_CAMERA_VIEW


class MainTab(QWidget):
    """Main 탭 - 시스템 맵, 주문 로그, 로봇 상태, 카메라 뷰"""
    
    def __init__(self, config_manager, comm_manager, parent=None):
        super().__init__(parent)
        self.config_manager = config_manager
        self.comm_manager = comm_manager
        self.camera_title = None
        self.camera_view_label = None
        
        # UI 업데이트를 위한 참조 저장
        self.robot_widgets = {} # {robot_role: {battery: label, state: label, indicator: frame}}
        
        self._setup_ui()
        
        # 주기적 업데이트를 위한 타이머 (2초)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(2000)
    
    def update_data(self):
        """API 서버에서 데이터를 가져와 UI 업데이트"""
        # 1. 로봇 데이터 업데이트
        robots_data = self.comm_manager.fetch_robots()
        for r_data in robots_data:
            role = r_data.get('robot_role')
            if role in self.robot_widgets:
                widgets = self.robot_widgets[role]
                
                # 배터리 업데이트
                battery = r_data.get('battery_percent', 0)
                widgets['battery'].setText(f"{int(battery)}%")
                
                # 상태 업데이트 (좌표 또는 작업 상태)
                state = r_data.get('action_state', 'IDLE')
                if r_data.get('robot_kind') == 'PINKY':
                    pos_x = r_data.get('pose_x', 0)
                    pos_y = r_data.get('pose_y', 0)
                    widgets['state'].setText(f"{state} ({pos_x:.1f}, {pos_y:.1f})")
                else:
                    widgets['state'].setText(state)
                
                # 표시등 (색상 변경)
                color_map = {
                    'IDLE': '#28a745',          # Green
                    'CHARGING': '#ffc107',      # Yellow
                    'ERROR': '#dc3545',         # Red
                    'OFFLINE': '#6c757d',       # Gray
                    'TRANSPORTING': '#007bff',   # Blue
                }
                color = color_map.get(state, '#007bff')
                widgets['indicator'].setStyleSheet(f"background-color: {color}; border-radius: 7px; border: 1px solid #333;")

        # 2. 주문 로그 업데이트
        orders_data = self.comm_manager.fetch_orders()
        if orders_data:
            log_text = ""
            for o in orders_data:
                time_str = o.get('ordered_at', '').split('T')[-1].split('.')[0]
                log_text += f"[{time_str}] {o['customer_name']}: {o['furniture_name']} x{o['quantity']} ({o['status']})\n"
            
            # 이전 로그와 다를 때만 업데이트 (커서 유지 등 UX 고려)
            if self.order_log_viewer.toPlainText() != log_text.strip():
                self.order_log_viewer.setPlainText(log_text.strip())

    def _setup_ui(self):
        """UI 구성"""
        # 좌상단: 시스템 맵
        self._create_system_map()
        
        # 우상단: 주문 로그
        self._create_order_log()
        
        # 좌하단: 로봇 상태 그리드
        self._create_robot_grid()
        
        # 우하단: 카메라 뷰
        self._create_camera_view()
    
    def _create_system_map(self):
        """시스템 맵"""
        x, y, w, h = MAIN_SYSTEM_MAP
        system_map = QFrame(self)
        system_map.setGeometry(x, y, w, h)
        system_map.setStyleSheet("QFrame { background-color: #e8e8e8; border: none; }")
        
        layout = QVBoxLayout(system_map)
        layout.addWidget(QLabel("시스템 맵", alignment=Qt.AlignmentFlag.AlignCenter))
    
    def _create_order_log(self):
        """주문 로그"""
        x, y, w, h = MAIN_ORDER_LOG
        order_log_frame = QFrame(self)
        order_log_frame.setGeometry(x, y, w, h)
        order_log_frame.setStyleSheet("QFrame { background-color: #f5f5f5; border: none; }")
        
        layout = QVBoxLayout(order_log_frame)
        layout.setContentsMargins(5, 5, 5, 5)
        
        title = QLabel("주문 로그")
        title.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        self.order_log_viewer = QTextEdit()
        self.order_log_viewer.setReadOnly(True)
        self.order_log_viewer.setStyleSheet("""
            background-color: white;
            color: #333;
            font-family: Consolas;
            font-size: 11px;
            border: 1px solid #ccc;
        """)
        layout.addWidget(self.order_log_viewer)
    
    def _create_robot_grid(self):
        """로봇 상태 그리드"""
        x, y, w, h = MAIN_ROBOT_GRID
        grid_container = QWidget(self)
        grid_container.setGeometry(x, y, w, h)
        grid_container.setStyleSheet("background-color: white;")
        
        grid_layout = QGridLayout(grid_container)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        
        # 헤더
        headers = ["로봇 이름", "서버 연결", "배터리", "현재 상태", "캠"]
        header_widths = [120, 100, 80, 200, 80]
        
        for col, header in enumerate(headers):
            header_label = QLabel(header)
            header_label.setStyleSheet("""
                background-color: #4a4a4a; color: white;
                font-weight: bold; font-size: 13px;
                padding: 10px; border: 1px solid #333;
            """)
            header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid_layout.addWidget(header_label, 0, col)
            grid_layout.setColumnMinimumWidth(col, header_widths[col])
        
        # 로봇 매핑 정보 (DB role -> GUI 이름)
        role_map = {
            'ARM_1': "상차 로봇팔",
            'ARM_2': "하차 로봇팔",
            'PINKY_TRANS_1': "운송 로봇 1",
            'PINKY_TRANS_2': "운송 로봇 2",
            'PINKY_PATROL': "청소 로봇"
        }
        
        for row, (role, name) in enumerate(role_map.items(), start=1):
            # 로봇 이름
            name_label = QLabel(name)
            name_label.setStyleSheet("background-color: #f0f0f0; color: black; padding: 8px; border: 1px solid #ccc;")
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid_layout.addWidget(name_label, row, 0)
            
            # 서버 연결 표시등
            status_widget = QWidget()
            status_layout = QHBoxLayout(status_widget)
            indicator = QFrame()
            indicator.setFixedSize(14, 14)
            indicator.setStyleSheet("background-color: #6c757d; border-radius: 7px; border: 1px solid #333;")
            status_layout.addWidget(indicator, alignment=Qt.AlignmentFlag.AlignCenter)
            status_widget.setStyleSheet("background-color: white; border: 1px solid #ccc;")
            grid_layout.addWidget(status_widget, row, 1)
            
            # 배터리 잔량
            battery_label = QLabel("-")
            battery_label.setStyleSheet("background-color: white; color: black; padding: 8px; border: 1px solid #ccc;")
            battery_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid_layout.addWidget(battery_label, row, 2)
            
            # 현재 상태
            state_label = QLabel("Loading...")
            state_label.setStyleSheet("background-color: white; color: black; padding: 8px; border: 1px solid #ccc;")
            state_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid_layout.addWidget(state_label, row, 3)
            
            # 캠 버튼
            cam_btn = QPushButton("📷")
            cam_btn.setFixedSize(60, 30)
            cam_btn.setStyleSheet("background-color: #007bff; color: white; font-weight: bold; border-radius: 4px;")
            cam_btn.clicked.connect(lambda checked, n=name: self.show_camera_view({'name': n}))
            
            btn_container = QWidget()
            btn_container.setStyleSheet("background-color: white; border: 1px solid #ccc;")
            btn_layout = QHBoxLayout(btn_container)
            btn_layout.setContentsMargins(0,0,0,0)
            btn_layout.addWidget(cam_btn, alignment=Qt.AlignmentFlag.AlignCenter)
            grid_layout.addWidget(btn_container, row, 4)
            
            # 업데이트를 위해 참조 저장
            self.robot_widgets[role] = {
                'battery': battery_label,
                'state': state_label,
                'indicator': indicator
            }
    
    def _create_camera_view(self):
        """카메라 뷰"""
        x, y, w, h = MAIN_CAMERA_VIEW
        self.camera_view_frame = QFrame(self)
        self.camera_view_frame.setGeometry(x, y, w, h)
        self.camera_view_frame.setStyleSheet("""
            QFrame {
                background-color: #2a2a2a;
                border: 2px solid #555;
                border-radius: 4px;
            }
        """)
        
        layout = QVBoxLayout(self.camera_view_frame)
        layout.setContentsMargins(0, 5, 0, 5)
        layout.setSpacing(5)
        
        self.camera_title = QLabel("카메라 선택 대기 중...")
        self.camera_title.setStyleSheet("font-size: 13px; font-weight: bold; color: #999;")
        self.camera_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.camera_title.setFixedHeight(20)
        layout.addWidget(self.camera_title)
        
        self.camera_view_label = QLabel("캠 버튼을 눌러 카메라를 선택하세요")
        self.camera_view_label.setFixedSize(420, 270)
        self.camera_view_label.setStyleSheet(
            "background-color: black; border: 1px solid #444; border-radius: 4px; color: #666;"
        )
        self.camera_view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.camera_view_label)
    
    def show_camera_view(self, robot):
        """카메라 뷰 표시"""
        robot_name = robot.get("name", "로봇")
        self.camera_title.setText(f"{robot_name} - 카메라 뷰")
        self.camera_view_label.setText("카메라 스트리밍 대기 중...")
