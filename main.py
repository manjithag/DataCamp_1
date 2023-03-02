import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.head(5))

sup_df = df.drop('Name',axis="columns")
print(sup_df.head(5))

sup_df = sup_df.drop(sup_df[sup_df.Speed > 70].index)
print(sup_df.head())