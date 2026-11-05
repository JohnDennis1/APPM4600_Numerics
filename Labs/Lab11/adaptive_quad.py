"""
Contains the adaptive quadrature subroutine and allows 
the user to change the underlying composite quadrature.  
Trapezoidal, Simpson, and Gaussian are provided.
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





# get lgwts routine and numpy
from gauss_legendre import *
import numpy as np


def eval_composite_trap(N,a,b,f):
  """
  N represents the number of points, not the number of intervals.
  So there are N-1 intervals.  The trapezoid rule is applied to each
  interval and summed.
  """
  if N < 2:
    raise ValueError("N must be at least 2.")
  h = (b-a)/(N-1)
  xnode = np.linspace(a,b,N)
  I_trap = f(xnode[0])
  for j in range(1,N-1):
    I_trap = I_trap + 2*f(xnode[j])
  I_trap = I_trap + f(xnode[N-1])
  I_trap = h/2*I_trap
  return I_trap, xnode, None



def eval_composite_simpsons(N,a,b,f):
  """
  Simpson's requires an even number of intervals or an odd number of points. If N
  is the number of points, it must be odd and greater than or equal to 3.

  If N is even, we will handle it using the trapezoid on the last interval.
  Scipy's implementation of simpson's does the same thing.

  I won't account for the case where N < 3. I'll just return an error.
  """
  if N < 3:
    raise ValueError("N must be at least 3.")
  elif N % 2 == 0:
    h = (b-a)/(N-1)
    I_simp, _, _ = eval_composite_simpsons(N-1,a,b - h,f)
    I_trap, _, _ = eval_composite_trap(2,b - h,b,f)
    return I_simp + I_trap, np.linspace(a,b,N), None
  else:
    h = (b-a)/(N-1)
    xnode = np.linspace(a,b,N)
    I_simp = f(xnode[0])

    nhalf = int((N-1)/2)
    for j in range(1,int(nhalf)+1):
        # odd part
        I_simp = I_simp +4*f(xnode[2*j-1])
        # even part (interior only; x_n is added below)
        if j < nhalf:
          I_simp = I_simp+2*f(xnode[2*j])

    I_simp= I_simp + f(xnode[N-1])
      
    I_simp = h/3*I_simp
      
  return I_simp, xnode, None


def eval_gauss_quad(M,a,b,f):
  """
  Non-adaptive numerical integrator for int_a^b f(x)w(x)dx
  Input:
    M - number of quadrature nodes
    a,b - interval [a,b]
    f - function to integrate
  
  Output:
    I_hat - approx integral
    x - quadrature nodes
    w - quadrature weights

  Currently uses Gauss-Legendre rule
  """
  x,w = lgwt(M,a,b)
  I_hat = np.sum(f(x)*w)
  return I_hat,x,w

def adaptive_quad(a,b,f,tol,M,method):
  """
  Adaptive numerical integrator for \int_a^b f(x)dx
  
  Input:
  a,b - interval [a,b]
  f - function to integrate
  tol - absolute accuracy goal
  M - number of quadrature nodes per bisected interval
  method - function handle for integrating on subinterval
         - eg) eval_gauss_quad, eval_composite_simpsons etc.
  
  Output: I - the approximate integral
          X - final adapted grid nodes
          nsplit - number of interval splits
  """
  # 1/2^50 ~ 1e-15
  maxit = 50
  left_p = np.zeros((maxit,))
  right_p = np.zeros((maxit,))
  s = np.zeros((maxit,1))
  left_p[0] = a; right_p[0] = b
  # initial approx and grid
  s[0],x,_ = method(M,a,b,f)
  # save grid
  X = []
  X.append(x)
  j = 1
  I = 0
  nsplit = 1
  while j < maxit:
    # get midpoint to split interval into left and right
    c = 0.5*(left_p[j-1]+right_p[j-1])
    # compute integral on left and right spilt intervals
    s1,x,_ = method(M,left_p[j-1],c,f); X.append(x)
    s2,x,_ = method(M,c,right_p[j-1],f); X.append(x)
    if np.max(np.abs(s1+s2-s[j-1])) > tol:
      left_p[j] = left_p[j-1]
      right_p[j] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j] = s1
      left_p[j-1] = 0.5*(left_p[j-1]+right_p[j-1])
      s[j-1] = s2
      j = j+1
      nsplit = nsplit+1
    else:
      I = I+s1+s2
      j = j-1
      if j == 0:
        j = maxit
  return I,np.unique(X),nsplit

