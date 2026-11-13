import csv

FILE_NAME = "module_assessment_grades 1 (2) (1).csv"

def load_students():
    students = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if validate_record(row):
                    students.append(row)

            return students

    except FileNotFoundError:
        print("Error: CSV file not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected Error:", e)

    return []


def validate_record(student):

    required_fields = [
        "Student No",
        "Name",
        "Surname",
        "Module",
        "Quiz(10%)",
        "Project(20%)",
        "Final Exam(50%)",
        "Practical(20%)"
    ]

    for field in required_fields:

        if student[field] == "":
            print("Missing data in:", field)
            return False

    return True


students = load_students()

for student in students:
    print(student)