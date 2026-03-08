import os


students = [] 


def clear_screen():
    # os.system("cls" if os.name == "nt" else "clear")
    print("\n" * 30)


def pause(msg="Press Enter to continue..."):
    input(msg)


def find_student_index_by_id(student_id):
    for i, st in enumerate(students):
        if st["id"] == student_id:
            return i
    return -1


def print_student_table(student_list):
    if not student_list:
        print("No students found.")
        return

    print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Address'}")
    print("-" * 60)
    for st in student_list:
        print(f"{st['id']:<10} {st['name']:<20} {str(st['age']):<5} {st['address']}")


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Input cannot be empty. Try again.")


def input_age(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Age must be a number (0-999). Try again.")


# ---------------------------
# Menu actions
# ---------------------------
def view_students():
    clear_screen()
    print("1. View Screen\n")
    print_student_table(students)
    pause("\nPress Enter to exit view...")


def add_students():
    while True:
        clear_screen()
        print("2. Add Student\n")

        student_id = input_non_empty("Id: ")
        if find_student_index_by_id(student_id) != -1:
            print("This ID already exists. Try a different ID.")
            pause()
            continue

        name = input_non_empty("Name: ")
        age = input_age("Age: ")
        address = input_non_empty("Address: ")

        students.append({
            "id": student_id,
            "name": name,
            "age": age,
            "address": address
        })

        print("\nData Saved.")
        choice = input("Press 1 to add more, 2 to return to menu: ").strip()
        if choice != "1":
            break


def edit_student():
    while True:
        clear_screen()
        print("3. Edit\n")

        student_id = input_non_empty("Input Id: ")
        idx = find_student_index_by_id(student_id)

        if idx == -1:
            print("Student not found.")
            choice = input("Press 1 to try again, 2 to return to menu: ").strip()
            if choice == "1":
                continue
            return

        st = students[idx]
        print("\nId: (Not changeable) =", st["id"])

        # Name
        print("Name: (Current) =", st["name"])
        new_name = input("Input New Name (leave empty to keep old): ").strip()
        if new_name != "":
            st["name"] = new_name

        # Age
        print("Age: (Current) =", st["age"])
        new_age = input("Input New Age (leave empty to keep old): ").strip()
        if new_age != "":
            if new_age.isdigit():
                st["age"] = int(new_age)
            else:
                print("Invalid age entered. Keeping old age.")

        # Address
        print("Address: (Current) =", st["address"])
        new_address = input("Input New Address (leave empty to keep old): ").strip()
        if new_address != "":
            st["address"] = new_address

        print("\nUpdated successfully.")
        choice = input("Press 1 to edit another, 2 to return to menu: ").strip()
        if choice != "1":
            break


def delete_student():
    while True:
        clear_screen()
        print("4. Delete\n")

        student_id = input_non_empty("Input Id: ")
        idx = find_student_index_by_id(student_id)

        if idx == -1:
            print("Student not found.")
            choice = input("Press 1 to try again, 2 to return to menu: ").strip()
            if choice == "1":
                continue
            return

        st = students[idx]
        print("\nStudent Details:")
        print_student_table([st])

        confirm = input("\nInput Y to delete, N to return: ").strip().lower()
        if confirm == "y":
            students.pop(idx)
            print("Deleted.")
        else:
            print("Cancelled.")

        choice = input("Press 1 to delete more, 2 to return to menu: ").strip()
        if choice != "1":
            break


def search_students():
    while True:
        clear_screen()
        print("5. Search\n")
        print("1. Search by Id")
        print("2. Search by Name")
        print("3. Return to menu")

        opt = input("\nChoose: ").strip()

        if opt == "1":
            clear_screen()
            sid = input_non_empty("Enter Id: ")
            idx = find_student_index_by_id(sid)
            if idx == -1:
                print("\nNo match found.")
            else:
                print("\nResult:")
                print_student_table([students[idx]])
            pause()

        elif opt == "2":
            clear_screen()
            name_part = input_non_empty("Enter Name (full or part): ").strip().lower()
            results = []
            for st in students:
                if name_part in st["name"].lower():
                    results.append(st)

            print("\nResults:")
            print_student_table(results)
            pause()

        else:
            break


def main():
    while True:
        clear_screen()
        print("Menu Screen\n")
        print("1. View Students")
        print("2. Add")
        print("3. Edit")
        print("4. Delete")
        print("5. Search")
        print("6. Exit")

        choice = input("\nInput choice: ").strip()

        if choice == "1":
            view_students()
        elif choice == "2":
            add_students()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_students()
        elif choice == "6":
            clear_screen()
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()

