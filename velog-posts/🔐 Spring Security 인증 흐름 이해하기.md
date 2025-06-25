<blockquote>
<p>인증과 인가는 필터 체인에서 시작된다.<br />Spring Security의 필터 기반 흐름과 주요 클래스별 역할을 이해하면 인증 커스터마이징이 쉬워진다.</p>
</blockquote>
<hr />
<h2 id="🔁-인증-흐름-요약">🔁 인증 흐름 요약</h2>
<blockquote>
<p>사용자의 로그인 요청 → 필터 체인에서 가로채기 → 인증 객체 생성 → 인증 처리 위임 → 인증 성공/실패 판단 → 결과 저장 및 응답</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/yumin991209/post/4f03e963-25a0-4331-9a37-96ed593f28d9/image.png" /></p>
<blockquote>
<p>출처: <a href="https://www.udemy.com/course/spring-security-6-jwt-oauth2-korean/?couponCode=ST16MT230625G2">Udemy 강의: Spring Security 6 | JWT &amp; OAuth2 | 실전 프로젝트로 배우는 보안</a></p>
</blockquote>
<ol>
<li>사용자가 보호된 API에 접근 시도  </li>
<li>Security의 필터 체인이 요청을 가로챔  </li>
<li>인증되지 않은 사용자면 로그인 페이지로 리다이렉트  </li>
<li>아이디/비밀번호를 기반으로 인증 객체 생성  </li>
<li>AuthenticationManager가 인증 처리 위임  </li>
<li>UserDetailsService, PasswordEncoder를 통해 실제 인증 진행  </li>
<li>인증 성공 시 SecurityContext에 저장 → 세션 유지  </li>
<li>인증 실패 시 로그인 페이지 or 오류 메시지 반환  </li>
</ol>
<hr />
<h2 id="📌-주요-컴포넌트-설명">📌 주요 컴포넌트 설명</h2>
<h3 id="🔐-필터-체인">🔐 필터 체인</h3>
<ul>
<li><p><code>SecurityFilterChain</code><br />→ HTTP 요청이 컨트롤러에 도달하기 전에 여러 개의 보안 관련 필터들이 순차적으로 요청을 검사하고 가공하는 구조. 모든 요청은 이 체인을 거친다.</p>
</li>
<li><p><code>UsernamePasswordAuthenticationFilter</code><br />→ 로그인 요청을 가로채 아이디/비밀번호 추출, 인증 객체 생성</p>
</li>
<li><p><code>DefaultLoginPageGeneratingFilter</code><br />→ 인증되지 않은 사용자를 로그인 페이지로 보냄</p>
</li>
<li><p><code>AuthorizationFilter</code><br />→ 권한이 없는 요청 시 <code>AccessDeniedException</code> 발생</p>
</li>
</ul>
<h3 id="🧪-인증-처리-구성요소">🧪 인증 처리 구성요소</h3>
<table>
<thead>
<tr>
<th>구성 요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>AuthenticationManager</code></td>
<td>인증 처리 담당, 내부적으로 <code>ProviderManager</code> 사용</td>
</tr>
<tr>
<td><code>DaoAuthenticationProvider</code></td>
<td>인증을 실제로 수행하는 Provider</td>
</tr>
<tr>
<td><code>UserDetailsService</code></td>
<td>사용자 정보 로드 (ex. DB, 메모리 등)</td>
</tr>
<tr>
<td><code>PasswordEncoder</code></td>
<td>비밀번호 암호화/비교</td>
</tr>
<tr>
<td><code>Authentication</code></td>
<td>인증 정보를 담은 객체 (id, pw, 인증 여부 등)</td>
</tr>
<tr>
<td><code>SecurityContextHolder</code></td>
<td>인증 객체를 보관 (ThreadLocal 기반)</td>
</tr>
</tbody></table>
<hr />
<h2 id="1-권한-없이-보호된-페이지에-접근할-때">1. 권한 없이 보호된 페이지에 접근할 때</h2>
<ul>
<li><p><strong>AuthorizationFilter</strong>  </p>
<ul>
<li>사용자가 보호된 API에 요청을 보내면 권한이 있는지 판단  </li>
<li>권한이 없으면 <code>AccessDeniedException</code> 예외 발생</li>
</ul>
</li>
<li><p><strong>AccessDeniedException 발생 시</strong>  </p>
<ul>
<li><code>DefaultLoginPageGeneratingFilter</code>가 실행되어 로그인 페이지로 리다이렉트  </li>
<li>이 필터는 <code>doFilter()</code> 메서드 내에서 리다이렉션 작업을 수행함</li>
</ul>
</li>
</ul>
<hr />
<h2 id="2-인증-요청을-처리하는-필터-및-추상-클래스">2. 인증 요청을 처리하는 필터 및 추상 클래스</h2>
<ul>
<li><p><strong>AbstractAuthenticationProcessingFilter</strong>  </p>
<ul>
<li>로그인 등 인증 요청을 처리하는 추상 필터 클래스  </li>
<li>이를 상속받아 인증 관련 필터들이 구현됨</li>
</ul>
</li>
<li><p><strong>UsernamePasswordAuthenticationFilter</strong>  </p>
<ul>
<li>위 추상 클래스를 상속한 필터  </li>
<li>로그인 시도 시 <code>attemptAuthentication()</code> 메서드에서 아이디, 비밀번호 추출  </li>
<li>인증 객체(<code>UsernamePasswordAuthenticationToken</code>)를 생성해 인증 매니저에 전달</li>
</ul>
</li>
</ul>
<pre><code class="language-java">@Override
public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response) throws AuthenticationException {
    // POST 요청 검사 (기본 설정)
    if (this.postOnly &amp;&amp; !request.getMethod().equals(&quot;POST&quot;)) {
        throw new AuthenticationServiceException(&quot;Authentication method not supported: &quot; + request.getMethod());
    }

    // 사용자 입력값 읽기
    String username = obtainUsername(request);
    username = (username != null) ? username.trim() : &quot;&quot;;
    String password = obtainPassword(request);
    password = (password != null) ? password : &quot;&quot;;

    // 인증 전 토큰 생성
    UsernamePasswordAuthenticationToken authRequest = UsernamePasswordAuthenticationToken.unauthenticated(username, password);

    // 추가 정보 설정 (IP, 세션 등)
    setDetails(request, authRequest);

    // AuthenticationManager에 인증 위임
    return this.getAuthenticationManager().authenticate(authRequest);
}</code></pre>
<hr />
<h2 id="3-인증-객체와-매니저">3. 인증 객체와 매니저</h2>
<ul>
<li><p><strong>UsernamePasswordAuthenticationToken</strong>  </p>
<ul>
<li><code>Authentication</code> 인터페이스 구현체  </li>
<li>사용자 이름, 비밀번호, 인증 성공 여부 등 인증 정보를 담음</li>
</ul>
</li>
<li><p><strong>Authentication</strong>  </p>
<ul>
<li>인증 정보를 담는 인터페이스  </li>
<li>구현체가 다양하며 인증 상태, 권한 등을 포함</li>
</ul>
</li>
<li><p><strong>ProviderManager</strong>  </p>
<ul>
<li><code>AuthenticationManager</code> 구현 클래스  </li>
<li>직접 인증을 수행하지 않고 여러 <code>AuthenticationProvider</code>에 인증을 위임  </li>
<li><code>authenticate()</code> 메서드로 인증 흐름 제어</li>
</ul>
</li>
</ul>
<hr />
<h2 id="4-실제-인증-처리-및-사용자-정보-관리">4. 실제 인증 처리 및 사용자 정보 관리</h2>
<ul>
<li><p><strong>DaoAuthenticationProvider</strong>  </p>
<ul>
<li>기본 인증 제공자 구현체  </li>
<li><code>authenticate()</code> 메서드에서 사용자 인증(비밀번호 검증 등)을 수행</li>
</ul>
</li>
<li><p><strong>InMemoryUserDetailsManager</strong>  </p>
<ul>
<li>메모리 기반 사용자 정보 관리 구현체  </li>
<li><code>loadUserByUsername()</code> 메서드로 사용자 상세 정보 반환</li>
</ul>
</li>
<li><p><strong>PasswordEncoder</strong>  </p>
<ul>
<li>입력 비밀번호와 저장된 비밀번호를 비교하는 역할  </li>
<li>일치 시 <code>true</code>, 불일치 시 <code>false</code> 반환</li>
</ul>
</li>
</ul>
<pre><code class="language-java">  @Override
public Authentication authenticate(Authentication authentication) throws AuthenticationException {
    String username = authentication.getName();
    String presentedPassword = authentication.getCredentials().toString();

    // UserDetailsService로 사용자 정보 조회
    UserDetails user = userDetailsService.loadUserByUsername(username);

    // 비밀번호 검증
    if (!passwordEncoder.matches(presentedPassword, user.getPassword())) {
        throw new BadCredentialsException(&quot;Invalid password&quot;);
    }

    // 인증 성공 토큰 생성 (인증 완료 상태, 권한 포함)
    return new UsernamePasswordAuthenticationToken(user, presentedPassword, user.getAuthorities());</code></pre>
<hr />
<h2 id="5-인증-결과-저장-및-로그인-상태-유지">5. 인증 결과 저장 및 로그인 상태 유지</h2>
<p>인증이 성공하면, <code>AuthenticationProvider</code>는 인증이 완료된 <code>Authentication</code> 객체를 반환합니다.  </p>
<p>이 객체는 최종적으로 <code>SecurityContextHolder</code>에 저장되며, 로그인 상태가 유지되는 핵심 역할을 합니다.</p>
<pre><code class="language-java">SecurityContextHolder.getContext().setAuthentication(authenticatedToken);</code></pre>
<p><code>SecurityContextHolder</code>는 인증 정보를 담고 있는 <strong>보안 컨텍스트를 저장하는 정적 클래스</strong></p>
<p>여기에 인증 정보가 저장되면,<br />이후 사용자의 모든 요청에서 <strong>현재 로그인된 사용자 정보를 참조</strong>할 수 있게 됨</p>
<p>즉, 한 번 로그인에 성공하면<br />세션을 통해 인증 정보가 유지되며 계속해서 <strong>인증된 상태로 동작</strong>할 수 있도록 도와주는 핵심적인 역할을 함.</p>
<p>💡 추가로, 이 작업은 <code>UsernamePasswordAuthenticationFilter</code>에서 인증이 완료된 후,<br /><code>SecurityContextPersistenceFilter</code>에 의해 자동으로 세션에 저장됩니다.</p>
<hr />
<h2 id="➕-세션을-통한-로그인-상태-유지-흐름">➕ 세션을 통한 로그인 상태 유지 흐름</h2>
<p>스프링 시큐리티는 한 번 로그인에 성공하면,<br />사용자가 다시 요청을 보낼 때도 <strong>세션에 저장된 인증 정보를 활용</strong>해 로그인 상태를 유지함</p>
<p>세션을 통한 로글인 상태 유지 흐름 :</p>
<ol>
<li><p>사용자가 로그인하면<br />👉 인증이 완료된 <code>Authentication</code> 객체가 생성되고<br />👉 <code>SecurityContextHolder</code>에 저장</p>
</li>
<li><p>필터 체인 마지막에 있는 <code>SecurityContextPersistenceFilter</code>가  
👉 이 인증 정보를 <strong>세션(HttpSession)</strong> 에 저장</p>
</li>
<li><p>이후 사용자가 다른 요청을 보낼 때<br />👉 요청이 시작되면 <code>SecurityContextPersistenceFilter</code>가  
👉 세션에 저장된 인증 정보를 꺼내 <code>SecurityContextHolder</code>에 다시 넣어줌</p>
</li>
<li><p>이렇게 하면 컨트롤러나 서비스 단에서<br />👉 현재 로그인한 사용자 정보를 항상 사용할 수 있게 됨</p>
</li>
</ol>
<pre><code class="language-java">// 인증된 사용자 정보 접근 예시
Authentication auth = SecurityContextHolder.getContext().getAuthentication();
String username = auth.getName(); // 현재 로그인한 사용자 이름</code></pre>
<hr />
<h2 id="✍️-요약">✍️ 요약</h2>
<ul>
<li>권한 검증 → <code>AuthorizationFilter</code>  </li>
<li>인증 시도 → <code>UsernamePasswordAuthenticationFilter</code> → <code>ProviderManager</code> → <code>AuthenticationProvider</code> → <code>UserDetailsService</code> → <code>PasswordEncoder</code>  </li>
<li>인증 결과 → <code>SecurityContextHolder</code>에 저장  </li>
</ul>
<hr />
<h2 id="📚-참고출처">📚 참고/출처</h2>
<ul>
<li><a href="https://www.udemy.com/course/spring-security-6-jwt-oauth2-korean/?couponCode=ST16MT230625G2">Udemy 강의: Spring Security 6 | JWT &amp; OAuth2 | 실전 프로젝트로 배우는 보안</a></li>
</ul>