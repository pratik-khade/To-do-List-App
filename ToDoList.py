import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        # Task entry
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        # Add Task button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        
        # Task list
        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(pady=10)
        
        # Mark as Complete button
        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.pack()
        
        # Populate task list
        self.populate_task_list()

    def populate_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "[X]" if task.completed else "[ ]"
            self.task_list.insert(tk.END, f"{status} {task.description}")
    
    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.tasks.append(Task(description))
            self.populate_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def mark_as_complete(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks[task_index]
            task.completed = True
            self.populate_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
