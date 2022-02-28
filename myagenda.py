from tkinter import *
from tkinter import ttk
import tkinter as tk
from calculator import Calculator
from notebook import Notebook


# Constants for fonts and colors


class MyAgenda(object):
    """An application for organizing classwork."""
    def __init__(self):
        """Sets up the application."""
        # Main window initialization

        self.windowRoot = Tk()
        self.windowRoot.title("MyAgenda")
        self.windowRoot.iconbitmap('icon.ico')
        self.windowRoot.geometry("800x960")
        self.windowRoot.resizable(False, False)

        self.buttonFrame = self.createButtonFrame()

        # Button options for the main window in a list, for easier maintenance
        self.commandButtons = ["Add/Edit Courses", "Add/Edit Chapter", "Add/Edit Tasks", "Calculator"]
        self.createButtons()

        self.createNotebook()

    def callCommand(self, command):
        """Calls the relevant module when its respective button is clicked."""
        if command == "Calculator":
            return Calculator()

    def createButtons(self):
        """Creates a vertically-oriented list of buttons based on the number of
        commands listed in commandButtons."""
        i = 0
        for item in self.commandButtons:
            button = tk.Button(self.buttonFrame, text=str(item), padx=5, pady=10,
                               command=lambda x=item: self.callCommand(x))
            button.grid(row=i)
            i += 1

    def createButtonFrame(self):
        """Creates the frame that houses the buttons."""
        frame = tk.LabelFrame(self.windowRoot, pady=300)
        frame.grid(row=0, column=0)
        return frame

    def createNotebook(self):
        """Creates the at-a-glance agenda interface."""
        # Create a treeview named 'notebook'
        notebook = ttk.Treeview()

        # Create the columns of 'notebook'
        notebook['columns'] = ("Course", "Chapter", "Task")

        # Name and format the columns of 'notebook'
        notebook.column("#0", width=0, stretch=NO)  # This line hides the "invisible" column placed by treeview module
        notebook.column("Course", anchor=W, width=120)
        notebook.heading("Course", text="Course", anchor=W)
        notebook.column("Chapter", anchor=W, width=160)
        notebook.heading("Chapter", text="Chapter", anchor=W)
        notebook.column("Task", anchor=W, width=400)
        notebook.heading("Task", text="Task", anchor=W)

        # Test data to fill 'notebook'
        testData = [
            ["Math", "Chapter 1", "Homework"],
            ["Math", "Chapter 1", "Study for quiz"],
            ["Biology", "Unit 2", "Study for quiz"],
            ["History", "Unit 2", "Write report"]
        ]

        # A for-loop inserts the test data records into 'notebook'
        for record in testData:
            notebook.insert(parent='', index='end', values=(record[0], record[1], record[2]))

        # Attach 'notebook' to the grid of the main window
        notebook.grid(row=0, column=1, sticky=N)
        return notebook

    def run(self):
        """Runs the main loop."""
        self.windowRoot.mainloop()


# Entry point of the program
if __name__ == "__main__":
    agenda = MyAgenda()
    agenda.run()
