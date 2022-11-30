#!/usr/bin/env python
# coding: utf-8

# # 1. What does an empty dictionary's code look like?

# Two curly brackets: {}

# # 2. What is the value of a dictionary value with the key 'foo' and the value 42?

# In[1]:


{'foo': 42}  ## value is 42


# # 3. What is the most significant distinction between a dictionary and a list?

# The items stored in a dictionary are unordered, while the items in a list are ordered.

# # 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# In[2]:


spam= {'bar': 100}


# In[5]:


spam['foo']


# We get a KeyError error.

# # 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# There is no difference. The in operator checks whether a value exists as a key in the dictionary.

# # 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

# 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

# # 7. What is a shortcut for the following code?
# if 'color' not in spam:
# spam['color'] = 'black'
# 

# spam.setdefault('color', 'black')

# # 8. How do you "pretty print" dictionary values using which module and function?

# pprint.pprint()
