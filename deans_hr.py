"""

Name: Henry Escoto
File name: deans_hr.py
Description: This program accepts student names and GPAs, then checks if
they qualify for Dean's list (GPA 3.5 or higher) or Honor Roll (GPA 3.25 or higher.).
Program ends when last name entered is 'ZZZ'.

"""

while True:
    # Asks for the last name (and you can quit with ZZZ)
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        print("Goodbye!")
        break

    # Asks for the student's first name
    first_name = input("Enter student's first name: ")

    # Asks for the GPA and converts to float
    gpa = float(input("Enter student's GPA (e.g., 3.5): "))

    # Test conditions
    if gpa >= 3.5:
        print(f"{first_name} {last_name} made the Dean's List (GPA {gpa:.2f}).")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} made the Honor Roll (GPA {gpa:.2f}).")
    else:
        print(f"{first_name} {last_name} did not qualify this term (GPA {gpa:.2f}).")

    print("-" * 40)