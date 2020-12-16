from pandas import DataFrame, Series
from typing import List
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def features_with_nans(df: DataFrame) -> List:
    missings = df.isnull().mean().sort_values(ascending=False)
    fwn = missings[missings > 0] # features_with_nan
    return fwn.index.tolist()


def missing_values_info(df: DataFrame) -> DataFrame:
    fwn = features_with_nans(df)
    if len(fwn) == 0:
        return None
    m = df[fwn].isnull().mean()
    mdf = pd.DataFrame(data=m, columns=['rate'])
    mdf.rate = 100 * mdf.rate.round(5)
    mdf['missings'] = df[mdf.index].isnull().sum()
    mdf['non_empty'] = \
        np.array([df[feature].value_counts().sum() for feature in mdf.index])
    mdf['mode_value'] = df[mdf.index].mode().loc[0]
    mdf['mode_count'] = \
        np.array([np.sort(df[feature].value_counts())[-1] for feature in mdf.index])
    mdf['uniques'] = np.array([len(df[x].unique()) - 1 for x in mdf.index])
    # mdf['variance'] = df[mdf.index].var().round(5)
    return mdf