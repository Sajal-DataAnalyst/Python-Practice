import random
num = random.randint(1,10)
tries=0

while True:
    guess=int(input(" Please Guess Your Number Between 1 to 10 "))

    if num==guess:
        tries+=1
        print(f" You are Right You guessed the number in {tries} tries")
        break

    elif num<guess:
        print(' Go a little lower ')
        tries+=1

    elif num>guess:
        print(' Go little Higher ')
        tries+=1

    else:
        tries+=1
        print(" Sorry, You are Wrong")