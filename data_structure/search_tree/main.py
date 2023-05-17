from avl_tree import AVLTree
from binary_search_tree import BinarySearchTree

if __name__ == "__main__":
    # Binary search tree
    t = BinarySearchTree()
    t.put(500, "apple")
    t.put(600, "banana")
    t.put(200, "melon")
    t.put(100, "orange")
    t.put(400, "lime")
    t.put(250, "kiwi")
    t.put(150, "grape")
    t.put(800, "peach")
    t.put(700, "cherry")
    t.put(50, "pear")
    t.put(350, "lemon")
    t.put(10, "plum")
    print("전위순회:\t", end="")
    t.preorder(t.root)
    print("\n중위순회:\t", end="")
    t.inorder(t.root)
    print("\n250: ", t.get(250))
    t.delete(200)
    print("200 삭제 후: ")
    print("전위순회:\t", end="")
    t.preorder(t.root)
    print("\n중위순회:\t", end="")
    t.inorder(t.root)

    print()
    print("-" * 50)
    # AVL tree
    t = AVLTree()
    t.put(75, "apple")
    t.put(80, "grape")
    t.put(85, "lime")
    t.put(20, "mango")
    t.put(10, "strawberry")
    t.put(50, "banana")
    t.put(30, "cherry")
    t.put(40, "watermelon")
    t.put(70, "melon")
    t.put(90, "plum")
    print("전위순회:\t", end="")
    t.preorder(t.root)
    print("\n중위순회:\t", end="")
    t.inorder(t.root)
    print("\n75와 85 삭제 후:")
    t.delete(75)
    t.delete(85)
    print("전위순회:\t", end="")
    t.preorder(t.root)
    print("\n중위순회:\t", end="")
    t.inorder(t.root)
