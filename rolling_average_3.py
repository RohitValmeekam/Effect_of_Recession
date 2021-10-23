#Advance Real Retail and Food Services Sales
import os
import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

tList = []
# to run this code effectively, my_path must be changed to wherever the data is on your computer
my_path="C:/Users/r020v/PycharmProjects/pythonProject/data/"
colNames = ["DSPIC96","INDPRO","PAYEMS","RRSFS","HOUST","ALTSALES","UNRATE","SAHMREALTIME", "AWHAE", "BUSINV", "UMCSENT", "RECPROUSM156N","ANXAVS_NEWORDER","ICSA", "DCOILWTICO", "PCEC96", "W875RX1"]
# Storing data in Lists
skiplist = list(range(0, 10))
for i in os.listdir(my_path):
    fPath = my_path + i
    tList.append(pd.read_excel(fPath, skiprows=skiplist))
df = tList[3]
df_1 = df[colNames[3]]
df2 = tList[11]
df2_1 = df2[colNames[11]]

# rolling average
roll = np.convolve(df_1, np.ones(12),'same')/12
roll2= np.convolve(roll, np.ones(12),'same')/12

dates=np.arange(0,162)
m, b = np.polyfit(dates, roll, 1)
# r-value
df_1_roll = roll-m*dates+b
df_1_roll2 = df_1_roll/np.max(df_1_roll)
r = np.corrcoef(df_1_roll,df2_1[0:162])
print(roll[0:16])
#print(df_1_roll[0:16]/np.max(df_1_roll))
dates2=df['observation_date']
# Plot
plt.plot(dates2,df2_1[0:162]/np.max(df2_1[0:162]),'o')
plt.title(colNames[3])
plt.xlabel('observation_date')
plt.ylabel('Advance Real Retail and Food Services Sales')
plt.plot(dates2[6:-6],df_1_roll2[6:-6])
#plt.scatter(df["observation_date"], roll2)
plt.show()

