import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("dati_covid.csv")    #I dati sono la data, giorni passati dal primo dato, i casi totali, i morti i guariti e i casi attualmente attivi
x=df["giorno"]
day=int(x[-1:].values)
colors=["red", "green", "black", "yellow"]
pred=[]

def regressor(x):
    return slope*x+intercept

for i in range(4):
    y=df.iloc[:, i+2]
    model=np.poly1d(np.polyfit(x,y,3))
    line=np.linspace(min(x), max(x))
    
    plt.figure(num="PREVISIONI COVID 14 APRILE 2020", figsize=(10,4))
    plt.subplot(1,2,2)
    plt.scatter(x,y, color=colors[i], alpha=0.5)
    plt.plot(line, model(line), color=colors[i])
    pred.append(model(day))
    
    plt.subplot(12,2, 2*i+1)
    plt.axis("off")
    plt.text(0,0,f"{df.columns[i+2].capitalize()}: {int(pred[i])}")
    print(f"{df.columns[i+2]} previsti il 14 aprile 2020: {int(pred[i])}")
plt.show()