"""
설정 파일 관리
"""
import json
import os


class ConfigManager:
    """robotname.json 설정 파일 관리"""
    
    def __init__(self, config_path="robotname.json"):
        self.config_path = config_path
        self.config = {}
        self.load()
    
    def load(self):
        """설정 파일 로드"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    self.config = json.load(f)
            except:
                self._set_default()
        else:
            self._set_default()
    
    def _set_default(self):
        """기본 설정 생성"""
        self.config = {
            "server_domain": 70,
            "robots": [
                {"name": "상차 로봇팔", "domain": 61, "id": "jecobot_126b", "ip": "192.168.0.61"},
                {"name": "하차 로봇팔", "domain": 60, "id": "jecobot_aab4", "ip": "192.168.0.60"},
                {"name": "운송 로봇 1", "domain": 52, "id": "d9ec", "ip": "192.168.0.10"},
                {"name": "운송 로봇 2", "domain": 51, "id": "20f0", "ip": "192.168.0.48"},
                {"name": "청소 로봇", "domain": 50, "id": "dfc6", "ip": "192.168.0.44"}
            ]
        }
        self.save()
    
    def save(self):
        """설정 파일 저장"""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
    
    def get_robots(self):
        """로봇 리스트 반환"""
        return self.config.get("robots", [])
    
    def get_server_domain(self):
        """서버 도메인 반환"""
        return self.config.get("server_domain", 70)
    
    def update_robot_name(self, index, new_name):
        """로봇 이름 업데이트"""
        if index < len(self.config.get("robots", [])):
            self.config["robots"][index]["name"] = new_name
            self.save()
            return True
        return False
    
    def get_robot_by_index(self, index):
        """인덱스로 로봇 정보 가져오기"""
        robots = self.get_robots()
        if 0 <= index < len(robots):
            return robots[index]
        return None
