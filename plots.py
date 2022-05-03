import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('kc_house_data.csv')


bedrooms = data['bedrooms'].hist()
plt.show(bedrooms)