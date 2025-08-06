# TCP 3-Way Handshake & 4-Way Handshake

## TCP(Transmission Control Protocol) 란?

> 인터넷에서 신뢰성 있는 데이터 전송을 담당하는 핵심 프로토콜

- **주요 특징**: 데이터를 **정확하게**, **순서대로**, **빠짐없이 전송**
- **실생활 예시**: 웹사이트 접속, 파일 다운로드, 이메일 등  
  반드시 수신자가 정보를 받아야 하는 **신뢰성 있는 통신**이 필요할 때 사용됨

TCP는 이러한 신뢰성을 보장하기 위해 **통신 시작 시**와 **종료 시** 특별한 절차를 거침
이때 사용되는 과정이 바로 **3-Way Handshake (연결 성립)**, **4-Way Handshake (연결 해제)** 

---

## 🔗 3-Way Handshake: 연결 성립

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/5ba2cf70-48ed-4d6d-813a-dcf91c279374" />


1. **Client → Server : SYN 전송 (연결 요청)**  
   클라이언트가 서버에 연결 요청을 하면서 **SYN 플래그**가 설정된 패킷을 보냄

2. **Server → Client : SYN + ACK 전송 (요청 수락 및 동기화 신호)**  
   서버는 클라이언트의 SYN을 받고, 응답으로 SYN과 ACK를 합친 패킷을 전송

3. **Client → Server : ACK 전송 (확인 응답)**  
   클라이언트가 서버의 응답을 받고 **최종 ACK**를 전송하면 연결이 성립됨

✅ 이렇게 **3번의 통신**이 완료되면 **TCP 연결이 성립**된다.

---

## 🔚 4-Way Handshake: 연결 해제

(<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/d12147a2-f794-4028-b413-6330600197b9" />)

### 1. Client → Server : FIN 전송  
클라이언트가 연결 종료를 요청하며 FIN 플래그를 보냄  
→ 클라이언트는 **FIN-WAIT-1** 상태로 진입

#### 🔸 FIN-WAIT 상태란?
> TCP에서 연결을 종료하고자 하는 쪽이  
> 먼저 FIN 패킷을 전송한 후 기다리는 상태

---

### 2. Server → Client : ACK 전송  
서버는 FIN을 받고 ACK를 전송  
→ 서버는 **CLOSE-WAIT** 상태로 진입

#### 🔸 CLOSE-WAIT 상태란?
- 상대방이 먼저 FIN 패킷을 보냈고
- 내가 그 FIN에 대해 ACK를 응답한 상태
- **아직 내 쪽에서 FIN을 보내지 않은 상태**

---

### 3. Server → Client : FIN 전송  
서버가 연결을 종료할 준비가 되면 FIN 플래그를 클라이언트에 전송  
→ 서버는 **LAST-ACK** 상태로 진입

#### 🔸 LAST-ACK 상태란?
- 내가 먼저 FIN을 받은 후,
- 그에 대한 ACK을 보낸 뒤,
- **나도 FIN을 보내고**,
- 상대방의 최종 ACK를 기다리는 상태

---

### 4. Client → Server : ACK 전송  
클라이언트는 서버의 FIN을 받고 **마지막 ACK**를 전송  
→ 클라이언트는 **TIME-WAIT** 상태로 진입하고 일정 시간 후 **CLOSED**

#### 🔸 TIME-WAIT 상태란?

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/b32f1328-90db-4057-9eef-5abd9bcf9906" />



- TCP 4-Way Handshake에서 **연결을 먼저 끊은 쪽에서 발생**
- 마지막 ACK 패킷의 유실이나 패킷 지연에 대비하여 **일정 시간 동안 소켓을 유지**

> 예: 마지막 ACK가 유실되면 서버는 다시 FIN을 보낼 수 있음.  
> 이때 클라이언트는 TIME-WAIT 상태 덕분에 FIN을 다시 받아 ACK를 재전송할 수 있음.


✅ 이렇게 4번의 통신이 완료되면 **TCP 연결이 안전하게 해제**된다.

---

## 📌 참고 자료

- [gyoogle/tech-interview-for-developer - GitHub](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Network/TCP%203%20way%20handshake%20%26%204%20way%20handshake.md)
- [네트워크 소켓 상태 정리 - Medium](https://medium.com/@hyukjuner/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%86%8C%EC%BC%93-%EC%83%81%ED%83%9C-time-wait-close-wait-21813a5c625)

---

