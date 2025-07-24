# 스택이란?
- 데이터를 저장하고 꺼내는 데 이용되는 자료 구조
- 후입선출(LIFO) - 가장 먼저 들어온 데이터가 가장 나중에 나가는 구조

<img width="100" height="350" alt="image" src="https://github.com/user-attachments/assets/868c556d-9727-4095-9182-283310b9c840" />

# 코드 구현(python)
```python
stack = []
stack.append("111") # push
stack.append("222") # push
stack.append("333") # push

stack.pop() # 333 pop
print(stack) # [ 111, 222 ]

print(stack.peek()) # 222(가장 위에 있는 요소를 반환(pop처럼 삭제하며 반환하지 않음))
print(stack) # [ 111, 222 ]

# isEmpyt -> 스택이 비어있으면 true를 반환
print(stack.isEmpty()) # false
```

# 스택의 사용 사례
- 웹 브라우저 방문 기록
- 수식의 괄호 검사(유효한 괄호 문자열 판별)
- 역순 문자열 만들기
