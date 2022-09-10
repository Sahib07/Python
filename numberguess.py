import random

print('WELCOME TO GUESS MY NUMBER!!!')
random_number = random.randrange(0,11)
guesses = 0 

while True:
    user_guess = input('Make a guess: ')
    guesses +=1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print('You were below the number!')


print('You got it in', guesses, 'guesses')
