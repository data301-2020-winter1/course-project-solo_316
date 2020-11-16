import pandas as pd
import numpy as np
import seaborn as sns
def load_and_process(url):
    df =(
    pd.read_csv(url)
    .dropna()
    .loc[lambda x: x['workclass'] != '?']
    .loc[lambda x: x['occupation'] != '?']
    .loc[lambda x: x['native.country'] != '?']
    .drop(['capital.gain','capital.loss','education.num','fnlwgset'],axis = 1)

    )
    return df 