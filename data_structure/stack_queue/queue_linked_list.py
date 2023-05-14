class Node:
    def __init__(self, item, n):
        self.item = item
        self.next = n


class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def add(self, item):
        new_node = Node(item, None)
        if self.size == 0:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def remove(self):
        if self.size != 0:
            item = self.front.item
            self.front = self.front.next
            self.size -= 1
            if self.size == 0:
                self.rear = None
            return item
        else:
            return None

    def print_queue(self):
        p = self.front
        print("front: ", end="")
        while p:
            if p.next != None:
                print(p.item, "-> ", end="")
            else:
                print(p.item, end="")
            p = p.next
        print(" :rear")
