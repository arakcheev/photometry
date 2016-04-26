import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

JUP_SUN_RADII = 0.102792236

data = pd.read_csv('data/data.csv', sep=',')

data = data[(data['radius'] > 0) & (data['star_radius'] > 0) & (data['mass'] > 0) & (data['star_mass'] > 0)]

data['rr'] = data.apply(lambda row: round(row['radius'] / row['star_radius'] * JUP_SUN_RADII, 2), axis=1)

grouped = data.groupby(['rr'], sort=True)

print grouped['rr'].count()
# f, ax = plt.subplots(figsize=(6, 15))

# data = sns.load_dataset(data).sort_values("rr", ascending=False)
sns.distplot(grouped['rr'].count())
plt.show()

# print (data['radius']/ data['star_radius'])

# plt.plot(data['rr'])
# plt.show()
