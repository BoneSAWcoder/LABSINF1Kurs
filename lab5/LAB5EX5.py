import matplotlib.pyplot as plt
import json

    
with open ('C:/PyProgs/Lab5/Data.json', 'r', encoding = "utf-8") as j:
    json_data = json.load(j)

#Выбор 
ChYear = '2012'

EmplList = list()
PayValuesMaxList = list()
PayValuesMinList = list()
for Employs in json_data['staff']:
    PayValuesList = list()
    Years = int()
    for Payments in Employs['Payments']:
        if ChYear == Payments['Year']:
            PayValuesList.append(int(Payments['Payment value']))
            Years = Years + 1
    if Years != 0:
        PayValuesMaxList.append(max(PayValuesList))
        PayValuesMinList.append(min(PayValuesList))
        EmplList.append(Employs["FIO"])
print(EmplList)


width = 0.4
plt.bar([x-width/2 for x in range(0, len(EmplList))],PayValuesMaxList , width, color = 'green', edgecolor = 'black')
plt.bar([x+width/2 for x in range(0, len(EmplList))],PayValuesMinList, width, color = 'red', edgecolor = 'black')
plt.xticks([x for x in range(0, len(EmplList))], EmplList)
plt.xlabel('Cотрудники') 
plt.ylabel('Количество') 
plt.legend()
plt.show()