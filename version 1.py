import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Investment Recommendation Quiz
# -------------------------------

questions = [
    {
        "question": "What is your age?",
        "options": [
            "Under 18",
            "18-30",
            "31-50",
            "Over 50"
        ],
        "scores": [1, 4, 3, 1]
    },

    {
        "question": "How long do you plan to invest for?",
        "options": [
            "Less than 1 year",
            "1-3 years",
            "3-5 years",
            "More than 5 years"
        ],
        "scores": [1, 2, 3, 4]
    },

    {
        "question": "If your investment dropped by 20%, what would you do?",
        "options": [
            "Sell immediately",
            "Sell some of it",
            "Keep it invested",
            "Buy more while prices are lower"
        ],
        "scores": [1, 2, 3, 4]
    },

    {
        "question": "What is your main investment goal?",
        "options": [
            "Keep my money safe",
            "Earn a little extra money",
            "Grow my wealth",
            "Maximise long-term returns"
        ],
        "scores": [1, 2, 3, 4]
    },

    {
        "question": "How much investing experience do you have?",
        "options": [
            "None",
            "A little",
            "Some",
            "A lot"
        ],
        "scores": [1, 2, 3, 4]
    }
]

score = 0
current_question = 0

root = tk.Tk()
root.title("Investment Recommendation Quiz")
root.geometry("600x400")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500)
question_label.pack(pady=20)

choice = tk.IntVar()

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=choice, value=i, font=("Arial", 12))
    rb.pack(anchor="w", padx=40)
    radio_buttons.append(rb)


def next_question():
    global current_question, score

    if choice.get() == -1:
        messagebox.showwarning("Error", "Please select an answer.")
        return

    score += questions[current_question]["scores"][choice.get()]
    current_question += 1

    if current_question == len(questions):
        show_results()
    else:
        load_question()


def load_question():
    choice.set(-1)

    question = questions[current_question]

    question_label.config(text=question["question"])

    for i in range(4):
        radio_buttons[i].config(text=question["options"][i])


def show_results():

    if score <= 8:
        result = (
            "Risk Profile: Conservative\n\n"
            "Suggested investments:\n"
            "- High-interest savings account\n"
            "- Term deposits\n"
            "- Government bonds"
        )

    elif score <= 14:
        result = (
            "Risk Profile: Moderate\n\n"
            "Suggested investments:\n"
            "- Index Funds (ETFs)\n"
            "- Balanced Managed Funds\n"
            "- Dividend-paying Shares"
        )

    else:
        result = (
            "Risk Profile: Growth\n\n"
            "Suggested investments:\n"
            "- Growth ETFs\n"
            "- Individual Shares\n"
            "- Global Index Funds"
        )

    question_label.config(text=result)

    for rb in radio_buttons:
        rb.pack_forget()

    next_button.pack_forget()


next_button = tk.Button(root, text="Next", command=next_question, font=("Arial", 12))
next_button.pack(pady=20)

load_question()

root.mainloop()