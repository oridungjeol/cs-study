# 컴퓨터 시스템 개요

컴퓨터 시스템은 크게 **하드웨어, 운영체제, 응용 프로그램, 사용자**로 구성됩니다.

이 중 하드웨어는 CPU, 메모리, 저장장치, 입출력 장치 등으로 구성되며, 운영체제가 하드웨어를 관리하고 응용 프로그램 실행을 돕습니다.

---

# 주요 하드웨어 구성 요소

## 1. CPU (Central Processing Unit)

- 컴퓨터의 두뇌 역할
- 명령어를 해석하고 실행
- 산술논리연산장치(ALU), 제어장치, 레지스터 등으로 구성됨

## 2. 메모리 (RAM)

- 프로그램 실행과 데이터 처리를 위한 **휘발성 메모리**
- 부트스트랩 프로그램과 운영체제 초기 로딩에 사용
- 전원이 꺼지면 데이터 사라짐

## 3. 저장장치

### HDD (Hard Disk Drive)

- 자기 디스크와 헤드로 구성된 **비휘발성 저장장치**
- 대용량 가능, 느린 속도, 충격에 약함

### SSD (Solid State Drive, 대표적인 NVM)

- 반도체 기반의 빠른 비휘발성 저장장치
- 소음 없고 충격에 강하며 전력 효율 높음
- 가격은 HDD보다 높음

| 구분 | HDD | SSD (NVM) |
| --- | --- | --- |
| 속도 | 느림 | 빠름 |
| 구조 | 기계식 | 반도체 |
| 내구성 | 충격에 약함 | 강함 |
| 가격 | 저렴 | 비쌈 |

## 4. 버스 (Bus)

- CPU, 메모리, 입출력 장치 사이 데이터를 전달하는 **물리적 통로**
- 종류
    - 데이터 버스: 실제 데이터 전달
    - 주소 버스: 데이터 위치 지정
    - 제어 버스: 읽기/쓰기 등 제어 신호 전달

---

# 인터럽트 (Interrupt)

## 하드웨어 신호로서의 인터럽트

- 장치 컨트롤러가 CPU에 보내는 **비동기적 신호**
- "지금 나 좀 처리해줘!"라는 요청을 전기 신호 형태로 전달

## 운영체제에서의 인터럽트 처리

- CPU가 현재 실행 중인 작업을 잠시 멈추고
- 인터럽트 벡터를 통해 해당 장치의 처리 루틴으로 이동
- 처리 후 원래 작업으로 복귀

## 인터럽트의 중요성

- CPU가 장치 작업 완료를 기다리지 않고 효율적으로 자원을 사용할 수 있게 해줌

---

# 운영체제와 하드웨어 연동

- 인터럽트, 입출력 장치 제어 등 하드웨어와 운영체제가 협력해 시스템 자원을 효율적으로 관리
- 프로세스와 스레드 관리, 메모리 관리 등도 운영체제 역할

---

# 명령어 실행 사이클

1. 명령어를 메모리에서 읽어 명령 레지스터에 저장
2. 제어장치가 명령어 해독
3. 필요한 데이터를 메모리에서 인출
4. CPU 내부 레지스터에 저장 후 연산 수행
5. 결과 저장 및 다음 명령 실행 준비