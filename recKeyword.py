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

keyword = "test"

#for submission in reddit.front.hot():
for submission in subreddit.hot(limit=5):
	title = submission.title
	text = submission.selftext
	score = submission.score

	print("Submission ID: " + submission.id) + "\n"

	if (score > 1):
		print('Score greater than 1!')
		print('Title: ' + submission.title)
		print("Score: " + str(submission.score))	
	else:
		print("Score less than 2")

	keyword = "test"

	if (keyword in title):
		print("\nkeyword: 'test' is in title!")
		print("Title: " + submission.title)
		keyHighlight = title[:title.find(keyword)] + "***" + keyword + "***" + title[title.find(keyword)+len(keyword):]
		#print("Keyword Highlight: ", title.find(keyword))
		print("Keyword Highlight: " + keyHighlight)

	#print("Text: ", submission.selftext)
	
	print("-----------------------------------------")
