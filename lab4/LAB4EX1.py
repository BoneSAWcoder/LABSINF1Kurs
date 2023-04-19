from prettytable import PrettyTable
import json
with open ('C:/PyProgs/Lab4/JsonFile.json', 'r', encoding = "utf-8") as j:
    json_data = json.load(j)

#1
count = 0
for comps in json_data["content"]["universalCompetencyRows"]:
    count = count + 1
print (count)

#2
ProfStandarts = PrettyTable()
ProfStandarts.field_names = ["ID", "Competition"]
for comps in json_data["content"]["professionalStandards"]:
    ID = comps["id"]
    Content = comps["content"]
    ProfStandarts.add_row([ID, Content])
print(ProfStandarts)

#3
UniversalCompetition = PrettyTable()
UniversalCompetition.field_names = ["ID", "Competition"]
for comps in json_data["content"]["universalCompetencyRows"]:
    ID = comps["competence"]["code"]
    Content = comps["competence"]["title"]
    UniversalCompetition.add_row([ID, Content])
print(UniversalCompetition)

#4
UniversalCompetition = PrettyTable()
UniversalCompetition.field_names = ["ID", "Code", "Competitions"]
InsertName = "УК-1." #Вставте имя
for comps in json_data["content"]["universalCompetencyRows"]:
    CompCode = comps["competence"]["code"]
    for indicators in comps['indicators']:
        ID = indicators['id']
        Code2 = indicators['code']
        Competition = indicators['content']
        if CompCode == InsertName: 
            UniversalCompetition.add_row([ID, Code2, Competition])
print(UniversalCompetition)