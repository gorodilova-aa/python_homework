import pandas as pd
import numpy as np

# ---- Task 1 ----
# -1.1-  Create a DataFrame from a dictionary:

data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

task1_data_frame = df.copy()

# -1.2-   Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

# -1.3-   Modify an existing column:
task1_older = task1_with_salary.copy()

task1_older["Age"] +=1  
print(task1_older)

# -1.4-   Save the DataFrame as a CSV file:
task1_older.to_csv('employees.csv', index=False)


# ---- Task 2 ----
# -2.1-  Read data from a CSV file:

task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

# -2.2-  Read data from a JSON file: 
json_employees = pd.read_json("additional_employees.json")

print(json_employees)

# -2.3- Combine DataFrames:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


# ---- Task 3 ----

# -3.1- Use the head() method:
first_three = more_employees.head(3)
print("First three rows:\n", first_three)

# -3.2- Use the tail() method:
last_two = more_employees.tail(2)
print("Last two rows:\n",last_two)

# -3.3- Get the shape of a DataFrame
employee_shape = more_employees.shape
print("Shape of data frame: ", employee_shape)

 # -3.4- Use the info() method
more_employees.info()

# ---- Task 4 ----
# -4.1-
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

clean_data = dirty_data.copy()

# -4.2-
clean_data = clean_data.drop_duplicates()
print("Remove any duplicate rows\n", clean_data)

# -4.3-
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("Convert Age to numeric:\n", clean_data)

# -4.4-
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("Clean and convert Salary to numeric:\n", clean_data)

# -4.5-
mean_age = clean_data['Age'].mean()
median_salary = clean_data['Salary'].median()

clean_data['Age'] = clean_data['Age'].fillna(mean_age)
clean_data['Salary'] = clean_data["Salary"].fillna(median_salary)
print("Fill missing age with mean, salary with median:\n", clean_data)

# -4.6-
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed', errors='coerce')
print("Convert Hire Date to datetime:\n", clean_data)

# -4.7-
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print('Strip extra whitespace and standardize Name and Department as uppercase:\n',clean_data)
