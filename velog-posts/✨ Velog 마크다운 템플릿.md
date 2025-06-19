<hr />
<p>title: &quot;[주제] 제목을 여기에 입력하세요&quot;
description: &quot;이 포스트는 [기술/라이브러리/문제해결]에 대해 다룹니다.&quot;
date: YYYY-MM-DD
tags: [언어, 라이브러리, 주제태그]</p>
<hr />
<h1 id="📌-개요">📌 개요</h1>
<p>해당 포스트에서는 <strong>무엇을 설명할 것인지</strong>,  
<strong>어떤 배경에서 이 주제를 다루게 되었는지</strong>에 대해 간단히 소개합니다.</p>
<blockquote>
<p>이 글은 실제 경험/프로젝트/공부 내용을 바탕으로 작성되었습니다.</p>
</blockquote>
<hr />
<h1 id="🧩-목차">🧩 목차</h1>
<ol>
<li><a href="https://api.velog.io/rss/@yumin991209#%EB%AC%B8%EC%A0%9C-%EC%83%81%ED%99%A9-%EB%98%90%EB%8A%94-%EC%A3%BC%EC%A0%9C-%EC%86%8C%EA%B0%9C">문제 상황 또는 주제 소개</a>  </li>
<li><a href="https://api.velog.io/rss/@yumin991209#%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%EB%98%90%EB%8A%94-%EC%A0%81%EC%9A%A9-%EB%B0%A9%EB%B2%95">해결 방법 또는 적용 방법</a>  </li>
<li><a href="https://api.velog.io/rss/@yumin991209#%EC%BD%94%EB%93%9C-%EC%98%88%EC%8B%9C">코드 예시</a>  </li>
<li><a href="https://api.velog.io/rss/@yumin991209#%EA%B2%B0%EA%B3%BC-%EB%B0%8F-%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8">결과 및 인사이트</a>  </li>
<li><a href="https://api.velog.io/rss/@yumin991209#%EC%B0%B8%EA%B3%A0%EC%9E%90%EB%A3%8C">참고자료</a></li>
</ol>
<hr />
<h1 id="🔍-문제-상황-또는-주제-소개">🔍 문제 상황 또는 주제 소개</h1>
<ul>
<li>겪고 있던 문제 상황  </li>
<li>또는 소개할 개념, 라이브러리, API 등</li>
</ul>
<p>예시:</p>
<blockquote>
<p>Axios를 사용하던 중 요청을 cancel 처리하는 방법이 필요했습니다.</p>
</blockquote>
<hr />
<h1 id="🛠️-해결-방법-또는-적용-방법">🛠️ 해결 방법 또는 적용 방법</h1>
<p>여기에 해결 과정을 단계별로 정리합니다.</p>
<ul>
<li>문제 접근 방식</li>
<li>선택한 도구나 기술</li>
<li>시행착오</li>
</ul>
<pre><code class="language-js">// 예시 코드
import axios from &quot;axios&quot;;

const controller = new AbortController();

axios.get('/api/data', {
  signal: controller.signal
});</code></pre>
<h1 id="💡-코드-예시">💡 코드 예시</h1>
<pre><code class="language-python">def greet(name):
    print(f&quot;Hello, {name}&quot;)</code></pre>
<h1 id="✅-결과-및-인사이트">✅ 결과 및 인사이트</h1>
<ul>
<li><p>결과 요약</p>
</li>
<li><p>적용 후 변화</p>
</li>
<li><p>얻은 교훈이나 느낀 점</p>
</li>
</ul>
<blockquote>
<p>&quot;간단한 AbortController 사용이지만, 사용자 경험이 훨씬 개선되었습니다.&quot;</p>
</blockquote>
<h1 id="📎-참고자료">📎 참고자료</h1>
<ul>
<li><p><a href="https://api.velog.io/rss/@yumin991209#MDN-AbortController">MDN - AbortController</a></p>
</li>
<li><p><a href="https://api.velog.io/rss/@yumin991209#Velog">Velog 마크다운 문법 정리</a></p>
</li>
</ul>