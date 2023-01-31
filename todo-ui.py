import tkinter as tk
from tkinter import ttk

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")

        self.left_frame = ttk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.right_frame = ttk.Frame(self.master)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.todo_list = ttk.Treeview(self.left_frame)
        self.todo_list.pack(fill=tk.Y)

        self.add_button = ttk.Button(self.right_frame, text="Add Todo", command=self.add_todo)
        self.add_button.pack()

        self.delete_button = ttk.Button(self.right_frame, text="Delete Todo", command=self.delete_todo)
        self.delete_button.pack()

    def add_todo(self):
        pass

    def delete_todo(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
