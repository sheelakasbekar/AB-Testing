#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import openpyxl
import seaborn as sns
import klib
import matplotlib.pyplot as plt
import datetime
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


# In[3]:


cg = pd.read_csv("C:\\Users\\Sheela\\Desktop\\Python\\Learn_Python\\control_group.csv")
cg


# In[4]:


cg.describe()


# In[5]:


cg.head(10)


# In[6]:


cg_null = cg.isnull().sum()
cg_null


# In[7]:


mean_i = cg["# of Impressions"].mean()

cg["# of Impressions"].fillna(value=mean_i, inplace=True)

mean_r =cg["Reach"].mean()
cg["Reach"].fillna(value=mean_r,inplace = True)

mean_wc= cg["# of Website Clicks"].mean()
cg["# of Website Clicks"].fillna(value=mean_wc,inplace=True)

mean_s= cg["# of Searches"].mean()
cg["# of Searches"].fillna(value=mean_s, inplace=True)
   
mean_vc= cg["# of View Content"].mean()
cg["# of View Content"].fillna(value=mean_vc, inplace=True)
   
mean_add= cg["# of Add to Cart"].mean()
cg["# of Add to Cart"].fillna(value=mean_add, inplace=True)


mean_pur= cg["# of Purchase"].mean()
cg["# of Purchase"].fillna(value=mean_pur,inplace = True)


# In[8]:


cg.dtypes


# In[9]:


tg = pd.read_csv("C:\\Users\\Sheela\\Desktop\\Python\\Learn_Python\\test_group.csv")
tg


# In[10]:


tg.describe()


# In[11]:


tg.head(10)


# In[12]:


tg_null = tg.isnull().sum()
tg_null


# In[13]:


cg.isnull().sum()


# In[14]:


comb_data = cg.merge(tg, how="outer").sort_values(["Date"])
comb_data


# In[15]:


comb_data["Campaign Name"].value_counts()


# In[16]:


comb_data.dtypes


# In[17]:


figure =px.scatter(data_frame=comb_data,

                   x= "# of Impressions",
                   y = "Spend [USD]",
                   size="Spend [USD]",
                   color ="Campaign Name",
                   trendline="ols")
        
figure.show()


# In[61]:


# The counts of each parameter to compare 

Reach_count= cg["Reach"].sum(),tg["Reach"].sum()
Reach_count

colors = ["green" , "red"]

plt.pie(Reach_count , labels= ['CG' ,'TG'],colors=colors , autopct ='1%.1f%%', startangle = 90,)


plt.axis('equal')

plt.title('Reach of Control Data VS Test Data')
plt.xlabel('Reach Count')

plt.show()


# In[46]:


Clicks_count= cg["# of Website Clicks"].sum(),tg["# of Website Clicks"].sum()
Clicks_count

colors = ["pink" , "yellow"]

plt.pie(Clicks_count , labels= ['CG' ,'TG'],colors=colors , autopct ='1%.1f%%', startangle = 90,)


plt.axis('equal')

plt.title('Website Clicks of Control Data VS Test Data')
plt.xlabel('Website Clicks Count')

plt.show()


# In[64]:


Searches_count= cg["# of Searches"].sum(),tg["# of Searches"].sum()
Searches_count

colors = ["blue" , "green"]

plt.pie(Searches_count , labels= ['CG' ,'TG'],colors=colors , autopct ='1%.1f%%', startangle = 90,)


plt.axis('equal')

plt.title('Search Count of Control Data VS Test Data')
plt.xlabel('Search Count')

plt.show()


# In[59]:


Content_count= cg["# of View Content"].sum(),tg["# of View Content"].sum()
Content_count

colors = ["pink" , "red"]

plt.pie(Content_count , labels= ['CG' ,'TG'],colors=colors , autopct ='1%.1f%%', startangle = 90,)


plt.axis('equal')

plt.title('Content of Control Data VS Test Data')
plt.xlabel('Content Count')

plt.show()


# In[63]:


Cart_count= cg["# of Add to Cart"].sum(),tg["# of Add to Cart"].sum()
Cart_count

colors = ["blue" , "yellow"]

plt.pie(Cart_count , labels= ['CG' ,'TG'],colors=colors , autopct ='1%.1f%%', startangle = 90,)


plt.axis('equal')

plt.title('Cart of Control Data VS Test Data')
plt.xlabel('Cart Count')

plt.show()


# In[58]:


Purchase_count= cg["# of Purchase"].sum(),tg["# of Purchase"].sum()
Purchase_count

colors = ["yellow" , "red"]

plt.pie(Purchase_count , labels= ['CG' ,'TG'],colors=colors , autopct ='1%.1f%%', startangle = 90,)


plt.axis('equal')

plt.title('Purchase of Control Data VS Test Data')
plt.xlabel('Purchase Count')

plt.show()


# In[ ]:




