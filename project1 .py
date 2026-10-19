

import tkinter as tk
from tkinter import messagebox

tasks = []

# GUI Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.config(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="===== TO-DO LIST =====",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=15)

# Task Input
task_entry = tk.Entry(root, font=("Arial", 12), width=25)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    command=lambda: (
        tasks.append(task_entry.get())
        if task_entry.get().strip() != ""
        else messagebox.showwarning("Warning", "Enter a task!")
    )
)
add_button.pack(pady=5)

# Task List Display
task_list = tk.Listbox(root, width=35, height=10, font=("Arial", 11))
task_list.pack(pady=10)

# View Tasks Button
view_button = tk.Button(
    root,
    text="View Tasks",
    font=("Arial", 12),
    command=lambda: (
        task_list.delete(0, tk.END),
        [task_list.insert(tk.END, str(i + 1) + ". " + tasks[i])
         for i in range(len(tasks))]
        if len(tasks) > 0
        else messagebox.showinfo("Tasks", "No tasks added yet!")
    )
)
view_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    command=root.destroy
)
exit_button.pack(pady=5)

root.mainloop()
