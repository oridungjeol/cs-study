# 주소창에 www.google.com을 치면 무슨 일이 일어날까?

- 흐름을 이해하기 위해서는 우선 IP주소 / Domain Name에 대한 이해가 필요합니다.

## IP 주소와 도메인 네임

### IP 주소
- 127.0.0.1과 같이 **숫자로 이루어진** 웹 주소이다.
- 컴퓨터가 식별할 수 있는 실제 웹 주소

### 도메인 네임(Domain name)
- 숫자로만 이루어진 주소는 사람이 식별하기 어렵다
- 이러한 IP주소를 문자로 알기 쉽게 표현한 것이 Domain Name
- 단, 컴퓨터는 IP주소를 기반으로 식별하므로 변환 과정을 필요로 한다.

## DNS (Domain Name System)
- 사람이 읽을 수 있는 Domain Name을 컴퓨터가 식별할 수 있는 IP주소로 변환해주는 서버
- 도메인 네임과 ip 주소를 한 쌍으로 저장하고 있어 변환이 가능하다
- Amazon Route 53가 DNS 서비스이다


## 처리 흐름
1. 사용자가 주소 입력창에 www.example.com을 입력하고 Enter를 누릅니다.
2. www.example.com에 대한 요청은 인터넷 서비스 제공 업체(ISP)의 DNS 해석기로 라우팅됩니다.
3. ISP는 DNS로 요청을 전달하고, DNS는 저장되어 있던 IP 주소를 DNS 해석기로 반환합니다.
4. DNS 해석기는 IP 주소를 웹 브라우저로 반환합니다.
5. 웹 브라우저는 www.example.com에 대한 요청을 전송하고 컨텐츠를 반환받습니다.
6. 응답 데이터를 HTTP를 통해 사용자에게 반환하여 사용자는 웹 페이지를 확인할 수 있습니다.

![image](https://github.com/user-attachments/assets/6fad727c-bc04-4ff3-8db0-9bdbb577f1e2)

## 추가 용어 정리
- 웹 브라우저
  - 사용자가 웹 사이트를 볼 수 있게 해주는 프로그램(Chrome, Safari 등등..)
- 웹 서버
  - 실제 컨텐츠들이 저장되어 있는 서버(EC2, Vercel 등 웹 서버를 호스팅하는 환경)
- ISP(Internet Service Provider)
  - 인터넷 서비스 제공자
  - SK 브로드밴드, KT 등등이 여기에 해당됨
  - 개인이나 기업에게 **인터넷 접속**을 제공하는 회사
  - 위의 예시에서는 ISP의 DNS 해석기를 통해 DNS 서버에 요청한다


## 참고자료
[DNS란 무엇입니까?](https://aws.amazon.com/ko/route53/what-is-dns/)    
[www.naver.com을 치면 일어나는 일](https://velog.io/@jaeyunn_15/Network-www.naver.com%EC%9D%84-%EC%B9%98%EB%A9%B4-%EC%9D%BC%EC%96%B4%EB%82%98%EB%8A%94-%EC%9D%BC)
