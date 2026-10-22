import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math
from scipy.integrate import quad

def driver(): #this will be for exercise 3.2.1
    '''Running a function to evaluate a legendre polynomial given a point.'''
    f = lambda x: 1./(1.+x**2)
    x = 5 #point to evaluate at
    n = 5 #degree of legendre polynomial
    p = eval_legendre(n, x) #values of phi

    w = lambda x: 1. #this is the weight function

    a = -5 #interval I'm interested in
    b = 5

    j = 1 #this is just a test for 1st coefficient

    aj = integrate_legendre(f,a,b,w,n,j)/normalize_legendre(a,b,w,n,j) #a_jth coefficient
    print(aj)

def driver2(): #for problem 3.2.2
   #  function you want to approximate
    f = lambda x: 1./(1.+x**2)

# Interval of interest    
    a = -1
    b = 1
# weight function    
    w = lambda x: 1.

# order of approximation
    n = 2

#  Number of points you want to sample in [a,b]
    N = 1000
    xeval = np.linspace(a,b,N+1)
    pval = np.zeros(N+1)

    for kk in range(N+1):
      pval[kk] = eval_legendre_expansion(f,a,b,w,n,xeval[kk])
      
    ''' create vector with exact values'''
    fex = np.zeros(N+1)
    for kk in range(N+1):
        fex[kk] = f(xeval[kk])
        
    plt.figure()    
    plt.plot(xeval,fex,'ro-', label= 'f(x)')
    plt.plot(xeval,pval,'bs--',label= 'Expansion') 
    plt.legend()
    plt.show()    
    
    err_l = abs(pval-fex)
    plt.semilogy(xeval,err_l,'ro--',label='error')
    plt.legend()
    plt.show()

def eval_legendre(n,x):
    '''this function evaluates the legendre polynomial of order n at the point x and returns a vector of length n+1 with the 
    values of the legendre polynomial at the point x'''
    p = np.zeros(n + 1) #Here we initialze a vector of length n+1 that we can populate later
    p[0] = 1 #by default the polynomial of order 0 is constant 1
    if n >= 1: #This will check if we want a higher order given by what's been passed in
        p[1] = x #the polynomial of order 1 is just x
    for i in range(2, n + 1):
        p[i] = ((2 * i - 1) * x * p[i - 1] - (i - 1) * p[i - 2]) / i
    return p

def integrate_legendre(f,a,b,w,n,j):
    '''This function integrates the product of f(x) and the jth legendre polynomial over the interval [a,b] with wt function w(x)'''
    integrand = lambda x: f(x)*eval_legendre(n,x)[j]*w(x) #creating the anon handle
    integral, abs_error = quad(integrand, a, b) #using quad to integrate, and we only really care about the integral for now
    return integral

def normalize_legendre(a,b,w,n,j):
    '''This function computes the normalization factor for the jth legendre polynomial with wt function w(x) over the interval [-1,1]'''
    integrand = lambda x: eval_legendre(n,x)[j]**2 * w(x) 
    norm_fac, abs_error = quad(integrand, a, b)
    return norm_fac
 
def eval_legendre_expansion(f,a,b,w,n,x): 

#   This subroutine evaluates the Legendre expansion

#  Evaluate all the Legendre polynomials at x that are needed
# by calling your code from prelab 
  p = eval_legendre(n, x)
  # initialize the sum to 0 
  pval = 0.0    
  for j in range(0,n+1):
      # make a function handle for evaluating phi_j(x)
      phi_j = lambda x: eval_legendre(n,x)[j]
      # make a function handle for evaluating phi_j^2(x)*w(x)
      phi_j_sq = lambda x: eval_legendre(n,x)[j]**2 * w(x)
      # use the quad function from scipy to evaluate normalizations
      norm_fac,err = quad(phi_j_sq, a, b)
      # make a function handle for phi_j(x)*f(x)*w(x)/norm_fac
      func_j = lambda x: phi_j(x)*f(x)*w(x)/norm_fac
      # use the quad function from scipy to evaluate coeffs
      aj,err = quad(func_j, a, b)
      # accumulate into pval
      pval = pval+aj*p[j] 
       
  return pval

if __name__ == '__main__':
  # run the drivers only if this is called from the command line
 # driver()   
  driver2()