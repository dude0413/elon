import web_apps, windows_work
import pyttsx3
import random
import os
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()
    with open('speechlogs.txt', 'a') as sl:
        sl.write(text + '\n')
        sl.close()

def process(input):
    KEYWORDS = ["play", "elon", "search", "who", "what", "when", "where", "why", "how"]
    # Break Down Words #
    new_list = input.split(' ')
    '''
    if new_list[0] == 'play':
        # Further processing #
        filepath_new = 'C:\Program Files (x86)\Steam\steamapps\common'
        steam_game_list = os.listdir(filepath_new)
        [x.lower() for x in steam_game_list]
        for game in steam_game_list:
            if new_list[1] == 'game':
    '''
    for keyword in KEYWORDS[3:]:
        if keyword == new_list[0] or keyword.title() == new_list[0]:
            try:
                wolf_question = web_apps.wolframalpha_question(input)
                say(wolf_question)
            except AttributeError:
                google_search = web_apps.search_google(input)
                say(google_search)
    if KEYWORDS[2] == new_list[0] and new_list[-2:] == ['on', 'Google']:
        input = input.replace('search', '')
        input = input.replace('on Google', '')
        web_apps.search_google(input)

    if KEYWORDS[2] == new_list[0] and new_list[-2:] == ['on', 'YouTube']:
        input = input.replace('search', '')
        input = input.replace('on YouTube', '')
        web_apps.play_youtube_video(input)

    if KEYWORDS[4] == new_list[0] and new_list[-2:] == ['CPU', 'usage']:
        windows_work.cpu_usage()



z
