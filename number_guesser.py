import random
target = random.randint(1, 100)
while True:
    guess = int(input("Guess (1-100): "))
    if guess == target:
        print("Correct!"); break
    elif guess < target: print("Too low.")
    else: print("Too high.")
