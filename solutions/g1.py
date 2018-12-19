"""
used a tuple instead :/
"""

def solution(A):
    current_a=A[0]
    current_b=-1
    count=1
    pair_count={}
    i=1
    while i<len(A):
        print(current_b,current_a,A[i])
        if current_b==-1 and A[i]!=current_a:
            current_b=A[i]
            count+=1
            
        elif A[i]!=current_b and A[i]!=current_a:
            try:
                if pair_count[A[i]]:
                    pass
            except:
                
                pair_count[current_a]=count
                pair_count[current_b]=count
                current_a=A[i]
                current_b=-1
                count=1
        else:
            count+=1

        i+=1

    if pair_count=={}:
        pair_count[current_a]=count
        pair_count[current_b]=count
    
    max_count=0
    for i in pair_count:
        if max_count<pair_count[i]:
            max_count=pair_count[i]
    print(max_count,pair_count)
    return max_count


if __name__=='__main__':
    A=[1,2,1,3,4,3,5,1,2]
    A=[1, 2, 1, 2, 1, 2, 1]
    print(A)
    solution(A)
