import xml.etree.ElementTree as ET

class SubjectClass():
    def __init__(self, name, Tasks, TD):
        self.Name = name
        self.Task = int(Tasks)
        self.TaskDone = int(TD)
        print(self.TaskDone)

class student():
    Surname = str()
    Midame = str()
    ID = str()
    SubjectList = []
    def __init__(self, name, surname, midname, ID):
        self.Name = name
        self.Surname = surname
        self.Midame = midname
        self.ID = ID
        self.SubjectList = []

class group():
    def __init__(self, Name):
        self.Name = Name
        self.GroupList = []

tree = ET.parse('C:/PyProgs/Lab3/tsst2.xml')
root = tree.getroot()
SuperList = [group(Groups.get("GNum")) for Groups in root.findall("Groups/Group")]
for GroupObj in SuperList:
    Formattext = "Groups/Group[@GNum='{0}']/Student".format(GroupObj.Name)
    GroupObj.GroupList = [student(Students.get("name"), Students.get("surname"), Students.get("midname"), Students.get("ID")) for Students in root.findall(Formattext)]
    for StudObj in GroupObj.GroupList:
        Formattext2 = "Groups/Group[@GNum='{0}']/Student[@ID='{1}']/Subject".format(GroupObj.Name, StudObj.ID)
        StudObj.SubjectList = [SubjectClass(Subjects.get('SName'), Subjects.find("Tasks").text, Subjects.find("Tasks_Done").text) for Subjects in root.findall(Formattext2)]
print('3')
for GroupObj in SuperList:
    print(GroupObj.Name,': ')
    for Studobj in GroupObj.GroupList:
        Counter = 0
        for GroupObj2 in SuperList:
            for Studobj2 in GroupObj2.GroupList:
                if (StudObj.Surname == Studobj2.Surname) and ((GroupObj.Name != GroupObj2.Name) or (StudObj.ID != Studobj2.ID)) :
                    print(StudObj.Surname, Studobj2.Surname)
                    Counter = Counter + 1
        print(Studobj.Surname, Studobj.Name, Studobj.Midame, Counter)
