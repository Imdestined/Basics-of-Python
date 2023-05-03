#!/usr/bin/env python
# coding: utf-8

# # Python Basics_Assignment 21

# # 1. Add the current date to the text file today.txt as a string.

# In[9]:



from datetime import date


# In[10]:


now = date.today()


# In[11]:


now_str = now.isoformat()


# In[12]:


with open('today', 'wt') as output:
    print(now_str, file=output)


# # 2. Read the text file today.txt into the string today_string

# In[13]:


with open('today', 'rt') as input:
    today_string = input.read()


# In[14]:


today_string


# # 3. Parse the date from today_string.

# In[15]:


fmt = '%Y-%m-%d\n'


# datetime.strptime(today_string, fmt)

# # 4. List the files in your current directory

# In[17]:


import os


# In[18]:


os.listdir('.')


# # 5. Create a list of all of the files in your parent directory (minimum five files should be available).

# In[19]:


import os


# In[21]:


os.listdir('..')


# # 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.

# import multiprocessing
# 
# def now(seconds):
#     from datetime import datetime
#     from time import sleep
#     sleep(seconds)
#     print('wait', seconds, 'seconds, time is', datetime.utcnow())
# 
# if __name__ == '__main__':
#     import random
#     for n in range(3):
#         seconds = random.random()
#         proc = multiprocessing.Process(target=now, args=(seconds,))
#         proc.start()

# # 7. Create a date object of your day of birth.

# In[26]:


my_day = date(1995, 7, 12)


# In[27]:


my_day


# # 8. What day of the week was your day of birth?

# In[29]:


my_day.weekday()


# In[30]:


my_day.isoweekday()


# With weekday(), Monday is 0 and Sunday is 6. With isoweekday(), Monday is 1 and Sunday is 7. Therefore, this date was a Saturday.

# # 9. When will you be (or when were you) 10,000 days old?

# In[31]:


from datetime import timedelta


# In[32]:


party_day = my_day + timedelta(days=10000)


# In[33]:


party_day

