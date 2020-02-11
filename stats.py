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

if __name__ == "__main__":
    
    # Question 1
    df = pd.read_csv('Laliga.csv', skiprows=[0])
    nd = replace_dashes(df)
    print(nd)


    # Question 1
    print(filter_on_start(df))
