import csv 
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)

def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)
        mean = statistics.mean(dataSet)
        return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

stdev = statistics.stdev(mean_list)
first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (3*stdev)  

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START")) 
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START")) 
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))  
fig.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))  
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))