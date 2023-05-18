import matplotlib.pyplot as plt
import json

    
with open ('C:/PyProgs/Lab5/Data.json', 'r', encoding = "utf-8") as j:
    json_data = json.load(j)

#Выбор 
ChNum = 12
ChYear = '2012'

PayMonthNums = []
PayValues = []
for Employs in json_data['staff']:
        if int(Employs['Number']) == ChNum:
            for Payments in Employs['Payments']:
                if ChYear == Payments['Year']:
                    PayMonthNums.append(int(Payments['Month']))
                    PayValues.append(int(Payments['Payment value']))

plt.bar(PayMonthNums ,PayValues ,width = 0.4, color = 'green', edgecolor= 'black')
plt.xlabel('Год') 
plt.ylabel('Количество') 
plt.legend()
plt.show()
