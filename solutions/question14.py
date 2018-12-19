import numpy.random as rnd
import numpy as np
def pi_estimation(r=1):
    inside = 0.0
    outside = 0.0
    total = 0.0
    #rnd = Random.new

    for i in range(10001):
        x = rnd.rand(0,10000)
        #x/=10000.0
        if x<50:
            x*=(-1)
        y = rnd.rand(0,10000)
        #y=10000.0
        if y<50:
            y*=(-1)

        measure = distance(x, y)
        if measure > r:
            outside += 1
        else:
            inside += 1
        
    total = outside + inside
    print(total,inside,outside)
    return  (4 * (inside / total))

def distance(x1, y1, x=0.0, y=0.0):
    x_diff = x1 - x 
    y_diff = y1 - y 
    x_diff *= x_diff 
    y_diff *= y_diff 
    return np.sqrt(x_diff + y_diff)


print( pi_estimation())
