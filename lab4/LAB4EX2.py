import datetime
from prettytable import PrettyTable
import json
with open ('C:/PyProgs/Lab4/ApartmentsData.json', 'r', encoding = "utf-8") as j:
    json_data = json.load(j)

#1
print('#1')
InputSum = 50000000 
for Apartments in json_data['apartments']:
    if int(Apartments["cost"]) > InputSum:
        print(Apartments["address"])

#2
print('#2')
District = 'tekstilshiki'
AllCost = float()
AllSquare = float() 
for Apartments in json_data['apartments']:
    if Apartments["district"] ==  District:
        AllCost = AllCost + float(Apartments["cost"])
        AllSquare = AllSquare + float(Apartments["square"])
print(AllCost/AllSquare)
#3
print('#3')
for Apartments in json_data['apartments']:
    if (int(Apartments["floor"]) == 2) and (float(Apartments["square"]) > 40):
        print(Apartments["address"])
#4
print('#4')
for Apartments in json_data['apartments']:
    DatePost = datetime.datetime.strptime(Apartments['DateOfPlacement'], '%d.%m.%Y').year
    if DatePost == datetime.datetime.now().year - 1:
        print(Apartments["address"])
        