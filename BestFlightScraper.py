from bs4 import BeautifulSoup
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
import numpy as np
import time
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
driver = webdriver.Chrome('/Users/huxsgirl/Downloads/chromedriver')
SouthWest = 'https://www.southwest.com/'
Kayak = 'https://www.kayak.com/'
Expedia = 'https://www.expedia.com/'
kayakList = [" "," "," " ]


#action = webdriver.common.action_chains.ActionChains(driver)

#these were for debugging, will hcange back to user input
originCity = "Pittsburgh"
destinationCity = "Tampa"
departureDate = "05/05"
returnDate = "06/06"


#originCity = input('Enter Your Origin City: ')
#destinationCity = input('Enter Your Destination City: ')
#departureDate = input("What is your departure date? Use date format MM/DD/YYYY: ")
#returnDate = input("What is your return date? Use date format MM/DD/YYYY: ")



def searchKayak(originCity, destinationCity, departureDate, returnDate):
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
    #same thing but destination
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[3]/div/div/div').click()
    time.sleep(1)
    element = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[1]/div[3]/input')
    element.clear()
    element.send_keys(destinationCity)
    time.sleep(1.5)
    driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[2]/div/ul/li[1]').click()
    time.sleep(0.5)
    #dates
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[4]/div/div[1]').click()
    time.sleep(0.5)
    element = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]')
    element.clear()
    element.send_keys(departureDate)
    element = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/div[1]/div/div[2]/div[1]')
    element.clear()
    element.send_keys(returnDate)
    main_window = driver.current_window_handle
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section/div/div/div[2]/form[1]/div[1]/div/div[2]/button').click()


    time.sleep(2)
    driver.switch_to.window(main_window)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/section[5]/div[3]/div[2]/div/section/div[2]/div[3]/div/div[2]/p[1]/span[2]").click()

    kayakList[0] = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/section[5]/div[3]/div[2]/div/section/div[2]/div[3]/div/div[2]/p[2]/span[2]").text
    kayakList[1] = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/section[5]/div[3]/div[2]/div/section/div[2]/div[3]/div/div[3]/p[2]/span[1]").text
    kayakList[2] = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/section[5]/div[3]/div[2]/div/section/div[2]/div[4]/div[2]/div[4]/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]").text

    print(kayakList[0])
    print(kayakList[1])
    print(kayakList[2])




def searchSouthwest(originCity, destinationCity, departureDate, returnDate):
    # Southwest
    driver.get(SouthWest)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[2]/div[1]/div[1]/label/div[1]/div/div/input').click()
    time.sleep(1.5)
    element = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[2]/div[1]/div[1]/label/div[1]/div/div/input')
    element.send_keys(Keys.BACK_SPACE)
    element.send_keys(Keys.BACK_SPACE)
    element.clear()
    element.send_keys(originCity)
    time.sleep(2.5)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[2]/div[1]/div[1]/label/div[1]/div/div/input').click()
    element.send_keys(Keys.RETURN)
    # same thing but destination
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[2]/div[1]/div[2]/label/div[1]/div/div/input').click()
    time.sleep(1)
    element = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[2]/div[1]/div[2]/label/div[1]/div/div/input')
    element.clear()
    element.send_keys(destinationCity)
    time.sleep(1.5)
    # dates
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/div[1]/label/div[1]/div/div/input')
    element.click()
    element.clear()
    element.click()
    element.send_keys(departureDate)
    time.sleep(0.5)
    element.send_keys(Keys.TAB)
    time.sleep(0.1)
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/div[2]/label/div[1]/div/div/input')
    element.clear()
    element.click()
    element.send_keys(returnDate)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span/div/div/div[2]/div/div/div/div/form/div[3]/div[3]/div/button').click()



def searchExpedia(originCity, destinationCity, departureDate, returnDate):
    #Expedia
    driver.get(Expedia)
    driver.implicitly_wait(30)
    time.sleep(1.5);
    driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[1]/ul/li[1]/button').click()
    driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[3]/div[1]/div/div[1]/label/input').click()
    time.sleep(1.5)
    element = driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[3]/div[1]/div/div[1]/label/input')
    element.send_keys(Keys.BACK_SPACE)
    element.send_keys(Keys.BACK_SPACE)
    element.clear()
    element.send_keys(originCity)
    time.sleep(2.5)
    driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[3]/div[1]/div/div[1]/label/input').click()
    #same thing but destination
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[3]/div[2]/div/div[1]/label/input').click()
    time.sleep(1)
    element = driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[3]/div[2]/div/div[1]/label/input')
    element.clear()
    element.send_keys(destinationCity)
    time.sleep(1.5)
    driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[3]/div[2]/div/div[1]/label/input').click()
    time.sleep(0.5)
    #dates
    driver.find_element_by_xpath('/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/fieldset[2]/div/div[2]/div/label/input').click()
    time.sleep(0.5)
    element = driver.find_element_by_xpath('')
    element.clear()
    element.send_keys(departureDate)
    element = driver.find_element_by_xpath('')
    element.clear()
    element.send_keys(returnDate)
    driver.find_element_by_xpath('').click()


def runProgram():
    searchKayak(originCity, destinationCity, departureDate, returnDate)


    #searchSouthwest(originCity, destinationCity, departureDate, returnDate)
    #searchExpedia(originCity, destinationCity, departureDate, returnDate)

if __name__ == "__main__":
    runProgram()







