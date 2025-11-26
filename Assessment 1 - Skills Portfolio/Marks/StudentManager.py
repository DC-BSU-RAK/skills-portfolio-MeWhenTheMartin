file_path = '_Resources/studentMarks.txt'  # Example: data.txt contains "ID, NAME, SCORES"
                                           # ['1345', 'John Curry', '8', '15', '7', '45']

# Lists
data = []
studentData = []
current = []
# Other Vars
is_on = True
sort = 0 # 0 = Default 1 = Highest 2 = Lowest
PageN = 1
studentN = 0
___ = "                                                                      "

with open(file_path, 'r') as file:
    for line in file:
        # Remove leading/trailing whitespace and split by comma
        elements = line.strip().split(',')
        data.append(elements)

def readStudent(studentNum):

    global studentData
    x = 0

    studentData = data[studentNum] # Split into different DataSets for formatting label text
    ID = studentData[0]
    Name = studentData[1]
    Scores = studentData[2:5]
    Exam = studentData[5]
    Total = int(Scores[0]) + int(Scores[1]) + int(Scores[2]) + int(Exam)
    Results = (Total/160) * 100

    print(f"Results: {Total} | {Results}%")
    x += 1

    cirno = f"student_scores{studentNum}|{x}" 
    print(f"Cirno: {cirno}") # student number in console

    global studentN
    if pageN == 1:
        studentN = studentNum - 2
    else:
        studentN = studentNum - 4

    cirno_text = f"{___}\nID: {ID} | Name: {Name}\nScores: {Scores[0]},{Scores[1]},{Scores[2]} | Exam {Exam}\nResults: {Total} | {Results}%"

    if studentN == 1:
        student_scores1.config(text=cirno_text)
    if studentN == 2:
        student_scores2.config(text=cirno_text)
    if studentN == 3:
        student_scores3.config(text=cirno_text)
    if studentN == 4:
        student_scores4.config(text=cirno_text)
    if studentN == 5:
        student_scores5.config(text=cirno_text)
    # Print for Console Debugging
    print(f"ID: {ID} Name: {Name}\n Scores: {Scores}\n Exam: {Exam}")

def studentPage(page):
    pageNum = page * 2
    count = pageNum
    print(f"\nPAGE NO.{page}\n")

    for _ in range(5): # Can't use for loops for multiple labels
        count += 1
        readStudent(count)

def toggle():

    global is_on
    global pageN

    if is_on: # Page 1
        pageN = 1
        studentPage(1)
        display_button.config(text="Next Page")
        is_on = False

    else: # Page 2
        pageN = 2
        studentPage(2)
        display_button.config(text="Previous Page")
        is_on = True

from tkinter import *
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("List in Label")

# Create a Label widget
my_label = tk.Label(root, text="Student Manager")
my_label.pack(pady=0)

student_id = tk.Label(root, text=f"{___}\nStudent Page", justify=tk.LEFT)
student_id.pack(pady=0)

student_scores1 = tk.Label(root, text=f"{___}\nScores", justify=tk.LEFT)
student_scores1.pack(pady=0)

student_scores2 = tk.Label(root, text=f"{___}\nScores", justify=tk.LEFT)
student_scores2.pack(pady=0)

student_scores3 = tk.Label(root, text=f"{___}\nScores", justify=tk.LEFT)
student_scores3.pack(pady=0)

student_scores4 = tk.Label(root, text=f"{___}\nScores", justify=tk.LEFT)
student_scores4.pack(pady=0)

student_scores5 = tk.Label(root, text=f"{___}\nScores", justify=tk.LEFT)
student_scores5.pack(pady=0)

display_button = tk.Button(root, text="PRESS ME", command=toggle)
display_button.pack()

root.mainloop()