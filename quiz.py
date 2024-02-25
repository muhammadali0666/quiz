quiz = {
  "question1": {
    "question": "What is the capital of Uzbekistan",
    "answer": "Tashkent"
  },
   "question2": {
    "question": "What is the capital of America",
    "answer": "Washington"
  },
   "question3": {
    "question": "What is the capital of Kazakhstan",
    "answer": "Almaty"
  },
   "question4": {
    "question": "What is the capital of Italy",
    "answer": "Rome"
  },
   "question5": {
    "question": "What is the capital of Austria",
    "answer": "Vienna"
  },
   "question6": {
    "question": "What is the capital of Portland",
    "answer": "Lissabon"
  },
   "question7": {
    "question": "What is the capital of Turkey",
    "answer": "Anqara"
  },
   "question8": {
    "question": "What is the capital of Kirgistan",
    "answer": "Bishkek"
  },
}

score = 0

for key, value in quiz.items(): 
  print(value["question"])
  answer = input("answer? ")
  if answer.lower() == value['answer'].lower():
    print("Correct")
    score = score + 1
    print("Your score is: " + str(score))
  else:
    print("Wrong!")
    print("The answer is: " + value['answer'])
    print("Your score is: " + str(score))
    print('')
    print('')

print("You got " + str(score) + "out of 8 questions correctly")
print("Your presantage is " + str(score/8 * 100) + "%")