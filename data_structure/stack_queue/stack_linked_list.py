class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1

    def peek(self):
        if self.size != 0:
            return self.top.item
        else:
            return None

    def pop(self):
        if self.size != 0:
            item = self.top.item
            self.top = self.top.next
            self.size -= 1
            return item
        else:
            return None

    def print_stack(self):
        print("top ->\t", end="")
        p = self.top
        while p:
            if p.next != None:
                print(p.item, "-> ", end="")
            else:
                print(p.item, end="")
            p = p.next
        print()
