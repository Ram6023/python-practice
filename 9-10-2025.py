#!/usr/bin/env python
# coding: utf-8

# # NUMPY
# NumPy is a Linear Algebra in Python and it is the holy grail and the main building block of data science in the pyData Ecosystem

# In[2]:


pip install numpy


# In[1]:


import numpy as np


# In[4]:


arr1=np.array([1,2,3,4,5])
arr1


# In[5]:


type(arr1)


# In[6]:


arr1.size


# In[7]:


arr1.ndim


# In[8]:


arr1.shape


# # arrays can be of n dimensions

# In[10]:


my_matrix=[[2,3,4.5,4],[3,5,43,64],[5,6.6,45,4]]
my_matrix


# In[11]:


b=np.array(my_matrix)
b


# In[12]:


print('the dimesnions or array',b.ndim)


# In[13]:


print('the size of araay:',b.size)


# In[16]:


print('the type of array',b.shape)


# # integer

# In[20]:


import numpy as np
int8_arr=np.array([1,2,3],dtype=np.int8)
int16_arr=np.array([1003,-2000,3000],dtype=np.int16)
int32_arr=np.array([1003000,-2000000,300000],dtype=np.int32)
int64_arr=np.array([1003000000,-200000000,30000000],dtype=np.int64)




# # float

# In[21]:


float16_arr = np.array([1.1,-2.2,3.3],dtype=np.float16)
float32_arr = np.array([1.112345,-2.212345,3.321123],dtype=np.float32)
float16_arr = np.array([1.5434534541,-2.2123456789,.31234234567],dtype=np.float16)


# # complex

# In[23]:


#complex types
complex64_arr=np.array([1+2j,3+4j],dtype=np.complex64)
complex128_arr=np.array([1+2j,3+4j],dtype=np.complex128)


# # boolean

# In[25]:


#boolean type
bool_arr=np.array([True,False,True],dtype=bool)
print("bool:",bool_arr,bool_arr.dtype)


# # string

# In[31]:


#string type
string_arr=np.array(["apple","banana","cherry"],dtype='<U10')


# # object  

# In[34]:


#object type(mixed data types)
object_arr=np.array([1,"two",3.0,True],dtype=object)


# In[ ]:
