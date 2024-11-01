
import pandas as pd
import os

import Q2 as Q2

def test_fn():

    assert Q2.monthly_returns is not None, "No DataFrame called monthly_returns"
    assert type(Q2.monthly_returns) == pd.core.frame.DataFrame, "monthly_returns is not a pandas DataFrame"

    assert 'Mkt' in Q2.monthly_returns.columns, "monthly_returns has no column named 'Mkt'"
    assert 'Year' in Q2.monthly_returns.columns, "monthly_returns has no column named 'Year'"
    assert 'Month' in Q2.monthly_returns.columns, "monthly_returns has no column named 'Month'"

    assert Q2.summary_stats is not None, "No DataFrame called summary_stats"
    assert type(Q2.summary_stats) == pd.core.frame.DataFrame, "summary_stats is not a pandas DataFrame"

    tst = (1.1**12-1,0.1*12**0.5)
    assert (Q2.annualise(.1, .1)==tst), "error in annualisation function"

    assert os.path.exists('summary_stats.csv'), "Can't find a 'summary_stats.csv' file"

    sds = [2.22264175, 4.73187345, 5.54334322]
    assert pd.Series(sds).sum().round(4)==Q2.GMS.sum().round(4), "GMS values appear incorrect"