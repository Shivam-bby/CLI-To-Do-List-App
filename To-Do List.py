
file_name = "task.txt"

# 🔃 Load tasks from file
def load_data():
    try:
        with open(file_name, "r") as file:
            tasks = [line.strip() for line in file.readlines()]  # 🛠️ FIXED: added () after strip
    except FileNotFoundError:
        tasks = []
    return tasks

# 💾 Save tasks to file
def save_task(tasks):
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ➕ Add task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_task(tasks)
    print("✔️ Task added.")

# 📋 View tasks
def view_task(tasks):
    if not tasks:
        print("⚠️ No tasks found.")
    else:
        print("🪟 Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")  # 🛠️ FIXED: it was printing the word "task", not the value

# ❌ Delete task
def delete_task(tasks):
    view_task(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_task(tasks)
            print(f"❌ Task removed successfully: {removed}")
        else:
            print("⚠️ Invalid task number. Please enter a correct number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 📢 Welcome banner
def banner():
    print("\n" + "="*40)
    print("🧮 Welcome to Persistent CLI To-Do App 🧮")
    print("="*40)

# 🔁 Main menu loop
def main():
    banner()
    tasks = load_data()
    while True:
        print("\nOptions: [1] View [2] Add [3] Remove [4] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose from 1 to 4.")

if __name__ == "__main__":
    main()
