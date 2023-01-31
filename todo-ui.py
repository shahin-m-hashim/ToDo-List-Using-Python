import tkinter as tk
from tkinter import ttk

class LeftFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side=tk.LEFT, fill=tk.Y)

        self.todo_list = ttk.Treeview(self)
        self.todo_list.pack(fill=tk.Y)

class RightFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.add_button = ttk.Button(self, text="Add Todo", command=self.add_todo)
        self.add_button.pack()

        self.delete_button = ttk.Button(self, text="Delete Todo", command=self.delete_todo)
        self.delete_button.pack()

    def add_todo(self):
        pass

    def delete_todo(self):
        pass

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")

        self.left_frame = LeftFrame(self.master)
        self.right_frame = RightFrame(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
