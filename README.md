# motor_vib
- socket 통신을 사용한 모터 이상 탐지 시스템
- 본 예제는 선풍기의 풍속에 따른 이상탐지에 관한 토이 프로젝트
- RPI 4, 진동감지센서(가속도 센서 : mw-ahrsv1), desktop 사용
- python, pytorch. socket, matplotlib


## socket
- config file의 정보를 기본으로 함.
- config file은 setConfigFile.py를 사용하여 수정 가능(argparser : --ip, --port)
### server : desktop
### client : RPI


## 개발현황
- socket 통신 구현 완료 (23.01.18)
- sensor data 전송 구현 완료 (23.01.20)
- 실시간 그래프 구현 완료 (23.01.25)
- mongoDB 등 NoSQL DB 구축중 (23.01.25)
- 풍속 1단 데이터 수집 후 학습 예정
  - OCSVM or IF
- Flutter 등 크로스플랫폼 사용하여 디바이스와 연동 예정
