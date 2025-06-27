class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SimplyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def delete_value(self, value):
        if not self.head:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        prev, current = self.head, self.head.next
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev, current = current, current.next