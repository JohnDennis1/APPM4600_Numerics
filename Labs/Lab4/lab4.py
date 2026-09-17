import math

#Exercise

#1
#%% [markdown]
# |\frac{f(x)f''(x)}{f'(x)^2}|<1

#2
def bisection(f_x,df,d2f,a,b,tol):
    d = 0.5*(a+b)

    root = a #initializing

    if f_x(a)*f_x(b) >0: #checking for sign change
        print("didn't work :(")
        return root

    if math.abs(f_x(d)*d2f(d)/2):
    
    if math.abs(a-b)/math.abs(b) < tol:
        root = b
        print("WORKED!")
        return root

    if math.abs(f_x(a)) ==0:
        print("WORKED!")
        return root

    if math.abs(f_x(b)) ==0:
            print("WORKED!")
            return root

    d = 0.5*(a+b)
    fa = f_x(a)
    fd = f_x(d)

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