import matplotlib.pyplot as plt
import json

    
with open ('C:/PyProgs/Lab5/Data.json', 'r', encoding = "utf-8") as j:
    json_data = json.load(j)

#Выбор 
ChYear = '2012'

EmplList = list()
PayValuesMidList = list()
for Employs in json_data['staff']:
    PaySum = int()
    Years = int()
    for Payments in Employs['Payments']:
        if ChYear == Payments['Year']:
            PaySum = PaySum + int(Payments['Payment value'])
            Years = Years + 1
    if Years != 0:
        PayValuesMidList.append(PaySum/Years)
        EmplList.append(Employs["FIO"])
print(EmplList)
print(PayValuesMidList)
plt.pie(PayValuesMidList, labels = EmplList)
plt.show()
