"""
 This script provides you the opprotunity play with different linear algebra solvers.
You will learn about the performance of the different solvers and how to build
test some test matrices to challenge the different methods. 
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


import time
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
from scipy.linalg import lu_factor, lu_solve


def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 100

     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)

     ''' Solve the system using numpy'''
     scila_start = time.perf_counter()
     x = scila.solve(A,b)
     scila_end = time.perf_counter()
     #print(f"Time taken for scipy.linalg.solve: {scila_end - scila_start:.2f} seconds")

     ''' Solving the system using LU_solve_rect'''
     x_lu, fact_time, sol_time = LU_solve_rect(A, b)
     test = np.matmul(A, x_lu)
     residual = la.norm(test - b)

     print(f"Residual for LU solve: {residual:.2e}")

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)

def driver_datframe():
     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = np.array([100, 500, 1000, 2000, 4000, 5000])

     datframe = np.zeros((len(N),5))

     for i in range(len(N)):
               ''' Right hand side'''
     b = np.random.rand(N[i],1)
     A = np.random.rand(N[i],N[i])

     ''' Solve the system using numpy'''
     scila_start = time.perf_counter()
     x = scila.solve(A,b)
     scila_end = time.perf_counter()
     datframe[i,0] = scila_end - scila_start
          #print(f"Time taken for scipy.linalg.solve: {scila_end - scila_start:.2f} seconds")

     ''' Solving the system using LU_solve_rect'''
     x_lu, fact_time, sol_time = LU_solve_rect(A, b)
     datframe[i,1] = fact_time
     datframe[i,2] = sol_time
     test = np.matmul(A, x_lu)
     residual = la.norm(test - b)
     datframe[i,3] = residual
     datframe[i,4] = N[i]

     #for col in datframe:
          #print(f"Scila Time: {col[0]:.2f} | {col[1]:<10} | {col[2]:>5}")
     #print(f"Residual for LU solve: {residual:.2e}")
     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B 

def LU_solve_rect(A,b):
     ''' This subroutine uses LU factorization
     from scipy to solve the system. Also times 
     how long it takes'''    
     start1 = time.perf_counter()
     lu, piv = lu_factor(A)
     end1 = time.perf_counter()
     start2 = time.perf_counter()
     x = lu_solve((lu, piv), b)
     end2 = time.perf_counter()
     #print(f"Time taken for the factorization: {end1 - start1:.2f} seconds")
     #print(f"Time taken for the solution: {end2 - start2:.2f} seconds")
     return x, (end1 - start1), (end2 - start2)

if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      #driver()       
      driver_datframe()


#Answer to How to do QR factorization
#Take the columns of a Matrix A and apply Gram-Schmidt to the columns to get an orthogonal basis
#Then normalize each of the orthogonal basis vactors to get an orthonormal basis.
#Construct Q from the orthonormal basis vectors and then find R by multiplying Q^T with A.
#Then A = QR. so Ax = b becomes QRx = b.
#Then multiply both sides by Q^T so we get Q^TQRx = Q^Tb.
#Because Q is orthonormal, Q^TQ = I, so we have Rx = Q^Tb.