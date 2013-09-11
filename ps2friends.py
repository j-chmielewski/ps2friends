#!/bin/env python

import sys
import urllib2
import json

# global params
api_url = 'https://census.soe.com/s:soe/json/get/ps2:v2/characters_friend/?c:join=character^show:name.first^on:friend_list.character_id^to:character_id^inject_at:character'
player_id_param = 'character_id'

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

def get_json(player_id):

    url = '{0}&{1}={2}'.format(api_url, player_id_param, player_id)
    response = urllib2.urlopen(url)

    data = json.load(response)   
    return data


def print_status(json):
    try:
        friend_list = json['characters_friend_list'][0]['friend_list']
    except (IndexError, KeyError):
        print 'Unknown response format'
        exit(1)

    for friend in friend_list:
        name = friend['character']['name']['first']
        print '{0}\t{1}'.format(name + ' ' * (30 - len(name)), Colors.RED + 'Offline' + Colors.END if friend['online'] == "0" else Colors.GREEN + 'Online' + Colors.END)

# main
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '\nUsage:\n{0} player_id\n\nGet your player id from http://players.planetside2.com (in url)\n'.format(sys.argv[0])
        sys.exit(1)
    else:
        player_id = sys.argv[1]

    json = get_json(player_id)
    print_status(json)
