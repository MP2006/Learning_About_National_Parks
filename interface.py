# interface.py, functions that are included in this file:
# include getMenuDict(), displayMenu(), getUserInput(), printAllParks(), getState(),
# printParksInState(), printLargestPark(), printParksForSearch(), extra credits functions
import tasks


# Parameter: None
# Return values: dictionary: keys are letter for user to input/ values are the description of menu options
def getMenuDict():
    menuDict = {}
    keys = ["A", "B", "C", "D", "E", "F", "Q"]
    values = ["All national parks", "Parks in a particular state", "The largest park",
              "Search for a park", "The oldest parks", "State with most parks", "Quit"]
    # assign the values to the correct key from the two lists created above
    for x in range(len(keys)):
        title = keys[x]
        menuDict[title] = values[x]

    return menuDict


# Parameter: menuDict
# Return value: None
def displayMenu(menuDict):
    # use the keys and values from the menuDict to print the display menu
    print()
    for key in menuDict:
        value = menuDict[key]
        # formatting the output
        print(key, "->", value)


# Parameter: menuDict
# Return value: valid choice string
def getUserInput(menuDict):
    validList = []
    choice = ""
    # create a list containing the key from the menuDict
    for key in menuDict:
        validList.append(key)
    # comparison between string choice and string in validList
    while choice not in validList:
        # input the choice then convert it to uppercase
        choice = input("Choice: ")
        choice = choice.upper()

    return choice


# Parameter: dictionary parksList
# Return value: None
# ['Code', 'Name', 'State', 'Acres', 'Latitude', 'Longitude', 'Date', 'Description']
def printAllParks(parksList):
    # crete a list for specific key from the imported dictionary
    keyList = ["Code", "Name", "State", "Acres", "Date"]
    codeList = parksList[keyList[0]]
    nameList = parksList[keyList[1]]
    stateList = parksList[keyList[2]]
    acresList = parksList[keyList[3]]
    dateList = parksList[keyList[4]]

    # loop through the length of all the park, and print in the desired format
    for j in range(len(codeList)):
        print(nameList[j] + " (" + codeList[j] + ")")
        print("\tLocation: " + stateList[j])
        print("\tArea: " + acresList[j] + " acres")
        print("\tDate Established: " + tasks.getDate(dateList[j]))
        print()


# Parameters: None
# Return Value: a string with a two-letter abbreviation of a state
def getState():
    state = ""
    # loop until two-letter abbreviation is meet
    while len(state) != 2:
        state = input("Enter a state: ")
        if len(state) != 2:
            print("Need the two letter abbreviation")

    # convert to uppercase
    state = state.upper()
    return state


# Parameter: parksList
# Return value: None
def printParksInState(parksList):
    x = 0
    locationList = []
    # crete a list for specific key from the imported dictionary
    keyList = ["Code", "Name", "State", "Acres", "Date"]
    codeList = parksList[keyList[0]]
    nameList = parksList[keyList[1]]
    stateList = parksList[keyList[2]]
    acresList = parksList[keyList[3]]
    dateList = parksList[keyList[4]]
    # get state from user
    state = getState()
    for j in range(len(stateList)):
        if state in stateList[j]:
            locationList.append(j)
            x += 1
    if x == 0:
        print("There are no national parks in " + state + " or it is not a valid state")
    else:
        for k in locationList:
            print(nameList[k] + " (" + codeList[k] + ")")
            print("\tLocation: " + stateList[k])
            print("\tArea: " + acresList[k] + " acres")
            print("\tDate Established: " + tasks.getDate(dateList[k]))
            print()


