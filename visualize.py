# importing neccessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing data from lotto script
from lotto import df

fig, ax = plt.subplots()

games = list(df['Game Number'].unique())
game = df[df['Game Number'] == games[-1]]

ax.bar(game['Prize Level'], game['Claim %'])
ax.set(xlim=(0,100), ylim=(0,100))
print(game['Claim %'].head())
plt.show()