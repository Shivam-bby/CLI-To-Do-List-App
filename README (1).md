# ✅ Persistent CLI To-Do List App

A simple and beginner-friendly command-line To-Do List application built using Python.
This app allows you to **add**, **view**, and **delete** tasks directly in the terminal,
and all tasks are saved in a file (`task.txt`) so they remain even after you close the program.

This task is created for the **Python Developer Internship** as part of Task 2.

---

## 🧾 Description

This is a **persistent CLI to-do list manager** where tasks are stored using **lists** in memory
and saved to a **text file** using Python's file handling. It is easy to use, runs in the terminal,
and does not require any external library.

---

## 📋 Features

- 📥 Add Task – Add a new task to your to-do list
- 📋 View Tasks – See all tasks in a numbered list
- ❌ Delete Task – Remove a task by selecting its number
- 💾 Save Automatically – All tasks are stored in task.txt and persist between runs

---

## 🧠 Key Concepts Used

- ✅ Python Lists
- ✅ File Handling (open, read, write)
- ✅ String Manipulation (.strip())
- ✅ Exception Handling (FileNotFoundError)
- ✅ Functions
- ✅ CLI input/output (input(), print())

---

## 🛠 Tools Used

- Python 3.x
- VS Code / Any Text Editor
- Terminal / Command Prompt

---

## 📁 File Structure

📦 persistent-cli-todo-app/
├── todo.py         # Python file (main logic)
├── task.txt        # Stores tasks (auto-created)
└── README.md       # (Included in code as this docstring)

---

## 🚀 How to Run

1. Open terminal or command prompt
2. Navigate to the folder where `todo.py` is saved
3. Run this command:
   python todo.py

---

## 💡 Sample Output

========================================
🧮 Welcome to Persistent CLI To-Do App 🧮
========================================

Options: [1] View [2] Add [3] Remove [4] Exit
Choose an option: 2
Enter a new task: Submit internship task
✔️ Task added.

Options: [1] View [2] Add [3] Remove [4] Exit
Choose an option: 1
🪟 Your tasks:
1. Submit internship task

---