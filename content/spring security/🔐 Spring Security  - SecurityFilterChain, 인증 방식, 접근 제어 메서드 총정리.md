<p>Spring Security를 적용하면서 가장 기본적이면서도 중요한 개념인 <strong>보안 설정(인증 방식 + 접근 제어)</strong>에 대해 정리한 글입니다.</p>
<p>이 글에서는 다음 내용을 다룹니다:</p>
<ul>
<li><code>SecurityFilterChain</code> 빈이란?</li>
<li><code>formLogin()</code> vs <code>httpBasic()</code>의 차이</li>
<li><code>permitAll()</code>, <code>denyAll()</code>, <code>authenticated()</code> 의미</li>
<li>예제 코드 포함</li>
</ul>
<hr />
<h2 id="🧩-1-사용자-정의-보안-설정을-위한-필수-빈-securityfilterchain">🧩 1. 사용자 정의 보안 설정을 위한 필수 빈: <code>SecurityFilterChain</code></h2>
<p>Spring Security 5.7부터는 <code>WebSecurityConfigurerAdapter</code>가 deprecated 되었고, 대신 <code>SecurityFilterChain</code>을 빈으로 등록해 보안 정책을 설정합니다.</p>
<h3 id="✅-예제-코드">✅ 예제 코드</h3>
<pre><code class="language-java">@Bean
@Order(2147483642)
SecurityFilterChain defaultSecurityFilterChain(HttpSecurity http) throws Exception {
    http
        .authorizeHttpRequests((requests) -&gt;
            ((AuthorizeHttpRequestsConfigurer.AuthorizedUrl) requests.anyRequest()).authenticated()
        );
    http.formLogin(Customizer.withDefaults());
    http.httpBasic(Customizer.withDefaults());
    return http.build();
}</code></pre>
<h3 id="🔍-코드-설명">🔍 코드 설명</h3>
<table>
<thead>
<tr>
<th>구성 요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>@Bean</code></td>
<td>이 보안 필터 체인을 Spring 컨테이너에 등록</td>
</tr>
<tr>
<td><code>@Order(...)</code></td>
<td>필터 체인 우선순위 설정 (숫자 작을수록 우선)</td>
</tr>
<tr>
<td><code>authorizeHttpRequests()</code></td>
<td>요청 경로별 인가 정책 정의</td>
</tr>
<tr>
<td><code>anyRequest().authenticated()</code></td>
<td>모든 요청은 로그인한 사용자만 접근 가능</td>
</tr>
<tr>
<td><code>formLogin()</code></td>
<td>기본 로그인 폼 사용 (<code>/login</code>)</td>
</tr>
<tr>
<td><code>httpBasic()</code></td>
<td>HTTP Basic 인증도 함께 활성화</td>
</tr>
</tbody></table>
<hr />
<h2 id="🔐-2-formlogin-vs-httpbasic-차이점">🔐 2. formLogin() vs httpBasic() 차이점</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th><code>formLogin()</code></th>
<th><code>httpBasic()</code></th>
</tr>
</thead>
<tbody><tr>
<td>인증 방식</td>
<td>HTML 로그인 폼</td>
<td>HTTP 헤더에 ID/PW 전달</td>
</tr>
<tr>
<td>UI 제공</td>
<td>O (사용자 친화적 로그인 화면)</td>
<td>X (브라우저 팝업 또는 API 툴)</td>
</tr>
<tr>
<td>사용 대상</td>
<td>웹 애플리케이션</td>
<td>REST API, 테스트용</td>
</tr>
<tr>
<td>보안 수준</td>
<td>강력 (CSRF, 세션 등)</td>
<td>비교적 낮음 (HTTPS 필수)</td>
</tr>
<tr>
<td>커스터마이징</td>
<td>가능 (로그인 페이지, 실패 시 리디렉션 등)</td>
<td>거의 불가</td>
</tr>
</tbody></table>
<hr />
<h2 id="🛡️-3-접근-제어-메서드-permitall-denyall-authenticated">🛡️ 3. 접근 제어 메서드: <code>permitAll()</code>, <code>denyAll()</code>, <code>authenticated()</code></h2>
<p>Spring Security에서 요청별 접근 권한을 설정할 때 자주 사용되는 메서드들입니다.</p>
<h3 id="✅-permitall">✅ <code>permitAll()</code></h3>
<blockquote>
<p>인증 여부와 관계없이 <strong>모든 사용자에게 접근 허용</strong></p>
</blockquote>
<ul>
<li>정적 리소스(css/js), 로그인/회원가입 페이지 등에 자주 사용됩니다.</li>
</ul>
<h4 id="🔸-예시">🔸 예시</h4>
<pre><code class="language-java">http
  .authorizeHttpRequests(auth -&gt; auth
    .requestMatchers(&quot;/login&quot;, &quot;/signup&quot;, &quot;/css/**&quot;).permitAll()
    .anyRequest().authenticated()
  );</code></pre>
<hr />
<h3 id="⛔-denyall">⛔ <code>denyAll()</code></h3>
<blockquote>
<p>인증 여부에 상관없이 모든 사용자 접근 차단</p>
</blockquote>
<ul>
<li>내부 전용 API, 미완성된 기능, 접근이 금지된 페이지 등에 사용됩니다.</li>
</ul>
<h4 id="🔸-예시-1">🔸 예시</h4>
<pre><code class="language-java">http
  .authorizeHttpRequests(auth -&gt; auth
    .requestMatchers(&quot;/admin/deprecated&quot;, &quot;/dev/hidden&quot;).denyAll()
    .anyRequest().permitAll()
  );</code></pre>
<ul>
<li>위 설정은 /admin/deprecated, /dev/hidden 경로는 어떤 사용자도 접근할 수 없게 만듭니다.</li>
</ul>
<hr />
<h3 id="🔐-authenticated">🔐 <code>authenticated()</code></h3>
<blockquote>
<p>로그인한 사용자만 접근 허용</p>
</blockquote>
<ul>
<li>마이페이지, 결제, 주문 등 민감한 사용자 정보 영역에 사용됩니다.</li>
<li>인증되지 않은 사용자는 로그인 페이지로 리디렉션 되거나 401 에러가 발생합니다.</li>
</ul>
<h4 id="🔸-예시-2">🔸 예시</h4>
<pre><code class="language-java">http
  .authorizeHttpRequests(auth -&gt; auth
    .requestMatchers(&quot;/mypage&quot;, &quot;/account/**&quot;, &quot;/order/**&quot;).authenticated()
    .anyRequest().permitAll()
  );</code></pre>
<ul>
<li>위 설정은 /mypage, /account/<strong>, /order/</strong> 경로는 로그인한 사용자만 접근 가능하게 합니다.</li>
</ul>
<hr />
<h3 id="📋-접근-제어-메서드-요약">📋 접근 제어 메서드 요약</h3>
<table>
<thead>
<tr>
<th>메서드</th>
<th>의미</th>
<th>사용 예</th>
</tr>
</thead>
<tbody><tr>
<td><code>permitAll()</code></td>
<td>누구나 접근 가능</td>
<td>로그인, 회원가입, 정적 리소스</td>
</tr>
<tr>
<td><code>denyAll()</code></td>
<td>모두 접근 차단</td>
<td>폐쇄된 기능, 제한된 관리자 API</td>
</tr>
<tr>
<td><code>authenticated()</code></td>
<td>로그인한 사용자만 접근 가능</td>
<td>마이페이지, 결제, 주문 내역 등</td>
</tr>
</tbody></table>
<hr />
<h2 id="✍️-정리">✍️ 정리</h2>
<ul>
<li><code>SecurityFilterChain</code> 빈을 통해 사용자 정의 보안 설정을 구성합니다.  </li>
<li><code>formLogin()</code>은 로그인 폼 기반 인증, <code>httpBasic()</code>은 HTTP 헤더 기반 인증 방식입니다.  </li>
<li><code>permitAll()</code>은 모든 사용자 접근 허용, <code>denyAll()</code>은 모든 사용자 접근 차단, <code>authenticated()</code>는 로그인한 사용자만 접근 허용합니다.</li>
</ul>
