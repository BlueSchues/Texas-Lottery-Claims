# importing necessary package
import pandas as pd

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

# Creating Claim % as target variable
df['Claim %'] = (df['Prizes Claimed']/df['Total Prizes in Level']*100).round(2)