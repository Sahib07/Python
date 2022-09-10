print('Welcome to my Quiz!')

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print('Okay! Lets play')
score = 0

answer = input('What does CPU stands for? ')
if answer == 'central processing unit':
    print('Correct')
    score +=1
else:
     print('Incorrect!!!')

answer = input('What does GPU stands for? ')
if answer.lower() == 'graphics processing unit':
    print('Correct')
    score +=1
else:
     print('Incorrect!!!')

answer = input('What does RAM stands for? ')
if answer == 'random access memory':
    print('Correct')
    score +=1
else:
     print('Incorrect!!!')

answer = input('What does PSU stands for? ')
if answer == 'power supply unit':
    print('Correct')
    score +=1
else:
     print('Incorrect!!!')
    
print('You got' + str(score) + 'questions correct')