# 이벤트 위임(Event Delegation)
- 하위 요소에 각각 이벤트를 붙이지 않고 상위 요소에서 하위 요소의 이벤트들을 제어하는 방식
<img width="1546" height="657" alt="image" src="https://github.com/user-attachments/assets/e9c0fb90-77cf-414c-8078-a857f71485a3" />

<br/>    
<hr/>    
<br/>    

## 이벤트 버블링(Event Bubbling)
예시)
```javascript
<style>
  body * {
    margin: 10px;
    border: 1px solid blue;
  }
</style>

<form onclick="alert('form')">FORM
  <div onclick="alert('div')">DIV
    <p onclick="alert('p')">P</p>
  </div>
</form>
```
- 결과 : p -> div -> form 순서대로 alert 창이 뜸
- 한 요소에 이벤트가 발생하면 해당 요소의 이벤트가 발생한 후, 가장 최상단의 조상 요소를 만날 때까지 올라가는 것 -> **버블링**

### event.target, this
- 예를 들어, javascript에서 클릭한 요소에 변화를 줘야할 때 event.target을 사용한다.
- 여기서 event.target은 클릭이벤트가 감지된 **해당 요소**를 뜻하며, this는 **이벤트가 감지된 최상단 요소**를 나타낸다.

### 버블링을 중단하는 방법?
```javascript
<body onclick="alert(`버블링은 여기까지 도달하지 못합니다.`)">
  <button onclick="event.stopPropagation()">클릭해 주세요.</button>
</body>
```
- 위의 코드에서 onClick 이벤트는 button 태그까지만 동작하고 body에게 버블링 되지 않는다

<br/>    
<hr/>    
<br/>    

## 이벤트 캡쳐링(Event Capturing)
- 이벤트가 상위 요소에서 하위 요소로 전달되는 관계
- 이벤트 버블링과는 반대로 진행되는 이벤트 전파 방식
- 이벤트 버블링에 비해서 코드상에서 많이 쓰이지 않는다.
  - 하지만 동작하는 걸 확인하고 싶다면?
    ```javascript
    	div.addEventListener('click', logEvent, {
    		capture: true
    	});
    ```
  - addEventListener의 capture 속성 값을 true로 설정한다.

<br/>    
<hr/>    
<br/>    

## 이벤트 위임(Event Delegation)
> 하위 요소에 각각 이벤트를 붙이지 않고 상위 요소에서 하위 요소의 이벤트들을 제어하는 방식

```javascript
<>
  <h1>오늘의 할 일</h1>
  <ul class="itemList">
  	<li>
  		<input type="checkbox" id="item1" onClick={() => alert('일정 완료!')}>
  		<label for="item1">이벤트 버블링 학습</label>
  	</li>
  	<li>
  		<input type="checkbox" id="item2" onClick={() => alert('일정 완료!')}>
  		<label for="item2">이벤트 캡쳐 학습</label>
  	</li>
  </ul>
</>
```
- 위의 예시처럼 input에 onclick 이벤트를 하나하나 넣을 수 있다.
  - 하지만 checkbox가 여러개로 늘어난다면? 모든 체크박스에 이벤트 리스너를 하나하나 다 달아야 할까?

- 이벤트 위임 코드
```javascript
<>
    <h1>오늘의 할 일</h1>
    <ul className="itemList" onClick={(e) => {
        if (e.target.type === 'checkbox') {
            alert('일정 완료!');
        }
    }}>
        <li>
            <input type="checkbox" id="item1" />
            <label htmlFor="item1">이벤트 버블링 학습</label>
        </li>
        <li>
            <input type="checkbox" id="item2" />
            <label htmlFor="item2">이벤트 캡쳐 학습</label>
        </li>
    </ul>
</>
```
- input의 상위 태그인 ul 태그에 onClick 이벤트를 설정해주면 모든 하위 태그에 적용된다

### 이벤트 위임의 장점
- 메모리 효율성: 수백 개의 요소가 있어도 이벤트 리스너는 하나만 필요
- 동적 요소 처리: 나중에 추가되는 요소들도 자동으로 이벤트 적용
- 성능 향상: 이벤트 리스너가 적어 브라우저 성능 개선
- 코드 간소화: 반복적인 이벤트 리스너 등록 코드를 줄일 수 있다

<br/>    
<hr/>    
<br/>    

- 참고자료    
[javascript.info - 버블링과 캡쳐링](https://ko.javascript.info/bubbling-and-capturing)    
[velog - [JavaScript] 이벤트 버블링, 캡쳐링, 위임](https://velog.io/@soulee__/JavaScript-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%B2%84%EB%B8%94%EB%A7%81-%EC%BA%A1%EC%B3%90-%EC%9C%84%EC%9E%84#4-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%9C%84%EC%9E%84---event-delegation)
