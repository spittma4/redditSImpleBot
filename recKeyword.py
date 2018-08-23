# Script to recognize keywords 
# Written By: Sam Pittman
# Started: 12 August 2018


import praw
import pdb
import re
import os

#cookiemonster bot is defined in a praw.ini file that is in this directory
reddit = praw.Reddit('cookiemonsterbot')
subreddit = reddit.subreddit("test")

#for submission in reddit.front.hot():
for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Text: ", submission.selftext)
	print("Score: ", submission.score)
	print("-----------------------------------------")
