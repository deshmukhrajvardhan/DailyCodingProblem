def min_n_color_cost(nk):
    cost=0
    s=[]
    house_i=0
    two_options=[] #2 low options[(i1,el1),(i2,el2)]
    chosen_color=[] # chosen[(i,el)]
    while house_i<len(nk):
        n_row=nk[house_i]
        if len(n_row)<=1:
            print("We have no options")
            return 0
        # get entry for two_options
        min_r_index,min_r_el =0,n_row[0]
        mtwo_r_index,mtwo_r_el=1,n_row[1]
        for i,el in enumerate(n_row):
            if el<=min_r_el:
                prev_r_index,prev_r_el = min_r_index,min_r_el
                min_r_index,min_r_el = i,el
            elif min_r_index==0: # 1st el smallest
                if el<=mtwo_r_el:
                    mtwo_r_index,mtwo_r_el = i,el
                
        if min_r_index==0:
            prev_r_index,prev_r_el = mtwo_r_index,mtwo_r_el
            
        two_options.append([(min_r_index,min_r_el),(prev_r_index,prev_r_el)])
        print(two_options)
        back=True
        row_number=house_i
        chosen_color.append((min_r_index,min_r_el))
        while back and (row_number>=1):
            
#            if len(chosen_color)<=1:
#                chosen_color.append((min_r_index,min_r_el))
#                back=False;
 #           else:
                #print(chosen_color)
                #index clash
            if 1:
                if chosen_color[row_number-1][0]==chosen_color[row_number][0]:#min_r_index:
                    # acconunt for prev and min
                    if two_options[row_number-1][0][0]==chosen_color[row_number][0]:
                        #compare 2nd mins
                        if (two_options[row_number-1][0][1]+two_options[row_number][1][1]) > (two_options[row_number][0][1]+two_options[row_number-1][1][1]):
                            chosen_color[row_number-1]=two_options[row_number-1][1]
                            chosen_color[row_number]=two_options[row_number][0]
                        else:
                            chosen_color[row_number-1]=two_options[row_number-1][0]
                            chosen_color[row_number]=two_options[row_number][1]
                             
                    else:#2nd el clash
                        if (two_options[row_number][1][1]+two_options[row_number-1][0][1]) > (two_options[row_number][0][1]+two_options[row_number-1][1][1]):
                            chosen_color[row_number-1]=two_options[row_number-1][1]
                            chosen_color[row_number]=two_options[row_number][0]
                        else:
                            chosen_color[row_number-1]=two_options[row_number-1][0]
                            chosen_color[row_number]=two_options[row_number][1]
                
                    row_number-=1
                
                else:
                    back=False
        
        house_i+=1
    print("chosen color:{}".format(chosen_color))
    
if __name__=='__main__':
    nk=[[1,2,3,4],[0,5,6,1],[1,7,3,8],[8,2,3,1]]
    #nk=[[1,8,9],[1,2,3],[1,2,4],[1,9,8]] # does not pass this test as 3rd smallest element has to be chosen but isn't included
    min_n_color_cost(nk)
