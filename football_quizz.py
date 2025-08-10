# Store quiz questions and answers in variables
quiz_questions_1 = "Who won the 2022 World Cup?"
quiz_answers_1 = "Argentina"
# Get user input
user_answer_1 = input(quiz_questions_1 + " ")   
# Check the answer
if user_answer_1.lower() == quiz_answers_1.lower():
    print("Correct! Good job")
else:
    print("Incorrect! The correct answer is " + quiz_answers_1 + ".")   
# Store additional quiz questions and answers
quiz_questions_2 = "Which of the team did the winner play with and lost?"
quiz_answers_2 = "France"
# Get user input
user_answer_2 = input(quiz_questions_2 + " ")
# Check the answer   
if user_answer_2.lower() == quiz_answers_2.lower():
    print("Correct! You're doing great") 
else:
    print("Incorrect! The correct answer is " + quiz_answers_2 + ".") 
# Store additional quiz questions and answers  
quiz_questions_3 = "What is the capital of the side that played and lost?"
quiz_answers_3 = "Paris"
# Get user input
user_answer_3 = input(quiz_questions_3 + " ")
# Check the answer   
if user_answer_3.lower() == quiz_answers_3.lower():
    print("Correct! You're exceptional!")
else:
    print("Incorrect! The correct answer is " + quiz_answers_3 + ".")   
# Store additional quiz questions and answers 
quiz_questions_4 = "Who is the top scorer of the 2022 World Cup?"
quiz_answers_4 = "Kylian Mbappe"
# Get user input
user_answer_4 = input(quiz_questions_4 + " ") 
# Check the answer  
if user_answer_4.lower() == quiz_answers_4.lower():
    print("Correct! You're a football expert!")
else:
    print("Incorrect! The correct answer is " + quiz_answers_4 + ".")   
# End of the script