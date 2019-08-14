class Deque(object):

     def __init__(self):
        self.items=[]

     def add_front(self,item):
         self.items.append(item)

     def add_back(self,item):
         self.items.insert(0,item)

     def remove_front(self):
         self.items.pop()

     def remove_end(self):
         self.items.pop(0)

     def is_empty(self):
         return self.items==[]

     def size(self):
         return len(self.items)