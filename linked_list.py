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

    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self, head: Node, tail: Node):
        self.len = 2
        self.head = head
        self.head.next_node = tail
        self.tail = tail
        self.tail.prev_node = head

    def remove(self, item: Node):
        indexed_item = self.head
        for _ in range(self.len):
            indexed_item = indexed_item.next_node
            if id(indexed_item) == id(item):
                break
        prev_indexed_item = indexed_item.prev_node
        next_indexed_item = indexed_item.next_node

        prev_indexed_item.next_node = next_indexed_item
        next_indexed_item.prev_node = prev_indexed_item

        self.len -= 1

    def remove_at(self, index: int):
        if index > self.len:
            raise ValueError("index is more than Linked list length")
        indexed_item = self.head
        for i in range(index + 1):
            indexed_item = indexed_item.next_node

        prev_indexed_item = indexed_item.prev_node
        next_indexed_item = indexed_item.next_node

        prev_indexed_item.next_node = next_indexed_item
        next_indexed_item.prev_node = prev_indexed_item

        self.len -= 1

    def insert_at(self, item: Node, index: int):
        if index > self.len:
            raise ValueError("index is more than Linked list length")
        prev_indexed_item = self.head
        for i in range(index):
            prev_indexed_item = prev_indexed_item.next_node
        next_indexed_item = prev_indexed_item.next_node
        item.prev_node = prev_indexed_item
        item.next_node = next_indexed_item
        prev_indexed_item.next_node = item
        next_indexed_item.prev_node = item
        self.len += 1

    def get_length(self) -> int:
        return self.len

    def append(self, node: Node):
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node
        self.len += 1

    def prepend(self, node: Node):
        node.next_node = self.head
        self.head.prev_node = node
        self.head = node
        self.len += 1

    def __str__(self):
        print_buffer = []
        print_buffer2 = []
        current = self.head

        for i in range(self.len):
            print_buffer.append(f" {current} ")
            current = current.next_node
        current = self.tail
        print_buffer.append("\n")
        for i in range(self.len):
            print_buffer2.append(f" {current} ")
            current = current.prev_node
        print_buffer2.reverse()
        print_buffer.extend(print_buffer2)
        return "".join(print_buffer)


n1 = Node("n1")
n2 = Node("n2")
n3 = Node("n3")
n4 = Node("n4")
n5 = Node("n5")
n6 = Node("n6")

m1 = Node("m1")
m2 = Node("m2")
m3 = Node("m3")
m4 = Node("m4")
m5 = Node("m5")
m6 = Node("m6")

llist = LinkedList(head=n1, tail=n2)

llist.append(n3)
llist.append(n4)
llist.append(n5)
llist.append(n6)

llist.prepend(m1)
llist.prepend(m2)
llist.prepend(m3)
llist.prepend(m4)
llist.prepend(m5)
llist.prepend(m6)

print(llist)
bbb = Node("bbb")


llist.insert_at(bbb, 2)

llist.remove(bbb)

print(llist)
