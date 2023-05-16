from binary_tree import BinaryTree


class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(BinaryTree):
    def __init__(self) -> None:
        self.root = None

    def get(self, key):
        return self.get_item(self.root, key)

    def get_item(self, node, key):
        if node is None:  # 탐색 실패
            return None
        if node.key > key:  # 왼쪽 서브트리 탐색
            return self.get_item(node.left, key)
        elif node.key < key:  # 오른쪽 서브트리 탐색
            return self.get_item(node.right, key)
        else:  # 탐색 성공
            return node.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, node, key, value):
        if node is None:
            return Node(key, value)
        if node.key > key:  # 왼쪽 서브트리에 삽입
            node.left = self.put_item(node.left, key, value)
        elif node.key < key:  # 오른쪽 서브트리에 삽입
            node.right = self.put_item(node.right, key, value)
        else:  # 노드의 value만 갱신
            node.value = value
        return node

    def min(self):
        if self.root is None:
            return None
        return self.minimum(self.root)

    def minimum(self, node):
        if node.left is None:
            return node
        return self.minimum(node.left)

    def delete_min(self):
        if self.root is None:
            print("트리가 비어있습니다.")
            return
        self.root = self.del_min(self.root)

    def del_min(self, node):
        if node.left is None:
            return node.right  # 최솟값을 가진 노드의 오른쪽 자식을 반환
        node.left = self.del_min(node.left)
        return node

    def delete(self, key):
        self.root = self.del_node(self.root, key)

    def del_node(self, node, key):
        if node is None:
            return None
        if node.key > key:
            node.left = self.del_node(node.left, key)
        elif node.key < key:
            node.right = self.del_node(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            target = node  # 삭제될 노드
            node = self.minimum(target.right)
            node.right = self.del_min(target.right)
            node.left = target.left
        return node
