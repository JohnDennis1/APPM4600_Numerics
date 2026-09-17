import numpy as np


# Pre-Lab
def fixed_pt_algo(g_x, p_0, tol, Nmax):
    p = np.zeros((Nmax+1,1)) #this inlcudes "space" for the initial guess
    p[0,0] = p_0 #sets the first "approximation" as the initial guess

    for n in range(Nmax):
        p[n+1,0] = g_x(p[n,0]) #using the function, creates the next approximation

        if abs(p[n+1,0]-p[n,0])<tol: #checks to see if the diff is lower than the tol to end the algo
            print("IT WORKED!")
            return p[:n+2,0] #returns approximations and includes the endpoint, also little message for success
    print("no work :(")
    return p[:,0] #the message indicates it didn't converge 

#2.2 Exercises
#1
def ord_convergence(approx,p):
    alpha = -1 #intializing alpha as number that couldn't be possible
    N = len(approx) #for the errors, there will be Nmax-1 values
    errors = np.zeros((N,1)) #initializing errors with zeros

    for n in range(N):
        errors[n,0] = abs(approx[n]-p) #finding absolute error between the approximations and the fixed point

        #calculates the order using that last few errors closest to the fixed point
        alpha = (np.log(errors[-1,0])-np.log(errors[-2,0]))/(np.log(errors[-2,0])-np.log(errors[-3,0]))

    return alpha