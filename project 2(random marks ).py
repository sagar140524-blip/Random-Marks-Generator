# import numpy
import numpy as np
# SEED(42) TO ENSURE RANDOM NUMBER ARE THE SAME ON EACH RUN 
np.random.seed(42)
#GENRATE RANDOM INTEGER BETWEEN 1 TO 100 , SIZE 100X5 (100 STUDENT 5 SUBJECTS)
marks= np.random.randint(1, 101, size=(100,5))
print(marks)

# STATISTICAL ANALYSIS
print("mean marks : ", np.mean(marks))
print("median marks : ", np.median(marks))
print("standard deviation : ", np.std(marks))
print("variance : ", np.var(marks))
print("max marks : ", np.max(marks))
print("min marks : ", np.min(marks))

# GIVE TOTAL MARKS AND TOP 5 STUDENTS
total_marks=np.sum(marks, axis=1)
# "NP.ARGSORT" SORT INDICES BY TOTAL MARKS 
# [-5:] SELECT THE LAST 5 
top_5_students = np.argsort(total_marks)[-5:]
print("Top 5 students based on total marks:")
for student in top_5_students:
    print(f"Student {student+1}: {total_marks[student]}")
# ADDED {STUDENT+1 }SO THAT STUDENT NUMBER START FROM 1 NOT 0
