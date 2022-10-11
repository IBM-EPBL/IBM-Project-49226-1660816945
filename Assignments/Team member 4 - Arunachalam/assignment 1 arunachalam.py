#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[1]:


s = "Hi there Sam!"
x=s.split()
print(x)


# ## 2. Use .format() to print the following string.
# 
# 
# ## Output should be: The diameter of Earth is 12742 kilometers.

# In[2]:


planet = "Earth"
diameter = 12742
print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));


# ## 3. In this nest dictionary grab the word "hello"

# In[3]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


# ## Numpy

# In[4]:


import numpy as np


# ## 4.1 Create an array of 10 zeros?
# ## 4.2 Create an array of 10 fives?

# In[5]:


array=np.zeros(10)
print("An array of 10 zeros:")
print(array)


# In[6]:


array=np.ones(10)*5
print("An array of 10 fives:")
print(array)


# ## 5. Create an array of all the even integers from 20 to 35
# 

# In[8]:


array=np.arange(20,35,2)
print("Array of all the even integers from 20 to 35")
print(array)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[9]:


x =  np.arange(0, 9).reshape(3,3)
print(x)


# ## 7. Concatenate a and b
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[10]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate((a, b), axis=0)


# ## Pandas
# ## 8. Create a dataframe with 3 rows and 2 columns

# In[11]:


import pandas as pd
data = [10,20,30]
df = pd.DataFrame(data,columns=["NUMBERS"])
print(df)


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[12]:


import pandas as pd
Date=pd.date_range(start='01-01-2023',end='10-02-2023')
print(Date)


# ## 10. Create 2D list to DataFrame

# In[14]:


import pandas as pd
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df = pd.DataFrame(lists, columns =['S.No', 'name','mark']) 
print(df )


# In[ ]:




