import xml.etree.ElementTree as ET

class student():
    Surname = str()
    Math = int()
    Infa = int()
    RusLang = int()
    def __init__(self, IDS):
        tree = ET.parse('C:/PyProgs/Lab3/tsst.xml') #Парсим
        root = tree.getroot() #Присваеваем Адрес
        STRFORM = "Students/Student[@id='{0}']".format(IDS) #Форматируем строку для поиска
        for student in root.findall(STRFORM): #Ищем
            self.Surname = student.find('Surname').text
            for exam in student.findall("Exams"): #Ищем в подкатологе Exams
                self.Math = int(exam.find('Math').text)
                self.Infa = int(exam.find('Inform').text)
                self.RusLang = int(exam.find('RusLang').text)
    def MidScore(self):
        return((self.Math + self.Infa + self.RusLang)//3)
    def MaxScore(self):
        List = [self.Math, self.Infa, self.RusLang]
        return (max(List))
    def MinScore(self):
        List = [self.Math, self.Infa, self.RusLang]
        return (min(List))
    def Summary(self):
        return int(self.Math + self.Infa + self.RusLang)

Stud1 = student(1)
Stud2 = student(2)
Stud3 = student(3)
Stud0 = [Stud1, Stud2, Stud3]
for i in range(0,2):
    print(Stud0[i].Surname,':')
    print('Средний Балл: ', Stud0[i].MidScore())
    print('Макс. Балл: ', Stud0[i].MaxScore())
    print('Мин. Балл: ', Stud0[i].MinScore())
print('Абитуриенты with 250+ баллов:')
for i in range(0,2):
    if Stud0[i].Summary() > 250:
        print(Stud0[i].Surname)
print('Абитуриенты with 50+ баллов по каждому экзамену:')
for i in range(0,2):
    if (Stud0[i].Math > 50) and (Stud0[i].RusLang > 50) and (Stud0[i].Infa > 50):
        print(Stud0[i].Surname)
