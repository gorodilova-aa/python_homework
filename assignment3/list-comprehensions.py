import csv

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    employees = list(reader)

employees_names = [f"{row[1]} {row[2]}" for row in employees[1:]]

print(employees_names)

employees_names_with_e = [row for row in employees_names if "e" in row.lower()]

print(employees_names_with_e)

