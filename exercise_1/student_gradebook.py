# Student Gradebook Manager
# This program helps you manage students and their grades in a simple way.
# All comments are written in plain, human-like English for easy understanding.

def get_letter_grade(avg):
    # This function takes a number (average) and returns a letter grade.
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def class_stats(gradebook):
    # This function shows the class average and the best/worst student.
    if not gradebook:
        print("No students in the gradebook yet.")
        return
    averages = {name: sum(grades)/len(grades) for name, grades in gradebook.items() if grades}
    if not averages:
        print("No grades entered yet.")
        return
    class_avg = sum(averages.values()) / len(averages)
    best = max(averages, key=averages.get)
    worst = min(averages, key=averages.get)
    print(f"\nClass Average: {class_avg:.2f}")
    print(f"Top Student: {best} ({averages[best]:.2f})")
    print(f"Lowest Student: {worst} ({averages[worst]:.2f})\n")

def main():
    # This is the main part of the program. It shows the menu and does what you pick.
    gradebook = {}
    while True:
        print("\n=== STUDENT GRADEBOOK MANAGER ===")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Report")
        print("4. Class Statistics")
        print("5. Exit")
        choice = input("Choice: ").strip()
        if choice == '1':
            # Add a new student
            name = input("Enter student name: ").strip()
            if name in gradebook:
                print("Student already exists.")
            else:
                gradebook[name] = []
                print(f"Added {name} to the gradebook.")
        elif choice == '2':
            # Add a grade to a student
            name = input("Enter student name: ").strip()
            if name not in gradebook:
                print("Student not found.")
            else:
                try:
                    grade = float(input("Enter grade (0-100): "))
                    if 0 <= grade <= 100:
                        gradebook[name].append(grade)
                        print(f"Added grade {grade} for {name}.")
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '3':
            # Show a student's average and letter grade
            name = input("Enter student name: ").strip()
            if name not in gradebook:
                print("Student not found.")
            elif not gradebook[name]:
                print(f"No grades for {name} yet.")
            else:
                grades = gradebook[name]
                avg = sum(grades) / len(grades)
                letter = get_letter_grade(avg)
                print(f"{name}'s Average: {avg:.2f} (Grade: {letter})")
                print(f"Grades: {grades}")
        elif choice == '4':
            # Show class statistics
            class_stats(gradebook)
        elif choice == '5':
            # Exit the program
            print("Goodbye!")
            break
        else:
            print("Please pick a valid option (1-5).")

if __name__ == "__main__":
    main()
