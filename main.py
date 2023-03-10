import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('pokemon_data.csv')
print(df.head(5))

## Suppressing name column
sup_df = df.drop('Name',axis="columns")
print(sup_df.head(5))

## Suppressing rows where Speed > 70
sup_df = sup_df.drop(sup_df[sup_df.Speed > 70].index)
print(sup_df.head(5))

## Masking Type 1
sup_df['Type 1'] = 'XXXXX'
print(sup_df.head(5))

## Masking Type 2
sup_df['Type 2'] = '*****'
print(sup_df.head(5))

## Define function
def doubler(x):
    return 2*x

## Applying a function
sup_df['Double Speed'] = sup_df['Speed'].apply(doubler)
print(sup_df.head(5))

sup_df['Trible Attack'] = sup_df['Attack'].apply(lambda x:x*3)
print(sup_df.head(10))

#sup_df['Leg'] = sup_df['Legendary'].apply(lambda s:s[0]+'ABC'+s[s.find('S'):])
#print(sup_df.head(5))

## Plotting a histogram
sup_df['Double Speed'].hist(bins=140)
plt.xlabel('Double Speed')
plt.ylabel('Frequency')
plt.title('Histogram for Double Speed')
plt.show()

## Generalization
sup_df['Double Speed'] = sup_df['Double Speed'].apply(lambda x: '>=80' if x>=80 else '<80')
print(sup_df.head(10))

## Bottom coding
sup_df['Trible Attack'].hist(bins=140)
plt.xlabel('Trible Attack')
plt.ylabel('Frequency')
plt.show()

print(sup_df[sup_df['Trible Attack'] < 50])
sup_df.loc[sup_df['Trible Attack'] < 50,'Trible Attack'] = 49
print(sup_df[sup_df['Trible Attack'] < 50])

sup_df['Trible Attack'].hist(bins=140)
plt.xlabel('Trible Attack')
plt.ylabel('Frequency')
plt.show()

## Top Coding
print(sup_df[sup_df['Trible Attack']>400])
sup_df.loc[sup_df['Trible Attack'] > 400 , 'Trible Attack'] = 401
print(sup_df[sup_df['Trible Attack']>400])

sup_df['Trible Attack'].hist(bins=140)
plt.xlabel('Trible Attack')
plt.ylabel('Frequency')
plt.show()

sup_df.to_csv('Annonymised_data')
