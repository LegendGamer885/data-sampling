import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import csv

df = pd.read_csv("sample-distribution.csv")
data = df["temp"].tolist()

# populationMean = statistics.mean(data)
# populationStDev = statistics.stdev(data)

# print("Mean is :", populationMean)
# print("Standard Deviation is :", populationStDev)

#function to plot the mean on the graph
def showFig(mean_list):
    df = mean_list

    fig = ff.create_distplot([df],["temp"],show_hist=False)
    # fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

#Function to get mean of the given data samples
def randomSetOfMean(counter):
    dataSet=[]

    for i in range (0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)

    Mean = statistics.mean(dataSet)
    return Mean

#To get mean of 100 data points 1000 times and plot the graph
def setup():
    mean_list =[]
    
    for i in range(0,1000):
        setOfMean = randomSetOfMean(100)
        mean_list.append(setOfMean)

    showFig(mean_list)
    mean2 = statistics.mean(mean_list)
    print("Mean2 is :",mean2)
setup()