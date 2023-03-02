import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.head(5))

#Suppressing name column
sup_df = df.drop('Name',axis="columns")
print(sup_df.head(5))

#Suppressing rows where Speed > 70
sup_df = sup_df.drop(sup_df[sup_df.Speed > 70].index)
print(sup_df.head(5))

#Masking Type 1
sup_df['Type 1'] = 'XXXXX'
print(sup_df.head(5))

#Masking Type 2
sup_df['Type 2'] = '*****'
print(sup_df.head(5))