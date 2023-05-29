import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    x = input(f"Enter a number for high value:")
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        print(guess)
        print("the actual number is", random_number)
        if guess < random_number:
            print("Sorry the number is too low")
        elif guess > random_number:
            print("sorry number too high")
    print(f"the actual number is", {random_number})


guess(1)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H) , too low(L), or correct (C ??)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed correct , {guess} , correctly ')


computer_guess(20)
