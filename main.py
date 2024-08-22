import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict ={
    "fur color":["GRAY","CINNAMON","BLACK"],
    "count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}
df=pd.DataFrame(data_dict)
df.to_csv("squrrel_count.csv")










