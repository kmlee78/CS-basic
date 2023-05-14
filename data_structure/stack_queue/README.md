## 요약
- 스택은 한 쪽 끝에서만 항목을 삭제하거나 새로운 항목을 저장하는 후입선출(LIFO) 자료구조이다.
- 스택은 컴파일러의 괄호 짝 맞추기, 회문 검사하기, 미로 찾기, 트리의 노드 방문, 그래프의 깊이 우선 탐색 등에 사용된다. 또한 프로그래밍에서 매우 중요한 함수 호출도 스택 자료구조를 바탕으로 구현된다.
- 큐는 삽입과 삭제가 양 끝에서 각각 수행되는 선입선출(FIFO) 자료구조이다.
- 큐는 CPU의 태스크 스케줄링, 네트워크 프린터, 실시간 시스템의 인터럽트 처리, 다양한 이벤트 구동 방식 컴퓨터 시뮬레이션, 콜 센터의 전화 서비스 등에 사용되며, 이진트리의 레벨 순회와 그래프의 너비 우선 탐색 등에도 사용된다.
- 데크는 양쪽 끝에서 삽입과 삭제를 허용하는 자료구조로서 스택과 큐 자료구조를 혼합한 자료구조이다.
- 데크는 스크롤, 문서 편집기의 undo/redo, 웹 브라우저의 방문 기록 등에 사용된다.

<스택, 큐, 데크 자료구조의 구현방법에 따른 연산 수행시간 비교>
- 파이썬 리스트: 삽입 삭제 모두 **O(n)**
- 연결 리스트: 삽입 삭제 모두 **O(1)**
---
main.py 실행 결과
```
['John', 'Jane', 'Mary']        <- top
top 항목: Mary
Andrew push 후: ['John', 'Jane', 'Mary', 'Andrew']      <- top
pop 후: ['John', 'Jane', 'Mary']        <- top
--------------------------------------------------
top ->  Mary -> Jane -> John
top 항목: Mary
Andrew push 후: top ->  Andrew -> Mary -> Jane -> John
pop 후: top ->  Mary -> Jane -> John
--------------------------------------------------
front -> ['John', 'Jane', 'Mary'] <- rear
remove 후:      front -> ['Jane', 'Mary'] <- rear
remove 후:      front -> ['Mary'] <- rear
Mike add 후:    front -> ['Mary', 'Mike'] <- rear
--------------------------------------------------
front: John -> Jane -> Mary :rear
remove 후:      front: Jane -> Mary :rear
remove 후:      front: Mary :rear
Mike add 후:    front: Mary -> Mike :rear
--------------------------------------------------
DATA
deque(['k', 'd', 'a', 't', 'a', 'r'])
a
False
deque(['p', 'y', 't', 'h', 'o', 'n', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e'])
```