import tkinter as tk
import random

def ask_question():
    question = "Which of the following ls commands, when executed, will only show information about the directory itself? (choose two)"
    options = ['ls -h','ls -d','ls -ld','ld -a']
    answers = ['ls -d','ls -ld']

    root = tk.Tk()
    root.title("Quiz")
    
    # إعداد واجهة المستخدم
    question_label = tk.Label(root, text=question)
    question_label.pack()

    options_with_indices = list(enumerate(options, start=1))
    random.shuffle(options_with_indices)  # يقوم بترتيب الخيارات بشكل عشوائي مع الفهارس

    for index, option in options_with_indices:
        option_label = tk.Label(root, text=f"{index}. {option}")
        option_label.pack()

    answer_entry = tk.Entry(root)
    answer_entry.pack()
    
    result_label = tk.Label(root, text="")

    def check_answer():
        user_answer = answer_entry.get()
        user_answer = user_answer.split(",")  # تجزئة الإجابات المدخلة
        user_answer = [int(answer.strip()) for answer in user_answer]  # تحويل القيم من نص إلى عدد صحيح

        correct_options = [index for index, option in options_with_indices if option in answers]

        if set(user_answer) == set(correct_options):
            result_label.config(text="Your answer is correct!")
        else:
            result_label.config(text=f"Your answer is incorrect! The correct answers are {correct_options}.")

    check_button = tk.Button(root, text="Check Answer", command=check_answer)
    check_button.pack()

    result_label.pack()

    root.mainloop()

ask_question()