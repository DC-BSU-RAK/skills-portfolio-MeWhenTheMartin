from tkinter import *
import tkinter as tk
import random

# edited from https://github.com/madrasacdemy/python/blob/main/educational-math-game.py

counter = 0
questions = 0

diff = 1
diff_name = "Easy"

minnum = 0
maxnum = 0

def generate_question():
    global answer
    global minnum
    global maxnum

    operation = random.choice(["+", "-", "*"])
    if diff == 1:
        minnum, maxnum = 1, 9
    if diff == 2:
        minnum, maxnum = 10, 99
    if diff == 3:
        minnum, maxnum = 1000, 9999

    num1 = random.randint(minnum, maxnum)
    num2 = random.randint(minnum, maxnum)
    
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    question_label.config(text=f"{num1} {operation} {num2} = ?")

def check_answer():
    global counter
    global questions
    user_answer = entry.get()
    if user_answer.isdigit() and int(user_answer) == answer:
        result_label.config(text="Correct!", fg="green")

        counter += 1
        questions += 1
        print(counter)
        counter_display.config(text=f"Count: {counter}/{questions}")
    else:
        result_label.config(text=f"Wrong! Answer: {answer}", fg="red")

        questions += 1
        counter_display.config(text=f"Count: {counter}/{questions}")

    entry.delete(0, tk.END) # clear the user's input
    generate_question()

def get_diff():
    global diff
    global diff_name
    # cycle 
    if diff == 3:
        diff = 1
    else:
        diff += 1

    # convert int into str
    if diff == 1:
        diff_name = "Easy"
    if diff == 2:
        diff_name = "Medium"
    if diff == 3:
        diff_name = "Hard"

    difficulty_button.config(text=f"{diff_name}")
    entry.delete(0, tk.END) # clear the user's input
    global counter 
    global questions
    counter = 0
    questions = 0
    counter_display.config(text=f"Count: {counter}/{questions}")
    result_label.config(text=f"")
    generate_question()

    print(f"{diff}")
    

# main window
root = tk.Tk()
root.title("Educational Math Game")
root.geometry("500x200")

question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

counter_display = tk.Label(root, text=f"Count: 0/0", font=("Arial", 14))
counter_display.pack()

difficulty_button = tk.Button(root, text=f"{diff_name}", command=get_diff)
difficulty_button.pack()

generate_question()

root.mainloop()