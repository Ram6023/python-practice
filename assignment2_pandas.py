#!/usr/bin/env python
# coding: utf-8

# # Part 1

# In[36]:


#load dataset
import pandas as pd
dataset_path = 'sales.csv' 

# Load dataset
df = pd.read_csv(dataset_path)


# In[6]:


# Display first and last 5 rows
print("First 5 rows:")
display(df.head())
print("\nLast 5 rows:")
display(df.tail())


# In[7]:


df.info()


# In[8]:


df.shape


# In[9]:


df.columns


# In[10]:


df.describe()


# In[11]:


# total + avg sales grouped by month (Jan to Apr included)
df.groupby('Month')['Sales'].agg(['sum', 'mean'])


# In[12]:


df['Sales'].sum()


# # Part 2

# In[13]:


# total sales per city per month
df.groupby(['City', 'Month'])['Sales'].sum()


# In[14]:


# average monthly sales per city
df.groupby('City')['Sales'].mean()


# In[15]:


# city with highest average sales
df.groupby('City')['Sales'].mean().idxmax()


# In[16]:


# city with lowest total sales
df.groupby('City')['Sales'].sum().idxmin()


# In[17]:


# each city's total across months
city_total = df.groupby('City')['Sales'].sum()
city_total


# In[18]:


city_total.nlargest(3)


# In[37]:


# top 3 stores by total sales
df.groupby('City')['Sales'].sum().nlargest(3)


# # part 3

# In[21]:


# store with highest sales in March
df[df['Month']==3].groupby('City')['Sales'].sum().idxmax()


# In[22]:


# store with lowest sales in April
df[df['Month']==4].groupby('City')['Sales'].sum().idxmin()


# In[23]:


# number of stores per city where avg monthly sales > 15
df.groupby('City')['Sales'].mean() > 15


# In[24]:


# stores in California having any monthly sales > 20
df[(df['Purchase Address'].str.contains(', CA')) & (df['Sales'] > 20)]


# # Part 4

# In[25]:


# mean, max, min sales per city
df.groupby('City')['Sales'].agg(['mean','max','min'])


# In[26]:


# city with highest avg March sales
df[df['Month']==3].groupby('City')['Sales'].mean().idxmax()


# In[27]:


# overall avg sales per city
df.groupby('City')['Sales'].mean()


# In[28]:


# month with highest overall sales
df.groupby('Month')['Sales'].sum().idxmax()


# In[29]:


# each city's best month
df.groupby(['City','Month'])['Sales'].sum().groupby('City').idxmax()


# In[30]:


# add average sales column per city
avg_city = df.groupby('City')['Sales'].mean()
avg_city


# In[31]:


# sorted by avg sales (desc)
avg_city.sort_values(ascending=False)


# # Part 5

# In[32]:


# total sales by city (bar chart)
import matplotlib.pyplot as plt

df.groupby('City')['Sales'].sum().plot(kind='bar')
plt.title("Total Sales by City")
plt.show()


# In[33]:


# average monthly sales (line chart)
df.groupby('Month')['Sales'].mean().plot(kind='line')
plt.title("Average Monthly Sales")
plt.show()


# In[34]:


df.groupby('City')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("City Share of Total Sales")
plt.ylabel("")  
plt.show()


# In[35]:


# top 10 stores total sales (horizontal bar chart)
df.groupby('City')['Sales'].sum().nlargest(10).plot(kind='barh')
plt.title("Top 10 Stores by Total Sales")
plt.show()


# In[ ]:




