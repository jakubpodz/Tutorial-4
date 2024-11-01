
import pandas as pd
import os

import Q1 as Q1

def test_fn():

    islands = ['Torgersen', 'Dream', 'Biscoe']
    islands.sort()
    species = ['Adelie', 'Chinstrap', 'Gentoo']
    species.sort()

    assert Q1.penguins is not None, "Can't find a DataFrame called penguins"
    assert type(Q1.penguins) == pd.core.frame.DataFrame, "penguins is not a pandas DataFrame"

    for spec in species:
        for island in islands:
            fn = spec + "_" + island + ".csv"
            assert os.path.exists(fn), "Can't find a " + fn + " file"

    assert Q1.body_mass is not None, "Can't find a DataFrame called body_mass"
    assert type(Q1.body_mass) == pd.core.frame.DataFrame, "Penguins is not a pandas DataFrame"
    assert (Q1.body_mass.columns.sort_values() == islands).all(), 'body_mass columns not set correctly'
    assert (Q1.body_mass.index.sort_values() == species).all(), 'body_mass index not set correctly'

    assert Q1.heaviest == ('Gentoo', 'Biscoe'), 'Incorrect subset of penguins identified.'