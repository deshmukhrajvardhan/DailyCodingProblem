H=0
T=1

def normalize(h,t,r):
    if h<5:
        return r
    elif h>=5:
        if t>=5:
            t=0
            h=0
            return r
        else:
            t+=1
            return T
    elif t<5:
        return r
    elif t>=5:
        if h>=5:
            t=0
            h=0
            return r
        else:
            h+=1
            return H


h = 0
t = 0
r = toss_baised()
if r=0:
    h+=1
    normalize(h,t,r)
else:
    t+=1
    normalize(h,t,r)
    
