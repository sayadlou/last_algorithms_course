from __future__ import annotations


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

    def __repr__(self) -> str:
        return f"{self.value}"


class Stack:
    def __init__(self):
        self.length = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def push(self, node: Node):
        if self.length < 1:
            self.tail = self.head = node
            self.head.next_node = node
            self.tail.prev_node = node
            self.length = 1
        else:
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node
            self.length += 1

    def pop(self) -> Node | None:
        if self.length > 1:
            temp = self.head
            self.head = self.head.next_node
            self.length -= 1
            return temp
        return None

    def print(self):
        print_buffer = []
        current = self.head

        for i in range(self.length):
            print_buffer.append(f" {current} ")
            current = current.next_node
        print_buffer.append("\n")
        print("".join(print_buffer))


n1 = Node("n1")
n2 = Node("n2")
n3 = Node("n3")
n4 = Node("n4")
n5 = Node("n5")
n6 = Node("n6")

s = Stack()
s.push(n1)
s.push(n2)
s.push(n3)
s.push(n4)
s.push(n5)
s.print()
s.pop()
s.pop()
s.pop()
s.pop()
s.print()
