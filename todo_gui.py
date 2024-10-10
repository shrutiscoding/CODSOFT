import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.root.configure(bg="#87CEEB")

        self.frame = tk.Frame(self.root, bg="#87CEEB")
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE, fg="black")
        self.task_listbox.pack(padx=20)

        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task,bg="#607D8B", fg="black",width=15,height=2)
        self.add_task_button.pack(pady=5)

        self.mark_done_button = tk.Button(self.frame, text="Mark Task as Done", command=self.mark_done,bg="#607D8B", fg="black",width=15,height=2)
        self.mark_done_button.pack(pady=5)

        self.edit_task_button = tk.Button(self.frame, text="Edit Task", command=self.edit_task,bg="#607D8B",  fg="black",width=15,height=2)
        self.edit_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task,bg="#607D8B",  fg="black",width=15,height=2)
        self.delete_task_button.pack(pady=5)

        self.delete_all_button = tk.Button(self.frame, text="Delete All Tasks", command=self.delete_all_tasks,bg="#607D8B", fg="black",width=15,height=2)
        self.delete_all_button.pack(pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit, bg="#607D8B", fg="black",width=15,height=2)
        self.exit_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter the task:")
        if task:
            self.tasks.append({"task": task, "done": False})
            self.update_task_listbox()

    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index]["done"] = True
            self.update_task_listbox()
            messagebox.showinfo("Info", "Task marked as done!")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            new_task = simpledialog.askstring("Input", "Edit the task:", initialvalue=self.tasks[task_index]["task"])
            if new_task:
                self.tasks[task_index]["task"] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks.pop(task_index)
            self.update_task_listbox()
            messagebox.showinfo("Info", "Task removed!")
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def delete_all_tasks(self):
        if self.tasks:
            self.tasks.clear()
            self.update_task_listbox()
            messagebox.showinfo("Info", "All tasks removed!")
        else:
            messagebox.showwarning("Warning", "No tasks to remove.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["done"] else "✗"
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
