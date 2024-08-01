# USIU Grading System:
# A: 80-100, B: 70-79, C: 60-69, D: 50-59, F: Below 50

# Infinite loop to continuously accept user input
while True:
    # Prompt user to enter a mark or 'q' to quit
    mark = input("Enter a mark (or 'q' to quit): ")
    
    # Check if user wants to quit
    if mark == 'q':
        break

    # Convert user input to float
    mark = float(mark)

    # Validate the entered mark
    if mark < 0 or mark > 100:
        # Print error message for invalid mark
        print("Invalid mark. Please enter a value between 0 and 100.")
        continue

    # Determine the grade based on the mark
    if mark >= 90:
        grade = 'A'
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

    # Print the mark and corresponding grade
    print(f"Mark: {mark:.2f}, Grade: {grade}")

# Print goodbye message when loop is exited
print("Goodbye!")
