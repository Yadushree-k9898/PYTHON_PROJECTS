questions = ("How many elements are there in Periodic table?: ",
             "What is the capital of India?: ",
             "When did our nation got Independence?: ",
             "What is the National Animal of India?: ",
             "Which animal lays the largest eggs? :")

options = (("A. 110 ", "B. 122 ", "C. 234 ", "D. 118 "),
           ("A. New Delhi", "B.Bangalore ", "C. Channai", "D. Pune"),
           ("A. 1947 ", "B.1823 ", "C. 1951 ", "D. 1977 "),
           ("A. Chimpanzee ", "B. Gorilla", "C.Tiger ", "D.Lion"),
           ("A.Whale ", "B. Crocodile ", "C. Eleplant", "D.Ostrich "))

answers = ('D', 'A', 'A', 'C', 'D')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('--------------------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print('CORRECT')
        
    else:
        print('INCORRECT')
        print(f'{answers[question_num]} is the correct answer!')
    question_num += 1
    
    
print('*****************************************************')
print('                      RESULT                         ')
print('*****************************************************')

print('answers: ', end='')
for answer in answers:
    print(answer, end= ' ')
    print() 
           
print('guesses: ', end='')
for guess in guesses:
    print(guess, end= ' ')
    print()      
    
score = int(score / len(questions)   * 100)

print(f'Your score is: {score}%')