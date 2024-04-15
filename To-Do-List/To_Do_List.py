from datetime import datetime

def add_task(to_do_list):
    name = input("Enter the task name: ")
    description = input("Enter the task description: ")
    
    while True:
        try:
            user_input = input("Enter the due date (YYYY-MM-DD format): ")
            due_date = datetime.strptime(user_input, "%Y-%m-%d").strftime("%Y-%m-%d")
            
            if datetime.strptime(due_date, "%Y-%m-%d") < datetime.now():
                raise ValueError("Due date cannot be in the past.")
            
            break  
        except ValueError as ve:
            if "time data" in str(ve):
                print("Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")
            else:
                print("Error:", ve)
                print("Due date cannot be in the past. Please try again.")
    
    My_Tasks = {"name": name, "description": description, "due_date": due_date}
    to_do_list.append(My_Tasks)
    
    save_to_file(to_do_list, "My_Tasks.txt")  

def remove_task(to_do_list, task_name):
    for task in to_do_list:
        if task["name"] == task_name:
            to_do_list.remove(task)
            update_file("My_Tasks.txt", task_name)
            print("Task Removed Successfully.")
            return
    print("Task Not Found.")

def update_task(to_do_list, task_name, new_name, new_description, new_due_date):
    for task in to_do_list:
        if task["name"] == task_name:
            task["name"] = new_name
            task["description"] = new_description
            task["due_date"] = new_due_date
            update_file("My_Tasks.txt", task_name, new_name, new_description, new_due_date)
            print("Task Updated Successfully.")
            return
    print("Task Not Found.")

def display_tasks(to_do_list):
    if not to_do_list:
        print("No Tasks In The To-Do List.")
    else:
        print("To-Do List:")
        for task in to_do_list:
            print(f"{task['name']}: {task['description']} (Due: {task['due_date']})")

def save_to_file(to_do_list, filename):
    with open(filename, "w") as file:
        for task in to_do_list:
            file.write(f"{task['name']}\n")
            file.write(f"{task['description']}\n")
            file.write(f"{task['due_date']}\n")
            file.write("---\n")

def load_tasks_from_file(filename):
    to_do_list = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                name = lines[i].strip()
                description = lines[i + 1].strip()
                due_date = lines[i + 2].strip()
                task = {"name": name, "description": description, "due_date": due_date}
                to_do_list.append(task)
                i += 4
        print("File Successfully Loaded....")
    except FileNotFoundError:
        print("File Not Found..... \nEnter A Valid File Name")
    except Exception as e:
        print(f"Error: {e}")
        print("Sorry, I can't Load The File.")
    return to_do_list

def update_file(filename, task_name, new_name=None, new_description=None, new_due_date=None):
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for i in range(0, len(lines), 4):
            if lines[i].strip() == task_name:
                continue
            file.write(lines[i])
            file.write(lines[i + 1])
            file.write(lines[i + 2])
            file.write("---\n")

def main():
    to_do_list = load_tasks_from_file("My_Tasks.txt")
    while True:
        print("\n")
        print("To-Do List Menu: \nPlease Select One Of The Following:")
        print("___________________________________")
        print("1. Add A New Task")
        print("2. Remove A Task")
        print("3. Update A Task")
        print("4. Display The To-Do List")
        print("5. Save The To-Do List To A File")
        print("6. Load The To-Do List From A File")
        print("7. Exit\n")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_task(to_do_list)
        elif choice == "2":
            task_name = input("Enter the task name to remove: ")
            remove_task(to_do_list, task_name)
        elif choice == "3":
            task_name = input("Enter the task name to update: ")
            new_name = input("Enter the new task name: ")
            new_description = input("Enter the new task description: ")
            new_due_date = input("Enter the new task due date (YYYY-MM-DD): ")
            update_task(to_do_list, task_name, new_name, new_description, new_due_date)
        elif choice == "4":
            display_tasks(to_do_list)
        elif choice == "5":
            save_to_file(to_do_list, "My_Tasks.txt")
        elif choice == "6":
            to_do_list = load_tasks_from_file("My_Tasks.txt")
        elif choice == "7":
            print("Exiting..........")
            break
        else:
            print("Invalid Choice: \nPlease Try Again: \n")

if __name__ == "__main__":
    main()
