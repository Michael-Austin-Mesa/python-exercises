#!/usr/bin/env python
# coding: utf-8

# ### Q1c

# In[3]:


from function_exercises import get_letter_grade
get_letter_grade()


# ### Q2a
# abc for 1, 2, 3 has 9 possible outcomes

# ### Q2b
# 6 combinations

# In[4]:


import itertools
letterlist = 'abcd'
for x in itertools.combinations(letterlist, 2):
    print(x)


# ### Q2c
# 12 permutations

# In[5]:


import itertools
letterlist = 'abcd'
for x in itertools.permutations(letterlist, 2):
    print(x)


# ### Q3

# In[6]:


import json

data = json.load(open('profiles.json'))


# In[7]:


data


# In[70]:


length = len(data)
for n in range(length):
    print(data[n]['_id'])
print(f"{length} unique user id's found")


# In[9]:


count = 0
for n in range(length):  
    if data[n]['isActive'] == True:
        count += 1
print(f"{count} users are still active.")


# In[10]:


count = 0
for n in range(length):  
    if data[n]['isActive'] != True:
        count += 1
print(f"{count} users are no longer active.")


# In[31]:


def remove_commas_dollars(n):
    
    n = n.replace(',','')
    n = n.replace('$','')
    
    return float(n)


# In[33]:


totalbalance = 0.00
for i in range(length):
    totalbalance += remove_commas_dollars(data[i]['balance'])
totalbalance = round(totalbalance, 2)
print(totalbalance)


# In[36]:


avgbalance = totalbalance/length
avgbalance = round(avgbalance, 2)
print(avgbalance)


# In[48]:


currentbalance = 0.00
balancelist = []
for i in range(length):
    currentbalance = remove_commas_dollars(data[i]['balance'])
    balancelist.append(currentbalance)
print(min(balancelist))


# In[49]:


currentbalance = 0.00
balancelist = []
for i in range(length):
    currentbalance = remove_commas_dollars(data[i]['balance'])
    balancelist.append(currentbalance)
print(max(balancelist))


# In[57]:


countStrawberry = 0
countBanana = 0
countApple = 0
fruitlist = []
for i in range(length):
    if data[i]['favoriteFruit'] == 'strawberry':
        countStrawberry += 1
    elif data[i]['favoriteFruit'] == 'banana':
        countBanana += 1
    elif data[i]['favoriteFruit'] == 'apple':
        countApple += 1
print(f'{countStrawberry} strawberry')
print(f'{countBanana} banana')
print(f'{countApple} apple')
fruitlist.append(countStrawberry)
fruitlist.append(countBanana)
fruitlist.append(countApple)

mostcommon = max(fruitlist)
print(f'{mostcommon} strawberry enjoyers make up the most common favorite fruit')


# In[59]:


leastcommon = min(fruitlist)
print(f'{leastcommon} apple enjoyers make up the least common favorite fruit')


# In[68]:


import re
messageslist = []
for i in range(length):
    #print(re.sub('\D','', data[i]['greeting']))
    messageslist.append(int(re.sub('\D','', data[i]['greeting'])))
print(f'{sum(messageslist)} total unread messages')

