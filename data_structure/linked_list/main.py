from circular_linked_list import CList
from doubly_linked_list import DList
from singly_linked_list import SList

if __name__ == "__main__":
    # Singly Linked List
    s = SList()
    s.insert_front("John")
    s.insert_front("Jane")
    s.insert_after("Bob", s.head.next)
    s.insert_front("Sam")
    s.print_list()
    print("Bob은 %d번째" % s.search("Bob"))
    print("Andrew는 ", s.search("Andrew"))
    print("Sam 다음 노드 삭제 후:\t", end="")
    s.delete_after(s.head)
    s.print_list()
    print("첫 노드 삭제 후:\t", end="")
    s.delete_front()
    s.print_list()

    print("-" * 50)
    # Doubly Linked List
    s = DList()
    s.insert_after(s.head, "John")
    s.insert_before(s.tail, "Jane")
    s.insert_before(s.tail, "Bob")
    s.insert_after(s.head.next, "Sam")
    s.print_list()
    print("마지막 노드 삭제 후:\t", end="")
    s.delete(s.tail.prev)
    s.print_list()
    print("맨 끝에 Andrew 삽입 후:\t", end="")
    s.insert_before(s.tail, "Andrew")
    s.print_list()
    print("첫 노드 삭제 후:\t", end="")
    s.delete(s.head.next)
    s.print_list()
    print("첫 노드 삭제 후:\t", end="")
    s.delete(s.head.next)
    s.print_list()
    print("첫 노드 삭제 후:\t", end="")
    s.delete(s.head.next)
    s.print_list()
    print("첫 노드 삭제 후:\t", end="")
    s.delete(s.head.next)
    s.print_list()

    print("-" * 50)
    # Circular Linked List
    s = CList()
    s.insert("John")
    s.insert("Jane")
    s.insert("Bob")
    s.insert("Sam")
    s.print_list()
    print("s의 길이 = ", s.no_items())
    print("s의 첫 항목: ", s.first())
    print("첫 노드 삭제 후:\t", end="")
    s.delete()
    s.print_list()
    print("s의 길이 = ", s.no_items())
    print("s의 첫 항목: ", s.first())
    print("첫 노드 삭제 후:\t", end="")
    s.delete()
    s.print_list()
    print("첫 노드 삭제 후:\t", end="")
    s.delete()
    s.print_list()
    print("첫 노드 삭제 후:\t", end="")
    s.delete()
    s.print_list()
