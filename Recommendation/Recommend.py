# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:19:53 2017

@author: sheet_000
"""

import numpy as np
import math
import xlrd
import matplotlib.pyplot as plt
def sim(a,b) :
     ad = []
     bd = []
     for j in range(len(a)):
         for k in range(len(b)) :
             if (a[j][1]== b[k][1] ) :
                 ad.append(a[j])
                 bd.append(b[k])
                 
     
     a = np.array(a)
     b = np.array(b)
     ma = np.mean(a[:,2])
     mb = np.mean(b[:,2])
     sum1 = 0
     sum2 = 0
     sum3 = 0
     for i in range(len(ad)) :
         sum1 = sum1 + (ad[i][2] - ma)*(bd[i][2] - mb)
         sum2 = sum2 + (ad[i][2] - ma)**2
         sum3 = sum3 + (bd[i][2] - mb)**2
     if (sum2 ==0 or sum3 ==0):
         return 0
        
     
     return sum1/ (math.sqrt(sum2) * math.sqrt(sum3))    
     
     
Ratings = []

           
book = xlrd.open_workbook("data.xlsx")
sheet = book.sheet_by_name('Sheet1')           
for i in range(0,sheet.nrows) :
     row_data = []
     for j in range(sheet.ncols) :
         
           row_data.append([i,j,float(sheet.cell(i,j).value)])
           
           
     Ratings.append(row_data)      

Test=[]
for l1 in range(len(Ratings)):
     for l2 in range(len(Ratings[0])) :
         if(Ratings[l1][l2][2]==0) :
             Test.append(Ratings[l1][l2])

count = 0
pred = [[] for i in range(10)]
err = [[] for i in range(10)]


while ( count <10) :
    
    
      
      Avail = []
      NonAvail = []
      for i1 in range(len(Ratings)):
           for j1 in range(len(Ratings[0])) :
               if(Ratings[i1][j1][2]!=0) :
                 if ((i1+j1)%11 == count ) :
                     NonAvail.append(Ratings[i1][j1])
                 else :
                     Avail.append(Ratings[i1][j1])
      
             
      for i2 in range(len(NonAvail)) :
               item = NonAvail[i2][1]
               user = NonAvail[i2][0]
               rat = NonAvail[i2][2]
               user_test = []
               
               for j4 in range(len(Avail)):
                           if (Avail[j4][0] == user) :
                               user_test.append(Avail[j4])
               
               Sim = []
               Sim_val = []
               for j2 in range(len(Avail)):
                   if (Avail[j2][1] == item and Avail[j2][2]!=0 and Avail[j2][0]!=user) :
                       Sim.append(Avail[j2])
                       user_j2 =[]
                       for j3 in range(len(Avail)):
                           if (Avail[j3][0] == Avail[j2][0]) :
                               user_j2.append(Avail[j3])
                       Sim_val.append(sim(user_test,user_j2))
                               
                               
               
                       
               m1 = Sim_val.index(np.max(Sim_val))
               Sim_val[m1] = -2
                       
               m2 = Sim_val.index(np.max(Sim_val))
               Sim_val[m2] = -2
                       
               m3 = Sim_val.index(np.max(Sim_val))
                       
               r  =[]
               r.append(Sim[m1][2])
               r.append(Sim[m2][2])
               r.append(Sim[m3][2])
               f=np.mean(r)
               pred[count].append(int(f))
               err[count].append(f-rat)   
               
                       
      count = count +1;      
rmserr=[]
for t in range(10) :
   su = 0
   for w in range(len(err[t])):
       su = err[t][w]**2
   merr = math.sqrt(su*1.0/len(err[t]))    
   rmserr.append(merr)
   
pl = [i for i in range(10)]

plt.title("RMS Error")
plt.ylabel("Error")
plt.xlabel("90-10 Fold number")   
plt.plot(pl,rmserr,'r' )         
plt.show()      
          
print "Prediction for unobserved"
for i3 in range(len(Test)) :
               item = Test[i3][1]
               user = Test[i3][0]
               rat = Test[i3][2]
               user_test = []
               
               for j4 in range(len(Avail)):
                           if (Avail[j4][0] == user) :
                               user_test.append(Avail[j4])
               
               Sim = []
               Sim_val = []
               for j2 in range(len(Avail)):
                   if (Avail[j2][1] == item and Avail[j2][2]!=0 and Avail[j2][0]!=user) :
                       Sim.append(Avail[j2])
                       user_j2 =[]
                       for j3 in range(len(Avail)):
                           if (Avail[j3][0] == Avail[j2][0]) :
                               user_j2.append(Avail[j3])
                       Sim_val.append(sim(user_test,user_j2))
                               
                               
               
                       
               m1 = Sim_val.index(np.max(Sim_val))
               Sim_val[m1] = -2
                       
               m2 = Sim_val.index(np.max(Sim_val))
               Sim_val[m2] = -2
                       
               m3 = Sim_val.index(np.max(Sim_val))
                       
               r  =[]
               r.append(Sim[m1][2])
               r.append(Sim[m2][2])
               r.append(Sim[m3][2])
               f=np.mean(r)
               print "user:  ",user, "  item : " ,item , " rating :", int(f)


              
                     
                     
                     
                     
                     
                     
                     
                     