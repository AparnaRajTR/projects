#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


# In[2]:


df=pd.read_csv(r'C:\Users\91623\Downloads/anxietyprediction.csv')


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


l=[] 
Res=[]
Pos=[]
Time=[]

for i in range(0, 42*3, 3):
    l.append(df.columns[i])

for i in range(0, 42*3, 3):
    Res.append(df[df.columns[i]].mean())
    
for i in range(0, 42*3, 3):
    Pos.append(df[df.columns[i+1]].mean())
    
for i in range(0, 42*3, 3):
    Time.append(df[df.columns[i+2]].mean())


# In[9]:


Qs=pd.DataFrame({'Response':Res, 'Position':Pos, 'Time':Time}, index=range(1,43))


# In[10]:


Qs


# In[11]:


Qs.index.name='Qs no.'
Qs


# In[12]:


Qs.info()


# In[13]:


Qs.describe()


# In[14]:


plt.figure(figsize=(20,10))
sns.lineplot(data=Qs, x=Qs.index, y='Response')


# #Between Question 20 and Question 30,Question number 23 has a very low response in general

# In[15]:


plt.figure(figsize=(20,10))
sns.lineplot(data=Qs, x=Qs.index, y='Time')


# #Most of the people took greater time for almost the same questions and hence the peaks.

# In[16]:


plt.figure(figsize=(20,10))
sns.lineplot(data=Qs, x=Qs.index, y='Position')


# #The questions are placed randomly and hence the positions vary
# 

# In[17]:


plt.figure(figsize=(20,6))
sns.displot(data=Qs, x='Response',kde=True)


# In[18]:


sns.heatmap(Qs.corr(), cmap='Greens', annot=True)


# #Position and Time are positively correlated,as expected for any questionnaire.
# 
# #Response and Position are negatively correlated,which means as the Response value increases,position decreases.

# In[19]:


new_df=df.iloc[:, 131:157]


# In[20]:


new_df


# In[21]:


new_df.mean()


# In[22]:


qr = df[l].mean(axis=1)
qr


# In[23]:


tip = df.iloc[:, 131:141]
tip


# In[24]:


tip.insert(0, 'response', qr)


# In[25]:


tip


# In[26]:


plt.figure(figsize=(10,6))
sns.heatmap(tip.corr(), cmap='Blues', annot=True)


# #The responses show a maximum correlation of 0.55 with TIPI4 i.e;Anxious and easily upset.
# 
# #Then comes a correlation of 0.35 for TIPI5 i.e;Open to new experiences and complex.
# 
# #The maximum negative correlation is for TIPI9 i.e; Calm, emotionally stable followed by reserved and quiet with a correlation of -0.51
# 

# In[28]:


demo=df.iloc[:, 157:]
demo


# In[29]:


demo.insert(0, 'response', qr.values)


# In[30]:


demo


# In[31]:


plt.figure(figsize=(15,15))
sns.heatmap(demo.corr(), cmap='Spectral', annot=True)


# In[32]:


fig, axes = plt.subplots(3,2, figsize=(20,20))
l = ['education', 'urban', 'gender', 'engnat', 'screensize', 'uniquenetworklocation', 'hand', 'religion',
       'orientation', 'race', 'voted', 'married', 'familysize']
for i, j in enumerate(axes.ravel()):
    sns.boxenplot(data=demo, y='response', x=l[i], ax=j,)
plt.show()


# In[33]:


demo.groupby('education').mean()


# #As education increases,the response values decrease as seen

# In[34]:


demo.groupby('gender').mean()


# #'Other' gender showed the most responses for the questionnaire where 1=Male,2=Female and 3=Other.
# 

# In[35]:


demo.groupby('married').mean()


# #Currently married people have low response values.

# In[36]:


df['major']=df['major'].replace(np.nan,'No Degree')


# In[37]:


