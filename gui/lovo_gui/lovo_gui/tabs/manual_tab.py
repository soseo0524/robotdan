"""
Manual 탭
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTabWidget
from lovo_gui.widgets.robot_dashboard import RobotDashboardWidget
from lovo_gui.widgets.camera_dialog import CameraWidget
from lovo_gui.widgets.amr_dashboard import AMRDashboardWidget


class ManualTab(QWidget):
    """Manual 탭 - 로봇별 제어"""
    
    def __init__(self, config_manager, parent=None):
        super().__init__(parent)
        self.config_manager = config_manager
        self.robot_tab_widgets = {}
        self.dashboard_widgets = {}  # robot_id: RobotDashboardWidget or AMRDashboardWidget
        self.camera_widgets = {}  # robot_id: CameraWidget
        self._setup_ui()
    
    def _setup_ui(self):
        """UI 구성"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.manual_tabs = QTabWidget()
        self.manual_tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.manual_tabs.setStyleSheet("QTabBar::tab { min-width: 150px; min-height: 40px; font-size: 16px; }")
        
        # 로봇별 탭 생성
        robots = self.config_manager.get_robots()
        for idx, robot in enumerate(robots):
            name = robot.get("name", f"로봇 {idx+1}")
            robot_id = robot.get("id", f"robot{idx+1}")
            
            # 탭 레이아웃: 왼쪽 카메라 + 오른쪽 대시보드
            tab_widget = QWidget()
            tab_layout = QHBoxLayout(tab_widget)
            tab_layout.setContentsMargins(0, 0, 0, 0)
            tab_layout.setSpacing(5)
            
            # 왼쪽: 카메라 위젯
            camera_widget = CameraWidget(name)
            self.camera_widgets[robot_id] = camera_widget
            tab_layout.addWidget(camera_widget, stretch=1)
            
            # 오른쪽: 대시보드 (로봇팔 또는 AMR)
            if idx < 2:
                # 1, 2번: 로봇팔 대시보드
                dashboard = RobotDashboardWidget(name, robot_id)
                self.dashboard_widgets[robot_id] = dashboard
                tab_layout.addWidget(dashboard, stretch=2)
            else:
                # 3, 4번: AMR 대시보드
                dashboard = AMRDashboardWidget(name, robot_id)
                self.dashboard_widgets[robot_id] = dashboard
                tab_layout.addWidget(dashboard, stretch=2)
            
            tab_index = self.manual_tabs.addTab(tab_widget, name)
            self.robot_tab_widgets[robot_id] = tab_index
        
        layout.addWidget(self.manual_tabs)
    
    def connect_controllers(self, communication_tab):
        """Communication 탭에서 컨트롤러 연결"""
        for robot_id, dashboard in self.dashboard_widgets.items():
            # 로봇 컨트롤러 연결
            controller = communication_tab.get_robot_controller(robot_id)
            if controller:
                dashboard.set_controller(controller)
            
            # 카메라 컨트롤러 연결
            camera_controller = communication_tab.get_camera_controller(robot_id)
            if camera_controller and robot_id in self.camera_widgets:
                self.camera_widgets[robot_id].set_camera_controller(camera_controller)
    
    def update_tab_name(self, robot_id, new_name):
        """탭 이름 업데이트"""
        tab_index = self.robot_tab_widgets.get(robot_id)
        if tab_index is not None:
            self.manual_tabs.setTabText(tab_index, new_name)
