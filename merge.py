import pandas as pd

student_details = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Age": [20, 21, 20, 22, 21],
    "Gender": ["Male", "Female", "Male", "Female", "Female"]
})

academic_records = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Course": ["BSc CS", "BSc CS", "BSc CS", "BSc CS", "BSc CS"],
    "Marks": [85, 90, 78, 88, 92],
    "Grade": ["A", "A+", "B+", "A", "A+"]
})

print("Student Details:")
print(student_details)

print("\nAcademic Records:")
print(academic_records)





integrated_data = pd.merge(
    student_details,
    academic_records,
    on="Student_ID"
)

print("\nIntegrated DataFrame:")
print(integrated_data)