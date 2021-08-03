class stack(object):
    def _init_(self):
        self.items=[]
    
    def push(self):
        self.items.append()

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items(len(self.items)-1)

    def size(self):
        return len(self.items)