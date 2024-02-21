questions = ("Which of the following is not a primary color?",
             "Who is credited with the discovery of penicillin?",
             "What is the chemical symbol for gold?",
             "What is the powerhouse of the cell?",
             "Which planet is known as the 'Red Planet'?")

options = (("A.Red", "B.Yellow", "C.Green", "D.Orange"),
           ("A.Alexander Flemming", "B.Louis Pasteur", "C.Marie Curie", "D.Isaac Newton"),
           ("A.Au", "B.Ag", "C.Fe", "D.Pb"),
           ("A.Nucleus", "B.Mitochondria", "C.Golgi Apparatus", "D.Endoplasmic Reticulum"),
           ("A.Venus", "B.Mars", "C.Jupiter", "D.Saturn"))

answers = ("D", "A", "A", "B", "B")
question_num = 0
guesses = []
score = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("------------------")
print("      RESULTS     ")
print("------------------")

print("answers: ", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses: ", end =" ")
for guess in guesses:
    print(guess, end=" ")
print()
score = int((score / len(questions)) * 100)
print(f"Your score is {score}%")

if 80 <= score <= 100:
    print("You have good knowledge!!")
elif 50 <= score < 70:
    print("You need to improve your knowledge!!")
elif 35 <= score < 50:
    print("You need to work out asap!!")
else:
    print("You are pathetic!!")
