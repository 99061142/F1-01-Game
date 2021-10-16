easy_lost = False # If the user is on the lowest difficulty

# Array for the sums, and the time the user gets
sum_information = {
    "questions": {
        "easy": [
            "3 - 6",
            "55 + 31",
            "74 + 31",
            "101 - 54",
            "-5 + -4"
        ],

        "medium": [
            "-5 - 47",
            "64 + 306",
            "6 * 23",
            "64 - 87",
            "789 * 2"
        ],

        "hard": [
            "342 / 2",
            "443 + 87",
            "593 * 3",
            "396 / 3",
            "583 - 957"
        ]
    },

    "max_fails": {
        "easy": 0,
        "medium": 0,
        "hard": 1
    }
}

difficulties = list ( sum_information['questions'].keys() ) # Makes an array of all the possible difficulties




# Ask the questions to the user

def sum_questions(difficulty):

    change_difficulty = False

    questions = sum_information['questions'][difficulty] # Array with the questions
    max_fails = sum_information['max_fails'][difficulty] # Max fails the user can make for the difficulty


    print('This questions are for the difficulty: "' + difficulty + '"')

    
    for sum_str in questions:
    
        user_chosen = False

        question = 'whats "' + sum_str + '" ?: '
    
        while not user_chosen and not change_difficulty: 
            
            user_answer = input(question)


            try:
                user_answer = int(user_answer)

            except:
                print("Choose a number")

            else:
                user_chosen = True

                answer = eval(sum_str) # Calculate the sum


                if user_answer == answer:
                    print("Thats correct!")
                
                else:
                    fail_message = "That is not correct, the answer was: " + str( int(answer) )

                    print(fail_message)


                    if max_fails > 0:
                        max_fails -= 1 # Decrease the fails the user has

                    else: 
                        try:
                            difficulty = difficulties.index(difficulty - 1) # Check if the difficulty could be decreased
                        
                        except: 
                            easy_lost = True

                        else: 
                            easy_lost = False

                        
                        change_difficulty = True # Go out of the loop with the questions

    else:
        return easy_lost # Return if the users difficulty must be decreaed



# Change the difficulty for the questions

def change_difficulty(difficulty, user_lost):

    question_index = difficulties.index(difficulty) # Get the index of the difficulty

    # Check which difficulty the user has, and decrease it
    
    if user_lost:
        difficulty = difficulties[question_index - 1] # Decrease the difficulty
    
    else:
        difficulty = difficulties[question_index + 1] # Increase the difficulty

    return difficulty




# Ask the user which mode he wants to begin with

def startScreen():

    difficulties_str = ", ".join(difficulties[:-1]) + " or " + difficulties[-1] # Add a ',' at the end of the value, and if its the last value it adds a 'or'


    print("Which mode you want to play?")

    choosing = True

    while choosing:
        
        question = "You have a choice between: " + difficulties_str + ": "
        
        difficulty = input(question).lower()


        try:
            difficulties.index(difficulty)

        except: 
            print("Choose between the 3 modes")

        else:   
            choosing = False


    return difficulty




difficulty = startScreen() # Ask the user which mode he wants to begin with


while not easy_lost:
    user_lost = sum_questions(difficulty) # Ask the questions to the user

    if difficulty != "easy":
        difficulty = change_difficulty(difficulty, user_lost) # Change the difficulty with the result of the user

    else:
        easy_lost = True