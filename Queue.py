class Queue(object):

    def __init__(self):
        self.items=[]


    def is_empty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop(len(self.items)-1)

    def size(self):
        return len(self.items)