def condition(title):
    if 'busin' in str(title).lower() or 'manage' in str(title).lower() or 'Buss' in str(title) or 'Bisness' in str(title) or 'Manag' in str(title) or 'buis' in str(title) or 'Entrepreneur' in str(title) or 'entrepr' in str(title).lower() or 'managment' in str(title).lower() or 'Buis' in str(title) or 'Busni' in str(title) or 'Mana' in str(title) or 'buss' in str(title).lower() or 'Bi' in str(title) or 'Mgt' in str(title) or 'MBA' in str(title) or 'Mgmt' in str(title) or 'MD' in str(title):
        return 'Business/Management'
    elif 'information technology' in str(title).lower() or 'IT' in str(title) or 'it' in str(title):
        return 'I.T'
    elif 'math' in str(title).lower() or 'LOGISTICS' in str(title) or 'st' in str(title).lower() or 'marh' in str(title).lower() or 'Mate' in str(title):
        return 'Mathematics'
    elif 'computer' in str(title).lower():
        return 'I.T'
    elif 'bio' in str(title).lower() or 'Plant' in str(title) or 'plant' in str(title).lower() or 'Micro' in str(title):
        return 'Biology'
    elif 'tesl' in str(title).lower() or 'TES' in str(title) or 'Teso' in str(title) or 'Enhlish' in str(title):
        return 'English'
    elif 'account' in str(title).lower() or 'Accoun' in str(title) or 'Acc' in str(title) or 'acc' in str(title).lower() or 'Acouunt' in str(title) or 'Acvount' in str(title) or 'Count' in str(title):
        return 'Accountacy'
    elif 'CA' in str(title):
        return 'CA'
    elif 'none' in str(title).lower() or '0' in str(title) or  '_' in str(title) or '.' in str(title) or 'Nine' in str(title) or '19' in str(title):
        return 'No Degree'
    elif 'nurs' in str(title).lower() or 'BSN' in str(title):
        return 'Nursing'
    elif '-' in str(title).lower() or 'NIL' in str(title):
        return 'No Degree'
    elif 'teach' in str(title).lower() or 'Lect' in str(title) or 'eet' in str(title).lower():
        return 'Teaching'
    elif 'pharma' in str(title).lower() or 'medic' in str(title).lower() or 'med' in str(title).lower() or 'hospi' in str(title).lower() or 'Mwdicine' in str(title) or 'Farmacy' in str(title) or 'Pharacology' in str(title) or 'farmasi' in str(title).lower() or 'Farmasy' in str(title):
        return 'Pharmacy/Medical'
    elif 'doctor' in str(title).lower() or  'MBBS' in str(title) or 'Mbbs' in str(title) or 'Surge' in str(title) or 'surge' in str(title) or 'mbbs' in str(title).lower()or 'dermat' in str(title).lower() or 'Podiat' in str(title) :
        return 'Doctor'
    elif 'no' in str(title).lower() or 'Undec' in str(title) or 'Idk' in str(title) or 'idk' in str(title).lower() or 'Hahaha' in str(title) or 'never' in str(title).lower() or 'T' in str(title) or 'Good' in str(title):
        return 'No Degree'
    elif 'film' in str(title).lower() or 'Cinema' in str(title) or 'fil' in str(title).lower() or 'Adver' in str(title) or 'adver' in str(title) or 'Act' in str(title) or 'Enter' in str(title) or 'digital' in str(title).lower() or 'cinema' in str(title).lower() or 'Video' in str(title) or 'Direct' in str(title) or 'Theat' in str(title) or 'Radio' in str(title) or 'theat' in str(title).lower() or 'drama' in str(title).lower():
        return 'Media'
    elif 'international' in str(title).lower() or 'Internatianal' in str(title):
        return 'International Relations'
    elif 'human' in str(title).lower() or 'hr' in str(title).lower() or 'Hs' in str(title) or 'Hm' in str(title) or 'Humam' in str(title):
        return 'Human Resources'
    elif 'art' in str(title).lower() or 'Painting' in str(title) or 'Drawing' in str(title) or 'ba' in str(title) or 'Printing' in str(title) or 'las' in str(title).lower() or 'Ma' in str(title) or 'paint' in str(title).lower() or 'creative' in str(title).lower() or 'AA' in str(title) or 'BA' in str(title):
        return 'Arts'
    elif 'islam' in str(title).lower() or 'Muamalat' in str(title) or 'Quran' in str(title) or 'Halal' in str(title) or 'Usul' in str(title) or 'Zakat' in str(title) or 'usul' in str(title).lower():
        return 'Islamic Studies'
    elif 'physio' in str(title).lower() or 'fis' in str(title).lower():
        return 'Physiotherapy'
    elif 'socio' in str(title).lower() or 'social' in str(title).lower() or 'soical' in str(title).lower() or 'Sis' in str(title) or 'Sosio' in str(title) or 'Sicio' in str(title) or 'sosiality' in str(title).lower():
        return 'Sociology'
    elif 'bank' in str(title).lower():
        return 'Banking'
    elif 'agri' in str(title).lower():
        return 'Agriculture'
    elif 'Market' in str(title) or 'Finan' in str(title) or 'finance' in str(title).lower() or 'MARKETING' in str(title) or 'market' in str(title).lower() or 'retail' in str(title).lower() or 'CMP' in str(title) or 'Merket' in str(title):
        return 'Marketing/Finance'
    elif 'counsel' in str(title).lower() or 'cauns' in str(title) or 'Kaunseling' in str(title) or 'kaunseling' in str(title) or 'Caunsel' in str(title):
        return 'Counselling'
    elif 'programming' in str(title).lower() or 'coding' in str(title).lower() or 'Ibm' in str(title) or 'ceit' in str(title) or 'Hacking' in str(title):
        return 'I.T'
    elif 'civil' in str(title).lower() or 'comp' in str(title).lower() or 'Mechanical' in str(title) or 'Electrical' in str(title) or 'Mechatronics' in str(title) or 'Eee' in str(title) or 'cs' in str(title).lower() or 'mecha' in str(title) or 'Chemical' in str(title) or 'chemical' in str(title) or 'tech' in str(title) or 'ec' in str(title).lower() or 'egineering' in str(title).lower() or 'manufacturing' in str(title).lower():
        return 'Engineering'
    elif 'ict' in str(title).lower() or 'developer' in str(title).lower() or 'I.T' in str(title) or 'CAE&D' in str(title) or 'It' in str(title):
        return 'I.T'
    elif 'commu' in str(title).lower() or 'comm' in str(title).lower() or 'com' in str(title).lower() or 'Conmunication' in str(title):
        return 'Communications'
    elif 'administration' in str(title).lower() or 'admin' in str(title).lower():
        return 'Administration'
    elif 'psycho' in str(title).lower() or 'psy' in str(title).lower() or 'Clinical osychology' in str(title) or 'hschology' in str(title) or 'Pysch' in str(title) or 'pys' in str(title).lower() or 'Pych' in str(title) or 'pscy' in str(title) or 'payc' in str(title).lower() or 'Phyc' in str(title) or 'psicologia' in str(title) or 'Phsychology' in str(title) or 'Phichology' in str(title) or 'psuchology' in str(title) or 'Pschology' in str(title) or 'psikologi' in str(title).lower():
        return 'Psychology'
    elif 'english' in str(title).lower() or 'Elglish' in str(title) or 'esl' in str(title).lower() or 'Emg' in str(title) or 'emglisj' in str(title).lower():
        return 'English'
    elif 'law' in str(title).lower() or 'BBA' in str(title) or 'llb' in str(title) or 'lew' in str(title).lower() or 'kaw' in str(title).lower() or 'enforcement' in str(title).lower() or 'Kaw' in str(title):
        return 'Law'
    elif 'engineering' in str(title).lower() or 'engi' in str(title).lower() or 'eng' in str(title).lower() or 'Software' in str(title) or 'soft' in str(title).lower() or 'mechanical' in str(title).lower() or 'Egineeering' in  str(title) or 'electronic' in str(title).lower() or 'CE' in str(title) or 'mech' in str(title).lower() or 'Ciclvil' in str(title) or 'Eggineering' in str(title) or 'Tech' in str(title) or 'Teol' in str(title) or 'EEE' in str(title) or 'PE' in str(title):
        return 'Engineering'
    elif 'architecture' in str(title).lower() or 'aechitecture' in str(title).lower() or 'archirecture' in str(title).lower() or 'architect' in str(title).lower() or 'Arsitechture' in str(title) or 'Building' in str(title) or 'building' in str(title).lower() or 'Arc' in str(title):
        return 'Architecture'
    elif 'design' in str(title).lower() or 'Desig' in str(title) or 'Dssign' in str(title):
        return 'Designer'
    elif 'science' in str(title).lower() or 'Sceince' in str(title) or 'Sci' in str(title) or 'sciene' in str(title) or 'BS' in str(title):
        return 'Pure Sciences'
    elif 'physics' in str(title).lower() or 'Phsyics' in str(title) or 'EMC' in str(title) or 'Physic' in str(title) or 'physi' in str(title):
        return 'Physics'
    elif 'chemistry' in str(title).lower() or 'CIS' in str(title) or 'Chem' in str(title):
        return 'Chemistry'
    elif 'french' in str(title).lower() or 'Fr' in str(title):
        return 'French'
    elif 'religi' in str(title).lower() or 'Relegion' in str(title) or 'Rel' in str(title) or 'Hukum' in str(title) or 'Sains' in str(title):
        return 'Religious Studies'
    elif title=='&#1593;&#1604;&#1605; &#1606;&#1601;&#1587;' or title=='&#22810;&#23186;&#39636;&#35373;&#35336;' or title=='nil' or title=='drop out' or title=='&#1055;&#1089;&#1080;&#1093;&#1086;&#1083;&#1' or title=='75' or title=='Secondary education' or title=='Thiê&#769;t kê&#769; &#273;ô&#768; ho&#803;a' or title=='18' or title=='ongoing' or title=='&#28888;&#22521;' or title=='lol' or title=='In college currently' or title=='secondary education' or title=='Dropped out' or title=='na' or title=='didnt attend' or title=='im going on the next year. ' or title=='&#304;lahiyat' or title=='lmfao, im 15' or title=='Elem Ed' or title=='yes' or title=='N/a' or title=='/' or title=='???' or title=='cocaine 101' or title=='doesnt matter' or title== 'oooo' or title=='G' or title=='Yes' or title=='Na' or title=='Na 'or title=='Want sure':
        return 'No Degree'
    elif 'Music' in str(title) or 'Dance' in str(title) or 'danc' in str(title).lower() or 'Vocational' in str(title) or 'Muisc' in str(title) or 'music' in str(title).lower() or 'Performance' in str(title):
        return 'Music/Dance'
    elif 'pol' in str(title).lower() or 'Govern' in str(title) or 'Right' in str(title):
        return 'Politics'
    elif 'photo' in str(title).lower() or 'Foto' in str(title) or 'Photo' in str(title):
        return 'Photography'
    elif 'Television' in str(title) or 'telev' in str(title).lower():
        return 'Television'
    elif 'bahasa' in str(title).lower() or 'Bahasa' in str(title) or 'Malay' in str(title) or 'malay' in str(title).lower():
        return 'Malaysian languages'
    elif 'Urban' in str(title) or 'Town' in str(title) or 'town' in str(title).lower() or 'planning' in str(title) or 'Plann' in str(title) or 'development' in str(title):
        return 'Economic Developments'
    elif 'Public' in str(title) or 'public' in str(title).lower():
        return 'Public Relations'
    elif 'Writing' in str(title) or 'writing' in str(title).lower() or 'Screenwritinf' in str(title) or 'Author' in str(title):
        return 'Writing/Author'
    elif 'philosophy' in str(title).lower() or 'Phil' in str(title) or 'philos' in str(title).lower() or 'Filo' in str(title) or 'Phylosophy' in str(title):
        return 'Philosophy'
    elif 'Actua' in str(title):
        return 'Acturial Studies'
    elif 'DENTALWORKS' in str(title) or 'dental' in str(title) or 'Dental' in str(title) or 'Odont' in str(title):
        return 'Dentist'
    elif 'beaut' in str(title).lower() or 'Fashion' in str(title) or 'make' in str(title) or 'fashion' in str(title).lower() or 'hair' in str(title).lower() or 'cosmet' in str(title).lower():
        return 'Fashion'
    elif 'Health' in str(title) or 'health' in str(title).lower() or 'wellness' in str(title).lower() or 'Healtcare' in str(title):
        return 'Healthcare'
    elif 'Language' in str(title) or 'lang' in str(title).lower() or 'Laq' in str(title):
        return 'Languages'
    elif 'cook' in str(title).lower() or 'bakery' in str(title).lower() or 'Bak' in str(title) or 'CULINARY' in str(title) or 'Food' in str(title) or 'food' in str(title) or 'chef' in str(title).lower() or 'Cul' in str(title) or 'Patiss' in str(title) or 'culi' in str(title).lower():
        return 'Cookings'
    elif 'Hotel' in str(title) or 'hotel' in str(title).lower() or 'food service' in str(title) or 'cater' in str(title).lower():
        return 'Hotel Management'
    elif 'therapy' in str(title).lower() or 'ot' in str(title).lower() or 'theraphy' in str(title):
        return 'Therapeutical Studies'
    elif 'veter' in str(title).lower() or 'Veter' in str(title) or 'Vet' in str(title):
        return 'Veterinary'
    elif 'Survey' in str(title) or 'survey' in str(title) or 'serveyors' in str(title).lower() or 'Qs' in str(title) or 'SURVEYING' in str(title) or 'QS' in str(title) or 'Surver' in str(title):
        return 'Surveyour Studies'
    elif 'Aircraft' in str(title) or 'aircraft' in str(title).lower() or 'aircr' in str(title).lower() or 'aviation' in str(title).lower() or 'Aero' in str(title) or 'navigation' in str(title).lower():
        return 'Aircrafts'
    elif 'environment' in str(title).lower() or 'Environment' in str(title) or 'envi' in str(title).lower():
        return 'Environmental Educations'
    elif 'Syariah' in str(title) or 'syariah' in str(title):
        return 'Syrian Languages'
    elif 'judicial' in str(title).lower() or 'juri' in str(title).lower() or 'legal' in str(title).lower():
        return 'Judicial Studies'
    elif 'Liter' in str(title) or 'literature' in str(title) or 'litt' in str(title).lower():
        return 'Literature'
    elif 'child' in str(title).lower() or 'Child' in str(title) or 'Preschool' in str(title):
        return 'Child Educations'
    elif 'Tour' in str(title) or 'tour'  in str(title).lower():
        return 'Tourisms'
    elif 'Gam' in str(title) or 'game' in str(title).lower():
        return 'Gaming'
    elif 'education' in str(title).lower() or 'Education' in str(title) or 'ed' in str(title).lower() or 'acad' in str(title) or 'Dploma' in str(title):
        return 'B.Ed or M.Ed'
    elif 'Sport' in str(title) or 'sport' in str(title).lower():
        return 'Sports'
    elif 'Petro' in str(title):
        return 'Petroleum'
    elif 'Journ' in str(title) or 'jour' in str(title).lower() or 'Joun' in str(title) or 'Jurn' in str(title):
        return 'Journalism'
    elif 'Mandarin' in str(title):
        return 'Chinese/Mandarin Languages'
    elif 'Electrician' in str(title):
        return 'Electrician'
    elif 'Network' in str(title) or 'network' in str(title).lower():
        return 'Networking'
    elif 'geo' in str(title).lower() or 'GEO' in str(title):
        return 'Geography'
    elif 'Librarian' in str(title) or 'lib' in str(title).lower():
        return 'Librarian'
    elif 'Mission' in str(title) or 'mission' in str(title).lower():
        return 'Missionary Studies'
    elif 'Forensic' in str(title) or 'foren' in str(title).lower() or 'Crime' in str(title) or 'crim' in str(title).lower():
        return 'Forensic/Criminal studies'
    elif 'Animation' in str(title) or 'animation' in str(title).lower() or 'imag' in str(title) or 'graphic' in str(title) or 'Graphic' in str(title):
        return 'Animations'
    elif 'aqua' in str(title).lower() or 'Aqu' in str(title):
        return 'Aquaculture'
    elif 'soldier' in str(title).lower() or 'lwa' in str(title).lower() or 'defence' in str(title):
        return 'Army'
    elif 'Kinesi' in str(title) or 'kines' in str(title).lower() or 'hod' in str(title):
        return 'Human Kinetics'
    elif 'Horti' in str(title) or 'horti' in str(title) or 'Landscape' in str(title):
        return 'Horticulture'
    elif 'commerce' in str(title).lower() or 'Coome' in str(title):
        return 'Commerce'
    elif 'Speech' in str(title) or 'speech' in str(title).lower():
        return 'Speech Pathology'
    elif 'SECRET' in str(title) or 'secret' in str(title).lower():
        return 'Secretary'
    elif 'Animals' in str(title) or 'animal' in str(title).lower() or 'Pet' in str(title):
        return 'Animal Care'
    elif 'Organisation' in str(title) or 'organi' in str(title).lower():
        return 'Organizational Behaviour'
    elif 'event' in str(title).lower() or 'Event' in str(title):
        return 'Event Managment'
    elif 'radiology' in str(title).lower() or 'Radiography' in str(title) or 'radiograpghy' in str(title).lower() or 'Radiation' in str(title) or 'radiography' in str(title):
        return 'Radiography'
    elif 'nutrition' in str(title).lower() or 'Nutrition' in str(title):
        return 'Nutritionist'
    elif 'Audit' in str(title) or 'audit' in str(title).lower():
        return 'Auditing'
    elif 'Neuro' in str(title) or 'neuroligy' in str(title).lower():
        return 'Neurology'
    elif 'Anato' in str(title) or 'anat' in str(title).lower():
        return 'Anatomy'
    elif 'trade' in str(title).lower():
        return 'Trading'
    elif 'Interpre' in str(title) or 'translation' in str(title).lower():
        return 'Interpreter'
    elif 'audio' in str(title).lower() or 'Audio' in str(title):
        return 'Audiology'
    elif 'insurance' in str(title).lower() or 'Insurance' in str(title):
        return 'Insurances'
    elif 'archaeology' in str(title).lower() or 'archaeology' in str(title).lower() or 'archeology' in str(title).lower() or 'treasury' in str(title):
        return 'Archeology'
    elif 'SERV'in str(title) or 'service' in str(title).lower():
        return 'Service Training'
    elif 'GERMAN' in str(title) or 'german' in str(title).lower():
        return 'German'
    elif 'KOREAN' in str(title) or 'Korea' in str(title):
        return 'Korean'
    elif 'valuat' in str(title).lower() or 'valuer' in str(title).lower():
        return 'Registered Valuer'
    elif 'skil' in str(title).lower() or 'Skill' in str(title) or 'Professional' in str(title) or 'practical' in str(title).lower():
        return 'Skilled Labour'
    elif 'virology' in str(title):
        return 'Virology'
    elif 'lab' in str(title).lower() or 'Lab' in str(title) or 'MLT' in str(title):
        return 'Laboratory Worker'
    elif 'GENERAL' in str(title) or 'General' in str(title):
        return 'General'
    elif 'Opto' in str(title) or 'opto' in str(title).lower():
        return 'Optometry'
    elif 'Zoo' in str(title) or 'zoo' in str(title).lower():
        return 'Zoology'
    elif 'office' in str(title).lower() or 'Office' in str(title):
        return 'Office Skills'
    elif 'found' in str(title).lower() or 'Found' in str(title):
        return 'Foundation Education'
    elif 'general' in str(title).lower() or 'General' in str(title):
        return 'General Education'
    elif 'real estate' in str(title).lower() or 'property' in str(title).lower():
        return 'Realtor'
    elif 'Meteorology' in str(title) or 'Metrology' in str(title):
        return 'Meterology'
    elif 'operations' in str(title).lower() or 'Operation' in str(title):
        return 'Operational Managment'
    elif 'Merchandising' in str(title) or 'merchand' in str(title).lower():
        return 'Merchandising'
    elif 'Spanish' in str(title):
        return 'Spanish'
    elif 'Nature' in str(title) or 'natur' in str(title).lower():
        return 'Nature Conservation/Resources'
    elif title=='a level ' or title==' ':
        return 'No Degree'
    elif 'Corporate' in str(title) or 'corporate' in str(title).lower():
        return 'Corporate'
    elif 'greek' in str(title).lower() or 'Greek' in str(title):
        return 'Greek'
    elif 'Behaviour' in str(title) or 'Behavior' in str(title) or 'Organizational Behaviour' in str(title):
        return 'Behaviour Analysis'
    elif 'publish' in str(title).lower():
        return 'Publishing'
    elif 'Safety' in str(title) or 'safety' in str(title).lower():
        return 'Safety Training'
    elif 'genetic' in str(title).lower() or 'Genetic' in str(title):
        return 'Genetics'
    elif 'Dietetic' in str(title):
        return 'Dietician'
    elif 'Production' in str(title) or 'manufacturing' in str(title).lower():
        return 'Production And Manufacturing'
    elif 'Welding' in str(title):
        return 'Welding'
    elif 'Geron' in str(title):
        return 'Gerontology'
    elif 'Research' in str(title) or 'Ph D' in str(title):
        return 'Ph.D'
    elif 'arabic' in str(title).lower() or 'Arabic' in str(title):
        return 'Arabic'

    else:
        return title


