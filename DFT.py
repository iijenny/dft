#Discrete Fourier Transform

import pandas as pd
import cmath

# Import the data:
data = pd.read_excel("C:\Projekty\l64_2007.xlsx")
data.columns = ["Date", "Number"]

# Change column type & sum by date:
data["Date"] = pd.to_datetime(data["Date"])
group_data = data.groupby(data["Date"].dt.date).sum()

# N - total rows
N = group_data.shape[0]

# DFT function slow version - function before computation into two parts
def DFT(x):
    receive_data = []
    for k in range(N):
        X = 0
        for n in range(N):
            X += x[n] * cmath.exp((-2j*cmath.pi*k*n )/N)
            receive_data.append(X)
    return receive_data

output = str(DFT(group_data.Number))
file = open("result.txt","w")
file.writelines(output)
file.close()