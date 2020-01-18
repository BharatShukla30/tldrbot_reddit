# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 02:47:45 2019

@author: mouseless
"""
import praw
import pandas as pd
import webbrowser as wb
reddit = praw.Reddit(client_id='lqBCpf4ONw7Yrw', client_secret="97XH5Nm7mMbZGcnmLidwxMmXA78",
                     username='stancom_bot', password='manrat0230',user_agent='LMGTFY (by /u/stan3098)')

subreddit = reddit.subreddit("stan_com")

for submission in subreddit.new(limit=1):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    #wb.open(submission.url)    
    #This part will parse the html page
    import requests 
    from bs4 import BeautifulSoup 
      
    URL = submission.url
    r = requests.get(URL).text
    
    soup = BeautifulSoup(r,features="lxml") 
    
    # Get text from all <p> tags.
    p_tags = soup.find_all('p')
    
    # Get the text from each of the “p” tags and strip surrounding whitespace.
    p_tags_text = [tag.get_text().strip() for tag in p_tags]
    
    from gensim.summarization.summarizer import summarize
    # Filter out sentences that contain newline characters '\n' or don't contain periods.
    sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
    # Combine list items into string.
    article = ' '.join(sentence_list)
    summary = summarize(article, ratio=0.03)
    print (summary)
    if submission.reply("This is the best tldr I could make:\n"+summary):
        print("done")