# Parameter: parksList
# Return: None
def printLargestPark(parksList):
    i = 0
    # create list for each keys
    keyList = ["Code", "Name", "State", "Acres", "Date", "Description"]
    codeList = parksList[keyList[0]]
    nameList = parksList[keyList[1]]
    stateList = parksList[keyList[2]]
    acresList = parksList[keyList[3]]
    dateList = parksList[keyList[4]]
    descriptionList = parksList[keyList[5]]
    codeLargest = tasks.getLargestPark(parksList)
    # use loop to find the location of the largest park from the list
    for i in range(len(codeList)):
        if codeLargest == codeList[i]:
            # stop the loop to save the i value
            break
    print(nameList[i] + " (" + codeList[i] + ")")
    print("\tLocation: " + stateList[i])
    print("\tArea: " + acresList[i] + " acres")
    print("\tDate Established: " + tasks.getDate(dateList[i]))
    print("\tDescription: " + descriptionList[i])


# Parameter: parksList
# Return value: None
def printParksForSearch(parksList):
    x = 0
    locationList = []
    # create list for each keys
    keyList = ["Code", "Name", "State", "Acres", "Date", "Description"]
    # convert the user input to lowercase
    print()
    search = input("Enter text for searching: ")
    search = search.lower()
    codeList = parksList[keyList[0]]
    nameList = parksList[keyList[1]]
    stateList = parksList[keyList[2]]
    acresList = parksList[keyList[3]]
    dateList = parksList[keyList[4]]
    descriptionList = parksList[keyList[5]]
    for i in range(len(codeList)):
        # making comparison between user input with code, name, and description in lowercase
        if search in descriptionList[i].lower() or search in codeList[i].lower() or search in nameList[i].lower():
            locationList.append(i)
            x += 1
    if x == 0:
        print("There are no national parks for the search text of '" + search + "'.")
    else:
        # print out the list of parks that contain search value
        for k in locationList:
            print(nameList[k] + " (" + codeList[k] + ")")
            print("\tLocation: " + stateList[k])
            print("\tArea: " + acresList[k] + " acres")
            print("\tDate Established: " + tasks.getDate(dateList[k]))
            print("\tDescription: " + descriptionList[k])
            print()


# Parameter: parksList
# Return: None
def printOldestPark(parksList):
    i = 0
    # create list for each keys
    keyList = ["Code", "Name", "State", "Acres", "Date", "Description"]
    codeList = parksList[keyList[0]]
    nameList = parksList[keyList[1]]
    stateList = parksList[keyList[2]]
    acresList = parksList[keyList[3]]
    dateList = parksList[keyList[4]]
    descriptionList = parksList[keyList[5]]
    codeLargest = tasks.getOldestPark(parksList)
    # use loop to find the location of the oldest park from the list, similar concept to printLargestPark()
    for i in range(len(codeList)):
        if codeLargest == codeList[i]:
            break
    print(nameList[i] + " (" + codeList[i] + ")")
    print("\tLocation: " + stateList[i])
    print("\tArea: " + acresList[i] + " acres")
    print("\tDate Established: " + tasks.getDate(dateList[i]))
    print("\tDescription: " + descriptionList[i])


# Parameter: parksList
# Return: None
def printMostCommonState(parksList):
    locationList = []
    # crete a list for specific key from the imported dictionary
    # similar concept to printParksInState()
    keyList = ["Code", "Name", "State", "Acres", "Date"]
    codeList = parksList[keyList[0]]
    nameList = parksList[keyList[1]]
    stateList = parksList[keyList[2]]
    acresList = parksList[keyList[3]]
    dateList = parksList[keyList[4]]

    state = tasks.mostFrequentState(parksList)
    print("The state with the most parks is", state, "\n")
    # loop to find locations that contain "state"
    for j in range(len(stateList)):
        if state in stateList[j]:
            locationList.append(j)

    # print out the parks from the position found above
    for k in locationList:
        print(nameList[k] + " (" + codeList[k] + ")")
        print("\tLocation: " + stateList[k])
        print("\tArea: " + acresList[k] + " acres")
        print("\tDate Established: " + tasks.getDate(dateList[k]))
        print()
