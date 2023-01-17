import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math

#Import the data
data = pd.read_csv("all_data.csv")

#Scatterplot
sns.scatterplot(data["Life expectancy at birth (years)"], housing_sub["GDP"], alpha = 0.2)
