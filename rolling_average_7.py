#Unemployment Rate
import os
import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

tList = []
colNames = ["DSPIC96","INDPRO","PAYEMS","RRSFS","HOUST","ALTSALES","UNRATE","SAHMREALTIME", "AWHAE", "BUSINV", "UMCSENT", "RECPROUSM156N","ANXAVS_NEWORDER","ICSA", "DCOILWTICO", "PCEC96", "W875RX1"]
# Storing data in Lists
skiplist = list(range(0, 10))
for i in os.listdir("C:/Users/r020v/OneDrive/Desktop/Stats Econ Project files/data"):
    fPath = "C:/Users/r020v/OneDrive/Desktop/Stats Econ Project files/data/" + i
    tList.append(pd.read_excel(fPath, skiprows=skiplist))
df = tList[6]
df_1 = df[colNames[6]]
df2 = tList[11]
df2_1 = df2[colNames[11]]

# rolling average
roll = np.convolve(df_1, np.ones(12),'same')/12
roll2= np.convolve(roll, np.ones(6),'same')/6

dates=np.arange(0,163)
m, b = np.polyfit(dates, roll, 1)
# r-value
df_1_roll = roll-m*dates+b
r = np.corrcoef(df_1_roll,df2_1[0:163])


# Plot
plt.plot(df['observation_date'],df2_1[0:163]/np.max(df2_1[0:163]),'o')
plt.title(colNames[6])
plt.xlabel('observation_date')
plt.ylabel('Unemployment Rate')
plt.plot(df['observation_date'],df_1_roll/np.max(df_1_roll))
#plt.scatter(df["observation_date"], roll2)
plt.show()

