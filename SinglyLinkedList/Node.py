class Node(object):

     def __init__(self,value):

         self.value=value
         self.next_node= None

     def get_value(self):
         return self.value

     def get_next(self):
         return self.next_node