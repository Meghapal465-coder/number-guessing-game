import random
Number=random.randint(1,10)
guess=int(input("guess a number: "))
if guess==Number:
    print("you win")
else:
    print("you loose")
print("number is",Number)
