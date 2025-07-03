# 대칭키와 비대칭키
![image](https://github.com/user-attachments/assets/b7e12eba-c614-4886-a257-aa3176ac4589)

## 대칭키
- 양 측에서 같은 암호화 키를 사용하여 암호화/복호화를 진행하는 방식
- 암호화 속도가 빠르다(같은 키를 사용하기 때문)
- 같은 키를 사용하기에 대칭키 전달 과정에서 보안 위험이 있다
- 이를 보완하여 등장한 것이 비대칭키(공개키)이다
- DES, 3DES, AES 등등이 있다

## 비대칭키(공개키)
- HTTPS에 사용되는 TLS에서 사용되는 암호화 방식이다.
- 암호화 속도가 상대적으로 느리다
- 공개키 / 개인키가 따로 존재한다
- 예를 들어, a가 b에게 데이터를 보낼 때 a는 공개키로 암호화를 한다. b는 데이터를 받아서 본인의 개인키로 복호화를 한다.
  - 즉, 공개키에 대응되는 개인키를 가지고 있는 b만이 해당 데이터를 볼 수 있다.
- 대표적으로 RSA, 전자서명이 있다

[대칭키와 비대칭키는 무슨 차이가 있을까?](https://velog.io/@minj9_6/%EB%8C%80%EC%B9%AD%ED%82%A4%EC%99%80-%EB%B9%84%EB%8C%80%EC%B9%AD%ED%82%A4%EB%8A%94-%EB%AC%B4%EC%8A%A8-%EC%B0%A8%EC%9D%B4%EA%B0%80-%EC%9E%88%EC%9D%84%EA%B9%8C)    
[공개 키 암호화는 어떻게 작동할까요?](https://www.cloudflare.com/ko-kr/learning/ssl/how-does-public-key-encryption-work)    
[대칭키공개키](https://github.com/Songwonseok/CS-Study/blob/main/Network/%EB%8C%80%EC%B9%AD%ED%82%A4%EA%B3%B5%EA%B0%9C%ED%82%A4.md)
