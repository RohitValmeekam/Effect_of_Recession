import os
import xlrd
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
#Gives a table of each individual data set compared with other data sets to find the highest r-values
tList = []
# Storing data in Lists
skiplist = list(range(0, 10))
numFiles=0
for i in os.listdir("C:/Users/r020v/OneDrive/Desktop/Stats Econ Project files/data"):
    fPath = "C:/Users/r020v/OneDrive/Desktop/Stats Econ Project files/data/" + i
    tList.append(pd.read_excel(fPath, skiprows=skiplist))
    numFiles=numFiles+1

#Setting up the array
b=np.zeros((numFiles+1,numFiles+1),dtype=float)
i=0
a=np.empty(numFiles+1, dtype=float)
while (i+1)<=(numFiles+1):
    a[i]=i
    i+=1
b[0]=a
i=0
for j in b:
    j[0] = i
    i+=1

#r-values
colNames = ["DSPIC96","INDPRO","PAYEMS","RRSFS","HOUST","ALTSALES","UNRATE","SAHMREALTIME", "AWHAE", "BUSINV", "UMCSENT", "RECPROUSM156N","ANXAVS_NEWORDER","ICSA", "DCOILWTICO", "PCEC96", "W875RX1"]
for y in b:
    if y[numFiles] != numFiles:
        x = 1
        while x <= numFiles:
            vals1 = tList[int(b[0][int(x)-1])][['observation_date', colNames[int(b[0][int(x)-1])]]]
            vals2 = tList[int(y[0]-1)][['observation_date', colNames[int(y[0]-1)]]]
            dataframes = [vals1, vals2]
            wt = pd.merge(vals1, vals2, how='inner', on='observation_date')
            if int(b[0][int(x)-1]) == int(y[0]-1):
                r = np.corrcoef(wt[colNames[int(b[0][int(x)-1])]+"_x"], wt[colNames[int(y[0]-1)]+"_y"])
            else:
                r = np.corrcoef(wt[colNames[int(b[0][int(x) - 1])]], wt[colNames[int(y[0] - 1)]])
            if math.isnan(r[0,1])==False:
                y[x]=round(r[0,1],1)
            if math.isnan(r[0,1])==True:
                y[x] = round(99)
            x += 1
np.set_printoptions(linewidth=np.inf)
for y in b:
    np.set_printoptions(linewidth=np.inf)
    print(y)