import random


class OpenAddressing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size

    def hash(self, key):
        return key % self.M  # 나눗셈 해시 함수

    def print_table(self):
        for i in range(self.M):
            print("{:4}".format(str(i)), " ", end="")
        print()
        for i in range(self.M):
            print("{:4}".format(str(self.a[i])), " ", end="")
        print()


class LinearProbing(OpenAddressing):
    def __init__(self, size):
        super().__init__(size)

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:  # 삽입 위치 발견
                self.a[i] = key
                self.d[i] = data
                return
            if self.a[i] == key:  # 이미 key 존재하므로 data만 갱신
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j) % self.M  # 다음 원소 검사
            if i == initial_position:  # 원래 위치로 돌아오면 루프 종료(저장 실패)
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:  # 탐색 성공
                return self.d[i]
            i = (initial_position + j) % self.M  # 다음 원소 검사
            j += 1
            if i == initial_position:  # 탐색 실패
                return None
        return None


class QuadProbing(OpenAddressing):
    def __init__(self, size):
        super().__init__(size)
        self.N = 0  # 테이블에 저장된 항목 수

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:  # 삽입 위치 발견
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:  # 이미 key 존재하므로 data만 갱신
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j * j) % self.M  # 다음 원소 검사
            if self.N > self.M:  # 저장된 항목 수가 테이블 크기보다 크면 실패
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j * j) % self.M
            j += 1
        return None


class RandProbing(OpenAddressing):
    def __init__(self, size):
        super().__init__(size)
        self.N = 0

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j = random.randint(0, 99)
            i = (initial_position + j) % self.M
            if self.N > self.M:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        random
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + random.randint(1, 99)) % self.M
            j += 1
        return None
