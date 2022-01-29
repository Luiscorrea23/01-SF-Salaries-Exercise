#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


sal = pd.read_csv("/Users/luiscorrea/Desktop/Salaries.csv")


# ** Check the head of the DataFrame. ** 

# In[3]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[4]:


sal.info()


# What is the average BasePay ?

# In[5]:


sal = sal[(sal["BasePay"] != "NaN") & (sal["BasePay"] != "Not Provided")]


# In[6]:


sal["BasePay"]= sal["BasePay"].astype("float64")


# In[7]:


sal["BasePay"].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[8]:


sal["OvertimePay"]= sal["OvertimePay"].astype("float64")


# In[9]:


sal["OvertimePay"].max()


# ** What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[10]:


sal.loc[sal["EmployeeName"] == "JOSEPH DRISCOLL", "JobTitle"]


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[11]:


sal.loc[sal["EmployeeName"] == "JOSEPH DRISCOLL", "TotalPayBenefits"]


# ** What is the name of highest paid person (including benefits)?**

# In[12]:


sal["TotalPayBenefits"].max()


# In[13]:


sal.loc[sal["TotalPayBenefits"] == 567595.43]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[14]:


sal["TotalPayBenefits"].min()


# In[15]:


sal.loc[sal["TotalPayBenefits"] == -618.13]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[16]:


sal.groupby(['Year'])[["BasePay"]].agg(["mean"])


# ** How many unique job titles are there? **

# In[17]:


sal["JobTitle"].value_counts()


# ** What are the top 5 most common jobs? **

# In[18]:


sal["JobTitle"].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **
# 

# In[19]:


((sal.loc[sal["Year"] == 2013, "JobTitle"].value_counts()) == 1).value_counts()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[20]:


len(sal.loc[sal["JobTitle"].str.contains("Chief")])


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[25]:


sal[["JobTitle","TotalPayBenefits"]].sort_index()


# In[34]:


sal["len_title"] = sal["JobTitle"].str.len()


# In[37]:


sal[["len_title", "TotalPayBenefits"]].corr()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




