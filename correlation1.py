import numpy as np
import pandas as pd 
import plotly.express as px
import csv

def getdatasource():
    Coffee = []
    hours = []
    with open("coffe.csv") as f:
        reader = csv.DictReader(f)
        print(reader)
        for row in reader:
            Coffee.append(float(row["Coffee"]))
            hours.append(float(row["hours"]))
        print(Coffee)
        print(hours)    
        return {"x":Coffee, "y":hours}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0, 1])

data = getdatasource()
findcorrelation(data)