# In[38]:


df['major'] = df['major'].apply(condition)


# In[39]:


df


# In[40]:


List=[]
for x in df['major']:
    List.append(x)
print(set(List))


# In[41]:


plt.figure(figsize=(10,5))
df['major'].value_counts()[:20].plot(kind='barh',color='green')
plt.ylabel('Majors')
plt.xlabel('Count')
plt.title('Majors of top 20 people who participated in the Survey')


# In[42]:


new_data=df.iloc[:,42:]
df_2=df.filter(regex='Q\d{1,2}A')
df_2


# In[43]:


def sub(df_2):
    return df_2.subtract(1,axis=1)


# In[44]:


df_2=sub(df_2) 
keys = {'Depression': [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42],
             'Anxiety': [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41],
             'Stress': [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]}
Dep=[]


# In[45]:


for i in keys["Depression"]:
    Dep.append('Q'+str(i)+'A')
Stress=[]
for i in keys["Stress"]:
    Stress.append('Q'+str(i)+'A')
Anx=[] 
for i in keys["Anxiety"]:
    Anx.append('Q'+str(i)+'A')
Depression= df_2.filter(Dep)
Stress = df_2.filter(Stress)
Anxiety = df_2.filter(Anx)


# In[46]:


def score(source):
    column=list(source)
    source['Total_Count']=source[column].sum(axis=1)
    return source


