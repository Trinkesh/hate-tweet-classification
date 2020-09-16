#!/usr/bin/env python
# coding: utf-8

# In[1]:


from joblib import load


# In[3]:


text = ["Virat Kohli, AB de Villiers set to auction their 'Green Day' kits from 2016 IPL match to raise funds"]

# load the saved pipleine model
pipeline = load("text.classification.joblib")


# In[4]:


pipeline.predict(text)


# In[ ]:




