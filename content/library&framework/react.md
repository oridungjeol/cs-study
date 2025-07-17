# React 동작 원리

## React 기본 개념
- React : UI를 만들기 위한 JavaScript 라이브러리
- JSX
  - 리액트에서 기존의 로직(JavaScript) / 마크업(HTML) 분리 형태를 보완
  - 마크업과 로직을 둘 다 포함하는 '컴포넌트' 라는 유닛으로 관심사 분리를 함.
  - React에서 JSX 사용이 필수는 아니지만, UI를 다루는 파일에서 로직을 함께 다룰 수 있어 편리함

<br/>     
<hr/>    
<br/>    

- 브라우저는 JSX를 이해하지 못해서 이를 JS로 변환하는 과정이 필요하다

- 우리가 create react app을 하면 index.js에 포함되어 있는 코드
```js
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

- ReactDOM.render를 통해 jsx에서 브라우저가 이해할 수 있는 HTML, CSS, JS로 변환되어 렌더링된다.


<br/>     
<hr/>    
<br/>    

- Element: 화면을 구성하는 가장 작은 단위
```jsx
const element = <h1>안녕!</h1>;
```

- Component: 태그로 이루어진 하나의 독립적인 모듈
  - UI를 만드는 함수 또는 클래스(함수형 컴포넌트, 클래스형 컴포넌트
```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>
}

const element = <Welcome name="이름" />;
```
- 컴포넌트 단위로 화면을 조작할 수 있다

- props: 상위 컴포넌트가 하위 컴포넌트에 내려주는 데이터
```jsx
function Welcome(props) {
  return <h1>안녕, {props.name}!</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="111" />
      <Welcome name="222" />
    </div>
  );
}
```
Welcome 컴포넌트가 2개 있고, props로 각각 111, 222를 전달
코드 실행시 안녕, 111과 안녕, 222가 화면에 렌더링됨

- state: 컴포넌트가 독립적으로 갖는 상태
  - 컴포넌트 내부에서 변경 가능한 데이터
  - 해당 데이터가 변화하면 화면을 다시 그림(리렌더링)
  - state는 useState hook으로 변경 가능
 
<br/>     
<hr/>    
<br/>     

## Virtual DOM
- 기존의 DOM 사용 말고 리액트에서는 Virtual DOM을 사용한다
- 실제 DOM을 조작하지 않고 가상의 DOM 트리를 따로 만들어 조작
- 실제 DOM에는 브라우저가 화면을 그리는데 필요한 모든 정보가 들어있기 때문에 느릴 수 있음
- 이를 보완하기 위해 메모리 상에서 계산할 수 있는 Virtual DOM을 활용
1. UI에 변경사항이 생김(state 변경 등)
2. 해당 변경 사항을 바탕으로 새로운 Virtual DOM 생성
3. 현재 Virtual DOM과 이전 것을 비교하여 차이를 계산(diffing)
4. 바뀐 부분만 실제 DOM 트리에 적용

## 렌더링 과정
1. 작성된 html, css 코드를 DOM, CSSOM으로 분리시킨다
   - 웹 엔진의 HTML/XML 파서가 문서를 파싱해 DOM Tree를, CSS 파서가 CSSOM 트리를 생성
2. 생성된 DOM과 CSSOM으로 렌더링 트리 생성
3. Layout:  페이지 안에 html 요소들이 어떤 위치에 어떤 사이즈로 렌더링 될 것인지 배치를 계산하는 작업
5. Paint: 실제 브라우저 화면에 그리기

## React의 렌더링 과정
1. 렌더링 트리거
   - 초기 렌더링이나 state가 변경되었을 때 일어납니다.
   - 변경이 일어난 컴포넌트를 재호출합니다.
2. React 컴포넌트 렌더링
   - 초기 렌더링에서 React는 루트 컴포넌트를 호출합니다.
   - 이후 렌더링에서 React는 state 업데이트가 일어나 렌더링을 트리거한 컴포넌트를 호출합니다.
3. DOM에 변경사항을 커밋
   - 렌더링이 끝나면 DOM에 변경 사항을 커밋
   - 초기 렌더링이었을 경우, 전체 DOM 커밋
   - 리렌더링의 경우 변경된 최소한의 부분만 커밋(Virtual DOM을 이용한 계산)

[React 입문자라면 꼭 알아야 할 기초 개념 5가지](https://medium.com/amhocode/react-%EC%9E%85%EB%AC%B8%EC%9E%90%EB%9D%BC%EB%A9%B4-%EA%BC%AD-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0-%EA%B8%B0%EC%B4%88-%EA%B0%9C%EB%85%90-5%EA%B0%80%EC%A7%80-component-props-state-life-cycle-lifting-state-up-95a416241ffe)
[React 톺아보기 - 01. Preview](https://goidle.github.io/react/in-depth-react-preview/)
[React, Virtual DOM 기초 동작 원리, 장단점](https://velog.io/@dongjun187/React-Virtual-DOM-%EA%B8%B0%EC%B4%88-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC)
[React JS 의 렌더링 프로세스](https://yngjnhyk.tistory.com/433)
[React Docs - 렌더링 그리고 커밋](https://ko.react.dev/learn/render-and-commit)