# In[47]:


Anxiety=score(Anxiety)


# In[48]:


Anxiety


# In[49]:


Anxiety.head()


# In[50]:


Anxiety=pd.merge(Anxiety,new_data,how='inner',left_index=True,right_index=True)


# In[51]:


Anxiety.head()


# In[52]:


Anxiety=Anxiety.rename(columns={'Q20A_x':'Q20A','Q15A_x':'Q15A','Q19A_x':'Q19A','Q23A_x':'Q23A','Q28A_x':'Q28A','Q40A_x':'Q40A','Q41A_x':'Q41A','Q36A_x':'Q36A','Q25A_x':'Q25A','Q30A_x':'Q30A'})


# In[53]:


Anxiety.head()


# In[54]:


def condition(x):
    if x<=7:
        return 'Normal'
    if  8<=x<=9:
        return 'Mild'
    if 10<=x<=14:
        return 'Moderate'
    if 15<=x<=19:
        return 'Severe'
    if x>19:
        return 'Extremely Severe'

Anxiety['Condition']=Anxiety['Total_Count'].apply(condition)


# In[55]:


Anxiety.head()


# In[56]:


plt.figure(figsize=(10,6))
sns.countplot(Anxiety.sort_values('Condition').Condition,palette='pastel')
plt.title('The levels of Anxiety',fontsize=15)


