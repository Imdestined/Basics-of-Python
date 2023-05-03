#!/usr/bin/env python
# coding: utf-8

# # Assignment_20

# # 1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.

# In[1]:


test1 = 'This is a test of the emergency text system'


# In[2]:


len(test1)


# In[3]:


outfile = open('test.txt', 'wt')


# In[4]:


outfile.write(test1)


# In[5]:


outfile.close()


# # 2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?

# In[6]:


with open('test.txt', 'rt') as infile:
    test2 = infile.read()


# In[7]:


len(test2)


# In[8]:


test1 == test2


# # 3. Create a CSV file called books.csv by using these lines:
# title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China Miéville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992

# In[9]:


text='''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''


# In[10]:


with open('books.csv', 'wt') as outfile:
    outfile.write(text)


# # 4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).

# In[11]:


import sqlite3


# In[12]:


db = sqlite3.connect('books.db')


# In[13]:


curs = db.cursor()


# In[14]:


curs.execute('''create table book (title text, author text, year int)''')


# In[15]:


db.commit()


# # 5. Read books.csv and insert its data into the book table.

# In[16]:


import csv


# In[17]:


import sqlite3


# In[18]:


ins_str = 'insert into book values(?, ?, ?)'


# In[19]:


with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))


# In[20]:


db.commit()


# # 6. Select and print the title column from the book table in alphabetical order.

# In[21]:


sql = 'select title from book order by title asc'


# In[22]:


for row in db.execute(sql):
    print(row)


# In[23]:


for row in db.execute(sql):
    print(row[0])


# # 7. From the book table, select and print all columns in the order of publication.

# In[24]:


for row in db.execute('select * from book order by year'):
    print(row)


# In[25]:


for row in db.execute('select * from book order by year'):
    print(*row, sep=', ')


# # 8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.

# In[26]:


import sqlalchemy


# In[27]:


conn = sqlalchemy.create_engine('sqlite:///books.db')


# In[28]:


sql = 'select title from book order by title asc'


# In[29]:


rows = conn.execute(sql)


# In[30]:


for row in rows:
     print(row)


# # 9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.

# In[32]:


get_ipython().system('pip install redis')


# import redis
# conn = redis.Redis()
# conn.delete('test')
# 1
# conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
# True
# conn.hgetall('test')
# {b'name': b'Fester Bestertester', b'count': b'1'}

# # 10. Increment the count field of test and print it.

# conn.hincrby('test', 'count', 3)
# 4
# conn.hget('test', 'count')
# b'4'
