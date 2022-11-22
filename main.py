
# -------------------------
#function for making a new quiz game 
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
  # function that notifies the player if they got the question right and also keeps track of the score
def check_answer(answer, guess):

    if answer == guess:
        print("Correct answer!")
        return 1
    else:
        print("Incorrect answer!")
        return 0

# -------------------------
      # Function for displaying score , what answers they picked and the percent of how much questions they got right
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
  #Function so the player can have the option to play again
def play_again():

    response = input("Would you like to retry the quiz? (Answer with yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------

# Dictionary for the questions
questions = {
 "Q1.What is the capital city of australia?: ": "B",
 "Q2.Where is the mountain mt.fuji located?: ": "C",
 "Q3.How many bones in the human body?: ": "B",
 "Q4.What shape is the earth?: ": "A", 
 "Q5.how many days are there in a year": "D",
 "Q6.What do the elements Sodium and Chlorine combine to make?": "B",
 "Q7.Which one of these letters is not a vowel?": "C",
 "Q8.What is the smallest country?": "C",
 "Q9.What does the symbol H in H^2O Mean?": "C"
}
# Dictionary for the Answers
options = [["A. Adelaide", "B. Canberra", "C. Melbourne", "D. Sydney"],
          ["A. Fiji", "B. Australia", "C. Japan", "D. America"],
          ["A. 2", "B. 206", "C. 1023", "D. 34"],
          ["A. Sphere","B. Square", "C. pyramid", "D. flat"],
          ["A.355", "B.375", "C.364", "D.365"],
          ["A.Water", "B.Salt", "C.Pottasium", "D.Chlorine"],
          ["A.I", "B.O", "C.L", "D.U"],
          ["A.Russia","B.Libya,","C.Vatican City","D.New Zealand"],
          ["A.Helium","B.Healium","C.Hydrogen","D.Hylogen"]
          ]

new_game()

while play_again():
    new_game()

print("Thank you for playing the Quiz!")


