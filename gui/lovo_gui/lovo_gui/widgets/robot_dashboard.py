"""
로봇팔 대시보드 위젯
"""
import time
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGroupBox,
    QGridLayout, QScrollArea, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QImage, QPixmap

# --- 공통 스타일 상수 ---
LABEL_WIDTH = 70      # Axis 라벨 (J1, X 등) 너비
JOG_ZONE_WIDTH = 130  # Jog 버튼+입력창 영역 너비
VALUE_WIDTH = 70      # 값 표시창 너비
MEM_WIDTH = 65        # 메모리(Pos1~5) 표시창 너비


class RobotDashboardWidget(QWidget):
    """로봇팔 제어 대시보드 위젯"""
    
    def __init__(self, robot_name, robot_key, parent=None):
        super().__init__(parent)
        self.robot_name = robot_name
        self.robot_key = robot_key
        self.main_font = QFont("Arial", 11, QFont.Weight.Bold)
        
        # 컨트롤러
        self.controller = None  # RobotArmController
        
        # UI 위젯 참조
        self.target_labels = [None] * 6
        self.actual_labels = [None] * 6
        self.error_labels = [None] * 6
        self.factor_inputs = [None] * 6
        self.jog_step_inputs = [None] * 6
        
        self.pose_target_labels = [None] * 6
        self.pose_actual_labels = [None] * 6
        self.pose_error_labels = [None] * 6
        self.pose_delta_inputs = [None] * 6
        
        # 메모리
        self.memory = {i: [0.0]*6 for i in range(1, 6)}
        self.pose_memory = {i: [0.0]*6 for i in range(1, 6)}
        self.mem_labels = {i: [None]*6 for i in range(1, 6)}
        self.pose_mem_labels = {i: [None]*6 for i in range(1, 6)}
        
        self._setup_ui()
    
    def set_controller(self, controller):
        """컨트롤러 설정 및 Signal 연결"""
        self.controller = controller
        
        # RobotArmController Signal 연결
        controller.angles_updated.connect(self.update_angles_display)
        controller.coords_updated.connect(self.update_coords_display)
        controller.pose_updated.connect(self.update_pose_display)
    
    def _setup_ui(self):
        """UI 구성"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # 제어 영역 (스크롤)
        control_widget = self._create_control_section()
        main_layout.addWidget(control_widget)
    
    def _create_control_section(self):
        """제어 섹션"""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        robot_layout = QVBoxLayout(scroll_content)
        
        # 1. System Control
        sys_group = self._create_system_control()
        robot_layout.addWidget(sys_group)
        
        # 2. 각도 컨트롤러
        jog_group = self._create_joint_controller()
        robot_layout.addWidget(jog_group)
        
        # 3. 좌표 컨트롤러
        cart_group = self._create_cartesian_controller()
        robot_layout.addWidget(cart_group)
        
        robot_layout.addStretch()
        
        scroll.setWidget(scroll_content)
        return scroll
    
    def _setup_grid_alignment(self, layout):
        """그리드 정렬 설정"""
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setColumnMinimumWidth(0, LABEL_WIDTH)
        layout.setColumnMinimumWidth(1, JOG_ZONE_WIDTH)
        layout.setColumnMinimumWidth(2, VALUE_WIDTH)
        layout.setColumnMinimumWidth(3, VALUE_WIDTH)
        layout.setColumnMinimumWidth(4, 90)
        for i in range(5, 10):
            layout.setColumnMinimumWidth(i, MEM_WIDTH)
    
    def _create_label(self, text, color, width):
        """라벨 생성"""
        lbl = QLabel(text)
        lbl.setFixedSize(width, 32)
        lbl.setFont(self.main_font)
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setStyleSheet(
            f"border: 2px solid {color}; background-color: white; color: black; border-radius: 3px;"
        )
        return lbl
    
    def _create_system_control(self):
        """시스템 컨트롤"""
        sys_group = QGroupBox("⚙️ System Control")
        sys_group.setFixedHeight(90)
        sys_h_layout = QHBoxLayout()
        
        controls = [
            ("✓ Servo ON", self._servo_on),
            ("✗ Servo OFF", self._servo_off),
            ("🏠 HOME", self._go_home),
            ("✊ GRIP", self._grip),
            ("🖐️ UNGRIP", self._ungrip)
        ]
        
        for text, func in controls:
            btn = QPushButton(text)
            btn.setFixedSize(105, 40)
            btn.setFont(QFont("Arial", 9, QFont.Weight.Bold))
            btn.clicked.connect(func)
            sys_h_layout.addWidget(btn)
        
        sys_h_layout.addStretch()
        sys_group.setLayout(sys_h_layout)
        return sys_group
    
    def _create_joint_controller(self):
        """관절 각도 컨트롤러"""
        jog_group = QGroupBox("🔧 각도 컨트롤러")
        grid = QGridLayout()
        self._setup_grid_alignment(grid)
        
        # 헤더
        headers = ["Axis", "Jog (+/-)", "Target", "Actual", "Err/F", "Pos 1", "Pos 2", "Pos 3", "Pos 4", "Pos 5"]
        for col, text in enumerate(headers):
            grid.addWidget(QLabel(text), 0, col, Qt.AlignmentFlag.AlignCenter)
        
        # 관절별 컨트롤 (6개)
        for i in range(6):
            row = 6 - i  # 역순 배치
            
            # 축 라벨
            axis_lbl = QLabel(f"J{i+1}(°)")
            axis_lbl.setFixedWidth(LABEL_WIDTH)
            axis_lbl.setFont(self.main_font)
            axis_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            axis_lbl.setStyleSheet(
                "border: 2px solid #666; background-color: #E0E0E0; color: black; border-radius: 3px; padding: 4px;"
            )
            grid.addWidget(axis_lbl, row, 0)
            
            # Jog 컨트롤 (-, step input, +)
            jog_box = QHBoxLayout()
            jog_box.setContentsMargins(0, 0, 0, 0)
            jog_box.setSpacing(4)
            
            btn_m = QPushButton("-")
            btn_m.setFixedSize(32, 32)
            btn_m.clicked.connect(lambda ch, idx=i: self._jog(idx, -1))
            
            btn_p = QPushButton("+")
            btn_p.setFixedSize(32, 32)
            btn_p.clicked.connect(lambda ch, idx=i: self._jog(idx, 1))
            
            step_input = QLineEdit("1.0")
            step_input.setFixedSize(40, 32)
            step_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.jog_step_inputs[i] = step_input
            
            jog_box.addWidget(btn_m)
            jog_box.addWidget(step_input)
            jog_box.addWidget(btn_p)
            grid.addLayout(jog_box, row, 1)
            
            # Target, Actual
            target_lbl = self._create_label("0.0", "#2196F3", VALUE_WIDTH)
            self.target_labels[i] = target_lbl
            grid.addWidget(target_lbl, row, 2)
            
            actual_lbl = self._create_label("0.0", "#757575", VALUE_WIDTH)
            self.actual_labels[i] = actual_lbl
            grid.addWidget(actual_lbl, row, 3)
            
            # Error + Factor
            err_f_box = QHBoxLayout()
            err_f_box.setContentsMargins(0, 0, 0, 0)
            
            err_lbl = self._create_label("0.0", "#f44336", 40)
            self.error_labels[i] = err_lbl
            
            f_input = QLineEdit("1.0")
            f_input.setFixedSize(35, 32)
            f_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.factor_inputs[i] = f_input
            
            err_f_box.addWidget(err_lbl)
            err_f_box.addWidget(f_input)
            grid.addLayout(err_f_box, row, 4)
            
            # 메모리 Pos1~5
            for m_idx in range(1, 6):
                mem_lbl = self._create_label("---", "#555", MEM_WIDTH)
                self.mem_labels[m_idx][i] = mem_lbl
                grid.addWidget(mem_lbl, row, m_idx + 4)
        
        # 저장/이동 버튼 라인
        for m_idx in range(1, 6):
            btn_vbox = QVBoxLayout()
            btn_vbox.setSpacing(4)
            btn_vbox.setContentsMargins(0, 0, 0, 0)
            
            save_btn = QPushButton("저장")
            save_btn.setFixedSize(MEM_WIDTH - 5, 28)
            save_btn.setStyleSheet("font-size: 10px; background-color: #1976D2;")
            save_btn.clicked.connect(lambda ch, m=m_idx: self._save_joint_memory(m))
            
            move_btn = QPushButton("이동")
            move_btn.setFixedSize(MEM_WIDTH - 5, 28)
            move_btn.setStyleSheet("font-size: 10px; background-color: #2E7D32;")
            move_btn.clicked.connect(lambda ch, m=m_idx: self._move_joint_memory(m))
            
            btn_vbox.addWidget(save_btn)
            btn_vbox.addWidget(move_btn)
            grid.addLayout(btn_vbox, 7, m_idx + 4)
        
        # Factor 저장 버튼
        factor_save_btn = QPushButton("보정계수\n저장")
        factor_save_btn.setFixedSize(80, 58)
        factor_save_btn.setStyleSheet("font-size: 10px; background-color: #FF9800;")
        grid.addWidget(factor_save_btn, 7, 4)
        
        jog_group.setLayout(grid)
        return jog_group
    
    def _create_cartesian_controller(self):
        """좌표 컨트롤러"""
        cart_group = QGroupBox("🎯 좌표 컨트롤러")
        c_grid = QGridLayout()
        self._setup_grid_alignment(c_grid)
        
        # 헤더
        c_headers = ["Axis", "Jog (+/-)", "Target", "Actual", "Error", "P1", "P2", "P3", "P4", "P5"]
        for col, text in enumerate(c_headers):
            c_grid.addWidget(QLabel(text), 0, col, Qt.AlignmentFlag.AlignCenter)
        
        axes = ["X(mm)", "Y(mm)", "Z(mm)", "R(°)", "P(°)", "Y(°)"]
        for i in range(6):
            row = i + 1
            
            # 축 라벨
            axis_lbl = QLabel(axes[i])
            axis_lbl.setFixedWidth(LABEL_WIDTH)
            axis_lbl.setFont(self.main_font)
            axis_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            axis_lbl.setStyleSheet(
                "border: 2px solid #666; background-color: #E0E0E0; color: black; border-radius: 3px; padding: 4px;"
            )
            c_grid.addWidget(axis_lbl, row, 0)
            
            # Jog 컨트롤
            jog_layout = QHBoxLayout()
            jog_layout.setContentsMargins(0, 0, 0, 0)
            jog_layout.setSpacing(4)
            
            jbtn_m = QPushButton("-")
            jbtn_m.setFixedSize(32, 32)
            jbtn_m.clicked.connect(lambda ch, idx=i: self._cart_jog(idx, -1))
            
            jbtn_p = QPushButton("+")
            jbtn_p.setFixedSize(32, 32)
            jbtn_p.clicked.connect(lambda ch, idx=i: self._cart_jog(idx, 1))
            
            delta_input = QLineEdit("5.0")
            delta_input.setFixedSize(40, 32)
            delta_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.pose_delta_inputs[i] = delta_input
            self.pose_target_labels[i] = None  # 아래에서 설정
            self.pose_actual_labels[i] = None
            self.pose_error_labels[i] = None
            
            jog_layout.addWidget(jbtn_m)
            jog_layout.addWidget(delta_input)
            jog_layout.addWidget(jbtn_p)
            c_grid.addLayout(jog_layout, row, 1)
            
            # Target, Actual
            target_lbl = self._create_label("0.0", "#2196F3", VALUE_WIDTH)
            self.pose_target_labels[i] = target_lbl
            c_grid.addWidget(target_lbl, row, 2)
            
            actual_lbl = self._create_label("0.0", "#757575", VALUE_WIDTH)
            self.pose_actual_labels[i] = actual_lbl
            c_grid.addWidget(actual_lbl, row, 3)
            
            # Error
            err_lbl = self._create_label("0.0", "#f44336", 90)
            self.pose_error_labels[i] = err_lbl
            c_grid.addWidget(err_lbl, row, 4)
            
            # 메모리 Pos1~5
            for m_idx in range(1, 6):
                mem_lbl = self._create_label("---", "#555", MEM_WIDTH)
                self.pose_mem_labels[m_idx][i] = mem_lbl
                c_grid.addWidget(mem_lbl, row, m_idx + 4)
        
        # 좌표 메모리 저장/이동 버튼 라인
        for m_idx in range(1, 6):
            btn_vbox = QVBoxLayout()
            btn_vbox.setSpacing(4)
            btn_vbox.setContentsMargins(0, 0, 0, 0)
            
            ps_btn = QPushButton("저장")
            ps_btn.setFixedSize(MEM_WIDTH - 5, 28)
            ps_btn.setStyleSheet("font-size: 10px; background-color: #1976D2;")
            ps_btn.clicked.connect(lambda ch, m=m_idx: self._save_pose_memory(m))
            
            pm_btn = QPushButton("이동")
            pm_btn.setFixedSize(MEM_WIDTH - 5, 28)
            pm_btn.setStyleSheet("font-size: 10px; background-color: #2E7D32;")
            pm_btn.clicked.connect(lambda ch, m=m_idx: self._move_pose_memory(m))
            
            btn_vbox.addWidget(ps_btn)
            btn_vbox.addWidget(pm_btn)
            c_grid.addLayout(btn_vbox, 7, m_idx + 4)
        
        cart_group.setLayout(c_grid)
        return cart_group
    
    # ==================== 데이터 업데이트 메서드 ====================
    
    def update_angles_display(self, angles):
        """각도 데이터 업데이트"""
        for i in range(6):
            if self.actual_labels[i]:
                self.actual_labels[i].setText(f"{angles[i]:.1f}")
                
                # Target과 비교하여 오차 계산
                try:
                    target = float(self.target_labels[i].text())
                    error = target - angles[i]
                    self.error_labels[i].setText(f"{error:.1f}")
                    
                    # 오차에 따라 색상 변경
                    color = "#C8E6C9" if abs(error) < 0.5 else "#FFCDD2"
                    self.error_labels[i].setStyleSheet(
                        f"background-color: {color}; color: black; "
                        f"border: 1px solid #f44336; border-radius: 3px;"
                    )
                except:
                    pass
    
    def update_coords_display(self, coords):
        """좌표 데이터 업데이트"""
        for i in range(6):
            if self.pose_actual_labels[i]:
                self.pose_actual_labels[i].setText(f"{coords[i]:.1f}")
                
                # Target 초기값 설정
                if self.pose_target_labels[i].text() == "0.0":
                    self.pose_target_labels[i].setText(f"{coords[i]:.1f}")
                
                # 오차 계산
                try:
                    target = float(self.pose_target_labels[i].text())
                    error = target - coords[i]
                    self.pose_error_labels[i].setText(f"{error:.1f}")
                    
                    color = "#C8E6C9" if abs(error) < 1.0 else "#FFCDD2"
                    self.pose_error_labels[i].setStyleSheet(
                        f"background-color: {color}; color: black; "
                        f"border: 1px solid #f44336; border-radius: 3px;"
                    )
                except:
                    pass
    
    def update_pose_display(self, pose):
        """포즈 데이터 업데이트 (current_pose)"""
        # pose_memory 저장용
        pass
    
    # ==================== 제어 메서드 ====================
    
    def _jog(self, axis, direction):
        """관절 Jog"""
        if not self.controller:
            return
        
        try:
            step = float(self.jog_step_inputs[axis].text())
            current = list(self.controller.current_angles)
            current[axis] += (direction * step)
            
            self.controller.publish_angles(current)
            self.target_labels[axis].setText(f"{current[axis]:.1f}")
        except:
            pass
    
    def _cart_jog(self, axis, direction):
        """좌표 Jog"""
        if not self.controller:
            return
        
        try:
            delta = float(self.pose_delta_inputs[axis].text())
            current = list(self.controller.current_coords)
            current[axis] += (direction * delta)
            
            self.controller.publish_coords(current)
            self.pose_target_labels[axis].setText(f"{current[axis]:.1f}")
        except:
            pass
    
    def _servo_on(self):
        if self.controller:
            self.controller.send_servo(True)
    
    def _servo_off(self):
        if self.controller:
            self.controller.send_servo(False)
    
    def _go_home(self):
        if self.controller:
            self.controller.go_home()
            for i in range(6):
                self.target_labels[i].setText("0.0")
    
    def _grip(self):
        if self.controller:
            self.controller.send_gripper(1)
    
    def _ungrip(self):
        if self.controller:
            self.controller.send_gripper(0)
    
    def _save_joint_memory(self, slot):
        """관절 메모리 저장"""
        if self.controller:
            self.memory[slot] = list(self.controller.current_angles)
            for i in range(6):
                self.mem_labels[slot][i].setText(f"{self.memory[slot][i]:.1f}")
    
    def _move_joint_memory(self, slot):
        """관절 메모리 이동"""
        if self.controller:
            self.controller.publish_angles(self.memory[slot])
            for i in range(6):
                self.target_labels[i].setText(f"{self.memory[slot][i]:.1f}")
    
    def _save_pose_memory(self, slot):
        """좌표 메모리 저장"""
        if self.controller:
            self.pose_memory[slot] = list(self.controller.current_coords)
            for i in range(6):
                self.pose_mem_labels[slot][i].setText(f"{self.pose_memory[slot][i]:.1f}")
    
    def _move_pose_memory(self, slot):
        """좌표 메모리 이동"""
        if self.controller:
            self.controller.publish_coords(self.pose_memory[slot])
            for i in range(6):
                self.pose_target_labels[i].setText(f"{self.pose_memory[slot][i]:.1f}")
    
    def _create_pose_memory_buttons(self):
        """좌표 메모리 저장/이동 버튼"""
        pose_mem_btn_layout = QHBoxLayout()
        for m in range(1, 6):
            btn_v_layout = QVBoxLayout()
            btn_v_layout.setSpacing(2)
            
            save_btn = QPushButton("저장")
            save_btn.setFixedSize(55, 22)
            save_btn.setStyleSheet("font-size: 9px; background-color: #1976D2;")
            
            move_btn = QPushButton("이동")
            move_btn.setFixedSize(55, 22)
            move_btn.setStyleSheet("font-size: 9px; background-color: #2E7D32;")
            
            btn_v_layout.addWidget(save_btn)
            btn_v_layout.addWidget(move_btn)
            pose_mem_btn_layout.addLayout(btn_v_layout)
        
        pose_mem_btn_layout.addStretch()
        return pose_mem_btn_layout

