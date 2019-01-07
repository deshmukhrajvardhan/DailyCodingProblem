def great_3_mul(l):
    pos_l=[]
    neg_l=[]
    # pos_l len<=3
    # neg_l len<=2
    for i in l:
        if len(pos_l)>3:
            pos_l.pop()
        if len(neg_l)>2:
            neg_l.pop()
        
        if i<0:
            if len(neg_l)>0 and i<=neg_l[-1]:
                if len(neg_l)==2:
                    neg_l[-1]= i
                else:
                    neg_l=sorted(neg_l,reverse=True)
                    neg_l.insert(0,i)
            elif len(neg_l)<2 and i<0:
                neg_l.insert(0,i)
        else:
            if len(pos_l)>0 and i>=pos_l[-1]:
                if len(pos_l)==3:
                    pos_l[-1]= i
                else:
                    #pos
                    pos_l=sorted(pos_l,reverse=True)
                    pos_l.insert(len(pos_l)-2,i)
            elif len(pos_l)<3 and i>0:
                pos_l.append(i)

    if len(neg_l)==2:
        if len(pos_l)==3:
            if neg_l[0]*neg_l[1]>pos_l[1]*pos_l[2]:
                print(pos_l[0],neg_l)
        else:
            print(neg_l,pos_l[0])
    else:
        print(pos_l)
        
    print(pos_l,neg_l)
        

if __name__=='__main__':
    l=[-10, -10, 5, 2,9,-9]
    great_3_mul(l)
