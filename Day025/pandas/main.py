# with open("weather_data.csv", mode="r") as weather_data:
#     weather = weather_data.readlines()
# print(weather)

# import csv
#
# with open("weather_data.csv", mode="r") as weather_data:
#     weather = csv.reader(weather_data)
#     temperatures = []
#     print(weather)
#     for row in weather:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

# weather_data = pandas.read_csv("weather_data.csv")
# print(weather_data)
# temps = weather_data["temp"]
# temp_list = temps.to_list()
# print(temps)
# print(temp_list)
# print(sum(temps)/len(temps))
# print(f"Mean: {temps.mean()}")
# print(f"High: {temps.max()}")
# print(weather_data[weather_data.day == "Monday"])
# print(weather_data[weather_data.temp == weather_data.temp.max()])
# print(weather_data[weather_data.day == "Monday"].temp * 9 / 5 + 32)

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_df = pandas.DataFrame({'Fur Color': ['Gray', 'Cinnamon', 'Black'],
                                'Count': [len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]),
                                          len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]),
                                          len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
                                          ]})
squirrel_df.to_csv("squirrel_count.csv")
