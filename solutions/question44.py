def num_inversions(A):
    i=0
    j=0
    j+=1
    inv=[]
    greater_dict=dict()
    while j<len(A) and i<len(A):
        if A[j]<A[i]:
            try:
                greater_dict[A[i]]
                l=[A[i]]
                l.extend(greater_dict[A[i]])
                greater_dict[A[j]]=l
            except KeyError:
                greater_dict[A[j]]=[A[i]]
                
            try:
                for val in greater_dict[A[j]]:
                    inv.append((val,A[j]))
            except KeyError:
                inv.append((A[i],A[j]))
            
            i+=1
        
        j+=1
        
    print(inv)
        
if __name__=='__main__':
    A=[5,4,3,2,1]
    num_inversions(A)
