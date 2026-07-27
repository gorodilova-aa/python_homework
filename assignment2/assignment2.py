# ---- Task 2 ----

import csv
import traceback

def read_employees():
    dict = { "fields": [], "rows": [] }
    
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            flag = True  # indicates first row
         
            for row in reader: 
                if flag:
                    dict["fields"] = row
                    flag = False
                else:
                    dict["rows"].append(row)

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"An exception occurred. {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        
    return dict

employees = read_employees()
print(employees)

# ---- Task 3 ----

def column_index(string):
    index = employees["fields"].index(string)
    return index

employee_id_column = column_index("employee_id")
print(f"Employee ID column index: {employee_id_column}")

# ---- Task 4 ----

def first_name(row_number):
    first_name_index = column_index("first_name")
    return employees["rows"][row_number][first_name_index]

print(f"First name of employee at row 3: {first_name(3)}")

# ---- Task 5 ----

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# ---- Task 6 ----

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# ---- Task 7 ----

def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

print(f"Employees sorted by last name: {sort_by_last_name()}")

# ---- Task 8 ----

def employee_dict(row):
    result = {}
    for i in range(1, len(employees["fields"])):
        result[employees["fields"][i]] = row[i]
    return result

print(f"Employee dictionary for row 3: {employee_dict(employees["rows"][3])}")

# --- Task 9 ----

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        result[row[employee_id_column]] = employee_dict(row)
    return result

print(f"All employees as a dictionary: {all_employees_dict()}")

# --- Task 10 ----

import os

def get_this_value():
    return os.getenv("THISVALUE")


# --- Task 11 ----

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Siberia")

print(f"Secret value from custom_module: {custom_module.secret}")


# ---- Task 12 ----

def read_minutes_file(file_path):           # helper function to read one the minutes file
    dict = { "fields": [], "rows": [] }
    
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            first_row = next(reader) # store first row as headers and goes to the next row
            dict["fields"] = first_row

            for row in reader: # reading the data rows
                dict["rows"].append(tuple(row))

    except Exception as e:
        print(f"An error occurred reading the file: {e}")
        return None
    return dict

def read_minutes():            
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(f"Minutes 1: {minutes1}")
print(f"Minutes 2: {minutes2}")


# ---- Task 13 ----

def create_minutes_set():
    minutes_set_1 = set(minutes1["rows"])
    minutes_set_2 = set(minutes2["rows"])

    return minutes_set_1.union(minutes_set_2)

minutes_set = create_minutes_set()
print(f"Combined minutes set: {minutes_set}")


# --- Task 14 ----  

from datetime import datetime

def create_minutes_list():
    minutes_list_temp = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list_temp))

    return minutes_list 

minutes_list=create_minutes_list()
print(f"Combined minutes list: {minutes_list}")

# --- Task 15 ----

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    minutes_list_string_back = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    try:
        with open("./minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(minutes_list_string_back)
    except Exception as e:
        print(f"An error occurred writing the file: {e}")
    return minutes_list_string_back

write_sorted_list()