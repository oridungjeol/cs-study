# HTTP와 HTTPS의 차이점

![image](https://github.com/user-attachments/assets/58a3ae7b-a9b7-4ef7-93a1-7bc89f695184)

## HTTP(Hyper Text Transfer Protocol)
- 서버/클라이언트 간에 데이터를 주고받기 위한 프로토콜
- 80번 포트를 사용한다
- 암호화가 되지 않은 텍스트 데이터를 전송하기에 보안 이슈가 있다(보안 레벨이 낮다)

- HTTP 요청 예시
```
GET /hello.txt HTTP/1.1
User-Agent: curl/7.63.0 libcurl/7.63.0 OpenSSL/1.1.l zlib/1.2.11
Host: www.example.com
Accept-Language: en
```
- 텍스트 형태로 바로 전달되기 때문에 모니터링하는 모든 사람이 요청/응답을 읽을 수 있다
<br><br>

## HTTPS(Hyper Text Transfer Protocol Secure)
- HTTP에 데이터 암호화가 추가된 프로토콜
- 443번 포트를 사용한다
- 보안 레벨 높음
- TLS의 공개키 암호화 기술을 사용하여 요청 암호화, 공개키를 SSL 인증서로 클라이언트와 공유한다.
  - [참고 문서(대칭키와 공개키 정리)](https://github.com/oridungjeol/cs-study/blob/main/content/secure/symmetric%20key%26public%20key.md)    
- HTTP 요청과 응답을 암호화하여 공격자는 요청 내용 대신 무작위 문자를 보게 된다.

- HTTP 요청 예시
```
GET /hello.txt HTTP/1.1
User-Agent: curl/7.63.0 libcurl/7.63.0 OpenSSL/1.1.l zlib/1.2.11
Host: www.example.com
Accept-Language: en
```
- 공격자가 보는 메시지
```
t8Fw6T8UV81pQfyhDkhebbz7+oiwldr1j2gHBB3L3RFTRsQCpaSnSBZ78Vme+DpDVJPvZdZUZHpzbbcqmSW1+3xXGsERHg9YDmpYk0VVDiRvw1H5miNieJeJ/FNUjgH0BmVRWII6+T4MnDwmCMZUI/orxP3HGwYCSIvyzS3MpmmSe4iaWKCOHQ==
```
<br><br>    




[참고 블로그 1](https://mangkyu.tistory.com/98)    
[cloudflare 문서](https://www.cloudflare.com/ko-kr/learning/ssl/why-is-http-not-secure/)
