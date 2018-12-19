class Node:
    def __init__ (self,data=None):
        self.data=data
        self.next=None
        self.prev=None
    
class DoubleLL:
    def __init__(self):
        self.head=Node()
        self.tail=None
        
    def insert(self, data):
        if self.head.next is None:
            node=Node(data)
            self.head.next=node
            node.prev=self.head
            self.tail=node
        else:
            node = Node(data)
            self.head.next.prev = node
            node.prev = self.head
            node.next = self.head.next
            self.head.next = node

    def pop(self):
        if self.head.next is not None and self.tail is not None:
            node = self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            data = node.data
            del node
            return data
        
    def __str__(self):
        curr=self.head.next
        string=''
        while curr is not None:
            string+="{}".format(curr.data)
            string+='->'
            curr=curr.next
        return string
            
class LRU:
    def __init__(self):
        self.double_ll=DoubleLL()
        self.data_addr=dict()
        self.size_limit=5
        self.curr_size=0
        
    def hit(self,data):
        if self.data_addr and data in self.data_addr:
            ##
            hit_node=self.data_addr[data]
            #print("{}hit{} :{}".format(hit_node.prev.data,hit_node.data,hit_node.next.data))
            if hit_node.prev is self.double_ll.head:
                print("1st already :{}".format(data))
                return
            elif hit_node.next:
                hit_node.prev.next=hit_node.next
                hit_node.next.prev=hit_node.prev
                hit_node.prev=self.double_ll.head
                hit_node.next = self.double_ll.head.next
                self.double_ll.head.next.prev=hit_node
                self.double_ll.head.next = hit_node
                print("updating hit :{}".format(data))
            else:
                hit_node.prev.next=hit_node.next
                hit_node.prev=self.double_ll.head
                hit_node.next = self.double_ll.head.next
                self.double_ll.head.next.prev=hit_node
                self.double_ll.head.next = hit_node
                print("tail node hit :{}".format(data))
                
        else:
            if self.curr_size <= self.size_limit:
                ##
                self.double_ll.insert(data)
                self.data_addr[data]=self.double_ll.head.next
                self.curr_size+=1
                print("new entry :{}, addr:{}".format(data,self.data_addr[data].data))
            else:
                data=self.double_ll.pop()
                del self.data_addr[data]
                print("deleting due to overflow:{}".format(data))
                self.curr_size-=1
                self.hit(data)
        
    def __str__(self):
        return "dll:{}".format(self.double_ll)
                
        
if __name__=='__main__':
    cache=LRU()
    l=[1,2,3,4,5,3,1,4,5]
    for i in l:
        cache.hit(i)
        print(cache)
    
