# PC - GUI & Server

PyQt6 기반 로봇 제어 GUI 및 ROS2 서버

## 패키지

- **lovo_gui**: 메인 GUI 애플리케이션
- **lovo_main_server**: ROS2 메인 서버
- **lovo_interfaces**: 커스텀 ROS2 메시지

## 빌드 & 실행

```bash
# 빌드
colcon build --symlink-install

# 실행
source install/setup.bash
ros2 run lovo_gui main_window
```

## 로봇 설정

`lovo_gui/robotname.json`에서 로봇 IP, Domain 설정

## UDP 카메라 포트

- 상차 로봇팔: 9510
- 하차 로봇팔: 9520
- 운송 로봇 1: 9530
- 운송 로봇 2: 9540
- 청소 로봇: 9550
