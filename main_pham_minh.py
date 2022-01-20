
# import other python files
import tasks

import interface


def main():
    print("National Parks")
    # import csv file
    parksList = tasks.createListOffParks("national_parks.csv")
    menuDict = interface.getMenuDict()
    userChoice = ""
    # use branching to provide the user with different options
    while userChoice != "Q":
        interface.displayMenu(menuDict)
        userChoice = interface.getUserInput(menuDict)
        if userChoice == "A":
            interface.printAllParks(parksList)
        if userChoice == "B":
            interface.printParksInState(parksList)
        if userChoice == "C":
            interface.printLargestPark(parksList)
        if userChoice == "D":
            interface.printParksForSearch(parksList)
        if userChoice == "E":
            interface.printOldestPark(parksList)
        if userChoice == "F":
            interface.printMostCommonState(parksList)


main()
