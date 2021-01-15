import numpy as np
import pandas as pd 
import plotly.express as px
import csv

def getdatasource():
    size = []
    time = []
    with open("tv.csv") as f:
        reader = csv.DictReader(f)
        print(reader)
        for row in reader:
            size.append(float(row["Size of TV"]))
            time.append(float(row["	Average time spent watching TV in a week (hours)"]))
        print(size)
        print(time)    
        return {"x":size, "y":time}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0, 1])

data = getdatasource()
findcorrelation(data)