# In[57]:


anx=Anxiety.copy()
def condition(x):
    if x<=9:
        return 0
    if  10<=x<=13:
        return 1
    if 14<=x<=20:
        return 2
    if 21<=x<=27:
        return 3
    if x>28:
        return 4

def cond(x):
    if x<=10:
        return 0
    if  10<=x<=16:
        return 1
    if 17<=x<=21:
        return 2
    if 21<=x<=35:
        return 3
    if 36<=x<=48:
        return 4
    if x>=49:
        return 5
anx['Condition']=anx['Total_Count'].apply(condition)
anx['Age_Groups']=anx['age'].apply(cond)
anx=anx.drop(columns=['age','Total_Count'])


# In[58]:


anx.head()


# In[59]:


anx.corr()


# In[60]:


print('Count of People participated as of Gender\n',df['gender'].value_counts())


# In[61]:


plt.figure(figsize=(10,6))
sns.countplot(Anxiety.sort_values('gender').gender,hue=Anxiety['Condition'],palette='pastel')
plt.title('Anxiety Condition of Different Gender',fontsize=15)


# In[62]:


plt.figure(figsize=(10,6))
sns.countplot(Anxiety.sort_values('orientation').orientation,hue=Anxiety['Condition'],palette='pastel')
plt.title('Anxiety Condition as per different sexual Orientations',fontsize=15)


