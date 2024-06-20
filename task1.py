import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            selectmode=tk.SINGLE,
            bg="white",
            fg="black",
            selectbackground="gray",
            selectforeground="white"
        )8
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=5)
        
        self.add_btn = tk.Button(self.root, text="Add Task", width=48, command=self.add_task)
        self.add_btn.pack(pady=5)
        
        self.update_btn = tk.Button(self.root, text="Update Task", width=48, command=self.update_task)
        self.update_btn.pack(pady=5)
        
        self.delete_btn = tk.Button(self.root, text="Delete Task", width=48, command=self.delete_task)
        self.delete_btn.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Update Task", "Update task:")
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
