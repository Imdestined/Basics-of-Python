#!/usr/bin/env python
# coding: utf-8

# ## 1. In the below elements which of them are values or an expression? eg:- values canbe integer or string and expressions will be mathematical operators.
# 
# 

# *: expression 
# 'hello':value 
# -87.8:value
# -:expression
# /:expression
# 6:value

# ## 2. What is the difference between string and variable?

# String is a class or reference datatype. It is used to represent text type data.
# Whereas, variable is any alphabet or gropu of alphabet which work as temporary storage locations , a variable is used to represent any value
# example :::
# String x="Sumanta";
# // here x is variable and type of value it stores is in string

# ## 3. Describe three different data types.

# * Text Type:	str
# * Numeric Types:	int, float, complex
# * Sequence Types:	list, tuple, range

# ## 4. What is an expression made up of? What do all expressions do?

# * Expressions consist of values (such as 5) and operators (such as +), and they can always evaluate (that is, reduce) down to a single value. 
# 
# * 2+5 : Expression
# 
# * That means one can use expressions anywhere in Python code that one could also use a value. In this example, 2 + 5 is evaluated down to a single value, 7.

# ## 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# * Expression:
# Expressions always returns a value
# Functions are also expressions. Even a non returning function will still return None value, so it is an expression.
# Can print the result value
# * Examples Of Python Expressions: “Sumanta” + “iNeuron”, 5 + 5 etc.
# 
# * Statement:
# A statement never returns a value
# Cannot print any result
# * Examples Of Python Statements: Assignment statements, conditional branching, loops, classes, import, def, etc.

# ## 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# In[8]:


bacon = 22
bacon + 1
print (bacon)

## Hence, The value of the bacon reamin same as 22


# ## 7. What should the values of the following two terms be?
# 'spam' +'spamspam'
# 'spam' * 3

# In[18]:


'spam' + 'spamspam' 


# In[19]:


'spam' * 3 


# ## 8. Why is eggs a valid variable name while 100 is invalid?

# Because variable names cannot begin with a number.

# ## 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# In[20]:


l= [1,2.3,"Sumanta"]

# int (): 
# float():
# str ():
## These are the functions used to get the data type


# In[22]:


for item in l:
    print (type(item))


# ## 10. Why does this expression cause an error? How can you fix it?
# * 'I have eaten &#39; + 99 + &#39; burritos.&#39;

# ##### Answer: This expression causes and error because in this line 'I have eaten' and 'burritos' are strings, while 99 is treated as integer. In order to fix the error and print 'I have eaten 99 burritos.', 99 needs '' around it to treat it as a string.

# In[23]:


print ('I have eaten 99 burritos')


# In[ ]:




