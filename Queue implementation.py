class queue(object):
    def _init_(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size():
        return len(self.items)