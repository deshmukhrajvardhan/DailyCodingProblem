def queen_pos(N):
    main_avail_pos=[i for i in range(N*N)]
    q_pos=[]
    possibilities=[]
    
    for times in range(N*N):
        
        main_avail_pos.insert(0,main_avail_pos.pop())
        avail_pos= main_avail_pos.copy()
        q_pos=[]
        while 1:
            if len(avail_pos)==0:
                break
            q_pos.append(avail_pos.pop(0))
            curr_q=q_pos[-1]
            
            row=curr_q//N
            
            print(curr_q)
            for r in range(row*N,(row+1)*N):
                if r in avail_pos:
                    try:
                        avail_pos.remove(r)
                        print("row{}".format(r))
                    except:
                        continue
            
            for c in range(-N+1,N):
                if curr_q+N*c in avail_pos:
                    try:
                        avail_pos.remove(curr_q+N*c)
                        print("column{}".format(curr_q+N*c))
                    except:
                        continue
            
            for d in range(-N+1,N):
                try:
                    if curr_q+(N+1)*d in avail_pos and curr_q+(N+1)*d <=(((N/2)+1)*(N+1))+curr_q:
                        avail_pos.remove(curr_q+(N+1)*d)
                        print("right diag{}".format(curr_q+(N+1)*d))
                    if curr_q+(N-1)*d in avail_pos and curr_q+(N-1)*d <=curr_q*N:
                        avail_pos.remove(curr_q+(N-1)*d)
                        print("left diag{}".format(curr_q+(N-1)*d))
                    
                    
                except:
                    continue
            #break
        
        if len(q_pos)>=N-1:
            possibilities.append(q_pos)
        
    
    print(possibilities,len(possibilities))
    
    
# Python program to solve N Queen 
# Problem using backtracking 


def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print("{},".format(board[i][j]),end=" ")
        print("")
    print("")


# A utility function to check if a queen can 
# be placed on board[row][col]. Note that this 
# function is called when "col" queens are 
# already placed in columns from 0 to col -1. 
# So we need to check only left side for 
# attacking queens 
def isSafe(board, row, col): 

	# Check this row on left,right side 
	for i in range(N): 
		if board[row][i] == 1: 
			return False

	# Check upper diagonal on left side 
	for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
		if board[i][j] == 1: 
			return False
            
     
	for i,j in zip(range(row,-1,-1), range(col,row,1)): 
		if board[i][j] == 1: 
			return False

	# Check lower diagonal on left side 
	for i,j in zip(range(row,N,1), range(col,-1,-1)): 
		if board[i][j] == 1: 
			return False
            
    	# Check lower diagonal on right side 
	for i,j in zip(range(row,N,1), range(col,N,1)): 
		if board[i][j] == 1: 
			return False

	return True

def solveNQUtil(board, col,N): 
    # base case: If all queens are placed 
    # then return true 
    if col >= N: 
        return True

    for i in range(N):
        # Consider this column and try placing 
        # this queen in all rows one by one 
        if isSafe(board, i, col): 
            # Place this queen in board[i][col] 
            board[i][col] = 1

            # recur to place rest of the queens 
            if solveNQUtil(board, col+1,N) == True: 
                return True

            # If placing queen in board[i][col 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            board[i][col] = 0

    # if the queen can not be placed in any row in 
    # this colum col then return false 
    return False

# This function solves the N Queen problem using 
# Backtracking. It mainly uses solveNQUtil() to 
# solve the problem. It returns false if queens 
# cannot be placed, otherwise return true and 
# placement of queens in the form of 1s. 
# note that there may be more than one 
# solutions, this function prints one of the 
# feasible solutions. 
def solveNQ(N):
    board = [[0 for i in range(N)]for j in range(N)] 
#	board = [ [0, 0, 0, 0], 
#			[0, 0, 0, 0], 
#			[0, 0, 0, 0], 
#			[0, 0, 0, 0] 
#			] 
    count=0
    for i in range(N):
        board[i][0] = 1
        if solveNQUtil(board,1,N) == False: 
            pass
            #print "Solution does not exist"
           # return False
        else:
            count+=1
            printSolution(board)
            
        board = [[0 for i in range(N)]for j in range(N)]
            
    print("Solutions:{}".format(count))



if __name__=='__main__':
    #queen_pos(4)
    # driver program to test above function 
    N=8
    solveNQ(N) 

    # This code is contributed by Divyanshu Mehta 
