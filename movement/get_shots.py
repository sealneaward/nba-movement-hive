import pandas as pd
import os
from os import listdir
from os.path import isfile, join, exists
import numpy as np
import re
import requests
from tqdm import tqdm

import movement.config as CONFIG

def get_shots(player_id, game_id=''):
    url = 'http://stats.nba.com/stats/shotchartdetail?Period=0&VsConference='\
    '&LeagueID=00&LastNGames=0&TeamID=0&Position=&Location=&Outcome='\
    '&ContextMeasure=FGA&DateFrom=&StartPeriod=&DateTo=&OpponentTeamID=0'\
    '&ContextFilter=&RangeType=&Season=2015-16&AheadBehind='\
    '&PlayerID='+str(player_id)+'&EndRange=&VsDivision=&PointDiff='\
    '&RookieYear=&GameSegment=&Month=0&ClutchTime=&StartRange='\
    '&EndPeriod=&SeasonType=Regular+Season&SeasonSegment='\
    '&GameID='+str(game_id)+'&PlayerPosition='

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    shots = pd.DataFrame(data, columns=headers)
    return shots

def get_shooters(game_id=''):
    url = 'http://stats.nba.com/stats/playbyplayv2?EndPeriod=10'\
    '&EndRange=55800&GameID='+game_id+'&RangeType=2&Season=2015-16'\
    '&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    while response.status_code != 200:
        response = requests.get(url)
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    events = pd.DataFrame(data, columns=headers)
    shots = events.loc[(events.EVENTMSGTYPE == 1) | (events.EVENTMSGTYPE == 2), :]
    players = shots['PLAYER1_ID'].drop_duplicates(inplace=False).values

    return players

def get_games():
    """
    Loads game movements CSV files and returns list of games to get event descriptions from
    """
    # Try converted directory..maybe user removed csv directory to free up memory
    potential_game_dirs = [CONFIG.data.movement.dir]
    games = []
    for path in potential_game_dirs:
        if exists(path):
            for f  in listdir(path):
                if isfile(join(path, f)):
                    game = f.split('.')[0]
                    if len(game) > 0:
                        games.append(game)
            if len(games) > 0:
                return games

    print('No games found.')
    return games

if __name__ == '__main__':
    if not os.path.exists(CONFIG.data.shots.dir):
        os.makedirs(CONFIG.data.shots.dir)

    shots = pd.DataFrame()
    games = get_games()
    for game in tqdm(games):
        players = get_shooters(game)
        for player in players:
            player_game_shots = get_shots(player, game)
            shots = shots.append(player_game_shots)

    shots.to_csv('%s/shots.csv' % (CONFIG.data.shots.dir), index=False)
