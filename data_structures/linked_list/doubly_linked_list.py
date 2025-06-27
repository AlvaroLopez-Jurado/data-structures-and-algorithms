class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        new_node = DNode(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def to_list_forward(self):
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def to_list_backward(self):
        result = []
        current = self.head
        if not current:
            return result
        
        while current.next:
            current = current.next

        while current:
            result.append(current.value)
            current = current.prev
        return result