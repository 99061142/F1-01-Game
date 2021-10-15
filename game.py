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

    "time": {
        "easy": 5,
        "medium": 15,
        "hard": 30
    }
}

def sum_questions(difficulty):
    
    questions = sum_information["questions"][difficulty] # Array with the questions
    time = sum_information["time"][difficulty] # Time for the user to answer the question
    
    for sum_str in questions:
    
        question = 'whats "' + sum_str + '" ?: '

        user_chosen = False
    
        while not user_chosen: 
            user_answer = input(question)


            try:
                user_answer = int(user_answer)

            except:
                print("Choose a number")

            else:
                user_chosen = True

                answer = eval(sum_str)

                if user_answer == answer:
                    print("Thats correct!")
                
                else:
                    fail_message = "Thats not correct, the answer is: " + str( int(answer) )

                    print(fail_message)




def startScreen():
    
    difficulties = list ( sum_information["questions"].keys() ) # Makes an array of all the keys of the difficulties

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


difficulty = startScreen()
sum_questions(difficulty)