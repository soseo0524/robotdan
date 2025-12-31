

# 🚜 스마트 팜 통합 방제 시스템 (Smart Farm Automation System)

**robotdan** 프로젝트는 자율주행 로봇(Pinky)과 로봇팔(JetCobot)을 결합하여 농장의 이상 지형을 탐지하고, 맞춤형 비료를 실시간으로 제조하여 정밀 방제하는 통합 자동화 솔루션

## 📑 프로젝트 개요 (Overview)

본 시스템은 인력 중심의 농업 방제 방식을 디지털화하여 정확성과 효율성을 극대화. \
Pinky 1의 AI 정찰 데이터를 기반으로 지점별 맞춤형 처방을 내리고, 로봇팔과 Pinky2,3 간의 유기적인 협업을 통해 자재 운반부터 방제까지 전 과정을 자동화

---


## 🛠 시스템 아키텍처 (Architecture)
<img width="732" height="410" alt="image" src="https://github.com/user-attachments/assets/dbb3a401-5c3d-4de0-875d-10b15561ea42" />


### **Section 1: 농장 정찰 구역 (Smart Farm Scouting)**

* **Pinky 1 (AMR)**: 지정된 경로를 주행하며 카메라와 정밀 센서로 지면 상태를 스캔합니다. 불규칙한 지형 탐지 및 미지의 장애물 회피 필요.


* **AI 탐지**: **YOLOv8-Seg** 모델을 사용하여 초록색(정상), 노란색(영양 부족), 빨간색(병충해) 지형을 분류하고 좌표를 추출.
* <img width="947" height="353" alt="image" src="https://github.com/user-attachments/assets/20923563-da61-42d0-bfe6-232637042cb7" />

* **데이터 전송**: 탐지된 좌표 및 상태 정보를 중앙 제어 시스템으로 실시간 전송.






### **Section 2: 비료 제조 구역 (Custom Fertilizer Production)**

* **Pinky 2 (AVG)**: 서버의 처방 데이터에 따라 제조에 필요한 여러 자재(Parts A, B, C)를 창고에서 조립장으로 운반


* **JetCobot A (Robot Arm)**: 수령한 자재를 조립하여 맞춤형 비료를 생성


* **가변 배합 알고리즘**: 탐지된 색상 라벨(Yellow/Red)에 따라 다른 제조 방식 사용







### **Section 3: 품질 검수 및 방제 구역 (QC & Dispatch)**

* **JetCobot B (Robot Arm)**: 제조된 제품의 외관 및 기능을 카메라 센서로 검사


* **데이터 연동형 오토인코더(Autoencoder)**: 서버의 Case 정보(1번/2번 비료)를 수신하여, 라즈베리 파이에서 해당 케이스에 최적화된 경량 AI 모델로 불량 여부를 판정합니다.
* <img width="939" height="414" alt="image" src="https://github.com/user-attachments/assets/fd0df86c-3983-4c53-a4a9-3257ffa80a09" />

* **Pinky 3 (AMR)**: 검수가 완료된 'OK' 판정 비료를 'OK'존으로 'NG' 판정 비료를 'NG'존으로 이동시킨다





---


## 🧠 인공지능 기술 스택 (AI Tech Stack)

* **Vision**: YOLOv8-Seg (지형 분할 및 분류)
* **Anomaly Detection**: Lightweight Autoencoder (라즈베리 파이 최적화 엣지 컴퓨팅)
* **Optimization**: 색상 기반 가변 배합 로직 및 다중 로봇 경로 최적화 알고리즘



---

## 💾 데이터베이스 설계 (Database Design)

모든 로봇과 로봇팔은 중앙 서버와 통신하며 데이터를 주고받아야 한다.

### 1. Field_Analysis_Table (정찰 데이터)
Pinky 1이 탐지한 정보를 저장 


### 2. Production_Log_Table (제조 및 검수)
JetCobot과 Pinky 2, 3의 작업 이력을 기록

  2-1. Production_Log_Table (JetCobot A: 제조)
  비료 배합 및 조립 공정 기록 
  
  * Case_ID: 서버에서 수신한 처방 케이스 (Case 1 또는 2).
  * Mixing_Ratio: 각 자재(A, B, C)의 투입 성공 여부.
  * Cycle_Time: 조립 시작부터 완료까지 걸린 시간.
  
  2-2. Inspection_Log_Table (JetCobot B: 검수)
  품질 검사 및 최종 판정 결과를 기록
  
  * Input_Case: 검수 대상의 비료 타입 (서버 데이터 연동).
  
  * AI_Score: Autoencoder 모델이 계산한 Reconstruction Error 값.
  
  * Final_Verdict: 최종 판정 (OK 또는 NG).
  
  * Next_Action: 판정에 따른 Pinky 3 호출 명령 발송.
  
  2-3. Logistics_Log_Table (Pinky 2 & 3: 운반 및 분류)
  운반 로봇들의 주행 및 목적지 도착 상태를 기록


### 3. Robot_Status_Table (실시간 모니터링)
전체 로봇의 상태를 관리하며, 특히 배터리 관리 



































