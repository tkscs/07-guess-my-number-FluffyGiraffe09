# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit
import random

x = None
lower_limit=0
higher_limit=10
random_number = random.randint(lower_limit, higher_limit) 

input("Pick a number between 0 and 10. Type 'OK' when you have a number!")
print(f"My guess is {random_number}")
guessed=random_number

while x == None:
    user_response = input("Yes, Lower, or Higher")
    if user_response == "Yes":
        print("Yay! I got it!")
        x == True
        break
    elif user_response == "Lower":
        higher_limit=guessed-1
        if higher_limit < lower_limit:
            print("are you sure about that??? The will have to start over because you gave WRONGE DIRECTION!")
            break
        guessed=random.randint(lower_limit,higher_limit) if guessed > 0 else 0
        print(f"Is it {guessed}")        
    elif user_response == "Higher":
        lower_limit=guessed+1
        if lower_limit > higher_limit:
            print("are you sure about that??? The will have to start over because you gave WRONGE DIRECTION!")
            break
        guessed=random.randint(lower_limit,higher_limit) if guessed < 10 else 10
        print(f"Is it {guessed}")
    else:
        print("please answer with one of the options")     

    