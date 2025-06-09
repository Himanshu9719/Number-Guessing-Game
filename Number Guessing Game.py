import random
print ('🎲 Welcome to the Number Guessing Game!')
Random_Number = random.randint(1, 100)

attemps=0

while True:
    guess = int(input("Guess a Number Between 1 and 100:"))
    attempts = 1
    
    if guess < Random_Number:
        print("Too low! Try again")
        
    elif guess > Random_Number:
        print("Too high! Try again")
        
    else:
        print('🎉 Yay! You gussed it right in {attemps} attemps:')
        
        break
        
    

