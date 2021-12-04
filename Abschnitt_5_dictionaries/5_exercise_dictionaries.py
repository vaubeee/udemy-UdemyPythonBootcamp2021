employees = [
    {"name" : "Blees Volker", "profession" : "Director of Purchasing", "salary" : 60_000},
    {"name" : "Kutsch Marcus", "profession" : "Purchaser", "salary" : 35_000},
    {"name" : "Blaeser Max", "profession" : "Purchaser", "salary" : 30_000},
    {"name" : "Heinze Marcel", "profession" : "Project Manager", "salary" : 60_000},
    {"name" : "Hamacher Ralf", "profession" : "Warehouse Manager", "salary" : 30_000}
    ]

total_salaries = 0
for employee in employees:
        total_salaries += employee['salary']

print(total_salaries)
        