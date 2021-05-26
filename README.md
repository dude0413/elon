Elon is a computer assistent that is based on Elon Musk because I found him to be a pretty cool dude (I still do, but he's a little rough around the edges). Search the web, find out the weather for tomorrow, or play a YouTube video. Just say it and Elon does it!
*Contents*
Package includes the configuration file
Testing includes different testing environments that I was working on
- aimlTesting.py -> 
- Games.txt -> testing being able to open games using Elon
- testing.py -> general testing file
- testing.xml -> testing script AI stuffs
main.py -> gets the contents from the Natural Language Processing api from Google
processing.py -> this is where a lot of the magic takes place.
- say() allows Elon to speak (using the pyttsx3 engine)
- process() processes whatever the user speaks and then points to other functions based on what they say
speech.py -> logging information for say() and some more testing with processing
Weather.py -> allows Elon to tell you the weather using the Dark Sky API
web_apps.py -> where anything from the web happens inside the brain of Elon
- Reddit Section
    - return_unread_items() -> speak anything in the inbox of your Reddit account
    - recent_sub_posts() -> reads the titles of the top recent posts of the subreddit you specify
- Web Section
    - search_google() -> allowed users to search anything fro google
    - play_youtube_video() -> say a video title that you would be interested in watching and Elon automatically brings it up for you
- Question section
    - Wolframalpha question -> if the question starts out with “who”, “what”, “when”, “where”, or “why”, send the request to wolframalpha who would send a response back
    - Wikipedia summary -> sends back a brief summary of whatever topic you are interested in
window_works.py -> includes some basic functions that allow the user to do things such as restart their pc, check how much ram they are using, shutdown in a certain amount of time, etc.
