def sub_of_k(l,k):
    i=0
    sub=[]
    till_k=k
    while i<len(l):
        if l[i]<k:
            till_k-=l[i]
            sub.append(l[i])
            if till_k>0:
                print('l')
            elif till_k==0:
                #sub.append(l[i])
                break
            else:
                #sub.append(l[i])
                p_els=[el for el in sub if el>= (-1*till_k)]
                rem_el=min(p_els)
                till_k+=rem_el
                #print("remove:{}".format(rem_el))
                sub.remove(rem_el)
        
        elif l[i]==k:
            sub=l[i]
            break
        
        i+=1
    
    if len(sub)>0:
        return sub
    else:
        return None

if __name__=='__main__':
    l=[12,1,61,5,9,2]
    print(sub_of_k(l,3))
