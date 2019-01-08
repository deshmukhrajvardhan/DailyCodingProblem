"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
[(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)]
"""
import random

def place_pivot(l,start,end,i_pivot):
#     print(l)
    if not(start<=i_pivot<=end):
        print("Piviot out of bound")
        
    l[i_pivot],l[start]=l[start],l[i_pivot]
    pivot=l[start][0]
    i=start+1
    j=start+1
    
    while j<= end:
        if l[j][0]<=pivot:
            l[i],l[j]=l[j],l[i]
            i+=1
        j+=1
    
    l[start],l[i-1]=l[i-1],l[start]
#     print(l)
    return i-1
        
def quic(array,start=None,end=None):
    if end is None:
        start=0
        end=len(array)-1
    
    if end-start<1:
#         print(array)
        return
    
    i_pivot=random.randint(start,end)
#     print(i_pivot)
    i = place_pivot(array,start,end,i_pivot)
    
    quic(array,start,i-1)
    quic(array,i+1,end)
    
if __name__=='__main__':
#     l=[4,6,1,10,2,90,3]
    l=[(1, 3), (5, 8), (4, 10), (20, 25),(2,3)]
    quic(l)
    
    i=0
    j=1
    while j<len(l)-1:
#         print(l[i])
        if l[i][0]<= l[j][0]<=l[i][1]:
            print(l[i],l[j])
            l[i]=(l[i][0],max(l[i][1],l[j][1]))
            l.pop(j)
        else:
            i+=1
#             print(l[i])
        j+=1
    print(l)
