"""
 This script provides you the opprotunity to insert your own line evaluator.
 You will practice some python skills while getting a better understanding of 
 how splines work.
 NOTE:  this code will not compile until you add the line evaluator in the 
 appropriate location.
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

import math
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 

def driver():
    '''Running a function to evaluate a line given a two points and a point.'''
    #x_0,x_1 = 0,1
    #y_0,y_1 = math.exp(x_0),math.exp(x_1) #Just test points
    #alpha = 0.5
    #y_alpha = eval_line(x_0,x_1,y_0,y_1,alpha)
    #print('y_alpha = ',y_alpha) #It worked! :)

    f = lambda x: np.exp(x)
    a = 0
    b = 1

    ''' number of points within each interval to evaluate at''' 
    n = 10
        
    ''' number of intervals'''
    Nint = 10

    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
        
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint,n)
        
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
          
    plt.plot(xeval,fex,'ro-',label='exact function')
    plt.plot(xeval,yeval,'bs--',label='natural spline') 
    plt.legend
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure() 
    plt.semilogy(xeval,err,'ro--',label='absolute error')
    plt.legend()
    plt.show()

def eval_line(x_0,x_1,y_0,y_1,alpha):
    '''evaluate the line at the point alpha given the two points (x_0,y_0) and (x_1,y_1)'''
    p_alpha = y_1 + (y_1-y_0)/(x_1-x_0)*(alpha-x_1)
    return p_alpha
  
def  eval_lin_spline(xeval,Neval,a,b,f,Nint,n):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    
    for jint in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        
        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1 = xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        
        for kk in range(n):
           yeval[kk] = eval_line(a1,b1,fa1,fb1,xeval[kk])
           '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
           '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
           the points (a1,fa1) and (b1,fb1)'''
    return yeval
           
           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               