import os
class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list
    
    def sill_has_question(self):
        return self.question_num < len(self.question_list)

    
    def next_question(self):
        
        current_question = self.question_list[self.question_num]
        
        self.question_num += 1  
        user_answer = input(f'Q{self.question_num}: {current_question.text} (True/false) : \n').capitalize()
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self, user_answer, current_answer):
        
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print('you got it!!')
            os.system('cls')
        
            
            
            
        else:
            print('you got it wrong')
            print(f'the correct answer was: {current_answer}.')
            os.system('cls')
        
        
        print(f'your total score is: {self.score} / {self.question_num}')
        
            
        


        
                

        


            
            
            



    
























