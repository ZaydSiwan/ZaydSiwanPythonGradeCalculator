# Zayd Siwan
# Grade Calculator Using Tkinter Messagebox

import tkinter as tk
from tkinter import messagebox

# Code for the different GUI features such as: size, text, and the buttons

class GradeCalculatorGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('260x125')

        self.tests_grade_label = tk.Label(self.main_window, text='Tests Grade')
        self.tests_grade_label.pack()
        self.tests_grade_entry = tk.Entry(self.main_window)
        self.tests_grade_entry.pack()

        self.labs_grade_label = tk.Label(self.main_window, text='Labs Grade')
        self.labs_grade_label.pack()
        self.labs_grade_entry = tk.Entry(self.main_window)
        self.labs_grade_entry.pack()

        self.exams_grade_label = tk.Label(self.main_window, text='Exams Grade')
        self.exams_grade_label.pack()
        self.exams_grade_entry = tk.Entry(self.main_window)
        self.exams_grade_entry.pack()

        self.grade_average_label = tk.Label(self.main_window, text='Grade Average')
        self.grade_average_label.pack()
        self.grade_average_result = tk.Label(self.main_window, text='---')
        self.grade_average_result.pack()

        self.calculate_button = tk.Button(self.main_window, text='Calculate', command=self.calculate_average)
        self.calculate_button.pack(side='left')
        self.quit_button = tk.Button(self.main_window, text='Quit', command=self.main_window.quit)
        self.quit_button.pack(side='left')

# Actual calculator portion using floats as they would be used for normal grading
    
    def calculate_average(self):
        try:
            tests_grade = float(self.tests_grade_entry.get())
            labs_grade = float(self.labs_grade_entry.get())
            exams_grade = float(self.exams_grade_entry.get())

            grade_average = (tests_grade * 0.2) + (labs_grade * 0.3) + (exams_grade * 0.5)
            self.grade_average_result.config(text=str(grade_average))

        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter numeric values.')

    def run(self):
        self.main_window.mainloop()

# Initializers 

if __name__ == '__main__':
    grade_calculator = GradeCalculatorGUI()
    grade_calculator.run()
