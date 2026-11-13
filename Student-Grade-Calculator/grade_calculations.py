import csv

FILE_NAME = "module_assessment_grades 1 (2) (1).csv"

def calculate_grade(quiz, project, final_exam, practical):
    overall = (
        (quiz * 0.10)
        + (project * 0.20)
        + (final_exam * 0.50)
        + (practical * 0.20)
    )
    return round(overall, 2)

def get_performance(grade):
    if grade >= 75:
        return "Distinction"
    elif grade >= 50:
        return "Pass"
    else:
        return "Fail"

try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        print("\nSTUDENT GRADE REPORT\n")

        for student in reader:

            quiz = float(student["Quiz(10%)"])
            project = float(student["Project(20%)"])
            final_exam = float(student["Final Exam(50%)"])
            practical = float(student["Practical(20%)"])

            overall = calculate_grade(
                quiz,
                project,
                final_exam,
                practical
            )

            performance = get_performance(overall)

            print(f"Student No: {student['Student No']}")
            print(f"Name: {student['Name']} {student['Surname']}")
            print(f"Module: {student['Module']}")
            print(f"Overall Grade: {overall}")
            print(f"Performance: {performance}")
            print("-" * 40)

except FileNotFoundError:
    print("CSV file not found.")
except Exception as e:
    print("Error:", e)