# In[63]:


Anxiety=Anxiety.drop(columns=['Total_Count','country'])


# #model prediction

# In[89]:


from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,plot_confusion_matrix,accuracy_score,precision_score, recall_score, f1_score,roc_auc_score,classification_report,mean_squared_error


# In[90]:


anx.columns


# In[91]:


Anxiety=Anxiety.rename(columns={'TIPI1':'Extraverted-enthusiastic','TIPI2':'Critical-quarrelsome',
                            'TIPI3':'Dependable-self_disciplined','TIPI4':'Anxious-easily upset',
                            'TIPI5':'Open to new experiences-complex','TIPI6':'Reserved-quiet',
                            'TIPI7':'Sympathetic-warm','TIPI8':'Disorganized-careless','TIPI9':'Calm-emotionally_stable',
                            'TIPI10':'Conventional-uncreative'})


# In[92]:


anx.head()


# In[93]:


anx


# In[94]:


scaler=MinMaxScaler()

X=Anxiety[['Q2A', 'Q4A', 'Q7A', 'Q9A', 'Q15A', 'Q19A', 'Q20A', 'Q23A', 'Q25A',
       'Q28A', 'Q30A', 'Q36A', 'Q40A', 'Q41A',
       'Extraverted-enthusiastic', 'Critical-quarrelsome',
       'Dependable-self_disciplined', 'Anxious-easily upset',
        'Open to new experiences-complex', 'Reserved-quiet', 'Sympathetic-warm',
        'Disorganized-careless', 'Calm-emotionally_stable',
        'Conventional-uncreative', 'education', 'urban', 'gender', 'engnat',
        'screensize', 'uniquenetworklocation', 'hand', 'religion',
        'orientation', 'race', 'voted', 'married', 'familysize']]

