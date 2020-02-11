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
    
