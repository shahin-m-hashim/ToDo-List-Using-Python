import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

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
        
        self.mark_status_button = ttk.Button(self, text="Mark Status", command=self.mark_status)
        self.mark_status_button.grid(sticky="we")
        
        self.search_button = ttk.Button(self, text="Search Todo", command=self.search_todo)
        self.search_button.grid(sticky="we")        
       
        self.columnconfigure(0, weight=1)

    def add_todo(self):
        add_todo_gui = tk.Toplevel(self)
        AddTodoGUI(add_todo_gui)

    def delete_todo(self):
        delete_todo_gui=tk.Toplevel(self)
        DeleteTodoGui(delete_todo_gui)
        
    def mark_status(self):
        mark_status_gui = tk.Toplevel(self)
        MarkStatusGui(mark_status_gui)
        
    def search_todo(self):
        search_todo_gui=tk.Toplevel(self)
        SearchTodoGui(search_todo_gui)
    
class AddTodoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Add Todo")
        self.master.geometry("400x230")
        self.master.attributes("-topmost", True)
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

        self.save_button = ttk.Button(self.master, text="Save",command=self.save, width=20)
        self.save_button.grid(row=3, columnspan=2, pady=10)
        
    def save(self):

        if not self.todo_name.get().strip():
            messagebox.showerror("Error", "Please enter a name for the ToDo.")
            return
        if not self.due_date.get():
            messagebox.showerror("Error", "Please enter a due date")
            return

        due_date = self.due_date.get()
        try:
            due_date = datetime.strptime(due_date, '%d/%m/%Y')
        except ValueError:
            messagebox.showerror("Invalid Date", "The date must be in the format DD/MM/YYYY")
            return           

        todo = {
            "id": 1,
            "todo_name": self.todo_name.get(),
            "todo_description": self.todo_description.get("1.0", "end-1c"),
            "due_date": self.due_date.get(),
        }

        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
                todo["id"] = len(todos) + 1
        except FileNotFoundError:
            todos = []

        todos.append(todo)

        with open("todos.json", "w") as file:
            json.dump(todos, file)

        self.master.destroy()
        
class DeleteTodoGui():
    def __init__(self, master):
        self.master = master
        self.master.title("Delete ToDo")
        self.master.geometry("330x100")
        self.master.attributes("-topmost", True)
        self.master.resizable(False, False)

        todo_number_label = ttk.Label(self.master, text="Enter the ToDo Number:", width=22)
        todo_number_label.grid(row=0, column=0, sticky="w", pady=5,padx=5)
        self.todo_number = ttk.Entry(self.master, width=15)
        self.todo_number.grid(row=0, column=1, padx=5)

        delete_button = ttk.Button(self.master, text="Delete", command=self.delete)
        delete_button.grid(row=3, columnspan=2, pady=10)

    def delete(self):
        todo_number_str = self.todo_number.get()
        if not todo_number_str:
            messagebox.showerror("Error", "Please enter a ToDo number")
            return

        try:
            todo_number = int(todo_number_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid ToDo number")
            return

        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
            return

        if todo_number > len(todos) or todo_number < 1:
            messagebox.showerror("Error", "Invalid ToDo number")
            return

        todos.pop(todo_number - 1)

        for i in range(len(todos)):
            todos[i]["id"] = i + 1

        with open("todos.json", "w") as file:
            json.dump(todos, file)

        messagebox.showinfo("Success", "ToDo deleted successfully")
        self.master.destroy()
    
class MarkStatusGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Mark ToDo Status")
        self.master.geometry("380x140")
        self.master.attributes("-topmost", True)
        self.master.resizable(False, False)

        todo_number_label = ttk.Label(self.master, text="Enter the ToDo Number:", width=22)
        todo_number_label.grid(row=0, column=0, sticky="w", pady=5,padx=5)
        self.todo_number = ttk.Entry(self.master, width=15)
        self.todo_number.grid(row=0, column=1, padx=5)

        todo_number_label = ttk.Label(self.master, text="Mark The Entered ToDo As:", width=25)
        todo_number_label.grid(row=1, column=0, sticky="w", pady=5,padx=5)

        self.status_var = tk.StringVar()
        self.status_var.set("Done")
        status_menu = ttk.OptionMenu(self.master, self.status_var, "Not Done", "Done")
        status_menu.grid(row=1, column=1, pady=1)

        mark_button = ttk.Button(self.master, text="Save", command=self.mark)
        mark_button.grid(row=2, columnspan=3, pady=20)

    def mark(self):
        try:
            todo_number = int(self.todo_number.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")
            return

        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
            return

        if todo_number > len(todos) or todo_number < 1:
            messagebox.showerror("Error", "Invalid ToDo number")
            return

        todos[todo_number - 1]["status"] = self.status_var.get()

        with open("todos.json", "w") as file:
            json.dump(todos, file)

        messagebox.showinfo("Success", "Status marked successfully")
        self.master.destroy()

class SearchTodoGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Search ToDo")
        self.master.geometry("330x100")
        self.master.attributes("-topmost", True)
        self.master.resizable(False, False)

        ttk.Label(self.master, text="Enter ToDo Name:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.todo_name = ttk.Entry(self.master, width=20)
        self.todo_name.grid(row=0, column=1, padx=10,pady=5)

        ttk.Button(self.master, text="Search", command=self.search).grid(row=2, columnspan=3, pady=20)

    def search(self):
        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
            return

        todo_name = self.todo_name.get()
        for todo in todos:
            if todo["todo_name"] == todo_name:
                message = f"ToDo Name: {todo['todo_name']}\nToDo Description: {todo['todo_description']}\nDue Date: {todo['due_date']}"
                if "status" in todo:
                    message += f"\nStatus: {todo['status']}"
                messagebox.showinfo("Results", message)
                self.master.destroy()
                return
        messagebox.showerror("Error", "No results found")
        self.master.destroy()        
        
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
