#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS,TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split


# In[5]:


#read the data

data = pd.read_csv(r"C:\Users\trinkesh\OneDrive\Documents\twitter_sentiments.csv")


# In[6]:


data.head()


# In[7]:


data.shape


# In[8]:


data.isnull().sum()


# In[9]:


#spliting into train test 
train,test =train_test_split(data ,test_size = 0.2,stratify = data["label"],random_state = 21)


# In[10]:


train.shape


# In[11]:


test.shape


# In[13]:


#by implimenting tfidf
tfidf_vectore = TfidfVectorizer(lowercase=True,stop_words=ENGLISH_STOP_WORDS,max_features=1000)


# In[14]:


tfidf_vectore.fit(train.tweet)


# In[15]:


train_idf = tfidf_vectore.transform(train.tweet)
test_idf = tfidf_vectore.transform(test.tweet)


# In[18]:


model_lr = LogisticRegression()
model_lr.fit(train_idf,train.label)


# In[22]:


pred_train = model_lr.predict(train_idf)


# In[23]:


pred_train


# In[24]:


pred_test = model_lr.predict(test_idf)


# In[25]:


pred_test


# In[29]:


f1_score(y_true = train.label,y_pred = pred_train)


# In[30]:


f1_score(y_true = test.label,y_pred = pred_test)


# In[33]:


#define the stages of piplines

pipeline = Pipeline(steps = [('tfidf',TfidfVectorizer( lowercase=True, max_features=None,stop_words=ENGLISH_STOP_WORDS)),
                            ('model',LogisticRegression())])


# In[34]:


pipeline.fit(train.tweet,train.label)


# In[35]:


#now we will test the pipline with sample tweet


# In[36]:


text = ["virat kholi ab de villiers set to auction  there 'Green Day' kits from 2016 ipl match to raise funds"]

pipeline.predict(text)


# In[37]:


from joblib import dump


# In[38]:


#dump the pipline model

dump(pipeline,filename="text.classification.joblib")
