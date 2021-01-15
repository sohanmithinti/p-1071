import csv
from collections import Counter
import pandas as pd 
import plotly.express as px
import math

with open ("class2.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

a = len(file_data)

total = 0

for i in file_data:
    total = total + float(i[1]) 

mean = total//a

print(mean)

stdd = []

for s in file_data:
    x = int(s[1]) - mean
    x = x**2
    stdd.append(x)
sum = 0
for o in stdd:
    sum = sum + o

result = sum//(a-1)

std_d = math.sqrt(result)

print(std_d)    

dataFrame2 = pd.read_csv("class2.csv")
scattergraph = px.scatter(dataFrame2, x = "Student Number", y = "Marks",  title = "Marks Percentage")
scattergraph.update_layout(shapes = [
    dict(
        type = "line",
        x0 = 0,
        y0 = mean,
        x1 = total,
        y1 = mean
    )
])
scattergraph.update_yaxes(rangemode = "tozero")
scattergraph.show()