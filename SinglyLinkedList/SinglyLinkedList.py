class SingleyLinkedList(object):

    def __init__(self, node):
        self.head = node
        self.tail = node

    def add_node(self, node):
        self.tail.next_node = node
        self.tail = node

    def print(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.get_value())
            curr_node = curr_node.get_next()

    def cycle_check(self):
        curr_node = self.head
        while curr_node != None:
            if curr_node == curr_node.get_next():
                return True
            curr_node = curr_node.get_next()
        return False

    def reverse_list(self):
        current = self.head
        previous = None
        next = None

        while current != None:
            next = current.next_node
            current.next_node = previous
            previous = current
            current = next
        temp = self.head
        self.head = self.tail
        self.tail = temp

        return previous


    def nth_to_last_node(self,n):
        left_pointer = self.head
        right_pointer = self.head

        for i in range(n - 1):

            # Check for edge case of not having enough nodes!
            if not right_pointer.next_node:
                raise LookupError('Error: n is larger than the linked list.')

            right_pointer = right_pointer.next_node

        while right_pointer.next_node:
            left_pointer = left_pointer.next_node
            right_pointer = right_pointer.next_node

        return left_pointer.value