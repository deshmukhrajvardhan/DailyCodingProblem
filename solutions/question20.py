"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
class Node:
    def __init__(self,value=None,next_p=None):
        self.value=value
        self.next_p=next_p
        
class LList:
    def __init__(self,value=None):
        self.head = Node(value)
        self.current = self.head
        self.ll_len=0
        
    def insert(self,value):
        if self.head==None:
            self.head.value=value
            self.ll_len+=1
        else:
            self.current.next_p = Node(value)
            self.current=self.current.next_p
            self.ll_len+=1
            
def find_el(l1,l2):
    ll1=l1.head
    ll2=l2.head
    ll1_len=l1.ll_len
    ll2_len=l2.ll_len
    while ll1!=None and ll2!=None:
        print("val1:{},val2:{}".format(ll1.value,ll2.value))
        if ll1.value == ll2.value:
            print(ll1.value)
            return ll1.value
        elif ll1_len>ll2_len:
            ll1=ll1.next_p
            ll1_len-=1
        elif ll2_len>ll1_len:
            ll2=ll2.next_p
            ll2_len-=1
        elif ll2_len==ll1_len:
            print("here")
            ll1=ll1.next_p
            ll2=ll2.next_p
    return -1

if __name__=='__main__':
    j=LList(2)
    j.insert(4)
    k=LList(4)
    j.insert(5)
    k.insert(5)
    print(find_el(j,k))
