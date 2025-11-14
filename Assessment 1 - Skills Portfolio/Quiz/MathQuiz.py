import tkinter as tk
import random

# edited from https://github.com/madrasacdemy/python/blob/main/educational-math-game.py

counter = 0
questions = 0

def generate_question():
    global answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])
    
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    question_label.config(text=f"{num1} {operation} {num2} = ?")

def check_answer():
    user_answer = entry.get()
    if user_answer.isdigit() and int(user_answer) == answer:
        result_label.config(text="Correct!", fg="green")

        counter += 1
        questions += 1
        print(counter)
        counter_display.config(text=f"Count: {counter}/{questions}")
    else:
        result_label.config(text=f"Wrong! Answer: {answer}", fg="red")


        counter_display.config(text=f"Count: {counter}/{questions}")

    entry.delete(0, tk.END)
    generate_question()

# Create the main window
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

counter_display = tk.Label(root, text=f"Count:", font=("Arial", 14))
counter_display.pack()

generate_question()

root.mainloop()