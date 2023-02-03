# ToDo List App In Python and JSON
* A simple and efficient ToDo list application built using Python that helps users keep track of their tasks, prioritize and manage their ToDo's. This ToDo list app is designed with a user-friendly GUI, making it easy to use and accessible to everyone.The program utilizes classes to make it easy for users to navigate through the different GUI's and its functionality. Additionally, the program has been optimized to include user validation,error handling and ensuring that any invalid input will be promptly dealt with, preventing any errors.

* The program uses two frames LeftFrame and RightFrame. The LeftFrame, displays ToDo items that are loaded from a JSON file. The RightFrame on the other hand, creates several buttons to perform operations on the ToDo items such as adding, deleting, setting priority, marking status... etc. However,it still does not handle database storage like Sql, but the ToDo and related Information will not be lost once the program is closed.

![An example image](https://github.com/shahin-m-hashim/ToDo-List-Using-Python/blob/main/todo_quick_reference.png)

## Features

* User-friendly interface.
* Display a list of ToDo's.
* Search for specific ToDo's.
* Add, Delete, And Update ToDo's.
* Set the priority of specific todo.
* Proper resizing for the UI interface.
* Validates user inputs and handles errors.
* Mark the status of a todo (completed or not).
* Filter ToDo's based on status (completed or not).
* Store and retrieve todo information in a JSON file.

## Drawbacks

This Python program was written for learning and improving knowledge on UI interface provided by python's Tkinter library.

* No Remainder: Doesn't support functionality to set remainders based on due date of the todo.
* No Automated Backup: Users need to manually backup their data(JSON file) in case of any loss.
* Dependence on JSON Files: The todo app uses JSON files for data storage, which can become a drawback for some users.
* No Real Time Sync b/w Left and Right Frame: Sorry to say that One major drawback of the Todo app is that it currently doesn't have the ability to update the left frame with respect to all the functionalities in the right frame. This can result in an inconsistent user experience. You may need to close and rerun the code to see changes in the left Frame.

## Getting Started
* Python 3: To use this program, you will need to have Python installed on your computer. You can download it from the official website if you do not have it already.
* Tkinter GUI library: For the UI to work you should have tkinter library installed, to install : pip install tk. You could also refer- https://docs.python.org/3/library/tkinter.html

## Getting Started

* Clone the repository to your local machine 
* Or You can simply download the zip file and use it.
* Navigate to the downloaded directory
* Open up the terminal
* Type python filename.py or py filename.py to run the program
* Alternatively you can simply use any application like pycharm,vscode etc

## Usage

Once the program is running, you will be prompted with a easy UI interface that allows you to perform different actions

* At First Left Frame won't have any todo. Start by creating some using the Right Frame.

* To add a new todo, you can fill in the required information in the fields provided, such as name and due date. After you fill in the required information, can click on the "Add Todo" button to add the todo to your todo list. Intially your todo will have no priority and status, you can specify it later if you want to

* To delete a todo, you can enter the todo number you wish to remove in the field provided. Then click on the "delete" button.

* To set priority for a todo, you can enter the priority numbers b/w 1 & 100 for the todo you are looking for in the field provided, and then click on the "Set priority" button.

* To set status for a todo, you can enter the todo number you wish to remove in the field provided and choose either done or not done depending on whether you have completed it or it is yet to finish. and then click on the "Set Status" button.

* To update a todo, you can enter the name of the todo you wish to update, then fill in the new information in the fields provided and click "Update" button.

* To search for a todo, you can enter the name of the todo you are looking for in the field provided, and then click on the "Search" button.

* To filter contacts based on done and not done, you can use the "Filter Todo" button.

## Contributing
If you find a bug or have an idea for an improvement,like how i can achieve synchronization b/w left and right frame, please open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the <a href="https://github.com/shahin-m-hashim/ToDo-List-Using-Python/blob/main/LICENSE">LICENSE.md</a> 

## Acknowledgments
Enjoy the Todo app and keep your Todos easy and organized
Please keep in mind the drawbacks of the program before using it.
