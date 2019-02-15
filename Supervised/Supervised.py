# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:40:37 2017

@author: sheet_000
"""

           
           
#Supervised learning
import xlrd
import math
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.01


u = 1.0
l = -1.0
traindata=[]
testdata=[]
data = []

def normalise(x, u ,l):
    X = (x-l)/(u-l)
    return X

def err(tprev ,t , n ):
    sum1= 0
    for k in range(n):
        sum1 =  sum1 + (tprev[k] - t [k])**2
    
    return sum1          
           
           
book = xlrd.open_workbook("Data for assignment #3.xlsx")
sheet = book.sheet_by_name('Sheet2')           
for i in range(1,sheet.nrows) :
     row_data = [1]
     for j in range(sheet.ncols) :
         
           row_data.append(float(sheet.cell(i,j).value))
           
           
     data.append(row_data)      
           

           
for i in range(0,1331):
    for j in range(4):
      data[i][j] = normalise(float(data[i][j]) , u ,l)     

for k in range(0,1331):
    if(k%5==0):
        testdata.append(data[k])
    else :
        traindata.append(data[k])            
           
def h(x,t): 
    y=0
    for i in range(4) :
        y = y + x[i]*t[i]
        
        
    y1=1.0/(1 + math.exp(-y))
    
    return y1    
        
def diff(traindata,t,z,lam) :    
    
    sum1 = 0
    for i in range(len(traindata)) :
            sum1 = sum1 + ((h(traindata[i],t) -  traindata[i][4])*traindata[i][z]  ) / len(traindata)
    return alpha*(sum1 + lam*(t[z])/len(traindata))
         

t = [0.1,0,2,0.1]
tprev = [3,3,3,3]
print err(tprev,t ,3)
count=0

#while (err(tprev,t ,4) >0.00001 or count > 1000):

te_avg = [[],[],[]]
te_max=[[],[],[]]
tr_avg=[[],[],[]] 
tw=-1
arr =[0,1,10]
hist = [0,0]
np.array([0.1,0.1,0.1,0.1])
for lam in arr:
   tw=tw+1
   count =0
   while(count<2000):
     acc= 0  
     print "Lambda is ", lam
 
     count = count +1
     print "Count is" ,count
     for c in range(4):
         tprev[c] = t[c]
     
     for z in range(4) :
           
           
           m = diff(traindata , t , z , lam)/alpha
           
           
           t[z] = t[z] - m
           
           if (z==1) :
               if (m*hist[1] < 0 and hist[1]*hist[0] <0) :
                   alpha = alpha - alpha*0.6
               elif( m*hist[0] > 0 and m*hist[1] > 0 ) :
                   alpha = alpha + alpha*0.6
               
               
           hist[0]= hist[1]
           hist[1] =m
      
     tr=[] 
     te=[]
     for h1 in range(len(testdata)) :
         g= h(testdata[h1] , t)
         te.append(( g - testdata[h1][4])**2) 
         if (g>=0.5) :
             g1 = 1
         else :
             g1 =0
         if( g1 ==testdata[h1][4] ):
             acc = acc+1
     print "Accuracy is" ,acc*100.0/len(testdata)
         
             
         
     for h2 in range(len(traindata)) :
         tr.append((h(traindata[h1] , t)  - traindata[h1][4])**2)    
         
     te_avg[tw].append( np.mean(te)  )  
     
     te_max[tw].append( np.max(te) )
     tr_avg[tw].append(np.mean(tr))
   
     
     
     #print "Convergence " ,err(tprev , t, 4)      
     
     print "theta is ",t 
    

e = np.linspace(0,2000,2000)
print len(te_avg[1]) ,len(e)
print "testing avg"
plt.title("Average Testing Error across Iterations")
plt.ylabel("Error : (actual - pred)^2 ")
plt.xlabel("Iterations")
plt.plot(e,te_avg[0],'r' ,label='Lamda = 0') 
plt.plot(e,te_avg[1], 'b' , label='Lamda = 1')
plt.plot(e,te_avg[2] , 'g' , label='Lamda = 10')
plt.legend(loc = 'upper right')
plt.show()
print "testing max"
plt.title("Maximum Testing Error across Iterations")
plt.ylabel("Error : (actual - pred)^2 ")
plt.xlabel("Iterations")
plt.plot(e,te_max[0],'r' , label='Lamda = 0') 
plt.plot(e,te_max[1], 'b' , label='Lamda = 1')
plt.plot(e,te_max[2] , 'g', label='Lamda = 10')
plt.legend(loc = 'upper right')



plt.show()
print "training avg"
plt.title("Average Training Error across Iterations")
plt.ylabel("Error : (actual - pred)^2 ")
plt.xlabel("Iterations")
plt.plot(e,tr_avg[0],'r',label='Lamda = 0') 
plt.plot(e,tr_avg[1], 'b',label='Lamda = 1')
plt.plot(e,tr_avg[2] , 'g',label='Lamda = 10')
plt.legend(loc = 'upper right')
plt.show()
'''
te_avg2= [[] for hg in range(5)]
tw=-1
for alpha in [0.01, 0.05, 0.1 , 0.5 ,1 ]    :
   tw =tw+1
   lam =10
   count =0
   while(count<2000):
     acc= 0  
     print "Lambda is ", lam
 
     count = count +1
     print "Count is" ,count
     for c in range(4):
         tprev[c] = t[c]
     
     for z in range(4) :
           t[z] = t[z] - diff(traindata , t , z , lam)
      
     tr=[] 
     te=[]
     for h1 in range(len(testdata)) :
         g= h(testdata[h1] , t)
         te.append(( g - testdata[h1][4])**2) 
         if (g>=0.5) :
             g1 = 1
         else :
             g1 =0
         if( g1 ==testdata[h1][4] ):
             acc = acc+1
     print "Accuracy is" ,acc*100.0/len(testdata)
         
             
         
         
     te_avg2[tw].append( np.mean(te)  )  
   
e = np.linspace(0,2000,2000)
print "testing avg"
plt.title("Average Testing Error across Iterations")
plt.ylabel("Error : (actual - pred)^2 ")
plt.xlabel("Iterations")
plt.plot(e,te_avg2[0],'yellow' ,label='Aplha =0.01') 
plt.plot(e,te_avg2[1], 'b' , label='Aplha =0.05')
plt.plot(e,te_avg2[2] , 'g' , label='Aplha =0.1')
plt.plot(e,te_avg2[3]  ,'black', label='Aplha =0.5')
plt.plot(e,te_avg2[4]  , 'red',label='Aplha =1')

plt.legend(loc = 'upper right')
plt.show()     

te_avg2= [[] for hg in range(5)]
tw=-1
for t in [[0,0,0,0] , [-1,-1,-1,-1]  , [1,1,1,1]]    :
   tw =tw+1
   lam =10
   count =0
   while(count<2000):
     acc= 0  
     print "Lambda is ", lam
 
     count = count +1
     print "Count is" ,count
     for c in range(4):
         tprev[c] = t[c]
     
     for z in range(4) :
           t[z] = t[z] - diff(traindata , t , z , lam)
      
     tr=[] 
     te=[]
     for h1 in range(len(testdata)) :
         g= h(testdata[h1] , t)
         te.append(( g - testdata[h1][4])**2) 
         if (g>=0.5) :
             g1 = 1
         else :
             g1 =0
         if( g1 ==testdata[h1][4] ):
             acc = acc+1
     print "Accuracy is" ,acc*100.0/len(testdata)
         
             
         
         
     te_avg2[tw].append( np.mean(te)  )  
   
e = np.linspace(0,2000,2000)
print "testing avg"
plt.title("Average Testing Error across Iterations")
plt.ylabel("Error : (actual - pred)^2 ")
plt.xlabel("Iterations")
plt.plot(e,te_avg2[0],'r' ,label='Initial =[0,0,0,0]') 
plt.plot(e,te_avg2[1], 'b' , label='Initial =[-1,-1,-1,-1]')
plt.plot(e,te_avg2[2] , 'g' , label='Initial =[1,1,1,1]')


plt.legend(loc = 'upper right')
plt.show() 
'''




