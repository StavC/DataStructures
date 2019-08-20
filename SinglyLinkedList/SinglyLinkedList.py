class SingleyLinkedList(object):

    def __init__(self,node):
        self.head=node
        self.tail=node

    def add_node(self,node):
        self.tail.next_node=node
        self.tail=node

    def print(self):
        curr_node=self.head
        while curr_node!= None:
            print(curr_node.get_value())
            curr_node=curr_node.get_next()


