#                                        Student Marks Analysis with NumPy
 ## Description

This project uses NumPy to generate random marks for 100 students across 5 subjects and applies statistical analysis to understand student performance. It calculates important statistics, total marks for each student, and identifies the Top 5 students based on overall scores.

 ## What We Applied

# Random Data Generation

Used np.random.randint() to create a dataset of marks (100 students × 5 subjects).

Used np.random.seed(42) to make results reproducible (same random numbers every run).

# Statistical Analysis

Mean, Median, Standard Deviation, Variance

Maximum and Minimum marks across all students

# Total Marks Calculation

Summed up marks of each student across 5 subjects (np.sum(marks, axis=1)).

# Ranking Students

Used np.argsort() to rank students by total marks.

Extracted the Top 5 students with the highest scores.






