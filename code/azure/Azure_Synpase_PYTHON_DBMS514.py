#!/usr/bin/env python
# coding: utf-8

# ## dbms_project
# 
# Twitter Network Analysis
# 

# # DBMS EUROVISION TWITTER ANALYSIS | DATA 514

# ---

# In[1]:


#Testing whether Azure Spark Pool is spinning up or not
"Hello World"


# # JSON SCHEMA

# In[4]:


df.printSchema()


# ---

# # Import JSON Data using Spark import

# In[2]:


import pandas as pd
df = spark.createDataFrame(pd.read_json("abfss://twitterdata@dbms514storage.dfs.core.windows.net/DBMS_EUROVISION_TWITTER.json"))
df.count()


# # Checking Dataframe Content

# In[29]:


display(df.limit(10))


# # Reviewing Columns

# In[4]:


df.columns


# # Create a SPARK SQL view to run queries

# In[5]:


df.createOrReplaceTempView("tweets")


# # Query 1: Which user has posted the most number of tweets

# In[6]:


spark.sql("select user_id, user_name, count(*) from tweets group by user_id, user_name order by count(*) desc").show()


# # Query 2: Which countries has the most tweets being actively posted

# In[7]:


spark.sql("select user_location, count(*) from tweets where user_location is not null group by user_location order by count(*) desc").show()


# # Query 3: How many tweets are associates with each hashtags

# In[8]:


spark.sql('select entities_hashtags_text, count(*) from tweets group by entities_hashtags_text order by count(*) desc').show()


# **NOTE 1** We had multiple tweets per each hastags in the original dataset. During the processing, we bifurcated the levels to one rows per each tweet for individual hashtags
# 
# **NOTE 2** In the above output, we see that we have difference cases of hashtags so we have to create a uniform case

# **WAY 1** Convert column in dataframe to lowercase() by using dataframe *lower()* function(import required) and then create a new SQL View

# In[9]:


from pyspark.sql.functions import lower
df_lower = df.withColumn("entities_hashtags_text_lower", lower(df["entities_hashtags_text"]))


# **WAY 2** Change the entities hashtags text to lower case using SQL *LOWER()* function

# In[12]:


spark.sql('SELECT lower(entities_hashtags_text), count(*) FROM tweets where entities_hashtags_text is not null group by lower(entities_hashtags_text) order by count(*) desc').show()


# # Query 4: For each verified user, what is the percentage of different type of tweets to their overall number of tweets

# In[13]:


display(df[['user_verified', 'retweeted_status', 'retweeted', 'is_quote_status', 'in_reply_to_status_id',
 'in_reply_to_status_id_str',
 'in_reply_to_user_id',
 'in_reply_to_user_id_str',
 'in_reply_to_screen_name',]].limit(10))


# Validating Group Category Breakdown

# In[14]:


df.groupBy('is_quote_status').count().show()


# In[15]:


df.groupBy('user_verified').count().show()


# In[16]:


spark.sql('SELECT CASE WHEN retweeted_status is not null THEN "retweet" \
WHEN is_quote_status is true THEN "quoted" \
WHEN in_reply_to_status_id_str is not null THEN "replied" \
ELSE "simple" END AS tweet_type, count(*)*100/(select count(*) from tweets WHERE user_verified is true) \
FROM tweets \
WHERE user_verified is true \
GROUP BY tweet_type').show()


# Checking if we have any simple tweets in the data we have considered for the project

# In[17]:


spark.sql('SELECT count(*) FROM tweets WHERE retweeted_status is null AND \
is_quote_status is false AND \
in_reply_to_status_id_str is null').show()


# # Q5: (path finding) Display the thread (replies) of tweets (the tweet, time, id, in reply to id, user name with their screen name) posted by user with screen_name “blcklcfr” in the order in which they were posted. [HINT: use tweet’s id to discover the thread]
# 

# In[18]:


display(df.filter(df['user_screen_name'] == "blcklcfr"))


# In[19]:


filtered_df = df.filter(df['user_screen_name'] == "Hannah_DeForest")
display(filtered_df)


# In[20]:


id_list = filtered_df.select("id_str").rdd.flatMap(lambda x: x).collect()
id_list


# In[21]:


replied_tweets = display(df.filter(df['in_reply_to_status_id_str'].isin(id_list)))


# In[22]:


from pyspark.sql.functions import desc
df.groupby('user_screen_name').count().orderBy(desc("count")).show()


# # Q6: Are there any three users A, B, C such that: Any of User A’s tweet/s were replied to by B and C and vice versa, and B has replied to any of C’s tweet/s and vice versa. How many such trios exist? Display each trio with names, screen names of users. 
#  

# In[23]:


spark.sql(' SELECT DISTINCT A.user_name AS A_name, A.user_screen_name AS A_screen_name, \
                B.user_name AS B_name, B.user_screen_name AS B_screen_name, \
                C.user_name AS C_name, C.user_screen_name AS C_screen_name \
FROM tweets A \
JOIN tweets B ON A.user_screen_name = B.in_reply_to_screen_name AND B.user_screen_name <> A.user_screen_name \
JOIN tweets C ON A.user_screen_name = C.in_reply_to_screen_name AND C.user_screen_name <> A.user_screen_name AND C.user_screen_name <> B.user_screen_name \
WHERE B.in_reply_to_screen_name = C.user_screen_name ').show()


# ---

# # END
