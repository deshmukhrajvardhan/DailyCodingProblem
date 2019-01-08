def r_to_c(l,n,m):
    a=[]
    r=[]
        
    for i in range(0,m):
        a=[]
        for j in range(0,n):
            a.append(l[j][i])
        r.append(a)
            
    print (r)
    
    return r

def num_col_rem(l,n,m):
    l_transpose=r_to_c(l,n,m)
    count=0
    for i in range(m):
        m=l_transpose[i][0]
        for j in range(n):
            if m>l_transpose[i][j]:
                count+=1
                break
            else:
                m=l_transpose[i][j]
    
    #print(count)
    return count
    
if __name__=='__main__':
#    l=[['z','y','x'],['w','v','u'],['t','s','r']]
#    l=[['a','d','g'],['b','e','h'],['c','f','h']]
    l=[['a','d','g'],['z','e','v'],['c','x','i']]
    print(num_col_rem(l,3,3))
