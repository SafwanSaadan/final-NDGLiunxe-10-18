import random

# اضافة اسئلة واجاباتها هنا
questions = [
    {"question": "ما الحيوان الذي ينام مرة واحدة في السنة؟",
     "choices": ["قط", "كلب", "نمر", "قرد"],
     "answer": "قرد"},
    {"question": "ما اللون الأكثر شعبية على مستوى العالم؟",
     "choices": ["أحمر", "أصفر", "أزرق", "أخضر"],
     "answer": "أحمر"},
    # إضافة المزيد من الأسئلة هنا
]

# تشغيل البرنامج
while True:
    # اختيار سؤال عشوائي
    question = random.choice(questions)

    # اظهار السؤال والخيارات
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i + 1}. {choice}")

    # استلام الإجابة من المستخدم
    user_answer = input("أختر الإجابة الصحيحة (على سبيل المثال: 1): ")

    # تحقق من الإجابة وعرض النتيجة
    if user_answer.strip() == str(question["choices"].index(question["answer"]) + 1):
        print("احسنت! اجابة صحيحة.")
    else:
        print(f"نأسف! الإجابة الصحيحة هي: {question['answer']}")

    # استعراض ما إذا كان المستخدم يريد استمرار اللعبة أم لا
    user_continue = input("هل تريد أن تسأل سؤالا آخر؟ (نعم/لا): ")
    if user_continue.lower() == "لا":
        break