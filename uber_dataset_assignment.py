#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# 

# In[ ]:


#load uber_data.csv dataset
import pandas as pd
uber_data = pd.read_csv(r"C:\Users\srira\OneDrive\ドキュメント\datasets-main\uber_data.csv")

# Display first 5 row
uber_data.head()


# In[17]:


# showing number of rows and col
uber_data.shape


# In[18]:


# showing all column names
uber_data.columns


# In[19]:


#data types of each column
uber_data.dtypes


# In[20]:


#  unique values in CATEGORY column
uber_data['CATEGORY*'].unique()


# In[21]:


#  null values in PURPOSE column
uber_data['PURPOSE*'].isnull().sum()


# In[45]:


# renaming all columns to uppercase
uber_data.columns = uber_data.columns.str.replace('*', '', regex=False).str.upper()

uber_data.columns


# # Assignment 2

# In[46]:


# display rides where category==Business
uber_data[uber_data['CATEGORY'] == 'Business']


# In[47]:


# show top 5 rides with the longest distance(miles)
uber_data.sort_values(by='MILES', ascending=False).head(5)


# In[25]:


# null values in purpose column
uber_data['PURPOSE'] = uber_data['PURPOSE'].fillna("Not Specified")

uber_data['PURPOSE'].isnull().sum()


# In[35]:


# Show a preview
print(uber_data[['START_DATE', 'END_DATE', 'TRIP_DURATION']].head())


# In[37]:


uber_data.sort_values(by='MILES', ascending=False)


# # Assignment 3

# In[38]:


# average miles per category
a_miles = uber_data.groupby('CATEGORY')['MILES'].mean()
a_miles


# In[39]:


# counting trips based on purpose
p_count = uber_data['PURPOSE'].value_counts()
p_count


# In[40]:


# finding top 3 most common start locations
t_start_loc = uber_data['START'].value_counts().head(3)
t_start_loc


# In[42]:


import matplotlib.pyplot as plt

# bar chart of average miles
a_miles.plot(kind='bar')

plt.title("Average Miles by Category")
plt.xlabel("Category")
plt.ylabel("Average Miles")
plt.show()


# In[44]:


# pie chart of trip purposes
p_count.plot(kind='pie', autopct='%1.1f%%')

plt.title("Distribution of Trip Purposes")
plt.ylabel("")  
plt.show()


# In[ ]:




