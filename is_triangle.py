
# coding: utf-8

# In[8]:


import math
from math import exp, expm1

def is_triangle(bundle):
    
    if ((bundle[0]+bundle[1]) > bundle[2] and (bundle[0]+bundle[2]) > bundle[1] and (bundle[1]+bundle[2]) > bundle[0]):
        return True
    else:
        return False


list_of_triples = [(4,8,12), (3,4,5),(5,12,13),(1,math.sqrt(3),2),(3*math.exp(1),4*math.exp(1),5*math.exp(1))]

print(list(filter(is_triangle,list_of_triples)))

