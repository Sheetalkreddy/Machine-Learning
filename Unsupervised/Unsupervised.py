# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:47:14 2017

@author: sheet_000
"""
import xlrd
import xlwt
import math
import numpy as np
import random
import matplotlib.pyplot as plt


n = 2
data = []
book = xlrd.open_workbook("Data Sets.xlsx")
sheet = book.sheet_by_name('Data Set 4')           
for i in range(2,sheet.nrows) :
     row_data = []
     for j in range(sheet.ncols) :
         
           row_data.append(float(sheet.cell(i,j).value))
           
           
     data.append(row_data)      
     
mining_data = []
classification_data =[]

for i in range(len(data)) :
    if (i%5 == 0) :
         classification_data.append(data[i])
    else :
        mining_data.append(data[i])
         
         
         

m = 2
epi = 0.001 
    

N = len(mining_data)   



def denom(D , l3 ,i3,c) :
    sum3 = 0.0
    for i in range(c) :
        sum3 = sum3 + (1.0*D[l3][i3]/D[i][i3])**2    
    return sum3                                        
        
        
def norma(u , u_prev ,c) :
    arr = []
    for ri in range(c) :
         for r2 in range(N) :
             arr.append(abs(u[ri][r2] - u_prev[ri][r2]))
    return max(arr)        
 
def J(z,v,u,c) :
    sum1 = 0
    for i in range(c) :
        sum2 = 0
        for k in range(N) :
            sum2 = sum2 + u[i][k]*u[i][k]*((mining_data[k][0] - v[i][0])**2  + (mining_data[k][1] - v[i][1])**2)
        sum1 = sum1 +sum2
    return sum1    
        
        
L=[ 0 for i in range(11)]    
Jval = [ 0 for i in range(11)]       
b =[2,3,4,5,6,7,8,9,10]
random.seed(0)
def FuzzyC_Means(a) :
    
 for c in  a: 
    
    l = 0 
    u = [ [0 for i in range(N)] for j in range(c) ]
    
    u_prev = [ [0 for i in range(N)] for j in range(c) ]
    
    
    v= [[0.5 for i  in range(n)] for j  in range(c)]
    D =  [ [0 for i  in range(N)] for j  in range(c)]
    
    sumc = [0 for i in range(c)] 
    for d2 in range(N) :
        
        
        for d3 in range(c) :
            
            u[d3][d2] = random.randint(0,10)
            sumc[d3] = sumc[d3] + u[d3][d2]
    for d1 in range(N) :        
       for d4 in range(c) :    
            u[d4][d1] =  1.0*u[d4][d1]/sumc[d4]
   


    while ( norma(u, u_prev,c) >0.001) :

  
      l= l+1
  
      for k5 in range(c) :
        for k6 in range(N):
           u_prev[k5][k6] = u[k5][k6]
         
 
      for i1 in range(c) :
        for j1 in range(n) :
          sum1 =0.0
          sum2 = 0.0
          for l1 in range(N) :
              
              sum1 = sum1  + (u[i1][l1]**2)*mining_data[l1][j1]
              
              sum2 = sum2 + u[i1][l1]**2
          
          v[i1][j1] = 1.0*sum1/sum2
      
      
      s = [ 0 ,0] 
      for i2 in range(c) :
         for j2 in range(N) :
           for l2 in range(n) :
              s[l2] =  mining_data[j2][l2] - v[i2][l2]
              
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
    print "******************************************"  
    print "c is :" ,c   
    kl =     J(mining_data,v,u,c) 
    print "J is :" , kl
    Jval[c] =kl
    print v    
    print l
    L[c] =l
    
 return u,v
      
FuzzyC_Means(b) 
rc=[ 0 for i in range(11)]    
for jh in range(2,11,1) :
    print " for " , jh
    print "  J is " , Jval[jh]

for jh in range(3,10,1) :
    r = 1.0*(Jval[jh] - Jval[jh-1]) /(Jval[jh+1] - Jval[jh])
    rc[jh] =r
for jh in range(3,10,1) :
    print " for " , jh
    print "  rc is " , rc[jh]

ind = rc.index(max(rc))
    
U_fin ,V_fin = FuzzyC_Means([ind])     
print V_fin   
V_fin = np.array(V_fin)
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
    
        Clusters[0][z1] = mining_data[z1][0]
        Clusters[1][z1] = mining_data[z1][1]
        Clusters[2][z1] = m(U_fin ,z1,ind)


x = Clusters[0]
y = Clusters[1]
t = Clusters[2]

plt.scatter(x, y, c=t)
plt.scatter(V_fin[:,0] ,V_fin[:,1],c='k',s=75 )
plt.title("Mining Data")
plt.show()

workbook = xlwt.Workbook()
sheet2 = workbook.add_sheet('Mining Data')
sheet = workbook.add_sheet('Classification Data')
sheet1 = workbook.add_sheet('Cluster Centers')

for tr in range(len(classification_data)) :
    sheet.write(tr , 0, classification_data[tr][0])
    sheet.write(tr , 1, classification_data[tr][1])
    
    
for tr2 in range(len(V_fin))   :
    sheet1.write(tr2,0,V_fin[tr2][0])
    sheet1.write(tr2,1,V_fin[tr2][1])
    
for tr3 in range(len(mining_data))  :  
    sheet2.write(tr3 , 0, mining_data[tr3][0])
    sheet2.write(tr3 , 1, mining_data[tr3][1])
    
workbook.save('Gen Data.xls')    