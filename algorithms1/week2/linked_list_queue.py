class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node

        else:
            self.tail.next = Node(data)
        self.size += 1

    def add_to_head(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            old_head = self.head
            self.head = Node(data)
            self.head.next = old_head
        self.size += 1

    def delete(self, target_data):
        if self.head.data == target_data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.data == target_data:
                    current_node.next = current_node.next.next
                    if current_node.next is None:
                        self.tail = current_node

                    self.size -= 1


class LinkedListQueue:
    def __init__(self):
        self.ll = LinkedList()

    @property
    def size(self):
        return self.ll.size

    def is_empty(self):
        return self.ll.size == 0

    def enqueue(self, data):
        self.ll.add_to_tail(data)

    def dequeue(self):
        if self.is_empty() is False:
            node = self.ll.tail
            self.ll.delete(node.data)
            return node
        else:
            raise Exception("Empty Queue.")


llq = LinkedListQueue()
llq.enqueue(10)
n = llq.dequeue()
print(llq.size)
print(llq.is_empty())
# for i in range(100):
#     llq.enqueue(i)
# print(llq.dequeue().data)


