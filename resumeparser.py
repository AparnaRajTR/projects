#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pdfminer')


# In[2]:


def pdf_to_text(text):
        from pdfminer.high_level import extract_text
        text = extract_text(text)
        return text
 


# In[3]:


text =('/home/aparna/Downloads/APARNA_RAJ_T_R- CV.pdf')
a=pdf_to_text(text)
 


# In[4]:


a


# In[5]:


x=a.replace('\n',' ')
y=x.replace('\x0c',' ')
z=y.replace(',','')


# In[6]:


z


# In[7]:


pip install spacy


# In[8]:


import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[9]:


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[10]:


tokens = nltk.word_tokenize(z)


# In[11]:


tokens


# In[12]:


stops = set(stopwords.words('english'))
print(stops)


# In[13]:


stopslist=list(stops)


# In[14]:


stopslist


# In[15]:


for word in tokens: 
    if word not in stopslist:
        print(word)


# In[16]:


import re

def extract_mobile_number(z):
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), y)
    
    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number


# In[17]:


extract_mobile_number(z)


# In[18]:


import re

def extract_email(z):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", y)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None


# In[19]:


extract_email(z)


# In[20]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[21]:


nlp = spacy.load("en_core_web_sm")  # load the English model
doc = nlp(z)  # process a text and create a Doc object
n=doc.noun_chunks
for chunk in doc.noun_chunks:       # iterate over the noun chunks in the Doc
   print(chunk.text)


# In[22]:


n


# In[23]:


skl={'English Language':[],'Leadership':[],'Collaboration':[],'HTML':[],'Python':[]}


# In[24]:


skl_list=['English lanuguage','Leadership','Collaboration','Python','HTML']


# In[25]:


def extract_skills(nlp_text,n):
    tokens=word_tokenize(nlp_text)
    
    
    skills_list=['English','Leadership','Collaboration','HTML','Python','Critical']
    skills_list_new=['English','Leadership','Collaboration','HTML','Python','Critical']
    #print(skills_list)
    
    skillset=[]
    
    #check for one gram
    for token in tokens:
        if token in skills_list_new:
            skillset.append(token)
    print("")
    #print("skillset is",skillset)
    
     # check for bi-grams and tri-grams
    for token in tokens:
        token = token.strip()
        if token in skills_list:
            skillset.append(token)
    return [i.capitalize() for i in set([i.lower() for i in skillset])]
    


# In[26]:


extract_skills(z,n)


# In[ ]:




