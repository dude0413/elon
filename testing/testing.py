import shutil
import os

def find_game_path(game):
    d = {}
    with open('games.txt') as f:
        for line in f:
            (key, val) = line.split(' = ')
            d[key] = val.rstrip()
    name_of_game = d[game]
    os.chdir('C:\Program Files (x86)\Steam\steamapps\common' + '\\' + name_of_game)
    try:
        new_name = name_of_game.lower()
        new_name = new_name.replace(' ', '')
        output = shutil.which(new_name)
    except output == None:
        output = shutil.which(name_of_game)
    print(output)

find_game_path('Prison Architect')

