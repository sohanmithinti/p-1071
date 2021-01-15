import numpy as np
import pandas as pd 
import plotly.express as px
import csv

def getdatasource():
    icecream = []
    temperature = []
    with open("icecreamsales.csv") as f:
        reader = csv.DictReader(f)
        print(reader)
        for row in reader:
            icecream.append(float(row["IcecreamSales"]))
            temperature.append(float(row["Temperature"]))
        print(icecream)
        print(temperature)    
        return {"x":icecream, "y":temperature}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0, 1])

data = getdatasource()
findcorrelation(data)
