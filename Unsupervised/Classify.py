# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:24:31 2017

@author: sheet_000
"""

import xlrd
import xlwt
import math
import numpy as np
import matplotlib.pyplot as plt


n = 2
data = []
book = xlrd.open_workbook('Gen Data.xls')
sheet = book.sheet_by_name('Classification Data')           
for i in range(0,sheet.nrows) :
     row_data = []
     for j in range(sheet.ncols) :
         
           row_data.append(float(sheet.cell(i,j).value))
           
           
     data.append(row_data)  
     
print data[2]
     
V=[]     
sheet1 = book.sheet_by_name('Cluster Centers')           
for i in range(0,sheet1.nrows) :
     row_data1 = []
     for j in range(sheet1.ncols) :
         
           row_data1.append(float(sheet1.cell(i,j).value))
           
           
     V.append(row_data1)  
     
print  V
print"***************************"  

V= np.array(V)
c= len(V)     
N= len(data)    
n=2 
D =  [ [0 for i  in range(N)] for j  in range(c)]
u = [ [0 for i in range(N)] for j in range(c) ]

count = 0
for k in range(N) :
      count = count +1
      o = count%c
      u[o][k] = 1
   

def denom(D , l3 ,i3,c) :
    sum3 = 0.0
    for i in range(c) :
        sum3 = sum3 + (1.0*D[l3][i3]/D[i][i3])**2    
    return sum3                                        
        

s = [ 0 ,0] 
for i2 in range(c) :
   for j2 in range(N) :
           for l2 in range(n) :
              s[l2] =  data[j2][l2] - V[i2][l2]
              
           D[i2][j2] = math.sqrt(s[0]**2 + s[1]**2)
           
           
for i3 in range(N) :
      
         zeroes = -1
      
         for j3 in range(c) :
          if D[j3][i3] == 0 :
              zeroes = j3
          
         if(zeroes == -1) :
          
              for l3 in range(c) :
                     u[l3][i3] = 1.0/ denom(D , l3 ,i3,c)
   
         else :
           for l4 in range(c) :
              if(l4 != zeroes) :
                  u[l4][i3] = 0.0
              else :
                   u[l4][i3] = 1.0           
                   
print u
                   
                   
Clusters= [[0 for i in range(N) ]  for j in range(3)]

def m (U , z,c) :
    ma = 0
    ind = 0
    for i in range(c):
        if (U[i][z] > ma) :
            ma = U[i][z]
            ind = i
    return ind   
    

for z1 in range(N) :
    
        Clusters[0][z1] = data[z1][0]
        Clusters[1][z1] = data[z1][1]
        Clusters[2][z1] = m(u ,z1,c)


x = Clusters[0]
y = Clusters[1]
t = Clusters[2]

print t

plt.scatter(x, y, c=t)
plt.scatter(V[:,0] ,V[:,1],c='k',s=75 )
plt.title("Classification Data")
plt.show()                   