import subprocess as sp
import os
import psutil
import shutil
''' 
    Windows Section
======================
- Open up the file explorer to said directory
- Open up the notepad and put contents into it
- Set a timer
- Shutdown (with a timer too if needed)
- Restart (with a timer too if needed)
- CPU and RAM usage
'''
def file_explorer(path_to_file):
    sp.Popen(r'explorer /select' + '"' + path_to_file + '"' + "'")

def shutdown_now():
    sp.call(["shutdown", "/s"])

def shutdown_timed(time):
    sp.call(["shutdown","/s", "/t", time])

def restart_now():
    sp.call(["shutdown", "/r"])

def restart_timed(time):
    sp.call(["shutdown", "/r", "/t", time])

def cpu_usage():
    print(psutil.cpu_percent())

def ram_usage():
    print(psutil.virtual_memory())

def play_overwatch():
    filepath = 'C:\\Program Files (x86)\\Overwatch'
    os.chdir(filepath)
    os.system( '"C:\\Program Files (x86)\\Overwatch\\Overwatch Launcher.exe"' )

def get_to_game_folder(game_name):
    filepath = 'C:\Program Files (x86)\Steam\steamapps\common'
    full_path = (filepath + '\\' + game_name.title())
    os.chdir(full_path)
    print('done')
    os.system(shutil.which('RustClient'))
def play_rust():
    rustfilepath = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Rust'
    os.chdir(rustfilepath)
    os.system( '"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Rust\\RustClient.exe"' )
