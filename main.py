from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import GuiInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    print(question_text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
GuiInterface(quiz)

# while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