y=Anxiety['Condition']


# In[95]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.35,random_state=9)


# In[96]:


X_train.shape


# In[97]:


X_test.shape


# In[98]:


y_train.shape


# In[99]:


y_test.shape


# In[100]:


X_train_scaled = scaler.fit_transform(X_train)


# In[101]:


X_test_scaled = scaler.transform(X_test)


# In[102]:


rand=RandomForestClassifier(criterion='entropy')
rand.fit(X_train_scaled,y_train)

accu_ran=round(accuracy_score(y_test,rand.predict(X_test_scaled)),3)

f1_score_ran=round(f1_score(y_test,rand.predict(X_test_scaled),average='weighted'),3)

Precision_ran=round(precision_score(y_test,rand.predict(X_test_scaled),average='weighted'),3)

Recall_ran=round(recall_score(y_test,rand.predict(X_test_scaled),average='weighted'),3)

print('Accuracy:',accu_ran)
print('F1_Score:',f1_score_ran)
print('Recall_Score:',Precision_ran)
print('Precision_Score:',Recall_ran)
print('Cross Validation Score:',(np.mean(cross_val_score(rand, X_train_scaled, y_train, cv = 6))))


# In[113]:


fig, ax = plt.subplots(figsize=(9, 7))
plot_confusion_matrix(rand,X_test_scaled,y_test,ax=ax)
classification=classification_report(
    digits=4,
    y_true=y_test,
    y_pred=rand.predict(X_test_scaled))
