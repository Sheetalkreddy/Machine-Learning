
# Differential Evolution

import random
import math
import numpy as np
import matplotlib.pyplot as plt


cr= 0.8

K =0.5
num_gen = 200

size = 200

Population =[[0 for i in range(2)] for j in range(size)]
Population_P =[[0 for i in range(2)] for j in range(size)]
fit =[0 for i in range(size)] 
x_co = [0 for j in range(num_gen)]
y_co = [0 for j in range(num_gen)]
print "Done"
N =2

#Y = input("Enter 1 for egg holder and 2 for other")
Y=2
if (Y==1):
 l =-512
 h= 512
 
else : 
 l=-10
 h=10

def fitness(X,Y):
    val=0
    if Y==1:
        val= -(X[1] +47) * math.sin (math.sqrt(abs (X[0]/2.0 + X[1] +47 )) ) -X[0]* math.sin(math.sqrt(abs(X[0] - X[1] - 47)))          
        
    else:   
        val = - abs(math.sin(X[0])*math.cos(X[1])*math.exp(abs( 1 - (math.sqrt(X[0]*X[0] + X[1]*X[1])/math.pi))))
    
    return val
    
    
for m in range(size):
    Population[m][0]=random.uniform(l,h)
    Population[m][1]=random.uniform(l,h)
    Population[m]= np.array(Population[m])
        
print "hello"    
    
for r in range(num_gen):  
   F = random.uniform(-2,2)
   print "Generation start:"
   for k in range(size):
     print k  
     trial = [0 for i in range(N)]
     Population_P[k]= Population[k]
     I = Population[k]
     
     for g in range(size):
         fit[g] = fitness(Population[g],Y)
        
         
     x_co[r] = np.mean(fit)
     
     y_co[r]=np.min(fit) 
     
       
     while True:  
       
       
       
       while True:
          x1= random.randint(0,size-1)
          x2= random.randint(0,size-1)
          x3= random.randint(0,size-1)
          if i!=x1 and x2!=i and x3!=i:
              break
       
       
       X1 = Population[x1]
       X2 = Population[x2]
       X3 = Population[x3]
       
       mutant = I + K*(X1-I) + F*(X2-X3)
       
       
       for n in range(N):
           c= random.uniform(0,1)
           if(c<cr) :
               trial[n]= mutant[n]
           else :   
               trial[n]=I[n ]
               
       if l<=trial[0]<=h and l<=trial[1]<=h:
         break      
     
     
         
         
       
     f1 = fitness(trial,Y)
     f2 = fitness(I,Y)
     if(f1<f2):
         Population[k]=np.array(trial)

       
gen=np.arange(0,num_gen,1)
      
plt.plot(gen,x_co,'ro',gen,y_co ,'bo')
plt.xlabel("Generation number")
plt.ylabel("Average value: Red , Best Value: Blue")
print y_co[num_gen-1]
plt.show()          