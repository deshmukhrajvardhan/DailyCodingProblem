def find_factors(x,curr=[],now=2):
    if x==1:
        print(curr)
        return curr
            
    if x%now==0:
        curr.append(now)
        x/=now
    else:
        now+=1
        
    print(x,curr,now)
    return find_factors(x,curr,now)
    
def n_table_factors(N,x,curr=[],now=2,x_l=[]):
    if x>N*N:
        return []
        
    if x==1:
        print(curr)
        return curr
            
    if x%now==0:
        if (x/now)<=N:
            curr.append(now)
        #if (x/now)*x>=N:
        #    x_l.append(x/now)
        x/=now
        
    else:
        now+=1
        
    print(x,curr,now)
    return n_table_factors(N,x,curr,now)

n_fact=n_table_factors(6,20)

if len(n_fact)>0:
    c=n_fact.copy()
    t=c.pop(0)
    c.append(t)
    #print(c)
    cnt=1
    while c!=n_fact:
        cnt+=1
        print(c,n_fact)
        t=c.pop(0)
        c.append(t)
else:
    cnt=0
if cnt>1:
    diff= len(n_fact)-len(set(n_fact)) 
    cnt+= diff
print(cnt)


