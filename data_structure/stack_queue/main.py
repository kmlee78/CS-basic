from collections import deque

from queue_linked_list import Queue as LLQueue
from queue_list import Queue as LQueue
from stack_linked_list import Stack as LLStack
from stack_list import Stack as LStack

if __name__ == "__main__":
    # Stack using list
    stack = LStack()
    stack.push("John")
    stack.push("Jane")
    stack.push("Mary")
    print(stack.stack, "\t<- top")
    print("top 항목:", stack.peek())
    print("Andrew push 후:\t", end="")
    stack.push("Andrew")
    print(stack.stack, "\t<- top")
    stack.pop()
    print("pop 후:\t", end="")
    print(stack.stack, "\t<- top")

    print("-" * 50)
    # Stack using linked list
    stack = LLStack()
    stack.push("John")
    stack.push("Jane")
    stack.push("Mary")
    stack.print_stack()
    print("top 항목:", stack.peek())
    print("Andrew push 후:\t", end="")
    stack.push("Andrew")
    stack.print_stack()
    stack.pop()
    print("pop 후:\t", end="")
    stack.print_stack()

    print("-" * 50)
    # Queue using list
    queue = LQueue()
    queue.add("John")
    queue.add("Jane")
    queue.add("Mary")
    queue.print_queue()
    queue.remove()
    print("remove 후:\t", end="")
    queue.print_queue()
    queue.remove()
    print("remove 후:\t", end="")
    queue.print_queue()
    queue.add("Mike")
    print("Mike add 후:\t", end="")
    queue.print_queue()

    print("-" * 50)
    # Queue using linked list
    queue = LLQueue()
    queue.add("John")
    queue.add("Jane")
    queue.add("Mary")
    queue.print_queue()
    queue.remove()
    print("remove 후:\t", end="")
    queue.print_queue()
    queue.remove()
    print("remove 후:\t", end="")
    queue.print_queue()
    queue.add("Mike")
    print("Mike add 후:\t", end="")
    queue.print_queue()

    print("-" * 50)
    # Deque using collections.deque
    dq = deque("data")
    for elem in dq:
        print(elem.upper(), end="")
    print()
    dq.append("r")
    dq.appendleft("k")
    print(dq)
    dq.pop()  # 맨 뒤의 항목 삭제
    dq.popleft()  # 맨 앞의 항목 삭제
    print(dq[-1])  # 맨 뒤의 항목 출력
    print("x" in dq)
    dq.extend("structure")  # 맨 뒤에 여러 항목 삽입
    dq.extendleft(reversed("python"))  # 맨 앞에 여러 항목 삽입
    print(dq)
