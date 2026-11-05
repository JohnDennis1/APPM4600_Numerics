"""
 This script tests the use of different composite quadrature methods
 for approximating integrals.  There is an option to adjust the commented
 lines to illustrate convergence when the number of panels is increased.
"""

############################################# 
"""
Copyright (C) 2025  Adrianna M. Gillman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
############################################# 




#import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():
    
    f = lambda x: np.sin(x)
    a = 0
    b = np.pi
    
    # exact integral
    I_ex = 2
    
#    N =100
#    ntest = np.arrange(0,N,step=2)
    
#    errorT = np.zeros(len(ntest))
#    errorS = np.zeros(len(ntest))
    
#    for j in range(0,len(ntest)):
#        n = ntest[j]

# for simpson's n must be even.        
# n+1 = number of pts.
    n = 20
    I_trap = CompTrap(a,b,n,f)
    print('I_trap= ', I_trap)
    
    err = abs(I_ex-I_trap)   
    
    print('absolute error = ', err)    
    
    I_simp = CompSimp(a,b,n,f)

    print('I_simp= ', I_simp)
    
    err = abs(I_ex-I_simp)   
    
    print('absolute error = ', err)    

        
def CompTrap(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    
    I_trap = h*f(xnode[0])*1/2
    
    for j in range(1,n):
         I_trap = I_trap+h*f(xnode[j])
    I_trap= I_trap + 1/2*h*f(xnode[n])
    
    return I_trap     

def CompSimp(a,b,n,f):
    """Composite Simpson's rule with n subintervals (n + 1 points)."""
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)):
        raise ValueError("n must be a positive even integer (number of subintervals).")
    if n < 2 or n % 2 != 0:
        raise ValueError("n must be a positive even integer (number of subintervals).")
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    I_simp = f(xnode[0])

    nhalf = n/2
    for j in range(1,int(nhalf)+1):
         # odd part
         I_simp = I_simp +4*f(xnode[2*j-1])
         # even part (interior only; x_n is added below)
         if j < nhalf:
             I_simp = I_simp+2*f(xnode[2*j])
    I_simp= I_simp + f(xnode[n])
    
    I_simp = h/3*I_simp
    
    return I_simp     


    
    
if __name__ == '__main__':
    driver()    
