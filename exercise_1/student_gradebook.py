# Function to determine the letter grade based on average score
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Function to add a new student to the gradebook
def add_student(gradebook):
    name = input("Enter student name: ").strip()
    if name in gradebook:
        print(f"{name} already exists.")  # Prevent duplicate entries
    else:
        gradebook[name] = []  # Initialize with empty grade list
        print(f"{name} added successfully.")

# Function to add a grade to an existing student
def add_grade(gradebook):
    name = input("Enter student name: ").strip()
    if name not in gradebook:
        print("Student not found.")  # Validate student existence
        return
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <= 100:
            gradebook[name].append(grade)  # Add grade to student's list
            print(f"Grade {grade} added to {name}.")
        else:
            print("Grade must be between 0 and 100.")  # Validate range
    except ValueError:
        print("Invalid input. Grade must be a number.")  # Handle non-numeric input

# Function to display a student's report (average & letter grade)
def view_student_report(gradebook):
    name = input("Enter student name: ").strip()
    if name not in gradebook:
        print("Student not found.")
        return
    grades = gradebook[name]
    if not grades:
        print(f"{name} has no grades yet.")  # Handle empty grade list
        return
    avg = sum(grades) / len(grades)  # Compute average
    letter = get_letter_grade(avg)  # Get corresponding letter grade
    print(f"{name}'s Average: {avg:.2f} (Grade: {letter})")
    print(f"Grades: {grades}")

# Function to compute and display overall class statistics
def class_statistics(gradebook):
    all_averages = []
    for grades in gradebook.values():
        if grades:
            avg = sum(grades) / len(grades)  # Compute student average
            all_averages.append((avg, grades))  # Store with their grades

    if not all_averages:
        print("No grades available to calculate statistics.")
        return

    class_avg = sum(avg for avg, _ in all_averages) / len(all_averages)  # Class average
    highest = max(all_averages)  # Student with highest average
    lowest = min(all_averages)  # Student with lowest average

    # Find the corresponding student names
    best_student = [name for name, grades in gradebook.items() if grades and sum(grades) / len(grades) == highest[0]][0]
    worst_student = [name for name, grades in gradebook.items() if grades and sum(grades) / len(grades) == lowest[0]][0]

    # Output statistics
    print(f"Class Average: {class_avg:.2f}")
    print(f"Top Student: {best_student} ({highest[0]:.2f})")
    print(f"Lowest Student: {worst_student} ({lowest[0]:.2f})")

# Main menu loop to interact with the gradebook
def gradebook_menu():
    gradebook = {}  # Dictionary to store student names and grades

    while True:
        print("\n=== STUDENT GRADEBOOK MANAGER ===")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Report")
        print("4. Class Statistics")
        print("5. Exit")

        choice = input("Choice: ").strip()

        # Decision logic for each menu option
        if choice == "1":
            add_student(gradebook)
        elif choice == "2":
            add_grade(gradebook)
        elif choice == "3":
            view_student_report(gradebook)
        elif choice == "4":
            class_statistics(gradebook)
        elif choice == "5":
            print("Exiting Gradebook Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    gradebook_menu()
