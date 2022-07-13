class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question=(self.question_list[self.question_number])
        self.question_number += 1
        user_in = input(f"Q{self.question_number} : is {question.text}..Please choose whether (True/False)")
        self.check_answer(user_in, question.answer)

    def check_answer(self, user_in, correct_answer):
        if user_in == correct_answer:
            self.score += 1
            print("it is a correct answer")
            print(f"the correct answer was :{correct_answer}")
            print(f"your final score is{self.score}/{self.question_number}")
            print("\n")
        else:
            print("it is a wrong answer!!")
            print(f"the correct answer was :{correct_answer}")
            print(f"your final score is{self.score}/{self.question_number}")
            print("\n")

