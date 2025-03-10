def add_employee(id, name, position, salary):
    with open('employees.txt', 'a') as f:
        f.write(f'{id},{name},{position},{salary}\n')
        print('Employee added successfully!')

def get_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.read()
            if not records:
                print("No records found.\n")
                return
            for record in records:
                print(record.strip())
            print()
    except FileNotFoundError:
        print("Error: The file does not exist.\n")
    except IOError:
        print("Error: Unable to read the file.\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip())
                found = True
                break
    if not found:
        print("Employee not found.\n")

def update_employee(name, position, salary):

    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False

    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_records.append(record)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee record updated successfully!\n")
    else:
        print("Employee not found.\n")

def delete_employee():

    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False

    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                found = True
            else:
                updated_records.append(record)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee record deleted successfully!\n")
    else:
        print("Employee not found.\n")

add_employee("5", "Employee5", "Data Analytic", "50000")
get_employees()
search_employee()
update_employee("Employee 5", "Software Developer", "60000")
delete_employee()