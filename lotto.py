# importing necessary package
import pandas as pd

# Mav number of different types of cards requested
games = 3

# Reading scratch ticket data from website into a dataframe
df = pd.read_csv('https://www.texaslottery.com/export/sites/' \
                 'lottery/Games/Scratch_Offs/scratchoff.csv',
                 header=1,
                 usecols=lambda x: x != 'Game Close Date',
                 skipinitialspace=True)

# Excluding Total column, converting to int, and converting claimed to int
df = df[df['Prize Level'] != 'TOTAL']
df['Prize Level'] = pd.to_numeric(df['Prize Level'])
df['Prizes Claimed'] = df['Prizes Claimed'].fillna(0).astype(int)

# Setting index to better organize data
df = df.set_index(['Game Number', 'Prize Level'])

# Creating Claim % as target variable
df['Claim %'] = (df['Prizes Claimed']/df['Total Prizes in Level']*100).round(2)

# Finding the smallest medians
median = df['Claim %'].groupby('Game Number').median().sort_values()[:games]

# Printing the claims in a clean way
for i in range(games):
    print(df[df.index.get_level_values(0) == median.index[i]])