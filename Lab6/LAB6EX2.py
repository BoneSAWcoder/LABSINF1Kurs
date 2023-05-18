import xml.etree.ElementTree as ET
tree = ET.parse('C:/PyProgs/Lab6/tsstN1.xml') #Парсим
root = tree.getroot()
def ReturnNumber():
    Number = 0
    for Student in root.findall('Students/Student'):
        Number = Number + 1
    return Number
def ReturnName(StudentID):
    STRFORM = "Students/Student[@id='{0}']".format(StudentID)
    for Student in root.findall(STRFORM):
        return Student.find('Surname').text
def RewriteScore(StudentID, ExamName, NewScore):
    print('FuncWork')
    print(StudentID)
    print(ExamName)
    print(NewScore)
    STRFORM = "Students/Student[@id='{0}']".format(StudentID)
    for Student in root.findall(STRFORM):
        for Exam in Student.findall("Exams"):
            Exam.find(ExamName).text = NewScore
            print(Exam.find(ExamName).text)
            tree.write('C:/PyProgs/Lab6/tsstN1.xml',encoding="UTF-8")

        