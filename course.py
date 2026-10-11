import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Course': ['BCA', 'BBA', 'B.Com', 'B.Sc', 'BA'],
    'Students': [60, 45, 75, 50, 35]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)



plt.bar(
    df['Course'],
    df['Students'],
    color=['red', 'blue', 'green', 'orange', 'purple']
)

plt.title("Number of Students Enrolled in Each Course")
plt.xlabel("Courses")
plt.ylabel("Number of Students")

plt.show()