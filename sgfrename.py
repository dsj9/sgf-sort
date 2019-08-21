import argparse
import glob
import re
import sys
from string import Template

default_format = '$date - $server - $black - $white'

server_identifiers = {
    'OGS': {
        'tag': 'PC',
        'value': 'OGS:'
    },
    'KGS': {
        'tag': 'PC',
        'value': 'The KGS Go Server'
    },
    'Tygem': {
        'tag': 'PC',
        'value': 'Tygem'
    },
    'WBaduk': {
        'tag': 'PC',
        'value': 'wbaduk'
    },
    'CyberOro': {
        'tag': 'US',
        'value': 'www.cyberoro.com'
    },
    'IGS': {
        'tag': 'PC',
        'value': 'IGS:'
    },
    'Fox': {
        'tag': 'AP',
        'value': 'foxwq'
    },
    'DGS': {
        'tag': 'PC',
        'value': 'Dragon Go Server' 
    },
    'GoShrine': {
        'tag': 'PC',
        'value': 'GoShrine'
    },
    'INGO': {
        'tag': 'PC',
        'value': 'Played on INGO'
    },
    'LankeWeiqi': {
        'tag': 'PC',
        'value': '烂柯围棋网'
    }
}

def find_key(data, key):
    reg = r'{0}\[([^]]+)\]'.format(key)
    matches = re.findall(reg, data)
    if matches:
        return matches
    return None

def find_server(data):
    for server in server_identifiers:
        try:
            info = find_key(data, server_identifiers[server]['tag'])
            if info:
                for value in info:
                    if value.startswith(server_identifiers[server]['value']):
                        return server
        except:
            continue
    return None

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("-r", "--recursive", action='store_true', help="Search folders recursively")
argument_parser.add_argument("-f", "--format", help="Renaming format")

options = vars(argument_parser.parse_args())

#template = Template(options.format)

for file in glob.glob('*.sgf', recursive=options['recursive']):
    with open(file, 'r', encoding='utf-8') as f:
        print(file , ': ')
        try:
            data = f.read()
        except:
            print('Could not read ' , file)
            continue
    black_player = find_key(data, "PB")
    white_player = find_key(data, "PW")

    