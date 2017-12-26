# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 00:03:11 2017

@author: Tejo Nutalapati


documentation for the simplex method in python:

https://docs.scipy.org/doc/scipy/reference/optimize.linprog-simplex.html

it returns the optimal solution value and vector as well as if 
the program is infeasible or unbounded among other things
"""


import numpy as np
import scipy.optimize as lp

print("This script solves linear programs of the form: \n 'Maximize c^T*x subject to Ax = b and x ≥ 0'"'\n')

#User input for the A matrix
print("What does your A matrix look like?")
n = int(input("number of rows?: "))
m = int(input("number of columns?: "))

#python is zero indexed so I made sure the input asked for the right row and column
A=[]
for i in range(0,n):
    for j in range(0,m):
        try:
            A.append(float(input("entry in row %u column %u: " %(i+1,j+1) )))
        except:
            print("thats not a number so I'm gonna assume its 0")
            A.append(0.0)

A=np.array(A)
A = A.reshape((n,m))

print("this is what your A matrix looks like:")
print(A)


#User input for the entries in the b vector
print("what are the entries for the b vector?")
b=[]
for i in range(0,n):
    try:
        b.append(float(input("entry in row %u: " %(i+1))))
    except:
        print("thats not a number so I'm gonna assume its 0")
        b.append(0.0)
print("this is what your b vector looks like:")
print(b)


# User input for the entries of the c vector
print("what are the entries for the c vector?")
c=[]
for i in range(0,m):
    try:
        c.append(-1*float(input("entry in row %u: " %(i+1)))) 
    except:
        print("thats not a number so I'm gonna assume its 0")
        c.append(0.0)

print("this is what your c vector looks like:")
print(c)
#you will notice the printed c vector is the negative of the entered values
#This is because the lp.linprog function below is for the LP of the form: 
#'Minimize c^T*x subject to Ax = b and x ≥ 0' NOT 'Max c^T*x ...'


#the solution to the LP using the linear programming stuff already in SciPy 
sol=lp.linprog(c, A_ub=None, b_ub=None, A_eq=A, b_eq=b, bounds=None, method='simplex', callback=None, options=None)




#Getting the relevant information from the variable 'sol'
solvector= sol['x'] # gets the optimal solution vector
solvalue=-1*sol['fun'] # gets the optimal value
solstatus=sol['status'] # whether the LP can be solved for an optimal solution


if solstatus==0:
    conclusion="This LP can be solved"
elif solstatus==1:
    conclusion= "The program timed out"
elif solstatus==2:
    conclusion = "The LP is not feasible"
    solvector=None
    solvalue=None
elif solstatus==3:
    conclusion = "The LP is unbounded"
    solvector=None
    solvalue=None
    
#putting the information into a neat output
report=(conclusion,solvector,solvalue)
print('\n''\n''''
HERE ARE 
THE RESULTS...      
'''
 ,report[0],'\n')
print("an optimal solution:",report[1],'\n')
print("The optimal value:",report[2])

# done!
