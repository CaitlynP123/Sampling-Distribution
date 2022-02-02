import plotly.figure_factory as ff
import statistics
import random
import pandas as pd

df = pd.read_csv("C:/Users/C/OneDrive/Desktop/Coding/python/Normal Distribution/medium_data.csv")
data = df["reading_time"].tolist()

popMean = statistics.mean(data)
print("Population Mean =", popMean)

def randSetMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex= random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans= randSetMean(30)
        meanList.append(setOfMeans)
    showFig(meanList)
    print("Sampling Mean =", statistics.mean(meanList))
setup()

