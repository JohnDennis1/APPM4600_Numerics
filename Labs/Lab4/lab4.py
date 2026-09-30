import math

#Exercise

#1
#%% [markdown]
# |\frac{f(x)f''(x)}{f'(x)^2}|<1

def bisection_newton(f_x,df,d2f,a,b,tol,Nmax = 50):
    d = 0.5*(a+b)

    if f_x(a)*f_x(b) >0: #checking for sign change
        print("didn't work :(")
        return root

    # The two conditions below exist to check if endpoints are roots
    if math.abs(f_x(a)) ==0:
            print("WORKED!")
            return root
    
    if math.abs(f_x(b)) ==0:
                print("WORKED!")
                return root
        
    #condition to see if the mid point lies outside a basin of convergence (use bisection)  g 
    while math.abs(f_x(d)*d2f(d)/df(x)^2)>=1: 

        fa = f_x(a)
        fd = f_x(d)     

        if fa*fd == 0:
            root = d
            print("WORKED!")
            return root

        
    #condition to check if the relative difference in the two points is less than the tol
    if math.abs(a-b)/math.abs(b) < tol: 
        root = b
        print("WORKED!")
        return root


    while :
         if fa*fd == 0:
              root = d
              print("WORKED!")
              return root

         if fa*fd > 0:
              a = d
              fa = fd
         else:
              b = d
              d = 0.5*(a+b)
              fd = f_x(d)
        root = d
        print("WORKED!")
return root