def stocks(l):
    lowest_num=l[0]
    highest_diff=[l[1]-l[0],(l[0],l[1])]
    for i in range(1,len(l)):
        if l[i]<lowest_num:
            lowest_num=l[i]
        
        if l[i]-lowest_num>highest_diff[0]:
            highest_diff=[l[i]-lowest_num,(lowest_num,l[i])]
    print(highest_diff)
    
if __name__=="__main__":
    stocks([9, 11, 1,8, 5,7,10,1,4])
