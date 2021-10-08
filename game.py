import random


# Array for the rock, paper and scissors game
rps_information = {
    "steen": {
        "lose": "schaar"
    },

    "papier": {
        "lose": "steen"
    },

    "schaar": {
        "lose": "papier"
    }
}


# Show the user why he lost
def loseScreen(info):
    print("\n"
        "------------------------",
        info,
        "------------------------",
    "\n")
    exit()




# Guess higher than the enemy (number between 1/6)
def diceGuessing():

    dice_roll = True # Loop through the question

    while dice_roll:

        diceAmount_enemy = random.randint(1, 6) # Choose a number between 1 and 6

        user_guess = input("Raad een getal wat gelijk of hoger is wat de tegenstander heeft gegooid (getal van 1 t/m 6): ")
        
        # Check if the user chose a number between 1 and 6
        try:
            user_guess = int(user_guess)
            if user_guess >= 1 and user_guess <= 6:
                return True

        except: 
            print("Vul een geldig getal in")

        # If it did go correctly
        else:

            # If the user guessed the same or higher than the enemy
            if user_guess >= diceAmount_enemy:
                print("Je hebt gewonnen")
                
                dice_roll = False

            
            # If the user guessed lower than the enemy
            else:
                
                info = "Je hebt verloren, de tegenstander heeft '", diceAmount_enemy, "' gegooid, en jij gokte lager, namelijk '" + user_guess + "'"

                loseScreen(info)




# Rock paper scissor game
def rpsGuessing():

    rps_roll = True # Loop through the question 

    while rps_roll:

        rps_randomNumber = random.randrange(3) # Get a random number
        
        rps_options = list ( rps_information.keys() ) # Make a array from the 3 options 
        rps_enemy = rps_options[rps_randomNumber] # Get a random option out of the array


        rps_user = input("Kies steen, papier of schaar: ")
        
        # Check if the user chose between the 3 options
        try: 
            rps_options.index(rps_user)

        except:
            print("Kies een geldige optie")
        
        # If it did go correctly   
        else:
            
            # If the user guess the same as the enemy
            if rps_user == rps_enemy:
                print("De tegenstander koos dezelfde optie als jou, kies opnieuw")
                

            # If the loses
            elif rps_user == rps_information[rps_enemy]["lose"]:

                # Go to the lose screen, with the text given    
                info = "Je hebt verloren, de tegenstander koos '" + rps_enemy + "' en jij koos '" + rps_user + "'"
                
                loseScreen(info)

            # If the user wins
            else:
                print("Je hebt gewonnen")

                rps_roll = False  # End the loop
                
                diceGuessing() # Go to the next game

rpsGuessing() # Start the first game