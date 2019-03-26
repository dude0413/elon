import webbrowser
from package.config import *
import requests as r
from bs4 import BeautifulSoup
import wunderpy2
import wikipedia
import wolframalpha
'''
    Reddit Section
=======================
-Read unread items in Inbox ✔
-Read recent posts to different subs (# included) ✔
-Read any post description 
-More features coming!
'''
# Read unread items for Reddit #
def return_unread_inbox():
    for unread_inbox in bot.inbox.unread():
        print(str(unread_inbox.author) + ' said: ' + str(unread_inbox.body))

# List the post titles of a certain subreddit #
# /// Input: Show me the recent posts from the LucidDreaming subreddit \\\ #
def recent_sub_posts(subreddit_name, limit):
    subreddit = bot.subreddit(subreddit_name)
    for submission in subreddit.new(limit=limit):
        print(submission.title)

# return_unread_inbox()
# recent_sub_posts('LucidDreaming', 5)
''' 
    Web Section
===================
- Play (song)
- Google (google)
- Start up (Reddit, Quora etc.)
- 
'''
'''
# Google Section #
# //// Input: Google fun ways to mess around with Raspberry pi \\\\ #
def search_google(contents, glimit=10):
    for url in search(contents, stop=glimit):
        source = r.get(url)
        source_text = source.text
        soup = BeautifulSoup(source_text, 'html.parser')
        title = soup.find('title')
        try:
            title_string = title.string
        except AttributeError:
            title_string = 'No title'
        print(title_string)
        print(url)
'''
# YouTube Music Section #
# //// Input: Play Congratulations \\\\ #
def play_youtube_video(video_choice):
    url = 'https://www.youtube.com/results?search_query=' + video_choice
    source_code = r.get(url, timeout=15)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    songs = soup.findAll('div', {'class': 'yt-lockup-video'})
    song = songs[0].contents[0].contents[0].contents[0]
    hit = song['href']
    webbrowser.open('https://www.youtube.com' + hit)
'''' 
    Question Section    
========================
'''
def wolframalpha_question(question):
    wolf_client = wolframalpha.Client(wolf_app_id)
    res = wolf_client.query(question)
    answer = next(res.results).text
    return answer

def wikipedia_summary(searching_for, sentencesNumber):
    print(wikipedia.summary(searching_for, sentences=sentencesNumber))

