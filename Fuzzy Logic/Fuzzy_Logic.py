
from numpy import *
from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


num_set = 5;
"""

v1 = raw_input("Enter the name of first variable")

l1 = input("lower limit of first variable")
u1 = input("upper limit of first variable")

v2 = raw_input("Enter the name of second variable")
l2 = input("lower limit of second variable")
u2 = input("upper limit of second variable")


v3 = raw_input("Enter the name of third variable")
l3 = input("lower limit of third variable")
u3 = input("upper limit ofthird variable") """

def normalise(x,l,u):
    X = (2.0*x - (l+u)) / (u-l)
    return X
    
def denormalise(X,l,u):
     y = (X*(u-l) + (l+u))/2.0
     return y
     

def lin_equ(l1,l2):
    m=Decimal((l2[1]-l1[1]))/Decimal(l2[0]-l1[0])
    c=(l2[1]-(m*l2[0]))
    return m,c      
      
def membership(x):
    mem = [ 0,0,0,0,0,0,0,0,0]
    
    if(x<=-0.8) :
        mem[0]=1
       
        
    elif(x>=0.8) :
         mem[8]=1    
         
    else :
        if(-0.8<x<=-0.6 ):
            y = (x +0.8)/0.2
            mem[1]=y
            mem[0]=1-y
            
        elif(-0.6<x<=-0.4):
            y = (x+0.6)/0.2
            mem[2]=y
            mem[1]=1-y
        
        elif(-0.4<x<=-0.2):
            y = (x+0.4)/0.2
            mem[3]=y
            mem[2]=1-y
        
        
        elif(-0.2<x<=0.0):
            y = (x+0.2)/0.2
            mem[4]=y
            mem[3]=1-y
            
        elif(0.0<x<=0.2):
            y = (x-0.0)/0.2
            mem[5]=y
            mem[4]=1-y   
        
        elif(0.2<x<=0.4):
            y = (x-0.2)/0.2
            mem[6]=y
            mem[5]=1-y 
        
        elif(0.4<x<=0.6):
            y = (x-0.4)/0.2
            mem[7]=y
            mem[6]=1-y 
            
        elif(0.6<x<=0.8):
            y = (x-0.6)/0.2
            mem[8]=y
            mem[7]=1-y    
      
    return mem
       
fam = [ [0,0,1,2,2,2,3,3,4], [0,1,1,1,2,2,3,4,5] ,[1,1,2,2,2,3,3,3,4], [2,2,2,2,3,3,3,4,4],[2,3,3,3,3,4,5,5,5],[3,3,4,4,4,5,5,5,6] ,[6,6,6,6,6,7,7,8,8] , [6,6,6,7,7,7,7,8,8] , [6,6,7,7,7,8,8,8,8] ]

l1= 0
u1 = 30

l2 = 0
u2 = 20

l3=0
u3=30

h = 15
i = 10

def output(h,i):
    
    centroid = [-0.9 , -0.6 , -0.4 , -0.2 , 0 , 0.2 ,0.4 , 0.6 , 0.9]
    x = normalise(h,l1,u1)
    y = normalise(i,l2,u2)
    
    #print x
    #print y
    
    memx = membership(x)
    memy = membership(y)
    
    
    #print memx , memy
    
    cx =0
    cy=0
    
    x1=x2=y1=y2=a1=a2=b1=b2=0
    
    for k in range(0,9):
       
       if(memx[k]!=0) : 
           if (cx==0):
               x1 =k
               a1 = memx[x1]
               cx=1;
           else :
               x2 = k 
               a2 = memx[x2]
               
       if(memy[k]!=0.0) : 
           if (cy==0):
               y1 = k
               b1 = memy[y1]
               cy=1;
           else :
               y2 = k 
               b2 = memy[y2]
     
    actv = [0,0,0,0]
    actv[0] = a1*b1
    actv[1] = a1*b2 
    actv[2] = a2*b1
    actv[3] = a2*b2   

 
   
    sum1 = centroid[fam[x1][y1]]*actv[0] +  centroid[fam[x1][y2]]*actv[1] + centroid[fam[x2][y1]]*actv[2] + centroid[fam[x2][y2]]*actv[3]
    sum1 = sum1/(actv[0]+actv[1]+actv[2]+actv[3])    
     
    return denormalise(sum1,l3,u3)
   

print output(0,10)    

print output(12,11)   
print output(15,15)   
print output(24,3)   
print output(17,6)   
print output(2,14)   
print output(28,19)   

x = np.linspace(0,30,70)
y = np.linspace(0,20,70)


(X,Y)=np.meshgrid(x,y)

z = [ [0 for a in range(len(X)) ] for b in range (len(X[0])) ]
for i in range(len(X)):
    for j in range(len(X[0])):
        z[i][j]=output(X[i][j],Y[i][j])
        print z[i][j]



c = plt.contourf(x, y, z , 100)
plt.colorbar(c)



lx = plt.xlabel("Height in m")
ly = plt.ylabel("Inflow in K Cusecs")

plt.show()

fig = plt.figure()
ax = Axes3D(fig)


ax.contourf(X, Y, z, 1000, zdir='z' )
ax.set_zlim(0,30)
ax.invert_xaxis()

ax.set_xlabel("Height  in m")
ax.set_ylabel("Inflow in K Cusecs")
ax.set_zlabel("Outflow in K cusecs")
plt.show()