print(classification)


# In[104]:


Dt=DecisionTreeClassifier(criterion='entropy',max_depth=100,min_samples_leaf=9,min_samples_split=3)
Dt.fit(X_train_scaled,y_train)

accuracy_dt=round(accuracy_score(y_test,Dt.predict(X_test_scaled)),3)
f1score_dt=round(f1_score(y_test,Dt.predict(X_test_scaled),average='weighted'),3)
precision_dt=round(precision_score(y_test,Dt.predict(X_test_scaled),average='weighted'),3)
recall_dt=round(recall_score(y_test,Dt.predict(X_test_scaled),average='weighted'),3)

print('Accuracy:',accuracy_dt)
print('F1_Score:',f1score_dt)
print('Recall_Score:',precision_dt)
print('Precision_Score:',recall_dt)
print('Cross Validation Score:',(np.mean(cross_val_score(Dt, X_train_scaled, y_train, cv = 6))))


# In[105]:


fig, ax = plt.subplots(figsize=(10, 10))
plot_confusion_matrix(Dt,X_test_scaled,y_test,ax=ax)
classification=classification_report(
    digits=4,
    y_true=y_test,
    y_pred=Dt.predict(X_test_scaled))
print(classification)


# In[106]:


GB=GaussianNB()
GB.fit(X_train_scaled,y_train)

accuracy_gb=round(accuracy_score(y_test,GB.predict(X_test_scaled)),3)
f1score_gb=round(f1_score(y_test,GB.predict(X_test_scaled),average='weighted'),3)
precision_gb=round(precision_score(y_test,GB.predict(X_test_scaled),average='weighted'),3)
recall_gb=round(recall_score(y_test,GB.predict(X_test_scaled),average='weighted'),3)

print('Accuracy:',accuracy_gb)
print('F1_Score:',f1score_gb)
print('Recall_Score:',precision_gb)
print('Precision_Score:',recall_gb)
print('Cross Validation Score:',(np.mean(cross_val_score(GB, X_train_scaled, y_train, cv = 6))))


# In[107]:


fig, ax = plt.subplots(figsize=(10, 10))
plot_confusion_matrix(GB,X_test_scaled,y_test,ax=ax)
classification=classification_report(
    digits=4,
    y_true=y_test,
    y_pred=GB.predict(X_test_scaled))
print(classification)


# In[108]:


K=KNeighborsClassifier(n_neighbors=19,weights='distance')
K.fit(X_train_scaled,y_train)
accuracy_knn=round(accuracy_score(y_test,K.predict(X_test_scaled)),3)
f1score_knn=round(f1_score(y_test,K.predict(X_test_scaled),average='weighted'),3)
precision_knn=round(precision_score(y_test,K.predict(X_test_scaled),average='weighted'),3)
recall_knn=round(recall_score(y_test,K.predict(X_test_scaled),average='weighted'),3)

print('Accuracy:',accuracy_knn)
print('F1_Score:',f1score_knn)
print('Recall_Score:',precision_knn)
print('Precision_Score:',recall_knn)
print('Cross Validation Score:',(np.mean(cross_val_score(K, X_train_scaled, y_train, cv = 6))))


# In[109]:


fig, ax = plt.subplots(figsize=(10, 10))
plot_confusion_matrix(K,X_test_scaled,y_test,ax=ax)
classification=classification_report(
    digits=4,
    y_true=y_test,
    y_pred=K.predict(X_test_scaled))
print(classification)


# In[111]:


svmc= SVC(kernel='linear', random_state=0)  
svmc.fit(X_train_scaled, y_train)
accuracy_svm=round(accuracy_score(y_test,svmc.predict(X_test_scaled)),3)
f1score_svm=round(f1_score(y_test,svmc.predict(X_test_scaled),average='weighted'),3)
precision_svm=round(precision_score(y_test,svmc.predict(X_test_scaled),average='weighted'),3)
recall_svm=round(recall_score(y_test,svmc.predict(X_test_scaled),average='weighted'),3)

print('Accuracy:',accuracy_svm)
print('F1_Score:',f1score_svm)
print('Recall_Score:',precision_svm)
print('Precision_Score:',recall_svm)
print('Cross Validation Score:',(np.mean(cross_val_score(suv, X_train_scaled, y_train, cv = 6))))


# In[112]:


fig, ax = plt.subplots(figsize=(10, 10))
plot_confusion_matrix(svmc,X_test_scaled,y_test,ax=ax)
classification=classification_report(
    digits=4,
    y_true=y_test,
    y_pred=svmc.predict(X_test_scaled))
print(classification)


# In[ ]:




