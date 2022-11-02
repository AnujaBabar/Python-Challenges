#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in range(0,10):
    print(i)


# In[4]:


student_name=['Rakesh','Ramesh','Suresh']
print(student_name)


# In[73]:


import math


# In[ ]:


import cube


# In[7]:


city=["Mumbai","Pune","goa"]
city


# In[49]:


for i in range(0,10):
    if i%2==0:
        print("Number is even")


# In[19]:


x = 3%2
x


# In[22]:


marks=[23,23,25,24,27]
marks[4]=23
marks


# In[23]:


import numpy as np


# In[ ]:


import pandas as pd
df=pd.read_csv("F:\Python\Datasets and problem statements\Fish_dataset.csv")


# In[62]:


## add 5 marks in every marks
Marks=[23,30,27,29]
for i in Marks:
    print(i+5)
    i


# In[28]:


def add(x,y):
    answer=x+y
    return(answer)
add(2,5)


# In[30]:


weight=[34,35,40, 48]
print(sum(weight))


# In[ ]:


import pandas as pd
df=pd.read_csv("Titanic.csv")
df.head()


# In[33]:


keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

sampleDict = dict(zip(keys, values))
print(sampleDict)


# In[35]:


Dictionary={1:'red',2:'green',3:'pink'}
Dictionary[1]


# In[70]:


odd=[]
for i in range(1,100):
    if i%2==0:
        odd.append(i)
    else:
        pass


# In[51]:


marks=[50,34,40,70,38,95]
for i in marks:
    if i <35:
        print("student failed")
    elif 35<i<60:
        print("Second class")
    elif 60<i<75:
        print("first class")
    elif 75<i<100:
        print("Distinction")


# In[71]:


sampleDict = {'a': 100, 'b': 200, 'c': 300}
print('200 in sampleDict.values()')


# In[ ]:




