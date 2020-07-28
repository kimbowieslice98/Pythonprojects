import random


def main():
    chips = 15                                                  # initial chip count
    menu()                                                      # menu function call
    while chips > 0 and chips < 25:                             # keep game running while chips are left

        horse1, horse2 = randomize_horses()                     # randomizes the horses and sends back the new order

        chips_to_bet = get_chips()                              # gets chips to bet

        wager = get_wager()                                     # picks odds 1 -> 4


        if wager == 4:                                          # double horse wager
            multiple_horse_pick1, multiple_horse_pick2 = (pick_two_horses(wager))
            if multiple_horse_pick1 == horse1 and multiple_horse_pick2 == horse2 or \
                    multiple_horse_pick1 == horse2 and multiple_horse_pick2 == horse1:
                new_chips = calculate_winnings(wager, chips_to_bet)
                chips = new_chips + chips
                print("You won this race! You're chip total is now:", chips, "chips")

            else:
                chips = chips - chips_to_bet
                print("You lost this race... You're chip total is now:", chips)





        elif wager == 1 or 2 or 3:                              # single horse wager
            single_horse_choice = pick_horse(wager)

            if horse1 == single_horse_choice:
                new_chips = calculate_winnings(wager, chips_to_bet)
                chips = new_chips + chips
                print("You won this race! You're chip total is now:", chips, "chips")
            else:
                chips = chips - chips_to_bet
                print("You lost this race... You're chip total is now: ", chips)

        if chips <= 0:                                           # end of game messages
            print("\n")
            print("YOU LOST THE GAME! MAYBE YOU SHOULD FIND ANOTHER HOBBY")
        if chips >= 25:
            print("\n")
            print("YOU WON THE GAME! ENJOY YOUR WINNINGS")


########################################################################################################################
################################################## start of functions ##################################################
########################################################################################################################


def menu():
    print("WELCOME TO THE HORSE RACE\n"
          "You will start with 15 chips. If your total drops to zero you lose. If you reach 25 or more, you WIN!\n"
          "You will have a choice of 4 different wagers with odds from 5 to 1 all the way to 15 to 1\n"
          "There will be six different horses to choose from as well\n"
          "And you will be able to bet up to 3 chips at a time per wager\n"
          "GOOD LUCK!!!\n")

def get_chips():
    while True:
        try:
            print("How many chips would you like to wager? ")
            chips = int(input("You can only bet up to 3 chips per wager\n"))
            break
        except ValueError:
            print("You need to enter an integer between 1 and 3")

    return chips

def get_wager():
    while True:
        try:
            print("Please select one of the following bets: ")
            wager = int(input("1. Win (5 to 1 if horse picked to win comes in 1st place\n"
                            "2. Place (3 to 1 if horse picked comes in 1st or 2nd place\n"
                            "3. Show (2 to 1 i1f the horse picked comes in 1st, 2nd, or 3rd place\n"
                            "4. Special (15 to 1 if the 2 horses picked come in 1st and 2nd place\n"))
            break
        except ValueError:
            print("You need to enter an integer between 1 and 3")

    return wager


def pick_horse(wager):
    if wager == 1 or 2 or 3:
        while True:
            try:
                horse_choice = int(input("Please pick a horse to bet on from horses 1, 2, 3, 4, 5, 6 \n"))
                break
            except ValueError:
                print("You need to enter an integer between 1 and 6")


    return horse_choice


def pick_two_horses(wager):
    horse_list = [1, 2, 3, 4, 5, 6]
    print("Congragulations, you picked the 'special' wager, you need to pick two horses")
    print("Pick your two horses that you would like to win: ")
    print(horse_list)
    multiple_horse_pick1 = int(input("Enter the first horse now\n"))
    horse_list.remove(multiple_horse_pick1)
    print("Remaining horses:", horse_list)
    multiple_horse_pick2 = int(input("Enter your second horse now. It must be different from the first horse\n"))

    return multiple_horse_pick1, multiple_horse_pick2




def calculate_winnings(wager, chips_to_bet):
    if wager == 1:
        wager = 5
    elif wager == 2:
        wager = 3
    elif wager == 3:
        wager = 2
    elif wager == 4:
        wager = 15

    new_chips_amt = wager * chips_to_bet
    print(new_chips_amt)

    return new_chips_amt


def randomize_horses():
    horse_list = [1, 2, 3, 4, 5, 6]
    random.shuffle(horse_list)
    #print(horse_list)                                           # Only needed for testing
    horse1, horse2 = [horse_list[i] for i in (0, 1)]
    return (horse1, horse2)


main()