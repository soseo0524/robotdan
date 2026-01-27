"""
Log 탭
"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCalendarWidget,
    QTextEdit, QSizePolicy
)


class LogTab(QWidget):
    """Log 탭 - 시스템 로그"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.log_viewer = None
        self._setup_ui()
    
    def _setup_ui(self):
        """UI 구성"""
        layout = QHBoxLayout(self)
        
        # 왼쪽 패널
        left_panel = self._create_left_panel()
        layout.addWidget(left_panel)
        
        # 오른쪽: 로그 뷰어
        self.log_viewer = QTextEdit()
        self.log_viewer.setReadOnly(True)
        self.log_viewer.setStyleSheet(
            "background-color: #1e1e1e; color: #00ff00; font-family: Consolas;"
        )
        layout.addWidget(self.log_viewer)
    
    def _create_left_panel(self):
        """왼쪽 패널 (캘린더 + 버튼)"""
        left_widget = QWidget()
        left_widget.setFixedWidth(350)
        left_layout = QVBoxLayout(left_widget)
        
        # 캘린더
        self.calendar = QCalendarWidget()
        self.calendar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.calendar.setFixedWidth(330)
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.filter_log_by_date)
        left_layout.addWidget(self.calendar)
        
        # 버튼들
        for text in ["자재", "모니터링", "알람"]:
            btn = QPushButton(text)
            btn.setFixedWidth(260)
            btn.setFixedHeight(40)
            left_layout.addWidget(btn)
        
        left_layout.addStretch()
        
        return left_widget
    
    def filter_log_by_date(self):
        """날짜별 로그 필터링"""
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        self.log_viewer.append(f"📅 [{selected_date}] 날짜 선택됨")
