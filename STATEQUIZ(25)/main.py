import pandas as pd
import csv

df = pd.read_csv("D:/안도윤/2. 3월/vscode/python100project/DAY25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df.info()
grey = len(df[df["Primary Fur Color"] == "Gray"])
red = len(df[df["Primary Fur Color"] == "Cinnamon"])
black = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, red, black]
}

df_1 = pd.DataFrame(data_dict)
print(df_1)
df_1.to_csv("D:/안도윤/2. 3월/vscode/python100project/DAY25/squirrel_count.csv")
