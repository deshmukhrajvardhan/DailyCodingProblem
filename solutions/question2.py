'''Given an array of integers, return a new array such 
that each element at index i of the new array is the product 
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected 
output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
import pandas

def prod_i_sans(l,i):
    
    total_prod=1
    
    for el in l:
        total_prod *=el
    
    for i in (range(len(l))):
        if i<0 or i>len(l)-1:
            print("illegal index")
            return
        times=0
        current_prod=total_prod
        current_el=l[i]
        while times * current_el < total_prod:
            current_prod -= current_el
            times+=1
        l[i]=times
        print("times:{},l:{}".format(times,l))
    
prod_i_sans([1, 2, 3, 4, 5],0)
        
