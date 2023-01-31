import tkinter as tk
from tkinter import ttk

class LeftFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=0, sticky="nswe")

        self.todo_list = ttk.Treeview(self)
        self.todo_list.grid(sticky="nswe")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

class RightFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=1, sticky="nswe")

        self.add_button = ttk.Button(self, text="Add Todo", command=self.add_todo)
        self.add_button.grid(sticky="we")

        self.delete_button = ttk.Button(self, text="Delete Todo", command=self.delete_todo)
        self.delete_button.grid(sticky="we")
       
        self.columnconfigure(0, weight=1)

    def add_todo(self):
        pass

    def delete_todo(self):
        pass

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")
        self.master.geometry("800x600")
        self.master.columnconfigure(0, weight=3)
        self.master.columnconfigure(1, weight=1)  # added line
        self.master.rowconfigure(0, weight=1)

        self.left_frame = LeftFrame(self.master)
        self.right_frame = RightFrame(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
