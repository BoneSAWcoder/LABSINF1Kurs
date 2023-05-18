import matplotlib.pyplot as plt
import json

class Payment():
    def __init__(self, Year, Month, Value):
        self.Year = Year
        self.Month = int(Month)
        self.Value = float(Value)

class Employ():
    def __init__(self, Number, Fio, Department):
        self.Number = Number
        self.Fio = Fio
        self.Department = Department
    def CreatePay(self, Year, Month, Value):
        self.Paymentlist = []
        self.Paymentlist.append(Payment(Year, Month, Value))
    def AllMnth(self):
        for x in self.Paymentlist:
            print(x)
            NumMonthList = []
            NumMonthList.append(x.Month)
            print(x.Month)
        return NumMonthList
    def AllValue(self):
        for x in self.Paymentlist:
            NumValueList = []
            NumValueList.append(x.Value)
        return NumValueList
    
with open ('C:/PyProgs/Lab5/Data.json', 'r', encoding = "utf-8") as j:
    json_data = json.load(j)

EmployList = []
i = 0

for Employs in json_data['staff']:
    EmployList.append(Employ(Employs['Number'], Employs['FIO'], Employs['Department']))
    for Payments in Employs['Payments']:
        EmployList[i].CreatePay(Payments['Year'], Payments['Month'], Payments['Payment value'])
    i = i + 1


#выбор сотрудника и года
ChEmpl = 0

print(EmployList[ChEmpl].AllMnth())
print(EmployList[ChEmpl].AllValue())

plt.bar(EmployList[ChEmpl].AllMnth(), EmployList[ChEmpl].AllValue(), width = 0.4, color = 'green', edgecolor = 'black')
plt.xlabel('Год') 
plt.ylabel('Количество') 
plt.legend()
plt.show()