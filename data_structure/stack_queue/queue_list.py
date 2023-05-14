class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) != 0:
            item = self.queue.pop(0)
            return item
        else:
            return None

    def print_queue(self):
        print("front -> ", end="")
        print(self.queue, end="")
        print(" <- rear")
