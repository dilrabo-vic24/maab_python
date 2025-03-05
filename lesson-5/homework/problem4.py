universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    student_counts = []
    tuition_fees = []
    
    for university in universities:
        student_counts.append(university[1])
        tuition_fees.append(university[2])
    
    return student_counts, tuition_fees

def mean(student_counts):
    total = sum(student_counts)
    return total / len(student_counts)

def median(student_counts):
    sorted_students = sorted(student_counts)
    n = len(sorted_students)
    if n % 2 == 0:
        mid1 = sorted_students[n // 2 - 1]
        mid2 = sorted_students[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_students[n // 2]

student_counts, tuition_fees = enrollment_stats(universities)

total_students = sum(student_counts)
total_tuition = sum(tuition_fees)
mean_students = mean(student_counts)
median_students = median(student_counts)
mean_tuition = mean(tuition_fees)
median_tuition = median(tuition_fees)

print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print(f"Student mean: {mean_students:.2f}")
print(f"Student median: {median_students}")
print(f"Tuition mean: $ {mean_tuition:.2f}")
print(f"Tuition median: $ {median_tuition}")