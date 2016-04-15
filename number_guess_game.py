"""
Application: Number_guess_game
by:jhew86
Adapted from: 'Guess the number' by A.Sweigart
"""
import random
secret= random.randint(1,10)
print('I am thinking of a number between 1 and 10. Try to guess the number')
print('you have 3 guesses')

for guess in range(1,4):
    print('take a guess')
    guess=int(input())

    if guess < secret:
        print('too low')
    elif guess > secret:
        print('too high')
    else:
        break

if guess == secret:
    print('congrats!!!. you guessed correctly in ' + str(guess) + ' guesses')
else:
    print('nope, the number was: ' + str(secret))
