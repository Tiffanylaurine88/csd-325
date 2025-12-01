import json


def print_students(students, title):
    """Print each student in the list with a label."""
    print(f"\n{title}")
    print("-" * len(title))
    for student in students:
        last = student["L_Name"]
        first = student["F_Name"]
        sid = student["Student_ID"]
        email = student["Email"]
        print(f"{last}, {first} : ID = {sid} , Email = {email}")
    print()  # blank line for spacing


def main():
    filename = "student.json"

    # load the original data
    with open(filename, "r") as f:
        students = json.load(f)

    print_students(students, "Original Student List")

    # add your own record
    my_student = {
        "F_Name": "Tiffany",
        "L_Name": "Davidson",
        "Student_ID": 99999,  # any fictional id
        "Email": "tdavidson@example.com"
    }

    students.append(my_student)

    print_students(students, "Updated Student List (after append)")

    # write updated list back to the json file
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)

    print("student.json file has been updated.")


if __name__ == "__main__":
    main()
