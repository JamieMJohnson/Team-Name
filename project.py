import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math

#Import the data
data = pd.read_csv("all_data.csv")

#Take the log of the values
data["log_gdp"] = np.log2(data["GDP"])

#Filter for lower life expectancy
younger_deaths = data[(data["Life expectancy at birth (years)"] < 65)]


#Scatterplot
sns.scatterplot(younger_deaths["Life expectancy at birth (years)"], younger_deaths["log_gdp"])

#Find a line of best fit using regplot
sns.regplot(younger_deaths["Life expectancy at birth (years)"], younger_deaths["log_gdp"], order=3)

plt.show()
plt.clf()

