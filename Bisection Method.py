def f(x):
    return x**4-x-10
    
def bisection_method(a,b,tol=1e-6,max_iter=10):
    if f(a)*f(b)>0:
        print("The function has the same sign at the endpoints a and b.")
        return None
        
    iter_count=0
    while iter_count<max_iter:
        c=(a+b)/2
        if abs(f(c))<tol:
            print(f'Root found: {c}')
            return c
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        iter_count+=1
        print(f"Iteration: {iter_count}: c = {c}, f(c)={f(c)}")
        
    print(f"Rppt approximation after {max_iter} iteration: {c}")
    return c
    
a=1.5
b=2

bisection_method(a,b)
