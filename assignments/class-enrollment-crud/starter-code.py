def show_menu():
    print("\nClass Enrollment CRUD")
    print("1. Create enrollment")
    print("2. View enrollments")
    print("3. Update enrollment")
    print("4. Delete enrollment")
    print("5. Exit")


def main():
    enrollments = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("TODO: create enrollment")
        elif choice == "2":
            print("TODO: view enrollments")
        elif choice == "3":
            print("TODO: update enrollment")
        elif choice == "4":
            print("TODO: delete enrollment")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()