"""

"""
go={("a","b"):[1,2]}

for i in go:
    print(go,len(go[i]))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(L):
    # write your code in Python 3.6
    rem_dot_ids=[]
    div=[]
    group={}
    for id in L:
        div=id.split('@')
        local=div[0]
        local_str=''
        for i in local:
            if i == '+':
                break
            elif i!='.':
                local_str+=i
        full_str=local_str+'@'+div[1]
        try:
            if group[full_str]:
                group[full_str].append(id)
        except:
            group[full_str]=[id]
    
    print(group)
    count=0
    for i in group:
        if len(group[i])>1:
            count+=1
    
    return count


if __name__=='__main__':
    L=['adu@ty.com','asu+i@ty.com']
    solution(L)
