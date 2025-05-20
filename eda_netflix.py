#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df = pd.read_csv('C:\\Users\\vtu18\\OneDrive\\Documents\\EDA-on-Netflix-Dataset\\netflix_titles.csv')


# In[9]:


df.head()


# In[41]:


print(df.shape)
print(df.dtypes)


# In[13]:


print(df.isnull().sum())


# In[15]:


df.dropna(subset=['rating','duration','date_added'],inplace=True)


# In[27]:


print(df.isnull().sum())


# In[25]:


df['director'].fillna('unknown', inplace=True)
df['cast'].fillna('not specified',inplace=True)
df['country'].fillna('unknown',inplace=True)


# In[31]:


df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')


# In[33]:


df[df['date_added'].isna()]


# In[35]:


df['date_added'] = pd.to_datetime(df['date_added'])


# In[39]:


df.drop_duplicates(inplace=True)


# In[43]:


df.to_csv("netflix_titles_cleaned.csv", index=False)

