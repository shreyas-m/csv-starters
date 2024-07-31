import csv
import pandas

# tempratures = []
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for i, datum in enumerate(data):
#         if i == 0:
#             continue
#         tempratures.append(int(datum[1]))
# print(tempratures)

data = pandas.read_csv("weather_data.csv")
temparatures = data['temp'].tolist()
print(temparatures)

print(f"Average temp : {sum(temparatures) / len(temparatures)}")
print(f"Average temp : {data['temp'].mean()}")
print(f"Max temp : {data['temp'].max()}")

print(f"Max temp in week data row: {data[data.temp == data.temp.max()]}")
monday = data[data.day == "Monday"]
print(f"Monday's temp : {(monday.temp[0]*9/5)+32}F ")

data_dict = {
    "Name" : ["Gayatri", "Shreyas", "Tejaswini"],
    "Age" : [36, 33, 30]
}

data_fr = pandas.DataFrame(data_dict)

print(data_fr)

# data_fr.to_csv("sigblings.csv")
