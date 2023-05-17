from binary_search_tree import BinarySearchTree


class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class AVLTree(BinarySearchTree):
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def put(self, key, value):  # 삽입 연산
        self.root = self.put_item(self.root, key, value)

    def put_item(self, node, key, value):
        if node is None:
            return Node(key, value, 1)
        if node.key > key:
            node.left = self.put_item(node.left, key, value)
        elif node.key < key:
            node.right = self.put_item(node.right, key, value)
        else:
            node.value = value
            return node
        # 노드의 height 갱신
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self.balance(node)  # 노드의 균형 유지

    def balance(self, node):  # 불균형 처리
        if self.bf(node) > 1:
            if self.bf(node.left) < 0:  # 왼쪽 자식의 오른쪽 서브트리가 높은 경우
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        elif self.bf(node) < -1:
            if self.bf(node.right) > 0:  # 오른쪽 자식의 왼쪽 서브트리가 높은 경우
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
        return node

    def bf(self, node):  # 노드의 왼쪽 서브트리와 오른쪽 서브트리의 높이 차이
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        # 노드의 height 갱신
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        # 노드의 height 갱신
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def delete(self, key):
        super().delete(key)
        self.root = self.balance(self.root)
