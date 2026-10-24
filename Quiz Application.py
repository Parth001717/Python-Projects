# Quiz Application

def start_quiz():
    questions = [
        {
            "question": "1. Which language is used to create this quiz application?",
            "options": ["A. HTML", "B. CSS", "C. Python", "D. SQL"],
            "answer": "C"
        },
        {
            "question": "2. Which function is used to take input from the user?",
            "options": ["A. print()", "B. input()", "C. scan()", "D. get()"],
            "answer": "B"
        },
        {
            "question": "3. Which symbol is used for a comment in Python?",
            "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
            "answer": "C"
        },
        {
            "question": "4. Which data type stores multiple values in an ordered collection?",
            "options": ["A. List", "B. Integer", "C. Boolean", "D. String"],
            "answer": "A"
        },
        {
            "question": "5. Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def", "C. fun", "D. define"],
            "answer": "B"
        }
    ]

    score = 0

    print("=" * 40)
    print("       WELCOME TO QUIZ APPLICATION")
    print("=" * 40)

    name = input("Enter your name: ")

    print("\nHello", name + "!")
    print("Choose the correct option for each question.")
    print("Enter A, B, C, or D.\n")

   
    for q in questions:
        print(q["question"])

        
        for option in q["options"]:
            print(option)

        answer = input("Your answer: ").upper()

   
        if answer == q["answer"]:
            print("Correct answer! ✓\n")
            score += 1
        else:
            print("Wrong answer! ✗")
            print("Correct answer:", q["answer"], "\n")

    
    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    
    print("=" * 40)
    print("             QUIZ RESULT")
    print("=" * 40)

    print("Name:", name)
    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Wrong Answers:", total_questions - score)
    print("Percentage:", percentage, "%")

    
    if percentage >= 80:
        print("Performance: Excellent! ")
    elif percentage >= 60:
        print("Performance: Good! ")
    elif percentage >= 40:
        print("Performance: Average.")
    else:
        print("Performance: Needs Improvement.")

    print("=" * 40)



start_quiz()