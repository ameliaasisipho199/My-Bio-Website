from tkinter import *
from tkinter import messagebox
import csv

from grade_calculations import (
    calculate_grade,
    get_performance
)

FILE_NAME = "module_assessment_grades 1 (2) (1).csv"

root = Tk()

root.title("Eduvos Student Grade Calculator")
root.geometry("600x500")


def capture_window():

    window = Toplevel(root)

    window.title("Capture Student")

    labels = [
        "Student No",
        "Name",
        "Surname",
        "Module",
        "Quiz",
        "Project",
        "Final Exam",
        "Practical"
    ]

    entries = []

    for i, label in enumerate(labels):

        Label(
            window,
            text=label
        ).grid(row=i, column=0)

        entry = Entry(window)

        entry.grid(row=i, column=1)

        entries.append(entry)

    def save():

        try:

            with open(
                    FILE_NAME,
                    "a",
                    newline="",
                    encoding="utf-8") as file:

                writer = csv.writer(file)

                writer.writerow([
                    entries[0].get(),
                    entries[1].get(),
                    entries[2].get(),
                    entries[3].get(),
                    entries[4].get(),
                    entries[5].get(),
                    entries[6].get(),
                    entries[7].get()
                ])

            messagebox.showinfo(
                "Success",
                "Student saved successfully"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    Button(
        window,
        text="Save",
        command=save
    ).grid(row=9, column=1)


def view_records():

    window = Toplevel(root)

    window.title("Records")

    listbox = Listbox(
        window,
        width=120,
        height=20
    )

    listbox.pack()

    try:

        with open(
                FILE_NAME,
                "r",
                encoding="utf-8") as file:

            reader = csv.reader(file)

            for row in reader:

                listbox.insert(
                    END,
                    row
                )

    except Exception as e:

        listbox.insert(
            END,
            str(e)
        )


def search_window():

    window = Toplevel(root)

    window.title("Search Student")

    Label(
        window,
        text="Student Number"
    ).pack()

    search_box = Entry(window)

    search_box.pack()

    result = Text(
        window,
        width=70,
        height=15
    )

    result.pack()

    def search():

        result.delete(
            "1.0",
            END
        )

        try:

            with open(
                    FILE_NAME,
                    "r",
                    encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for student in reader:

                    if student["Student No"] == search_box.get():

                        overall = calculate_grade(
                            float(student["Quiz(10%)"]),
                            float(student["Project(20%)"]),
                            float(student["Final Exam(50%)"]),
                            float(student["Practical(20%)"])
                        )

                        performance = get_performance(overall)

                        result.insert(
                            END,
                            f"""
Student No: {student['Student No']}
Name: {student['Name']}
Surname: {student['Surname']}
Module: {student['Module']}

Overall Grade: {overall}

Performance: {performance}
"""
                        )

        except Exception as e:

            result.insert(
                END,
                str(e)
            )

    Button(
        window,
        text="Search",
        command=search
    ).pack()


Label(
    root,
    text="Eduvos Student Grade Calculator",
    font=("Arial", 18, "bold")
).pack(pady=20)

Button(
    root,
    text="Capture Student Marks",
    bg="green",
    width=30,
    command=capture_window
).pack(pady=10)

Button(
    root,
    text="View / Delete Records",
    width=30,
    command=view_records
).pack(pady=10)

Button(
    root,
    text="Search / Update Records",
    bg="orange",
    width=30,
    command=search_window
).pack(pady=10)

Button(
    root,
    text="Close Application",
    bg="red",
    width=30,
    command=root.destroy
).pack(pady=10)

root.mainloop()