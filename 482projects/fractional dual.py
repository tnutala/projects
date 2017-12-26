# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:22:09 2017

@author: tnuta
"""
import numpy as np
import math
import scipy.optimize as lp

# User input for the rows, columns and entries of the A matrix

tabform=input("Is the tableau in stadard form? (y/n):")
    

print("What does your A matrix look like?")

n = int(input("number of rows?: "))
m = int(input("number of columns?: "))

A=[]
for i in range(0,n):
    for j in range(0,m):
        try:
            A.append(float(input("entry in row %u column %u: " %(i,j) )))
        except:
            print("thats not a number so I'm gonna assume its 0")
            A.append(0.0)

#formating entries into n rows and m columns
A=np.array(A)
A = A.reshape((n,m))
""""
Aid = np.identity(n)
A = np.hstack((Aid,A))
"""


print("this is what your A matrix looks like:")
print(A)

# User input for the entries of the b vector
print("what are the entries for the b vector?")
b=[]
for i in range(0,n):
    try:
        b.append(float(input("entry in row %u: " %(i))))
    except:
        print("thats not a number so I'm gonna assume its 0")
        b.append(0.0)
print("this is what your b vector looks like:")
"""
b=np.array(b)
b=b.reshape((n,1))
"""
print(b)

# User input for the entries of the c vector
print("what are the entries for the c vector?")
c=[]
for i in range(0,m):
    try:
        c.append(-1*float(input("entry in row %u: " %(i))))
    except:
        print("thats not a number so I'm gonna assume its 0")
        c.append(0.0)
"""
if tabform=="n":
    czeros= [0]*n
    for i in c:
        czeros.append(i)
    c= czeros
"""
print("this is what your c vector looks like:",c)


"""
c=np.array(c)
print(c)
c=c.reshape((1,m))
print(len(c))
"""

"""
#converting to standard tableau form
Aid = np.identity(n)
cid= np.zeros((1,n))
cfunc=np.zeros((1,1))
c = np.hstack((cid,c,cfunc))
tab = np.hstack((Aid,A,b))
tab = np.vstack((tab,c))
print("this is what your tableau looks like:")
print(tab)

"""

##REMEMBER THAT ROWS AND COLUMNS ARE 0-indexed
print("new:")
def gomory_cut(tab):        #returns one gomory cut using the topmost row with a non-integer entry in the last column
    tabrows=tab.shape[0]
    tabcols=tab.shape[1]
    gcut = np.zeros((1,tabcols))
    gcut = gcut.reshape((1,tabcols)) 
    for row in range(0,tabrows):
        if (tab[row][tabcols-1]).is_integer() == False:
            for column in range(0,tabcols):
                gcut[0][column] = -1*(tab[row][column]-math.floor(tab[row][column]))
                if gcut[0][column]== -0: #reseting -0 to 0 because apparently there is a difference
                    gcut[0][column]= 0
        
            newtab=np.vstack((gcut,tab))
            gcutslack= np.zeros((newtab.shape[0],1))
            gcutslack[0][0]= 1
            newtab=np.hstack((gcutslack,newtab))
          #  print(newtab)
            return newtab
        else:
            continue
      
if tabform =="y":
    A_ub=None
    b_ub=None
    A_eq=A
    b_eq=b
elif tabform=="n":
    A_ub=A
    b_ub=b
    A_eq=None
    b_eq=None


print(type(lp.linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=None, method='simplex', callback=None, options=None)))

def simplex(c,A,b):    
    
    return lp.linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=None, method='simplex', callback=None, options=None)

        
            
            
            
            





