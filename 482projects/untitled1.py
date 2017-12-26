# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:19:29 2017

@author: tnuta
"""


import numpy as np
import math
import scipy.linalg as slin
import scipy.optimize as lp

n=4
c= [1,2,4,2,1]
czeros= [0]*n
for i in c:
    czeros.append(i)
print(czeros)

"""
n=3
m=4

tab=[]
for i in range(0,n):
    for j in range(0,m):
        tab.append(np.random.uniform(-2,4) )
        
        

#formating entries into n rows and m columns
tab=np.array(tab)
tab = tab.reshape((n,m))

# can only index like this after reshaping
tab[1][3]=5

print(tab)
print("NEW TABLEAU:")

#generates a gomory cut from a tableau 
def gomory_cut(tab):
    gcut = np.zeros((1,m))
    gcut = gcut.reshape((1,m)) 
    for row in range(0,n):
        if (tab[row][m-1]).is_integer() == False:
            for column in range(0,m):
                gcut[0][column] = tab[row][column]-math.floor(tab[row][column])

    newtab=np.vstack((gcut,tab))

        
    print(newtab)
    return newtab

gomory_cut(tab)

def transpose(mat):
    rows=mat.shape[0]
    cols=mat.shape[1]
    for i in range(0,rows):
        for j in range(0,cols):
            mat[i][j]=mat[j][i]

    return mat
"""


A = np.array(([1,0,0,1,0,1],[0,1,0,-1,-1,1],[0,0,1,1,1,1]))
print(A)
b= [2,1,3]
c=[1,1,-1,3,2,1]
for i in range(0,len(c)):
    c[i]=-1*c[i]

print(c)

sol=lp.linprog(c, A_ub=None, b_ub=None, A_eq=A, b_eq=b, bounds=None, method='simplex', callback=None, options=None)


"""
documentation for the simplex in python
https://docs.scipy.org/doc/scipy/reference/optimize.linprog-simplex.html
0 : Optimization terminated successfully
1 : Iteration limit reached
2 : Problem appears to be infeasible
3 : Problem appears to be unbounded
"""

solvector= sol['x']
solvalue=-1*sol['fun']
solstatus=sol['status']
conclusion="This LP can be solved"

if solstatus==2:
    conclusion = "The LP is not feasible"
elif solstatus==3:
    conclusion = "The LP is unbounded"
elif solstatus==1:
    conclusion= "The program timed out"

report=(conclusion,solvector,solvalue,)
print(report[0],'\n')
print("an optimal solution:"'\n',report[1],'\n')
print("The optimal value:",report[2])






