class Client():
    def __init__(self, Surname, Name, Age, Balance):
        self.Surname = Surname
        self.Name = Name
        self.Age = Age
        self.__Balance = Balance
    def GetInfo(self):
        print(self.Surname)
        print(self.Name)
        print(self.Age)
        print(self.__Balance)
    def __ChangeBalance(self, Money, type):
        if type == 0:
            self.__Balance = self.__Balance + Money
        elif type == 1:
            self.__Balance = self.__Balance - Money
    def __CheckChange(self, Value, type):
        if self.__Balance >= Value:
            self.__ChangeBalance(Value, type)
        else: 
            print('no way')
#InterfaceВроде
    def Transaction(self, MoneyValue):
        Tran = TransAction(MoneyValue)
        #Комиссия
        self.__CheckChange(Tran.ComissionProcess(0.1), 1)
    def GetMoney(self, MoneyValue):
        self.__CheckChange(MoneyValue, 1)
    def SetMoney(self, MoneyValue):
        self.__CheckChange(MoneyValue, 0)
class TransAction():
    def __init__(self, value):
        self.value = value
    def ComissionProcess(self, Comission):
        return self.value + (self.value * Comission)
    
#Операции
Person1 = Client('Glorbo', 'Florbo', 31, 99999)
Person1.GetInfo()
Person1.GetMoney(100)
Person1.GetInfo()
Person1.SetMoney(1000)
Person1.GetInfo()
Person1.Transaction(3500)
Person1.GetInfo()
