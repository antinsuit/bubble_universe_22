#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


'''importing librareis to do the calculations, plot curve, find solutions and save them'''
import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python\dataset3cnew.csv")
pp = PdfPages(r"C:\Users\HP\Downloads\NSSCgraphs.pdf")

'''adding the values to respective lists'''
mylist1 = df['k2'].tolist()
mylist2 = df['k1'].tolist()
mylist3 = df['4T'].tolist()
delta = df['delta'].tolist()

'''loop for doing calculations, ploting the data and saving them in pdf formate'''
for h in range(50):
    '''numpy array x contains 40 discreate and equally intervaled points in [-2,2)'''
    x = np.linspace(-2, 2 , 40)
    '''putting values of K1, K2 and T as coefficient of polinmial eqation that gives the solutions'''
    coeffs = [mylist1[h],-1*mylist2[h],0,mylist3[h]]
    
    '''saving the values of the polinomial for the values in array x'''
    y = np.array([np.sum(np.array([coeffs[i]*(j**i) for i in range(len(coeffs))])) for j in x])
    
    '''ploting values of y vs x and roots on the same graph'''
    plt.axvline(0, color='grey', lw=0.5)
    plt.axhline(0, color='grey', lw=0.5)
    if delta[h] > 0:
        p = [coeffs[3-k] for k in range(4)]
        roots = np.roots(p)
        for r in roots:
            '''marking the positive roots of the eqation'''
            if r>0:
                plt.plot(r, 0, marker = "o", markersize=10, markeredgecolor="red", markerfacecolor="yellow")
                plt.annotate(math.trunc(r*10000)/10000, (r, 0))
        plt.xlabel(f"possible radii are {roots[1]} and {roots[2]}")
    else:
        plt.xlabel("no possible radii for given constants")
                
    plt.plot(x, y)
    plt.savefig(pp, format='pdf')
    plt.show()
pp.close()


# In[13]:


import numpy as np
import pandas as pd
import math
import cmath
df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python\3b_dataset.csv")

''' adding values of k2,k1 and T to the lists'''
mylist1 = df['k2'].tolist()
mylist2 = df['k1'].tolist()
mylist3 = df['T'].tolist()

count = 0

'''calculating the number of positive roots of the polynomial eqation and saving in csv file'''

for h in range(51):
    p = [4*mylist3[h],0,-1*mylist2[h],mylist1[h]]
    roots = np.roots(p)
    for r in set(roots):
        if r.imag == 0 and r.real>=0:
            count += 1
    df.loc[h,'number of possible radii'] = count
    count = 0
    df.to_csv(r"C:\Users\HP\OneDrive\Desktop\python\3b_dataset.csv", index=False)
    
            
            
            
    
    


# In[14]:


import numpy as np
import pandas as pd
import math

df = pd.read_csv(r"C:\Users\HP\Downloads\3c_dataset.csv")

mylist1 = df['k1'].tolist()
mylist2 = df['k2'].tolist()
mylistT = df['T'].tolist()
mylistR = df['R'].tolist()

count = 0

'''finding the value of the polynomial (and hence state of the universe) for given value of k1,k2 and 3'''
for h in range(50):
    k1 = mylist1[h]
    k2 = mylist2[h]
    T = mylistT[h]
    R = mylistR[h]
                
    delta = (k2/(R**4)) + (4*T/R) - (k1/(R**3))  
    if delta>0:
        df.loc[h,'state of universe'] = 'contracting'
    elif (delta == 0):
        df.loc[h,'state of universe'] = 'expanding'
    elif delta<0:
        df.loc[h,'state of universe'] = 'stable'
    df.to_csv(r"C:\Users\HP\Downloads\3c_dataset.csv", index=False)
    print(delta)


# In[ ]:




