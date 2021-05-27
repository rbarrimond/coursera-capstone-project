import pandas as pd
import os
import pickle

df = pd.DataFrame()
with pd.ExcelWriter('tables.xlsx') as writer:
    for f in [ 'fsa_df.pkl', 'toronto_venue.pkl', 'restaurants.pkl', 'asian_restaurants.pkl' ]:
        df = pd.read_pickle(f)
        df.to_excel(writer, sheet_name=f)
