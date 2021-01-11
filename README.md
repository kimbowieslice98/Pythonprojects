# PythonProjects
#BestFlightScraper

#RestaurantSelector

#HorseBet


# Description 
> Best Flight: A scraping program used to find the most ideal domestic flights across the three booking websites: Kayak, South West, and Expedia.

> Dietary Restaurant Selector: A program used to aid the user in selecting which restaurants listed have vegtarian, vegan, and/or gluten free options.

> Horse Bet: A gambling program used to place bets on horses, keep count of chips, and announces the winner for horse races.

## General info
> Best Flight: The idea for this project was to originally find a real world issue and create a solution using all of the python language techniques learned in the class. Creating a scraping program to find the best flight from multiple booking websites seemed like a decent idea, because it would save people from scouring the internet for one flight. 

> Dietary Restaurant Selector: The object of this program was to help a user determine which restaurant they can eat at based on if they follow a vegetarian, vegan, and/or gluten free diet. As someone with celiac disease, a program that can tell me which restaurants listed are best for my dietary needs is a huge relief when trying to find places to eat. 

> Horse Bet: The object of this program was to create a program that lets the user choose a horse, type of bet, how many chips to bet, shows the results or the race, and calculates the amount of chips gained or lost. Creating this program was meant to provide users with a way to place bets and keep track of their earnings and losses. 

## Technologies
> BestFlight:
* Python 3.8
* Beautiful Soup 4-4.9.0
* Numpy 1.18.2
* Pandas 1.0.3
* Selenium 3.141.0
* ChromeDriver 88
> Restaurant Selector
* Python 3.8
> Horse Bet
* Python 3.8

## Setup
> BestFlight:
* Download the following to run the program:
  * All of the exact libraries and drivers in the technologies section
* Making sure the chrome browser is updated
* In the driver variable, adding the location of the chrome driver in the computer being used

## Code Examples
Show examples of usage:
> BestFlight
* def searchKayak(originCity, destinationCity, departureDate, returnDate):
    #Kayak
    driver.get(Kayak)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div').click()
    time.sleep(1.5)
    element = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[3]/input')
    element.send_keys(Keys.BACK_SPACE)
    element.send_keys(Keys.BACK_SPACE)
    element.clear()
    element.send_keys(originCity)
    time.sleep(2.5)
    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/ul/li').click()
> RestaurantSelector
* if listChoice[2] == 'yes':
    if "   Joe's Gourmet Burgers" in listPrint:
        listPrint.remove("   Joe's Gourmet Burgers")
    if "   Mama's Fine Italian" in listPrint:
        listPrint.remove("   Mama's Fine Italian")
##print the remaining places
for x in range(len(listPrint)):
    print(listPrint[x])
    
> HorseBet
* import random
def main():    #main function initializes variables and calls menu function
    bet = 0
    chips = 15
    betType = 0
    horseChoice = "default"
    specialChoice = "default"
    horseList = ['Jotaro', 'JoJo', 'Polnareff', 'Avdol', 'Kakyoin', 'Dio']
    menu(horseList, chips,betType,specialChoice)
    
## Features
List of features:
> BestFlight:
* Google Chrome webdriver opens up the websites used in the program once the user runs the program.
* Program prompts user to enter dates and destinations for flights and enters all the information into the websites.
* The program searches for the flight results and scrapes the data, finding the best result.
> RestaurantSelector:
* Helps the user find which restaurant is best for them based on their dietary needs and their choice through lists.
> HorseBet:
* Using a series of if statements and calculations useing chip amount, the user is able to places bets on horses and see the results of each race.

To-do list:
> BestFlight:
* Update the program so it can also scrape for international flights.
* Have it scrape date from all types of travel websites.
* Update the program to relect the new websites since they have been updated.

## Status
BestFlight is: _in progress_ - the program needs to be updated a bit, because the websites included have been updated since due to COVID, and the x-path needs to be changed. I also plan on improving my design to have it scrape more data.

RestaurantSelector is: _finished_ - the program does not need updated and completes the task it was meant to. Possible updates could be made to improve upon the current function.

HorseBet is: _finished_ - the program completed the function required of it, so nothing more needs to be done.
