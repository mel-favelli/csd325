import json
from pathlib import Path

def print_students(students: list[dict]) -> None:

    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

def main() -> None:

    candidate_files = [Path("Student.json")]
    json_path = next((p for p in candidate_files if p.exists()), None)

    if json_path is None:
        raise FileNotFoundError("Could not find Student.json in this folder.")


    with json_path.open("r", encoding="utf-8") as f:
        students = json.load(f)


    print("Original Student list:")
    print_students(students)

   
    new_student = {
        "F_Name": "Melissa",
        "L_Name": "Favelli",
        "Student_ID": 99999,
        "Email": "mfavelli@my365.bellevue.edu"
    }
    students.append(new_student)

  
    print("\nUpdated Student list:")
    print_students(students)

   
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)


    print(f"\nThe .json file was updated: {json_path.name}")

if __name__ == "__main__":
    main()
