from typing import Counter


class DLLNode:
    def _init_(self,d):
        self.head=None
        self.data=d
        self.prev=None

class mystack:
    def _init_(self):
        self.head=None
        self.count=0
        self.middle=None

def createmystack():
    ms = myStack()
    ms.count = 0
    return ms

def push(ms,newdata):
    new_DLLNode = DLLNode(new_data)
    new_DLLNode.prev=None
    new_DLLNode.next=ms.head
    ms.count = ms.count + 1
    if(ms.count==1):
        return -1
    else:
        ms.prev=new_DLLNode
        if ms.count % 2 != 0:
            ms.mid=ms.mid.prev
    ms.head=new_DLLNode

def pop(ms):
    if ms.count==0:
        print("Stack is empty")
        return -1
    head=ms.head
    item=head.data
    ms.head=head.next
    if(ms.head != None):
        ms.head.prev = None
    ms.count -= 1
    if(ms.count % 2 == 0):
        ms.mid = ms.mid.next
    return item

def findMiddle(ms):
    if(ms.count == 0):
        print("Stack is empty now")
        return -1
    return ms.mid.data
