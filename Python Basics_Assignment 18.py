#!/usr/bin/env python
# coding: utf-8

# # Python Basics_Assignment 18

# # 1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

# In[1]:


import zoo


# In[2]:


zoo.hours()


# # 2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[3]:


import zoo as menagerie


# In[4]:


menagerie.hours()


# # 3. Using the interpreter, explicitly import and call the hours() function from zoo.

# In[5]:


from zoo import hours


# In[6]:


hours()


# # 4. Import the hours() function as info and call it.

# In[7]:


from zoo import hours as info


# In[8]:


info()


# # 5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

# In[14]:


plain = {'a': 1, 'b': 2, 'c': 3}


# In[16]:


plain


# # 6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

# In[11]:


from collections import OrderedDict


# In[12]:


fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# In[13]:


fancy 


# # 7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

# In[17]:


from collections import defaultdict


# In[18]:


dict_of_lists = defaultdict(list)


# In[19]:


dict_of_lists['a'].append('something for a')


# In[20]:


dict_of_lists['a']

