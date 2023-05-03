#!/usr/bin/env python
# coding: utf-8

# # Assignment_10

# # 1. How do you distinguish between shutil.copy() and shutil.copytree()?
# The shutil.copy() function will copy a single file, while shutil.copytree() will copy an entire folder, along with all its contents.
# 

# # 2. What function is used to rename files??
# The shutil.move() function is used for renaming files as well as moving them.

# # 3. What is the difference between the delete functions in the send2trash and shutil modules?
# The send2trash functions will move a file or folder to the recycle bin, while shutil functions will permanently delete files and folders.
# 

# # 4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
# 
# The equivalent method of the open() method for ZipFile objects is the ZipFile() constructor method.
# 
# This method is used to create a ZipFile object that represents a ZIP archive file. It takes the path to the ZIP archive file as its first argument, and an optional mode string as its second argument, which determines how the archive file is opened.
# 
# Here's an example of how to use the ZipFile() method to open a ZIP archive file:
# 
# 

# In[2]:


import zipfile

# Open the ZIP archive file in read mode
with zipfile.ZipFile('example.zip', 'r') as zip_file:
    # Do something with the zip file, such as extracting its contents
    zip_file.extractall('extracted_contents')


# # 5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
# 
# 
# 

# In[1]:


import os
import shutil

# Source directory to search for files with the desired extension
source_dir = "/path/to/source/directory"

# Destination directory to copy the matching files to
dest_dir = "/path/to/destination/directory"

# Desired file extension to search for
file_extension = ".txt"

# Recursively search the source directory for files with the desired extension
for dirpath, dirnames, filenames in os.walk(source_dir):
    for file in filenames:
        if file.endswith(file_extension):
            # Construct the full path to the source file
            source_file_path = os.path.join(dirpath, file)
            
            # Construct the full path to the destination file
            dest_file_path = os.path.join(dest_dir, file)
            
            # Copy the source file to the destination directory
            shutil.copy(source_file_path, dest_file_path)
            
            # Print a message to confirm that the file was copied
            print(f"Copied {source_file_path} to {dest_file_path}")


# In[ ]:




