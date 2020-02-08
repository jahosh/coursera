
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            old_head = self.head
            self.head = node
            self.head.next = old_head

    def add_to_tail(self, data):
        if self.head is None:
            self.add_to_head(self, data)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)

    def delete(self, target_data):
        if self.head.data == target_data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.data == target_data:
                    current_node.next = current_node.next.next


class LinkedListStack:
    def __init__(self):
        self.list = LinkedList()
        self.size = 0

    def push(self, data):
        self.list.add_to_head(data)
        self.size += 1

    def pop(self):
        data = self.list.head.data
        self.list.delete(data)
        self.size -= 1
        return data

    def is_empty(self):
        return self.size == 0


lls = LinkedListStack()
for i in range(20):
    lls.push(i)

print(lls.pop())
print(lls.size)

