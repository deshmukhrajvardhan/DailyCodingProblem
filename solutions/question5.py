def f(a,b):
    return (a,b)

def cons(a,b):
    global f
    def pair(f):
        return f(a,b)
    return pair

def car(fc):
    return fc[0]
    
def cdr(fc):
    return fc[1]

print(car(cons(3,4)(f)), cdr(cons(3,4)(f)))
