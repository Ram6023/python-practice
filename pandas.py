#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[]
type(a)


# In[2]:


a=[23,45,67,78]
a


# In[3]:


a[2] 


# In[4]:


a


# In[5]:


a[1]=100
a


# In[6]:


a


# In[7]:


# append()
# insert()
# extend()


# In[8]:


a


# In[9]:


print(a)  # 23 100 67 78
a.append(50)
print(a)   # 23 100 67 78 50


# In[10]:


print(a)  #  23, 100, 67,78, 50
b=[34,56,89,67] 
a.append(b) 
print(a)    #  23,100,67,78,50, 34,56,89,67


# In[11]:


print(a[4])  #
print(a[5])
print(a[5][0])


# In[12]:


# 1. List is a data structure in python
# 2. List is mutable and it allows duplicate values
# 3. Append() method is used to append the values to existing list
# 4. using append method we can add single element or multiple elements
# 5. List follows indexing order.


# In[13]:


# append()
# insert()
a=[23,45,77,99,11,43,66]
a


# In[14]:


print(a)
a.insert(1,33)
print(a)


# In[15]:


print(a)
b=[10,20,30]
a.insert(2,b)
print(a)
print(a[2])


# In[16]:


# append() 
# insert()
# extend()
a=[23,45,77,99,11,43,66]
print(a)
b=[10,20,30]
a.extend(b)
print(a)


# In[17]:


# append(): it is used to add element in a end of list
#   it provides single index position for multiple values also 
# insert() : it is used to insert an element in a specific index
# extend() : it is used to add list of elements to exisiting list.
#     it provides separate index postion for each value


# In[18]:


# remove()
# pop()
# pop(index)
# clear()

list=[34,56,67,89,10]
print(list)
list.remove(67)
print(list)


# In[19]:


# remove()
# pop()
# pop(index)
# clear()

list=[34,56,67,89,10]
print(list)
list.pop()
print(list)


# In[20]:


# remove()
# pop()
# pop(index)
# clear()

list=[34,56,67,89,10]
print(list)
list.pop(1)
print(list)


# In[21]:


# Sort
list=[34,56,67,89,10]
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)


# In[22]:


list=[34,56,67,89,10]
list1=list.copy()
print(list)
print(list1)
list1.append(100)
print(list)
print(list1)


# In[23]:


list=[34,56,67,89,10,10,34,10]
print(list.index(56))
print(list.count(10))


# In[24]:


# Write a program to print even numbers in a given list
a=[23,78,45,67,71,90]
for i in a:
    print(i,end=" ")


# In[25]:


a=[23,78,45,67,71,90]
for i in a:
    if i%2==0:
        print(i,end=" ")


# In[26]:


# Write a program to print prime numbers in a given list
# Write a program to print second max element in a given list


# # Tuple:
#   -- min()
#   -- max()
#   -- count()
#   -- sum()
#   -- slicing

# In[27]:


list=[34,56,67,78,32,90]

for i in list:
    if i%2==0:
        print(i, end=" ")
    


# In[28]:


list=[34,56,67,78,32,90,11,13,17]
fact=0
for i in list:
    fact=0
    for j in range(1, (i+1)):
        if i%j==0:
            fact=fact+1
    if fact==2:
        print(i, end=" ")
        


# In[29]:


list=[34,56,67,78,32,90,11,13,17]
list.sort(reverse=True)
print(list[1])


# In[30]:


# Write a program to find number of words in a given string
# input : Hi hello this is Nagul
# Eouput: 5


# In[31]:


str="Hi hello this is Nagul"
words=str.split(" ")
print(type(words))
print(words[2])
print("Number of words :",len(words)) 


# In[34]:


#  Tuple:  min() -- max() -- count() -- sum() -- slicing


# In[35]:


#1. Tuple allows duplicate values
#2. it follows the indexing order
#3. it is immutable

a=(23,45,56,89)
print(a)
print(a[1])
print("Max : ", max(a))
print("Min : ", min(a))
print("Total: ",sum(a))
print("No.of values :",len(a));

a[1]=100  # Error because tuple is immutable
a[:]
a[2:]
a[:5]
a[-1]
a[::]
a[::-1]




# In[43]:


uber_data = pd.read_csv(r"C:\Users\srira\OneDrive\ドキュメント\datasets-main\uber_data.csv")


# In[44]:


uber_data.head()


# In[45]:


uber_data.loc[1, 'START*']


# In[48]:


uber_data.loc[[1,2,3],['START*','STOP*','MILES*']] #- This selects the rows with index labels 1, 2, and 3.


# In[49]:


temp=pd.DataFrame({'A':[1,2,3,4],'B':[10,20,30,40],'C':['2025-1-19','2025-1-21','2025-1-11','2025-1-22']}) # creating the temporary data set
temp.dtypes               # to check the datatype
temp.head()               # to get the head of dataframe


# In[50]:


temp['C']=pd.to_datetime(temp['C'])        # changing the datatype of a data set
temp.dtypes                                  # to display the datatypes in the dataset


# In[54]:


a=uber_data[uber_data['MILES*']>6]
a #- This creates a Boolean mask — a series of True or False values — where each row is checked to see if the value in the 'MILES*' column is greater than 6.


# In[55]:


uber_data.loc[uber_data['START*']=="New York"]  
#display only new york data


# In[59]:


uber_data.loc[uber_data['START*'].isin(['New York','Cary'])]
# displays newyork and cary data


# In[61]:


b=uber_data.loc[(uber_data['MILES*']>10) & (uber_data['START*'].isin(['Cary','Morris']))]
b


# In[ ]:




