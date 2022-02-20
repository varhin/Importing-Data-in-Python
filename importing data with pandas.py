#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing .txt files
import pandas as pd
pd.read_table("filelocation/filename.txt")


# In[ ]:


#importing excel files
import pandas as pd
pd.read_excel("filename.xlsx")


# In[ ]:


#importing .csv files
import pandas as pd 
pd.read_csv("filename.csv")


# In[ ]:


#importing from the web
import requests as req
url = "url.of.website"
req.get(url, allow_redirects = True)


# In[ ]:


#importing from sql database
import pyodbc
sql_connection = pyodbc.connect("sqlserverpathway")
pd.read_sql_query('type your sql query here', sql_connection)

