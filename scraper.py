import praw
from gtts import gTTS
import os

reddit_read_only = praw.Reddit(client_id = "MeWv3fdcOs_MrnkjK5poVw", client_secret =  "2PpgrtO2taOk8hvuoXjzJrWb32reww",user_agent =  "sogen")

subreddit = reddit_read_only.subreddit("AskReddit")

myText = " "

language = "en"



for post in subreddit.hot(limit = 1):

    myText = myText + post.title + post.comments[1].body + str(post.comments[1].ups) + post.comments[2].body + str(post.comments[2].ups) + post.comments[3].body + str(post.comments[3].ups)

myobj = gTTS(text=myText, lang=language, slow=False)

myobj.save("output.mp3")


