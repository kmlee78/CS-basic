## 요약
- 이진탐색트리는 이진탐색의 개념을 트리 형태의 구조에 접목시킨 자료구조이다.
- 이진탐색트리는 이진트리로서 각 노드 n의 키가 n의 왼쪽 서브트리에 있는 노드들의 키들보다 크고, n의 오른쪽 서브트리에 있는 노드들의 키들보다 작다.
- 이진탐색트리의 삭제는 삭제할 노드가 자식이 없는 경우, 하나인 경우, 둘인 경우로 나누어 진다. 자식이 둘인 경우는 중위 후속자를 삭제할 노드로 이동하여 삭제를 수행한다.
- 이진탐색트리의 탐색, 삽입, 삭제 연산의 수행시간은 각각 트리 높이에 비례한다.
- AVL 트리는 임의의 노드 n에 대해 노드 n의 왼쪽 서브트리의 높이와 오른쪽 서브트리의 높이 차이가 1을 넘지 않는 이진탐색트리이다.
- AVL 트리는 트리가 한쪽으로 치우쳐 자라나는 것을 LL, RR, LR, RL 회전 연산들을 통해 조절하여 트리 높이의 균형을 유지하는 이진탐색트리이다.
- AVL 트리의 탐색, 삽입, 삭제 연산의 수행시간은 각각 O(logN)이다.
- 2-3 트리는 내부노드의 차수가 2 또는 3인 완전 균형탐색트리다. 삽입에는 분리 연산들 사용하고, 삭제에는 이동 연산과 통합 연산을 사용하여 트리의 완전한 균형을 유지한다.
- 2-3 트리의 탐색, 삽입, 삭제 연산의 수행시간은 각각 트리의 높이에 비례하므로 O(logN)이다.
- 2-3-4 트리는 2-3 트리를 확장한 트리로 4-노드까지 허용한다. 2-3트리보다 높이가 낮아서 보다 빠른 탐색, 삽입, 삭제 연산이 실행된다. 그러나 2-3-4 트리의 각 연산의 이론적인 수행시간은 2-3 트리의 경우와 동일한 O(logN)이다.
- 2-3-4 트리에서는 루트로부터 이파리노드로 한 번만 내려가며 미리 분리 또는 통합 연산을 수행하는 효율적인 삽입 및 삭제가 가능하다.
- 레드블랙트리는 노드의 색을 이용하여 트리의 균형을 유지하며, 탐색, 삽입, 삭제 연산의 수행시간이 각각 O(logN)을 넘지 않는 매우 효율적인 자료구조이다.
- 좌편향 레드블랙트리는 삽입이나 삭제 시 고려해야 하는 경우의 수가 매우 작고 프로그램의 길이도 일반 레드블랙트리 프로그램의 1/5 정도에 불과하다.
- N개의 노드를 가진 레드블랙트리의 높이는 2logN보다 크지 않다. 탐색, 삽입, 삭제 연산의 수행시간은 각각 트리의 높이에 비례하므로 O(logN)이다.
- B-트리는 다수의 키를 가진 노드로 구성되어 다방향 탐색이 가능한 완전 균형트리이다.
- 차수가 M인 B-트리의 모든 이파리노드들은 동일한 깊이를 갖고, 각 내부노드의 자식 수는 M/2이상 M 이하이며, 루트의 자식 수는 2 이상이다.
- B-트리의 삽입과 삭제는 분리, 이동, 통합 연산을 사용한다.
- B*-트리는 B-트리로서 루트를 제외한 다른 노드의 자식 수가 2/3M~M이어야 한다. B*-트리는 노드의 공간을 B-트리보다 효율적으로 사용한다.
- B+-트리는 키들 만을 가지고 B-트리를 만들고, 이파리노드에 키와 관련된 정보를 저장한다.
- B-트리는 몇 개의 디스크 페이지(블록)를 메인 메모리로 읽어 들이는지가 더 중요하므로 1개의 노드가 1개의 디스크 페이지에 맞도록 차수 M을 정한다.

---
main.py 실행 결과
```
전위순회:       500  200  100  50  10  150  400  250  350  600  800  700  
중위순회:       10  50  100  150  200  250  350  400  500  600  700  800  
250:  kiwi
200 삭제 후: 
전위순회:       500  250  100  50  10  150  400  350  600  800  700  
중위순회:       10  50  100  150  250  350  400  500  600  700  800
--------------------------------------------------
전위순회:       75  40  20  10  30  50  70  85  80  90  
중위순회:       10  20  30  40  50  70  75  80  85  90  
75와 85 삭제 후:
전위순회:       40  20  10  30  80  50  70  90  
중위순회:       10  20  30  40  50  70  80  90
```