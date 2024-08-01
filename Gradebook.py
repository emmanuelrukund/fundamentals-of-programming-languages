# USIU Grading System:
# A: 80-100, B: 70-79, C: 60-69, D: 50-59, F: Below 50

while True:
    mark = float(input("Enter a mark (or 'q' to quit): "))

    if mark == 'q':
        break

    if mark < 0 or mark > 100:
        print("Invalid mark. Please enter a value between 0 and 100.")
        continue

    if mark >= 90:
        grade ='A'
    elif mark >= 87:
        grade = 'A-'
    elif mark >= 84:
        grade = 'B+'
    elif mark >= 80:
        grade = 'B'
    elif mark >= 77:
        grade = 'B-'
    elif mark >= 74:
        grade = 'C+'
    elif mark >= 70:
        grade = 'C'
    elif mark >= 67:
        grade = 'C-'
    elif mark >= 64:
        grade = 'D+'
    elif mark >= 62:
        grade = 'D'
    elif mark >= 60:
        grade = 'D-'
    else:
        grade = 'F'

    print(f"Mark: {mark:.2f}, Grade: {grade}")

print("Goodbye!")