def new_game():

  guesses = []
  correct_guesses = 1
  question_num = 1

  for key in question:
    print("----------------------------------------------------------------------------")
    print(key)
    for i in options[question_num-1]:
      print(i)
      guess = input("Enter (A,B,C or D)")
      guess = guess.upper()
      guesses.append(guess)

     check_answer(question.get(key),guess)
      question_num += 1
  
  
def check_answer(answer,guess):
  if answer == guess:
    print("correct!")
    return 1
  else:
    print("wrong!")
    return 0
  
def display_score():
  pass
  
def play_again():
  pass

question = {
  "what is the capital of australia?: ": "B",
    "Where is Mount Fuji located?: ": "C",
    "How many bones in the human body?: ": "B",
    "What shape is the earth?: ": "B",
    "How many days are there in a year?: ": "D",
    "Na + CL = ?: ": "B",
    "Which one of these letters is not a vowel?: ": "C",
    "What is the smallest country?: ": "C",
    "What does the H in H^20 mean*?: ": "C",
  }

options = [["A. Adelaide", "B. Canberra", "C. Melbourne", "D. Sydney"]],
["A. Fiji", "B. Australia", "C. Japan", "D. America"], 
["A. 2", "B. 206", "C. 1023", "D. 34"],
["A. Sphere", "B. Square", "C. Pyramid", "D. Flat"]
["A. 355", "B. 375", "C. 364", "D. 365"]
["A. Water", "B. Salt", "C. Pottasium", "D. Chlorine"]
["A. I", "B. O", "C. L", "D. U"]
["A. Russia", "B. Libya", "C. Vatican City", "D. New Zealand"]
["A. Helium", "B. Healium", "C. Hydrogen", "D. Hylogen"]

new_game()