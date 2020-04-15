import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

title="PREVISIONE DATI COVID 15 APRILE"
df=pd.read_csv("dati_covid.csv")
x=df["giorno"]
day=int(x[-1:].values)
colors=["red", "green", "purple", "yellow"]
pred=[]

def regressor(x):
    return slope*x+intercept

for i in range(4):
    j=i
    while (j+1)>len(colors):
        j-=len(colors)
    with plt.style.context("dark_background"):
        y=df.iloc[:, i+2]
        last=int(y[-1:].values)
        model=np.poly1d(np.polyfit(x,y,3))
        line=np.linspace(min(x), max(x))

        plt.figure(num=title, figsize=(10,5))
        plt.subplot(1,2,2)
        plt.scatter(x,y, color=colors[j], alpha=0.25)
        plt.plot(line, model(line), color=colors[j])
        pred.append(model(day+1))
        plt.axvline(day+1)
        plt.scatter(day+1, pred[-1:], color="blue")

        result=int(pred[i]-last)
        if i==0:
            plt.subplot(12,2,1)
            plt.text(0,0,title, fontsize=11)
            plt.axis("off")
        plt.subplot(12,2, 2*i+3)
        plt.axis("off")
        plt.text(0,0,f"{df.columns[i+2].capitalize()}: {int(pred[i])}",bbox=dict(facecolor=colors[j], alpha=0.5))
        if result>=0:
            plt.text(0.4,0,f"[+{result}]")
        elif i==3 and result<0:
            plt.text(0.4,0,f"[{result}]", c="green")
        else:
            plt.text(0.4,0,f"[{result}]", c="red")
        print(f"{df.columns[i+2].capitalize()} previsti il 14 aprile 2020:\t{int(pred[i])}")
plt.show()