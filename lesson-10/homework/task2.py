import csv

def create_grades_csv():
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Subject', 'Grade'])
        writer.writerow(['Alice', 'Math', '85'])
        writer.writerow(['Bob', 'Science', '78'])
        writer.writerow(['Carol', 'Math', '92'])
        writer.writerow(['Dave', 'History', '74'])
    print("grades.csv created successfully.")

def calculate_average_grades():
    subjects = {}
    try:
        with open('grades.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                subject = row['Subject']
                grade = float(row['Grade'])
                
                if subject in subjects:
                    subjects[subject].append(grade)
                else:
                    subjects[subject] = [grade]
    except FileNotFoundError:
        print("Error: grades.csv file not found.")
        return
    except Exception as e:
        print(f"Error reading grades.csv: {e}")
        return
    
    averages = {}
    for subject, grades in subjects.items():
        averages[subject] = sum(grades) / len(grades)
    
    try:
        with open('average_grades.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Subject', 'Average Grade'])
            
            for subject, avg in averages.items():
                writer.writerow([subject, avg])
        
        print("average_grades.csv created successfully.")
    except Exception as e:
        print(f"Error writing average_grades.csv: {e}")

def main():
    create_grades_csv()
    
    calculate_average_grades()
    
    print("\nContents of grades.csv:")
    try:
        with open('grades.csv', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    
    print("\nContents of average_grades.csv:")
    try:
        with open('average_grades.csv', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()