# Small Task: Highest Score
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(f"The highest score is: {highest}")