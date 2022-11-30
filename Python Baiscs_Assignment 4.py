#!/usr/bin/env python
# coding: utf-8

# # 1. What exactly is []?
# 

# The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.
# 

# # 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value?
# (Assume [2, 4, 6, 8, 10] are in spam.)

# In[19]:


spam=[2,4,6,8,10]


# In[20]:


spam[2]='hello'


# In[21]:


spam


# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# 

# In[22]:


spam=['a', 'b', 'c', 'd']


# # 3. What is the value of spam[int(int('3' * 2) / 11)]?
# 

# In[23]:


spam[int(int('3' * 2) / 11)]


# # 4. What is the value of spam[-1]?
# 

# In[24]:


spam[-1]


# # 5. What is the value of spam[:2]?
# 

# In[25]:


spam[:2]


# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 

# In[26]:


bacon=[3.14, 'cat', 11, 'cat', True]


# # 6. What is the value of bacon.index('cat')?
# 

# In[27]:


bacon.index('cat')


# # 7. How does bacon.append(99) change the look of the list value in bacon?
# 

# In[28]:


bacon.append(99)


# In[29]:


bacon


# # 8. How does bacon.remove('cat') change the look of the list in bacon?
# 

# In[30]:


bacon.remove('cat')


# In[31]:


bacon


# # 9. What are the list concatenation and list replication operators?
# 

# The operator for list concatenation is +, while the operator for replication is *.
# 

# # 10. What is difference between the list methods append() and insert()?
# 

# While append() will add values only to the end of a list, insert() can add them anywhere in the list.

# # 11. What are the two methods for removing items from a list?

# The del statement and the remove() list method are two ways to remove values from a list.

# # 12. Describe how list values and string values are identical.

# Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.
# 

# # 13. What's the difference between tuples and lists?

# Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists use the square brackets, [ and ].

# # 14. How do you type a tuple value that only contains the integer 42?

# In[32]:


(42,)


# # 15. How do you get a list value's tuple form? How do you get a tuple value's list form?

# The tuple() and list() functions, respectively

# # 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

# They contain references to list values.

# # 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.
