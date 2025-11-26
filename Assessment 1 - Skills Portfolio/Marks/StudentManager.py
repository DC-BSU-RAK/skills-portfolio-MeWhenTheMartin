file_path = '_Resources/studentMarks.txt'  # Example: data.txt contains "ID, NAME, SCORES"
                                           # ['1345', 'John Curry', '8', '15', '7', '45']
data = []
studentData = []
current = []

with open(file_path, 'r') as file:
    for line in file:
        # Remove leading/trailing whitespace and split by comma
        elements = line.strip().split(',')
        data.append(elements)

# DEBUG
#print(f"First Student: {data[1]}")
#print(f"Name: {data[1]} Student ID: {data[0]}")
#print(f"Scores: {data[2]}, {data[3]}, {data[4]}, {data[5]}")

def readStudent(studentNum):

    global studentData

    studentData = data[studentNum]
    ID = studentData[0]
    Name = studentData[1]
    Scores = studentData[2:5]

    print(f"ID: {ID} Name: {Name}\n Scores: {Scores}")

def studentPage(page):

    pageNum = page * 2
    count = pageNum
    print(f"\nPAGE NO.{page}\n")

    for _ in range(5):
        count += 1
        readStudent(count)

studentPage(1)
studentPage(2)
    

# Main Window
from tkinter import * 