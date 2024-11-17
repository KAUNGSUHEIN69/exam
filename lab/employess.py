employees = [
    {"name": "Alice", "projects_completed": 10, "hours_worked": 200, "rating": 4.5},
    {"name": "Bob", "projects_completed": 7, "hours_worked": 150, "rating": 4.2},
    {"name": "Charlie", "projects_completed": 5, "hours_worked": 120, "rating": 3.8},
    {"name": "David", "projects_completed": 8, "hours_worked": 180, "rating": 4.7},
    {"name": "Eve", "projects_completed": 6, "hours_worked": 140, "rating": 4.0},
]


def display_all_employees():
    """Display all employee records."""
    for employee in employees:
        print(employee)

def add_employee(name, projects_completed, hours_worked, rating):
    """Add a new employee record."""
    new_employee = {
        "name": name,
        "projects_completed": projects_completed,
        "hours_worked": hours_worked,
        "rating": rating,
    }
    employees.append(new_employee)

def high_rated_employees(min_rating):
    """Return employees with rating >= min_rating."""
    result=[]
    for employee in employees:
        if employee["rating"]>min_rating:
            result.append(employee)
    return result
            
def get_top_performer():
    return max(employees, key=lambda emp: emp["projects_completed"])


def average_hours_worked():
    """Return the average hours worked by all employees."""
    total_hours = sum(emp["hours_worked"] for emp in employees)
    return total_hours / len(employees)

def main():
    while True:
        print("\nEmployee Performance Tracker")
        print("1. Display all employees")
        print("2. Add a new employee")
        print("3. Get employees with high ratings")
        print("4. Get the top performer")
        print("5. Get the average hours worked")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_employees()
        elif choice == "2":
            name = input("Enter name: ")
            projects_completed = int(input("Enter projects completed: "))
            hours_worked = int(input("Enter hours worked: "))
            rating = float(input("Enter rating: "))
            add_employee(name, projects_completed, hours_worked, rating)
        elif choice == "3":
            min_rating = float(input("Enter minimum rating: "))
            result = high_rated_employees(min_rating)
            print(result)
        elif choice == "4":
            top_performer = get_top_performer()
            print("Top Performer:", top_performer)
        elif choice == "5":
            avg_hours = average_hours_worked()
            print("Average Hours Worked:", avg_hours)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
