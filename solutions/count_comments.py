MULTI_L=1

def count_comments(com_file):
    com_type = 0
    num_comments = 0
    with open(com_file,'r') as fil:
        line=fil.readline()
        while line:
            i=0
            while i<len(line):
                if line[i]=='/' and i<len(line)-1 and line[i+1]=='/' and com_type==0:
                    #print(line)
                    num_comments+=1
                    break
                elif line[i]=='/' and i <len(line)-1 and line[i+1]=='*' and com_type==0:
                    com_type = MULTI_L
                    i+=1
                    #print('start',line)
                elif line[i]=='*' and i <len(line)-1 and line[i+1]=='/' and com_type== MULTI_L:
                    com_type = 0
                    i+=1
                    #print('end',line)
                    num_comments+=1
                
                i+=1
            line=fil.readline()
    
    print(num_comments)
    
if __name__=='__main__':
    count_comments('comments.txt')
