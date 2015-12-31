import os
import subprocess
import re
import sys
import json

def open_tabs(tabs):
    ''' The main function that forms the command and executes it'''
    
    command = ['gnome-terminal']
    for tab in tabs:
        command.append('--tab')
        command.append('--working-directory='+tab['working-directory'])

    subprocess.call(command)
    return

def get_config(tabs_to_open):
    ''' Get the config from the config file and create the list of tabs that are to be opened'''

    with open(os.path.dirname(os.path.realpath(__file__))+'/config.json') as json_file:
        config_data = json.load(json_file)

    tabs = []
    for tab in tabs_to_open:
        if(tab == 'all'):
            for k,v in config_data.iteritems():
                tabs.append(v)
            break
        try:
            project = config_data[tab]
        except KeyError:
            print 'unknown tab: '+tab
            continue

        tabs.append(project)

    if len(tabs) != 0:
        open_tabs(tabs)
    else:
        print 'no working directories to open'
    
    return

    

tabs_to_open =[]
if len(sys.argv) >= 2:
    ''' Check if there are any specific directories to open '''
    tabs_to_open = sys.argv[1::]
else:
    ''' Fallback to 'all' i.e. open all directories specified in config.json '''
    tabs_to_open =['all']
get_config(tabs_to_open)