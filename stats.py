import pandas as pd
import numpy as np


def replace_dashes(df):
    """
    Question 1
    Replaces - with 0
    returns nd
    """

    nd = df.replace('-', 0)
    return nd


def filter_on_start(df):
    """
    Question 2
    Filters row and returns 
    """

    teams = []
    for ind in df.index:
        print(df['Team'][ind], df['Debut'][ind]) 
        debut =  df['Debut'][ind]

        if '-' in debut:
            start, end = list(map(int, debut.split('-')))
            if start  >= 1930:
                teams.append(df['Team'][ind])
        else:
            if int(debut) >= 1930 and int(debut) <= 1980:
                teams.append(df['Team'][ind])
 
    return teams


def top_5_teams(df):
    df[ ["Points"] ] = df[ ["Points"] ].apply(pd.to_numeric)
    
    top5 = df.nlargest(5, "Points")

    teams = []
    for ind in top5.index:
        teams.append( top5['Team'][ind] )

    return teams


def Goal_diff_count(df):
    
    teams = []
    for ind in df.index:
        teams.append( (df['Team'][ind], int(df['GoalsAgainst'][ind]) - int(df['GoalsFor'][ind])) )

    max_diff_team = max(teams, key = lambda x: x[1])
    min_diff_team = min(teams, key = lambda x: x[1])

    return max_diff_team[0], min_diff_team[0]

        
def add_winning_percent_column(df):

    percent_list = []
    for ind in df.index:
        total_matches = int(df['GamesPlayed'][ind]) + int(df['GamesWon'][ind]) + int(df['GamesDrawn'][ind])
        if total_matches <= 0.0:
            percent_list.append(0)
            continue
        win_percent = (int(df['GamesWon'][ind])*1.0) / total_matches
        percent_list.append(win_percent)

    df["Winning Percent"] = percent_list 
    
def group_teams_by_best_position(df):
    
    position_points = {}

    for ind in df.index:
        position_points[df['BestPosition'][ind]] = int( position_points.get(df['BestPosition'][ind], 0) ) + int(df['Points'][ind])

    return position_points
        

if __name__ == "__main__":
    
    # Question 1
    df = pd.read_csv('Laliga.csv', skiprows=[0])
    nd = replace_dashes(df)
    print(nd)


    # Question 2
    print(filter_on_start(df))

    # Question 3
    print(top_5_teams(nd))

    # Question 4
    print(Goal_diff_count(nd))

    # Question 5
    add_winning_percent_column(nd)
    print(nd)

    # Question 6
    print(group_teams_by_best_position(nd))
    
