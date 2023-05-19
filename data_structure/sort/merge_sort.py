def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1):  # b 배열에 정렬된 원소 저장
        if i > mid:  # 앞부분이 먼저 소진된 경우
            b[k] = a[j]
            j += 1
        elif j > high:  # 뒷부분이 먼저 소진된 경우
            b[k] = a[i]
            i += 1
        elif a[j] < a[i]:  # 뒷부분 원소가 더 작은 경우
            b[k] = a[j]
            j += 1
        else:  # 앞부분 원소가 더 작은 경우
            b[k] = a[i]
            i += 1
    for k in range(low, high + 1):  # 원래 배열로 복사
        a[k] = b[k]


def merge_sort(a, b, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2  # 중간 인덱스
    merge_sort(a, b, low, mid)  # 앞부분 재귀 호출
    merge_sort(a, b, mid + 1, high)  # 뒷부분 재귀 호출
    merge(a, b, low, mid, high)  # 합병 수행


a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
b = [None] * len(a)
print("정렬 전:\t", end="")
print(a)
merge_sort(a, b, 0, len(a) - 1)
print("정렬 후:\t", end="")
print(a)
