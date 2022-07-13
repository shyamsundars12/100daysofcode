from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for quiz in question_data:
    question_text = quiz["text"]
    question_answer = quiz["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
q1 = QuizBrain(question_bank)
while q1.still_has_questions():
    q1.next_question()

print("you have completed the quiz")
print(f"your final score was:{q1.score}/{q1.question_number}")
