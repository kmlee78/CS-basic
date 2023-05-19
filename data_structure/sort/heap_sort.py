def down_heap(i, size):  # 루트로 올라온 키에 대해 힙속성을 회복시킴
    while 2 * i <= size:
        k = 2 * i
        if k < size and a[k] < a[k + 1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k


def create_heap(a):  # 정렬하기 전에 최대힙 만들기
    hsize = len(a) - 1
    for i in reversed(range(1, hsize // 2 + 1)):
        down_heap(i, hsize)


def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]  # 루트와 힙의 마지막 항목 교환
        down_heap(1, N - 1)
        N -= 1  # 힙 크기 1 감소


a = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print("정렬 전:\t", end="")
print(a)
create_heap(a)
print("최대힙:\t", end="")
print(a)
heap_sort(a)
print("정렬 후:\t", end="")
print(a)

print("-" * 50)
print("heapq 모듈을 이용한 힙 정렬")
import heapq

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print("정렬 전:\t", a)
heapq.heapify(a)  # 최소힙 만들기
print("최소힙:\t", a)
result = []
while a:
    result.append(heapq.heappop(a))
print("정렬 후:\t", result)
