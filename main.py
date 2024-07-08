import random

global number
global strnum


number = random.randrange(1000, 9999)
print(number)
strnum = str(number)
right = 0
count: int = 0

def start ():

    global count
    win = False

    print('You have to guess a random number')

    while not win:
        try:
            guess = int(input('Bitte gebe eine Zahl ein: '))
        except ValueError:
            print('Bitte gebe eine vierstellige Zahl ein!')
            continue

        if guess >= 1000 and guess <= 9999:
            winning = find(guess)

            if winning == 'win':
                win = True
                print('Du hast gewonnen und ' + str(count) + ' Versuche gebraucht.')
                break

        else:
            print('Bitte gebe eine vierstellige Zahl ein!')

def find (guess):

    global right
    global count
    
    guessstr = str(guess)

    count += 1

    if guess == number:
        return 'win'

    elif strnum[0] in guessstr[0]:
        print(strnum[0] + ' ist bereits richtig')
        right += 1


    if strnum[1] in guessstr[1]:
        print(strnum[1] + ' ist bereits richtig')
        right += 1

    if strnum[2] in guessstr[2]:
        print(strnum[2] + ' ist bereits richtig')
        right += 1

    if strnum[3] in guessstr[3]:
        print(strnum[3] + ' ist bereits richtig')
        right +=1



    if right == 0:
        print('Es war keine Zahl richtig!')
    else:
        right = 0

start()