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
        add_todo_gui = tk.Toplevel(self)
        AddTodoGUI(add_todo_gui)

    def delete_todo(self):
        pass
    
class AddTodoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Add Todo")
        self.master.geometry("400x230")
        self.master.resizable(False, False)
        self.master.columnconfigure(0, weight=1, pad=1)
        self.master.columnconfigure(1, weight=1, pad=1)
        self.master.rowconfigure(0, pad=3)
        self.master.rowconfigure(1, pad=3)
        self.master.rowconfigure(2, pad=3)
        self.master.rowconfigure(3, pad=3)

        todo_name_label = ttk.Label(self.master, text="ToDo Name:", width=25)
        todo_name_label.grid(row=0, column=0, sticky="w",pady=5)
        self.todo_name = ttk.Entry(self.master, width=40)
        self.todo_name.grid(row=0, column=1,padx=5)

        todo_description_label = ttk.Label(self.master, text="ToDo Description:", width=25)
        todo_description_label.grid(row=1, column=0, sticky="w",pady=5)
        self.todo_description = tk.Text(self.master, width=30, height=5)
        self.todo_description.grid(row=1, column=1,padx=4)

        due_date_label = ttk.Label(self.master, text="Due Date:", width=25)
        due_date_label.grid(row=2, column=0, sticky="w",pady=5)
        self.due_date = ttk.Entry(self.master, width=40,)
        self.due_date.grid(row=2, column=1,padx=5)

        self.save_button = ttk.Button(self.master, text="Save", width=20)
        self.save_button.grid(row=3, columnspan=2, pady=10)

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")
        self.master.geometry("800x600")
        self.master.columnconfigure(0, weight=3)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.left_frame = LeftFrame(self.master)
        self.right_frame = RightFrame(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
