import pandas as pd
import numpy as np

data = pd.read_csv('data/data.csv', sep=',')

data = data[(data['radius'] > 0) & (data['star_radius'] > 0) & (data['mass'] > 0) & (data['star_mass'] > 0)]

