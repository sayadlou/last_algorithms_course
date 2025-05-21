from __future__ import annotations

from copy import copy


class Node:
    def __init__(self, value, next_node: Node | None = None, prev_nod: Node | None = None):
        self._value = value
        self.next_node = next_node
        self.prev_node = prev_nod

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return f"{self.value}"


class Queue:
    def __init__(self):
        self.length = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def enqueue(self, item: Node):
        if self.length < 1:
            self.tail = self.head = item
            self.head.next_node = self.tail
            self.tail.prev_node = self.head
            self.length = 1
        else:
            item.prev_node = self.tail
            self.tail.next_node = item
            self.tail = item
            self.length += 1

    def deque(self) -> Node | None:
        temp = self.head
        self.head = self.head.next_node
        self.length -= 1

    def peek(self) -> Node:
        pass

    def print(self):
        print_buffer = []
        current = self.head

        for i in range(self.length):
            print_buffer.append(f" {current} ")
            current = current.next_node
        print_buffer.append("\n")
        print("".join(print_buffer))


q = Queue()
n1 = Node("n1")
n2 = Node("n2")
n3 = Node("n3")
n4 = Node("n4")
n5 = Node("n5")
n6 = Node("n6")
q.enqueue(n1)
q.enqueue(n2)
q.enqueue(n3)
q.enqueue(n4)
q.enqueue(n5)
q.enqueue(n1)
q.enqueue(n2)
q.enqueue(n3)
q.enqueue(n4)
q.enqueue(n5)
q.print()
q.deque()
q.print()
