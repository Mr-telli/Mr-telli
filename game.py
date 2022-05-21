import random
def main():
    Level = checking("Level: ")
    rndLevel = random.randint(1, Level)
    while True:
        Guess = checking("Guess: ")
        result = compares(rndLevel, Guess)
        print(result)
        if result == "Just right!":
            break
    #print(result)
def checking(ifNum):
    while True:
        try:
            num = int(input(ifNum))
            if num > 0:
                break
        except:
            ValueError
    return num
def compares(varX, varY):
    if varX == varY:
        return "Just right!"
    elif varX > varY:
        return "Too small!"
    elif varX < varY:
        return "Too large!"
main()
