def decode(msg):
    l=[int(i) for i in list(msg)]
    print(l)

    if(len(l)%2==0):
        ones=len(l)
    else:
        ones=len(l)-1
            
    pos_in_list=[0]*len(l)
    levels = ones/2 # levels
    combs=1
    end= len(l)-1
    print("comb:{},list:{}".format(combs,pos_in_list))
    while levels:
        i=0
        while i<end:
            if l[i+1]<=2:
                 if l[i]<=6:
                    pos_in_list[i] = 1
                    pos_in_list[i+1] = 1
                    combs+=1
                    print("comb:{},list:{},i:{},end:{}".format(combs,pos_in_list,i,end))
#                     print(pos_in_list)
                    if i<end-1:
                        pos_in_list[i] = 0
                        pos_in_list[i+1] = 0
            i+=1
#             print("comb:{},list:{},i:{},end:{}".format(combs,pos_in_list,i,end))
                        
        end -=2 
        levels-=1
    
message='27111'
decode(message)
