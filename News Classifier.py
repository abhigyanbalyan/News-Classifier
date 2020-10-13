#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


data=pd.read_csv("bbc-text.csv")


# In[23]:


data.head()


# In[25]:


data.isnull().any()


# In[26]:


data["category"].unique()


# In[29]:


data['News_length']=data['text'].str.len()
print(data['News_length'])


# In[31]:


data.shape


# In[79]:


import re


# In[103]:


from nltk.corpus import stopwords
sw=stopwords.words("english")


# In[111]:


from nltk.stem.porter import PorterStemmer

def process_text(text):
    corpus=[]
    for i in range(len(data["text"])):
        review = re.sub( '[^a-zA-Z]', ' ', data['text'][i] )
        review=review.lower()
        review=review.split()
        #ps=PorterStemmer()
        review=[word for word in review if word not in sw]
        review=" ".join(review)
        corpus.append(review)


# In[112]:


process_text(data["text"])


# In[116]:


from sklearn import preprocessing 
le = preprocessing.LabelEncoder() 
data['Category_target']=le.fit_transform(data['category'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[86]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




