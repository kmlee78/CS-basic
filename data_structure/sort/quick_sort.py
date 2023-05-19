def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot - 1)
        qsort(a, pivot + 1, high)


def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:  # a[i]가 피벗보다 작으면 i 증가
            i += 1
        while j > pivot and a[j] > a[pivot]:  # a[j]가 피벗보다 크면 j 감소
            j -= 1
        if j <= i:  # 루프 중단
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    return j


a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print("정렬 전:\t", end="")
print(a)
qsort(a, 0, len(a) - 1)
print("정렬 후:\t", end="")
print(a)
