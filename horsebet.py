import random
def main():    #main function initializes variables and calls menu function
    bet = 0
    chips = 15
    betType = 0
    horseChoice = "default"
    specialChoice = "default"
    horseList = ['Jotaro', 'JoJo', 'Polnareff', 'Avdol', 'Kakyoin', 'Dio']
    menu(horseList, chips,betType,specialChoice)

def horseRace(bet, betType, specialChoice, horseChoice, chips, horseList):    #determines what type of race you want to choose and calculates winnings
    random.shuffle(horseList)
    if betType in [1]:
        if horseList[0] == horseChoice:
            chips = chips + bet * 5
    if betType in [2]:
        if horseList[1] == horseChoice or horseList[0] == horseChoice:
            chips = chips + bet * 3
    if betType in [3]:
        if horseList[0] in [horseChoice] or horseChoice in [horseList[1]] or horseChoice in [horseList[2]]:
            chips = chips + bet * 2
    if betType in [4]:
        if horseList[0] == horseChoice and horseList[1] == specialChoice or horseList[1] == horseChoice and horseList[0] == specialChoice:
            chips = chips + bet * 15
    return int(chips)


def menu(horseList, chips, betType, specialChoice):     #gets all user input: bet, horsechoice, special horse choice. Also tests the exceptions in the program.
    while chips > 0 and chips <= 25:                    # exceptions tests all possible errors that the user could enter.
        print(chips, "chips")
        while True:
            betType = int(input('Enter what type of bet you want to place: 1. Win, 2. Place, 3. Show, 4. Special: '))
            try:
                betType = int(betType)
            except ValueError:
                continue
            if betType > 0 and betType <= 4:
                break
            else:
                print("You need to enter an integer between 1 and 4")
        print("Jotaro, JoJo, Polnareff, Avdol, Kakyoin, Dio")
        while True:
            horseChoice = input('Choose which horse you want to bet on: ')
            try:
                horseChoice = str(horseChoice)
            except ValueError:
                continue
            if horseChoice in "Dio" or horseChoice in "Jotaro" or horseChoice in "JoJo" or horseChoice in "Kakyoin" or horseChoice in "Polnareff" or horseChoice in "Avdol":
                break
            else:
                print("Valid Horse's names: Jotaro, JoJo, Polnareff, Avdol, Kakyoin, Dio")

        if betType == 4:
            while True:
                specialChoice = input('Choose which special horse you want to bet on: ')
                try:
                    specialChoice = str(specialChoice)
                except ValueError:
                    continue
                if specialChoice in "Dio" or specialChoice in "Jotaro" or specialChoice in "JoJo" or specialChoice in "Kakyoin" or specialChoice in "Polnareff" or specialChoice in "Avdol":
                    break
                else:
                    print("Valid Horse's names: Jotaro, JoJo, Polnareff, Avdol, Kakyoin, Dio")
        compare(horseChoice, specialChoice)
        while True:
            bet = int(input("How many chips would you like to bet? 1-3: "))
            try:
                bet = int(bet)
            except ValueError:
                continue
            if bet > 0 and bet <= 3:
                break
            else:
                print("You need to enter an integer between 1 and 3")
        chips = chips - bet
        chips = horseRace(bet, betType, specialChoice, horseChoice, chips, horseList)
        display(chips, horseList)

def compare(horseChoice, specialChoice):         #compare function compares the horse choice and the special horse choice to make sure that one horse is not tested twice in race 4.
    if horseChoice not in [specialChoice]:
        return 0
    else:
        while True:
            print("You cannot bet on the same horse twice!")
            horseChoice = input('Choose which horse you want to bet on: ')
            specialChoice = input('Choose which special horse you want to bet on: ')
            try:
                horseChoice = str(horseChoice)
                specialChoice = str(specialChoice)
            except ValueError:
                continue
            if specialChoice not in [horseChoice]:
                break




def display(chips, horseList):       #displays the race results and chip amount.
    print("Race Result")
    print(chips, "chips")
    for x in range(0, 6):
        print(horseList[x])
main()   #calls the main function to start the program.










