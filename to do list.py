import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import json

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Refresh the listbox view
def update_task_listbox():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        title = task['title']
        status = "✓" if task['completed'] else "✗"
        due = task.get('due', '')
        priority = task.get('priority', '')
        listbox.insert(tk.END, f"{idx+1}. [{status}] {title} (Due: {due}, Priority: {priority})")

# Add a new task
def add_task():
    title = entry.get()
    if title:
        due = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")
        priority = simpledialog.askstring("Priority", "Enter priority (Low, Medium, High):")
        task = {
            "title": title,
            "due": due or "",
            "priority": priority or "Medium",
            "completed": False
        }
        tasks.append(task)
        entry.delete(0, tk.END)
        update_task_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task title.")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        removed = tasks.pop(selected)
        update_task_listbox()
        save_tasks()
        messagebox.showinfo("Deleted", f"Task '{removed['title']}' removed.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Mark selected task as complete/incomplete
def toggle_complete():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]['completed'] = not tasks[selected]['completed']
        update_task_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Edit selected task
def edit_task():
    try:
        selected = listbox.curselection()[0]
        task = tasks[selected]

        new_title = simpledialog.askstring("Edit Title", "Update task title:", initialvalue=task['title'])
        new_due = simpledialog.askstring("Edit Due Date", "Update due date:", initialvalue=task.get('due', ''))
        new_priority = simpledialog.askstring("Edit Priority", "Update priority:", initialvalue=task.get('priority', 'Medium'))

        if new_title:
            task['title'] = new_title
            task['due'] = new_due or ""
            task['priority'] = new_priority or "Medium"
            update_task_listbox()
            save_tasks()
        else:
            messagebox.showinfo("Edit Cancelled", "Task title cannot be empty.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Main GUI
root = tk.Tk()
root.title("Advanced To-Do List")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#800080")

# Load tasks
tasks = load_tasks()

# UI Components
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18), bg="#800080", fg="white")
title_label.pack(pady=10)

entry = tk.Entry(root, width=35, font=("Helvetica", 14))
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, width=20, bg="white", fg="black")
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task, width=20, bg="white", fg="black")
edit_button.pack(pady=5)

complete_button = tk.Button(root, text="Toggle Complete", command=toggle_complete, width=20, bg="white", fg="black")
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=20, bg="white", fg="black")
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=60, height=12, font=("Helvetica", 12))
listbox.pack(pady=10)

update_task_listbox()

# Run app
root.mainloop()