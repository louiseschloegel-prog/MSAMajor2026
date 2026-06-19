import random
def difficulty_level():
    while True:
        try:
            selected_level = int(input("Enter Level 1, 2, 3: "))
            if (selected_level > 3) or (selected_level < 1):
                print("ERROR: Invaild input!")
                continue
            break
        except:
            print("ERROR: Invaild input!")
        
        



    return selected_level

def number_questions():
    while True:
        try:
            number_of_questions = int(input("Enter number of questions to ask: 3 to 10: "))
            if (number_of_questions > 10) or (number_of_questions < 3):
                print("ERROR: Please enter an integer between 3 and 10!")
                continue
            break
        except:
            print("ERROR: Please enter  an integer between 3 and 10!")
    return number_of_questions





def main():
    level_difficulty = difficulty_level()
    number_of_questions = number_questions()
    correct_user_answers = 0
    random_generator = random.Random()
    
    for question_number in range(number_of_questions):

        if level_difficulty == 1:
            X = random_generator.randint(0,10)
            Y = random_generator.randint(0,10)
        elif difficulty_level == 2:
            X = random_generator.randint(10,99)
            Y = random_generator.randint(10,99)
        elif difficulty_level == 3:
            X = random_generator.randint(100,999)
            Y = random_generator.randint(100,999)

        
        correct_answer = X + Y
        for question_number1 in range(3):
            try:
                user_answer = int(input(f"{X} + {Y} = "))
            except:
                print("WRONG!!!!")
                continue

            if user_answer == correct_answer:
                print("CORRECT!!!!")
                correct_user_answers = correct_user_answers + 1
                break   
            else:   
                print("WRONG!!!!!")
                continue
            
        
        if question_number1 == 2:
            print(f"{X} + {Y} = {int(correct_answer)}\n")
            
                
    grade = correct_user_answers / number_of_questions
    user_score = grade * 100
    print(f"your score is: {user_score: .2f}%")
    

       
        


    

main()

    

#  Valid options are 1, 2, or 3.If the user does not input 1, 2, or 3, the program should prompt again.
#return selected level





# The program should prompt the user for the number of questions to ask. 
# Valid options are 3 - 10.If the user does not input 3 - 10, the program should prompt again.
#return the selected level





# The program should randomly generate the number of questions the user entered in the previous step.
#call the functions
# make two variables that adress the two inputs:
#number_of_questions = question_numbers
#user_level = level_input

#use an if statement that if the user selected level one:
# If the user chose difficulty level 1 then X and Y should be 1 digit, non-negative, numbers (0 - 9).
# it should already be defined in the main loop then it will print:
# random_value1 + random_value1



#using an if statement it will 
#  For example, if the user entered 5 for the number of questions the program should ask, the program should then generate 5 math problems. Likewise, if they entered 10 the program should generate 10 problems. The problems should be formatted as X + Y = , wherein each of X and Y is a non-negative integer with difficulty level of digits. For example:


# If the user chose difficulty level 2 then X and Y should be 2 digit, non-negative, numbers (10 - 99).
# If the user chose difficulty level 3 then X and Y should be 3 digit, non-negative, numbers (100 - 999).
# Your program does not need to support operations other than addition (+).
# The program should prompt the user to solve each problem.
# If an answer is correct the program should output CORRECT!!! and the prompt the user to answer the next question.
# If an answer is not correct (or not even a number), the program should output WRONG!!! and prompt the user again, allowing the user up to three tries in total to answer the question. If the user has still not answered correctly after three tries, the program should output the correct answer and the prompt the user to answer the next question.
# The program should ultimately output the user’s score and the percentage (formatted to 2 decimal places) correct.
# End the program