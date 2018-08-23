 
import praw
import pdb
import re
import os

#cookiemonster bot is defined in a praw.ini file that is in this directory
reddit = praw.Reddit('cookiemonsterbot')
subreddit = reddit.subreddit("test")