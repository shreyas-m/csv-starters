import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = {"Fur colour":[], "Count":[]}
for color in data['Primary Fur Color'].unique():
    data_dict['Fur colour'].append(color)
    data_dict['Count'].append(data[data['Primary Fur Color'] == color]['Primary Fur Color'].count())

pandas.DataFrame(data_dict).to_csv("Analysis.csv")
