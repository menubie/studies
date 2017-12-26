
# coding: utf-8

# In[28]:


get_ipython().magic('matplotlib inline')


# In[7]:


import pandas as pd


# In[8]:


OUTPUT = "./datasets/"


# # Distributions Exercises
# 
# Identify:
# 
# * Random variable types
# * FDP, FDA, FMP
# 
# ## Dataset 1: Joint child malnutrition estimates – 2017 edition
# 
# Datasource: https://data.unicef.org/topic/nutrition/malnutrition/
# 
# * Severe Wasting: Percentage of children aged 0–59 months who are below minus three standard deviations from median weight-for-height of the WHO Child Growth Standards.
# * Wasting – Moderate and severe: Percentage of children aged 0–59 months who are below minus two standard deviations from median weight-for-height of the WHO Child Growth Standards.
# * Overweight – Moderate and severe: Percentage of children aged 0-59 months who are above two standard deviations from median weight-for-height of the WHO Child Growth Standards. 
# * Stunting – Moderate and severe: Percentage of children aged 0–59 months who are below minus two standard deviations from median height-for-age of the WHO Child Growth Standards.
# * Underweight – Moderate and severe: Percentage of children aged 0–59 months who are below minus two standard deviations from median weight-for-age of the World Health Organization (WHO) Child Growth Standards

# In[9]:


d1 = pd.read_csv(OUTPUT+'dataset1_joint_child_malnutrition_estimates.csv')

d1c = d1[['Region', 'Country and areas', 'Year', 'Severe wasting',      'Wasting',  'Overweight',  'Stunting',  'Underweight']].copy()

d1c.sort_values(by=['Region', 'Country and areas', 'Year'], inplace=True)


# In[77]:


d1c[(d1c.Year == 2000)].groupby(['Region'])["Severe wasting"].count()


# Answer after analyze the figures below
# 1. Looking to Density Chart, which curve represents the worst region in terms of Severe Wasting? How to calculate this?
# 1. What is the probability of a country in Africa and Asia be under 1% of Severe Wasting?
# 1. Is the histogram a correct visualization?

# In[79]:


d1c[(d1c.Region.isin(['AFRICA', 'ASIA']))&(d1c.Year == 2000)][['Severe wasting', 'Region']]                        .groupby('Region').boxplot(figsize=(10,10))


# In[80]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20,10))

bp = d1c[(d1c.Region.isin(['AFRICA', 'ASIA']))&(d1c.Year == 2000)]                    .groupby('Region')['Severe wasting']                    .plot.density(legend=True, title='Density - Severe Wasting in Africa, Europe and Latin America in years 2000')


# In[82]:


import matplotlib.pyplot as plt2

fig2, ax2 = plt2.subplots(figsize=(20,10))

bp = d1c[(d1c.Region.isin(['AFRICA', 'ASIA']))&(d1c.Year == 2000)]                    .groupby('Region')['Severe wasting']                    .plot.hist(legend=True, title='Histogram - Severe Wasting in Africa, Europe and Latin America in years 2000')


# In[ ]:




