import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    def add_employee(employee):
        if EmployeeManager.employee_exists(employee.employee_id):
            print("Employee ID already exists!")
            return
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")
    
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            employees = file.readlines()
        if not employees:
            print("No records found.")
        else:
            print("Employee Records:")
            for emp in employees:
                print(emp.strip())
    
    def search_employee(employee_id):
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("Employee not found.")
    
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        updated = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            employees = file.readlines()
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for emp in employees:
                emp_data = emp.strip().split(", ")
                if emp_data[0] == employee_id:
                    if name:
                        emp_data[1] = name
                    if position:
                        emp_data[2] = position
                    if salary:
                        emp_data[3] = salary
                    emp = ", ".join(emp_data) + "\n"
                    updated = True
                file.write(emp)
        print("Employee updated successfully!" if updated else "Employee not found.")
    
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        deleted = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            employees = file.readlines()
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for emp in employees:
                if not emp.startswith(employee_id + ","):
                    file.write(emp)
                else:
                    deleted = True
        print("Employee deleted successfully!" if deleted else "Employee not found.")
    
    def employee_exists(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    return True
        return False

    
emp_id = input("Enter Employee ID: ")
name = input("Enter Name: ")
position = input("Enter Position: ")
salary = input("Enter Salary: ")

EmployeeManager.add_employee(Employee(emp_id, name, position, salary))
EmployeeManager.view_all_employees()

emp_id = input("Enter Employee ID to search: ")

EmployeeManager.search_employee(emp_id)

emp_id = input("Enter Employee ID to update: ")
name = input("Enter new name (press enter to skip): ") or None
position = input("Enter new position (press enter to skip): ") or None
salary = input("Enter new salary (press enter to skip): ") or None

EmployeeManager.update_employee(emp_id, name, position, salary)

emp_id = input("Enter Employee ID to delete: ")

EmployeeManager.delete_employee(emp_id)