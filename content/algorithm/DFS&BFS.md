# DFS(깊이 우선 탐색)
- 한 노드의 자식을 끝까지 순회한 후 다른 노드 순회
- 스택(LIFO) 사용
- 메모리 효율적

## 구현 코드
```python
def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:  # 방문하지 않았다면
      dfs(graph, i, visited)

#graph 생략(2차원 리스트 가정)
visited = [False] * 9
dfs(graph, 1, visited)
```
ex) 바이러스 문제

# BFS(너비 우선 탐색)
- 한 단계씩 내려가며 **같은 레벨에 있는** 노드 순회
- 큐(FIFO) 사용
- 최단 경로 보장

```python
from collections import deque

def bfs(graph, start, visited)
  queue = deque([start])
  # 현재 노드 방문 처리
  visited[start] = True
  while queue:
    # queue에서 꺼내 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된 노드를 queue에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#graph 생략(2차원 리스트 가정)
visited = [False] * 9
bfs(graph, 1, visited)
```
ex)미로찾기 문제


