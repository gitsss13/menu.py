


def _prompt_nonempty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty. Please try again.")


def _prompt_cgpa() -> float:
    while True:
        raw = input("Enter CGPA: ").strip()
        try:
            cgpa = float(raw)
        except ValueError:
            print("Invalid CGPA. Please enter a numeric value (e.g., 8.75).")
            continue

        # Optional: keep CGPA reasonable if you want. Comment out if not desired.
        if cgpa < 0:
            print("CGPA cannot be negative. Please try again.")
            continue

        return cgpa


def main() -> None:
    students = []  # list[dict]

    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student Details")
        print("2. Display Student Details")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = _prompt_nonempty("Enter Name: ")
            roll = _prompt_nonempty("Enter Roll Number: ")
            department = _prompt_nonempty("Enter Department: ")
            cgpa = _prompt_cgpa()

            students.append(
                {
                    "name": name,
                    "roll": roll,
                    "department": department,
                    "cgpa": cgpa,
                }
            )
            print("Student added successfully!")

        elif choice == "2":
            if not students:
                print("No student records found.")
                continue

            print("\nStored Student Details")
            print("-" * 70)
            for i, s in enumerate(students, start=1):
                print(f"{i}. Name       : {s['name']}")
                print(f"   Roll Number: {s['roll']}")
                print(f"   Department  : {s['department']}")
                print(f"   CGPA        : {s['cgpa']:.2f}")
                print("-" * 70)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

