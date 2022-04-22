import plotly.express as px
import csv
import numpy as np
#co
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    marks_percentage = []
    present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_percentage.append(float(row["Marks In Percentage"]))
            present.append(float(row["Days Present"]))

    return {"x" : marks_percentage, "y": present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in Percentage and Days Present is ",correlation[0,1])

def setup():
    data_path  = "marks.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()