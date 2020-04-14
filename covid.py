import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("dati_covid.csv")
x=df["giorno"]
day=int(x[-1:].values)
colors=["red", "green", "black", "yellow"]
pred=[]

def regressor(x):
    return slope*x+intercept

for i in range(4):
    y=df.iloc[:, i+2]
    last=int(y[-1:].values)
    model=np.poly1d(np.polyfit(x,y,3))
    line=np.linspace(min(x), max(x))
    
    plt.figure(num="PREVISIONI COVID 14 APRILE 2020", figsize=(10,4))
    plt.subplot(1,2,2)
    plt.scatter(x,y, color=colors[i], alpha=0.5)
    plt.plot(line, model(line), color=colors[i])
    pred.append(model(day+1))
    plt.axvline(day+1)
    plt.scatter(day+1, pred[-1:], color="blue")
    
    result=int(pred[i]-last)
    plt.subplot(12,2, 2*i+1)
    plt.axis("off")
    plt.text(0,0,f"{df.columns[i+2].capitalize()}: {int(pred[i])}")
    if result>=0:
        plt.text(0.4,0,f"[+{result}]")
    else:
        plt.text(0.4,0,f"[{result}]")
    print(f"{df.columns[i+2].capitalize()} previsti il 14 aprile 2020:\t{int(pred[i])}")
plt.show()