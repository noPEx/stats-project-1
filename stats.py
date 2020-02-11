import pandas as pd
import numpy as np


def replace_dashes(df):
    """
    Replaces - with 0
    returns nd
    """

    nd = df.replace('-', 0)
    return nd


if __name__ == "__main__":
    
    # Question 1
    df = pd.read_csv('Laliga.csv')
    nd = replace_dashes(df)
    print(nd)
