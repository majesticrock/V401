import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

werte = csv_read("csv/messung1.csv")

data1 = np.zeros(10)
data2 = np.zeros(10)
data3 = np.zeros(10)

i=0
for values in werte:
    data1[i] = float(values[0])
    data2[i] = float(values[1])
    data3[i] = float(values[2])
    i+=1

data4 = data1 / 5.017


data5 = 2 * data4 / data3 #Wellenlänge direkt
data6 = 2 * data2 / data3 #Wellenlänge mit gerundeten Werten
print(data5*1000000)
#print(data6*1000000)
print(np.mean(data5)*1000000)
print(np.std(data5, ddof=1) / np.sqrt(len(data5))*1000000)