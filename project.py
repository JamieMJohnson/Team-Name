import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math

#Import the data
data = pd.read_csv("all_data.csv")

#Scatterplot
sns.scatterplot(data["Life expectancy at birth (years)"], data["GDP"])

#Find a line of best fit using regplot
sns.regplot(x="GDP", y="Life expectancy at birth (years)", data=data, order=5)

plt.show()
plt.clf()

plt.plot(data["Life expectancy at birth (years)"], data["GDP"])
