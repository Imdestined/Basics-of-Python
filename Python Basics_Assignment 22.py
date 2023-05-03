#!/usr/bin/env python
# coding: utf-8

# # Python Basics_Assignment 22

# # 1. What is the result of the code, and explain?

# In[1]:


X = 'iNeuron'


# In[2]:


def func():
    print(X)


# In[3]:


func()


# Here when func() is called it will execute the statement written inside it which print the value of x whose value is assigned as 'ineuron'.

# # 2. What is the result of the code, and explain?

# In[4]:


X = 'iNeuron'


# In[5]:


def func():
    X = 'NI!'


# In[6]:


func()


# In[7]:


print(X)


# Here when func() is called it will execute the statement written inside it which only initialize value of x='NI' but it doesnot return anything(None).So it comes out of the block and doesnot print anything.
# Again when print(x) is executed it prints the value of X = 'iNeuron'.
# 

# # 3. What does this code print, and why?

# In[8]:


X = 'iNeuron'


# In[33]:


def func():
    X = 'NI'
    print(X)


# In[34]:


func()


# In[35]:


print(X)


# Here when func() is called it will execute the statement written inside it which initialize value of x='NI' and subsequently print the value of X.The scope of  X = 'NI'is within the block func().
# But when a print statement i.e print(X) is executed it prints x value as iNeuron.(X is treated as global variable)

# # 4. What output does this code produce? Why?

# In[13]:


X = 'iNeuron'


# In[14]:


def func():
    global X
    X = 'NI'


# In[15]:


func()


# In[16]:


print(X)


# Here in func() we have declared X as global variable hence it's previous value i.e 'iNeuron' is overrided and when print(x) is executed it prints latest updated value i.e 'NI'.

# # 5. What about this code—what’s the output, and why?

# In[17]:


X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)
nested()


# In[18]:


func()


# In[19]:


X


# Here when nested() is called it prints X = 'iNeuron'(Global variable).
# In func(), X = 'NI' the scope of X is within func() as it is a local variable.

# # 6. How about this code: what is its output in Python 3, and explain?

# In[37]:


def func():
    X = 'NI'
def nested():
    nonlocal X
    X = 'Spam'
nested()
print(X)


# In[31]:


func()


# 
# A variable if we want to access outside the block as well as within the block should be declared as global.
