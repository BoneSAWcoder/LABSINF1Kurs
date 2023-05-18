import xml.etree.ElementTree as ET
tree = ET.parse('C:/PyProgs/Lab6/tsstN1.xml') #Парсим
root = tree.getroot()
def AddStudent(Id, Surname, MathScore, InfaScore, LangScore):
    print('1')
    Student = ET.Element('Student')
    Student.set("id",Id)
    print('2')
    ET.SubElement(Student, "Surname").text = Surname
    Exams = ET.SubElement(Student,"Exams")
    ET.SubElement(Exams, "Math").text = MathScore
    ET.SubElement(Exams, "RusLang").text = LangScore
    ET.SubElement(Exams, "Inform").text = InfaScore
    root.find("Students").append(Student)
    print('3')
    tree.write("C:/PyProgs/Lab6/tsstN1.xml",encoding="UTF-8")
