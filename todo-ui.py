import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class LeftFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=0, sticky="nswe")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Arial 14 bold"))
        style.configure("Treeview", 
            font=('Comic Sans MS', 12),
            rowheight=45,
            foreground="red", 
            background="yellow",
            fieldbackground="yellow") #set row gap and color
        
        self.todo_list = ttk.Treeview(self, columns=("Name", "Due Date", "Priority", "Status"))
        self.todo_list.grid(sticky="nswe")
        self.todo_list.column("#0", anchor="center")
        self.todo_list.column("Name", anchor="center")
        self.todo_list.column("Due Date", anchor="center")
        self.todo_list.column("Priority", anchor="center")
        self.todo_list.column("Status", anchor="center")
        self.todo_list.heading("#0", text="ToDo ID")
        self.todo_list.heading("Name", text="ToDo Name")
        self.todo_list.heading("Due Date", text="Due Date")
        self.todo_list.heading("Priority", text="Priority")
        self.todo_list.heading("Status", text="Status")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.load_todos()

    def load_todos(self):
        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            self.todo_list.insert("", "end", text="You don't have any ToDo's yet, wish to make some?")
            return

        for i, todo in enumerate(todos):
            priority = todo.get("priority", "N/A")  # add default value
            status = todo.get("status", "N/A")  # add default value
            self.todo_list.insert("", "end", text=f"ToDo {i+1}", values=(todo["todo_name"], todo["due_date"], priority, status))

class RightFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=1, sticky="nswe")

        self.add_button = ttk.Button(self, text="Add Todo", command=self.add_todo)
        self.add_button.grid(sticky="we")

        self.delete_button = ttk.Button(self, text="Delete Todo", command=self.delete_todo)
        self.delete_button.grid(sticky="we")

        self.mark_status_button = ttk.Button(self, text="Set Priority", command=self.set_priority)
        self.mark_status_button.grid(sticky="we")

        self.mark_status_button = ttk.Button(self, text="Mark Status", command=self.mark_status)
        self.mark_status_button.grid(sticky="we")

        self.search_button = ttk.Button(self, text="Search Todo", command=self.search_todo)
        self.search_button.grid(sticky="we")

        self.edit_button = ttk.Button(self, text="Update Todo", command=self.update_todo)
        self.edit_button.grid(sticky="we")
        
        self.edit_button = ttk.Button(self, text="Filter Todo", command=self.filter_todo)
        self.edit_button.grid(sticky="we")

        self.columnconfigure(0, weight=1)

    def add_todo(self):
        add_todo_gui = tk.Toplevel(self)
        AddTodoGUI(add_todo_gui)

    def delete_todo(self):
        delete_todo_gui=tk.Toplevel(self)
        DeleteTodoGui(delete_todo_gui)

    def set_priority(self):
        set_priority_gui = tk.Toplevel(self)
        SetPriorityGui(set_priority_gui)

    def mark_status(self):
        mark_status_gui = tk.Toplevel(self)
        MarkStatusGui(mark_status_gui)
    
    def search_todo(self):
        search_todo_gui=tk.Toplevel(self)
        SearchTodoGui(search_todo_gui)

    def update_todo(self):
        update_todo_gui=tk.Toplevel(self)
        UpdateTodoGui(update_todo_gui)
        
    def filter_todo(self):
        filter_todo_gui=tk.Toplevel(self)
        FilterTodoGui(filter_todo_gui)

class AddTodoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Add Todo")
        self.master.geometry("400x150")
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

        due_date_label = ttk.Label(self.master, text="Due Date:", width=25)
        due_date_label.grid(row=1, column=0, sticky="w",pady=5)
        self.due_date = ttk.Entry(self.master, width=40,)
        self.due_date.grid(row=1, column=1,padx=5)

        self.save_button = ttk.Button(self.master, text="Save", command=self.save, width=20)
        self.save_button.grid(row=2, columnspan=2, pady=10)

    def save(self):

        if not self.todo_name.get().strip():
            messagebox.showerror("Error", "Please enter a ToDo Name.", parent=self.master)
            self.master.lift()
            return
        if not self.due_date.get():
            messagebox.showerror("Error", "Please enter a Due Date", parent=self.master)
            self.master.lift()
            return

        due_date = self.due_date.get()
        try:
            due_date = datetime.strptime(due_date, '%d/%m/%Y')
        except ValueError:
            messagebox.showerror("Invalid Date", "The date must be in the format DD/MM/YYYY", parent=self.master)
            self.master.lift()
            return           

        todo = {
            "id": 1,
            "todo_name": self.todo_name.get(),
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


        messagebox.showinfo("Success", "ToDo Added successfully", parent=self.master)
        self.master.lift()
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
            messagebox.showerror("Error", "Please enter a ToDo number", parent=self.master)
            self.master.lift()
            return

        try:
            todo_number = int(todo_number_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid ToDo number", parent=self.master)
            self.master.lift()
            return

        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found", parent=self.master)
            self.master.lift()
            return

        if todo_number > len(todos) or todo_number < 1:
            messagebox.showerror("Error", "ToDo Not Found", parent=self.master)
            self.master.lift()
            return

        todos.pop(todo_number - 1)

        for i in range(len(todos)):
            todos[i]["id"] = i + 1

        with open("todos.json", "w") as file:
            json.dump(todos, file)

        messagebox.showinfo("Success", "ToDo deleted successfully", parent=self.master)
        self.master.lift()
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
        
        todo_number_str = self.todo_number.get()
        if not todo_number_str:
            messagebox.showerror("Error", "Please enter a ToDo number", parent=self.master)
            self.master.lift()
            return

        try:
            todo_number = int(todo_number_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid ToDo number", parent=self.master)
            self.master.lift()
            return

        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found", parent=self.master)
            self.master.lift()
            self.master.destroy()

        if todo_number > len(todos) or todo_number < 1:
            messagebox.showerror("Error", "ToDo Not Found", parent=self.master)
            self.master.lift()
            return

        todos[todo_number - 1]["status"] = self.status_var.get()

        with open("todos.json", "w") as file:
            json.dump(todos, file)

        messagebox.showinfo("Success", "Status marked successfully", parent=self.master)
        self.master.lift()
        self.master.destroy()

class SetPriorityGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Mark ToDo Priority")
        self.master.geometry("380x140")
        self.master.attributes("-topmost", True)
        self.master.resizable(False, False)

        todo_number_label = ttk.Label(self.master, text="Enter the ToDo Number:", width=22)
        todo_number_label.grid(row=0, column=0, sticky="w", pady=5,padx=5)
        self.todo_number = ttk.Entry(self.master, width=15)
        self.todo_number.grid(row=0, column=1, padx=5)

        todo_priority_label = ttk.Label(self.master, text="Set Priority Of ToDo:", width=25)
        todo_priority_label.grid(row=1, column=0, sticky="w", pady=5,padx=5)
        self.todo_priority = ttk.Entry(self.master, width=15)
        self.todo_priority.grid(row=1, column=1, padx=5)

        mark_button = ttk.Button(self.master, text="Save", command=self.set)
        mark_button.grid(row=2, columnspan=3, pady=20)

    def set(self):
        
        todo_number_str = self.todo_number.get()
        if not todo_number_str:
            messagebox.showerror("Error", "Please enter a ToDo number", parent=self.master)
            self.master.lift()
            return

        try:
            todo_number = int(todo_number_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid ToDo number", parent=self.master)
            self.master.lift()
            return

        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found", parent=self.master)
            self.master.lift()
            self.master.destroy()

        if todo_number > len(todos) or todo_number < 1:
            messagebox.showerror("Error", "ToDo Not Found", parent=self.master)
            self.master.lift()
            return

        todo_priority_str = self.todo_priority.get()
        if not todo_priority_str:
            messagebox.showerror("Error", "Please enter a Priority", parent=self.master)
            self.master.lift()
            return

        try:
            todo_priority = int(todo_priority_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid Priority", parent=self.master)
            self.master.lift()
            return
        
        if todo_priority > 100 or todo_priority < 1:
            messagebox.showerror("Error", "Priority should be b/w 1-100",parent=self.master)
            self.master.lift()
            return

        todos[todo_number - 1]["priority"] = todo_priority

        with open("todos.json", "w") as file:
            json.dump(todos, file)

        messagebox.showinfo("Success", "Priority set successfully", parent=self.master)
        self.master.lift()
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
        
        if not self.todo_name.get().strip():
            messagebox.showerror("Error", "Please enter a ToDo Name.", parent=self.master)
            self.master.lift()
            return
        
        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found", parent=self.master)
            self.master.lift()
            return

        todo_name = self.todo_name.get()
        for todo in todos:
            if todo["todo_name"] == todo_name:
                message = f"ToDo Name: {todo['todo_name']}\nDue Date: {todo['due_date']}"
                if "status" in todo or "priority" in todo:
                    message += f"\nTodo Priority: {todo.get('priority', 'N/A')}"
                    message += f"\nTodo Status: {todo.get('status', 'N/A')}"
                else:
                    message += f"\nTodo Priority: {todo.get('priority', 'N/A')}"
                    message += f"\nTodo Status: {todo.get('status', 'N/A')}"


                messagebox.showinfo("Results", message, parent=self.master)
                self.master.lift()
                self.master.destroy()
                return

        messagebox.showerror("Error", "No results found", parent=self.master)
        self.master.lift()
        self.master.destroy()

class UpdateTodoGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Update Todo")
        self.master.geometry("500x250")
        self.master.attributes("-topmost", True)
        self.master.resizable(False, False)
        self.master.columnconfigure(0, weight=1, pad=1)
        self.master.columnconfigure(1, weight=1, pad=1)

        ttk.Label(self.master, text="Enter Todo Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.todo_name = ttk.Entry(self.master, width=40)
        self.todo_name.grid(row=0, column=1, padx=5,pady=5)

        new_todo_name_label = ttk.Label(self.master, text="New ToDo Name:", width=20)
        new_todo_name_label.grid(row=1, column=0, sticky="w",pady=5)
        self.new_todo_name = ttk.Entry(self.master, width=40)
        self.new_todo_name.grid(row=1, column=1,padx=5)

        new_due_date_label = ttk.Label(self.master, text="New Due Date:", width=20)
        new_due_date_label.grid(row=2, column=0, sticky="w",pady=5)
        self.new_due_date = ttk.Entry(self.master, width=40,)
        self.new_due_date.grid(row=2, column=1,padx=5)

        new_priority_label = ttk.Label(self.master, text="New Priority:", width=20)
        new_priority_label.grid(row=3, column=0, sticky="w",pady=5)
        self.new_priority = ttk.Entry(self.master, width=40,)
        self.new_priority.grid(row=3, column=1,padx=5)

        new_status_label = ttk.Label(self.master, text="New Status:", width=20)
        new_status_label.grid(row=4, column=0, sticky="w",pady=10)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Done")
        status_menu = ttk.OptionMenu(self.master, self.status_var, "Not Done", "Done")
        status_menu.grid(row=4, column=1, sticky="w",pady=5,padx=6)

        ttk.Button(self.master, text="Udpate", command=self.search_and_edit_todo).grid(row=5, columnspan=3, pady=20)


    def search_and_edit_todo(self):

        #validate inputs 

        if not self.todo_name.get().strip():
            messagebox.showerror("Error", "Please Enter a ToDo Name.", parent=self.master)
            self.master.lift()
            return

        due_date = self.new_due_date.get()
        try:
            due_date = datetime.strptime(due_date, '%d/%m/%Y')
        except ValueError:
            messagebox.showerror("Invalid Date", "The date must be in the format DD/MM/YYYY", parent=self.master)
            self.master.lift()
            return

        flag = False
        if not self.new_priority.get() and not flag:
            messagebox.showwarning("Warning", "You Haven't entered a value for priority", parent=self.master)
            self.master.lift()
            flag = True
            new_priority = "N/A"

        else:
            try:
                new_priority = int(self.new_priority.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid priority.",parent=self.master)
                self.master.lift()
                return
            
            if new_priority > 100 or new_priority < 1:
                messagebox.showerror("Error", "Priority should be b/w 1-100",parent=self.master)
                self.master.lift()
                return

        # Load the ToDo items from the JSON file
        
        try:
            with open("todos.json", "r") as file:
                todos = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found", parent=self.master)
            self.master.lift()
            return

        # Search for the ToDo item with the given name
        todo_name = self.todo_name.get()
        for todo in todos:
            if todo['todo_name'] == todo_name:
                if self.new_todo_name.get():
                    todo['todo_name'] = self.new_todo_name.get()
                else:
                    todo['todo_name'] = self.todo_name.get()
                
                if self.new_due_date.get():
                    todo['due_date'] = self.new_due_date.get()

                todo['due_date']= self.new_due_date.get()
                if "status" in todo or "priority" in todo:
                    todo['priority']= new_priority
                    todo['status']=  self.status_var.get()                                  

                with open("todos.json", "w") as file:
                    json.dump(todos, file)

                messagebox.showinfo("Success", "Todo Updated successfully", parent=self.master)
                self.master.lift()
                self.master.destroy()
                return
                        
        messagebox.showerror("Error", "Todo not found", parent=self.master)
        self.master.lift()
        return

class FilterTodoGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Mark ToDo Priority")
        self.master.geometry("390x125")
        self.master.attributes("-topmost", True)
        self.master.resizable(False, False)

        todo_number_label = ttk.Label(self.master, text="Filter ToDo's Based on:", width=20, font=(8))
        todo_number_label.grid(row=0, column=0, sticky="w", pady=5,padx=10)

        self.status_var = tk.StringVar()
        self.status_var.set("Done")
        status_menu = ttk.OptionMenu(self.master, self.status_var, "Not Done", "Done")
        status_menu.grid(row=0, column=1, sticky="w",pady=5,padx=6)
        mark_button = ttk.Button(self.master, text="Filter Todo's", command=self.filter)
        mark_button.grid(row=1, columnspan=3, pady=20)

    def load_todos(self):
        with open("todos.json", "r") as file:
            return json.load(file)

    def filter(self):
        todos = self.load_todos()
        filtered_todos = [todo for todo in todos if 'status' in todo and todo['status'] == self.status_var.get()]
        if filtered_todos:
            todos_list = [f"{todo['id']}. Name: {todo['todo_name']}, Due Date: {todo['due_date']}, Priority: {todo.get('priority', 'N/A')}, Status: {todo['status']}" for todo in filtered_todos]
            messagebox.showinfo("Filtered Todo's", "\n".join(todos_list), parent=self.master)
            self.master.lift()
            return

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")
        self.master.geometry("1300x700")
        self.master.columnconfigure(0, weight=3)
        self.master.columnconfigure(1, weight=1)  # added line
        self.master.rowconfigure(0, weight=1)

        self.left_frame = LeftFrame(self.master)
        self.right_frame = RightFrame(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
