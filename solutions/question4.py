l=[1,3,5,7,9,8,4,2]
def find_lowest_missing(l):
    front = 1
    end = 1
    for i in range(len(l)):
        for j in [0,1]:
            if l[i] == front:
                front = l[i] + 1
            if l[len(l)-1-i] == end:
                end = l[len(l)-1-i] +1
            
            if front == end+1:
                end = front
            else:
                front = end
    print(front)

find_lowest_missing(l)
