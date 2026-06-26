#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(*n):
    s = 0 
    for i in n :
        s += i 
    return s 


# In[2]:


def mul(*n):
    m = 1 
    for i in n :
        m *= i 
    return m


# In[3]:


def check(num):
    if num % 2 == 0 :
        return f"{num} is Even"
    else:
        return f"{num} is Odd"


# In[ ]:




