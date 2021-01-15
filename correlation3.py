import numpy as np
import pandas as pd 
import plotly.express as px
import csv

def getdatasource():
    height = []
    weight = []
    with open("height-weight.csv") as f:
        reader = csv.DictReader(f)
        print(reader)
        for row in reader:
            height.append(float(row["Height(Inches)"]))
            weight.append(float(row["Weight(Pounds)"]))
        print(height)
        print(weight)    
        return {"x":height, "y":weight}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0, 1])

data = getdatasource()
findcorrelation(data)
