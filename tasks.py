# tasks.py, functions that are included in this file:
# createListOfParks(), getDate(), getLargestPark(), extra credits functions

# Parameter: fileName
# Return value: a list of dictionary objects; keys = strings from header row
# values = information from the rest
def createListOffParks(fileName):
    keyList = []
    parksList = {}
    # read the header to create a list of the keys that will be use in the dictionary
    fileIn = open(fileName, "r")
    header = fileIn.readline()
    keys = header.split(",")
    # remove the \n symbol at the end of the line
    for i in keys:
        keyList.append(i.strip("\n"))

    for x in range(len(keyList)):
        title = keyList[x]
        # use this open method, so that the program could loop through the lines
        # multiples time, also don't need to call file.close()
        with open(fileName, "r") as file:
            # remove header
            file.readline()
            # empty tempList that will reset at the beginning of the loop
            tempList = []
            # use to create dictionary with list of values for all keys except "description"
            if x < (len(keyList) - 1):
                for line in file:
                    line = line.strip()
                    dataList = line.split(",")
                    tempList.append(dataList[x])
                # add the list to the dictionary with the assigned key
                parksList[title] = tempList
            # use to create dictionary with list of values for "description" key.
            if x == (len(keyList) - 1):
                for line in file:
                    line = line.strip()
                    dataList = line.split(",")
                    # use slicing and join at a specific location to get all information of the string
                    description = dataList[7:]
                    description = "".join(description)
                    description = description.replace('"', '')
                    tempList.append(description)
                # add the list to the dictionary with the assigned key
                parksList[title] = tempList

    return parksList


# Parameter: dateString (YYYY-MM-DD)
# Return: String in Month Day, Year Format
def getDate(dateString):
    # create list of string with numerical month values and actual month (both are string)
    monthList = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
    monthNumList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    # split the "-" to get a list with there string in [YYYY, MM, DD] format
    stringList = dateString.split("-")
    month = stringList[1]
    # loop through the monthNumList to find the location, use the location to assign the month value
    for x in range(len(monthNumList)):
        if month == monthNumList[x]:
            month = monthList[x]
            break
            # stop the loop to keep the x value (location)
    # combined all of the string
    updatedDate = month + " " + stringList[2] + ", " + stringList[0]

    return updatedDate


# ['Code', 'Name', 'State', 'Acres', 'Latitude', 'Longitude', 'Date', 'Description']
# Parameter: dictionary of parksList
# Return: string of the park code of the largest park
def getLargestPark(parksList):
    k = 0
    x = "Acres"
    y = "Code"
    largest = 0
    # create lists that have the information of the code and acres
    acresList = parksList[x]
    codeList = parksList[y]
    # convert list from string to int
    for i in range(len(acresList)):
        acresList[i] = int(acresList[i])
    # use loop to find the largest value
    for j in range(len(acresList)):
        temp = acresList[j]
        if temp > largest:
            largest = temp
    # find the location of the largest value
    for k in range(len(acresList)):
        if largest == acresList[k]:
            break
            # stop the loop to save the k value(location)

    # convert back to string for using in interface.py
    for i in range(len(acresList)):
        acresList[i] = str(acresList[i])

    return codeList[k]


# Parameter: parksList
# Return value: string of the code of the oldest park
# similar to getLargestPark()
def getOldestPark(parksList):
    x = "Date"
    z = "Code"
    y = 0
    oldYear = 2000
    newDateList = []
    dateList = parksList[x]
    codeList = parksList[z]
    # convert from string to int
    for i in range(len(dateList)):
        stringList = dateList[i]
        stringList = stringList.split("-")
        year = stringList[0]
        newDateList.append(int(year))

    # use loop to find the oldest value
    for x in range(len(newDateList)):
        if newDateList[x] < oldYear:
            oldYear = newDateList[x]

    # find the location of the oldest value
    for y in range(len(newDateList)):
        if oldYear == newDateList[y]:
            break
            # stop the loop to save the y value(location)

    return codeList[y]


# Parameter: parksList
# Return value: string of the most common state
def mostFrequentState(parksList):
    state = "State"
    stateList = parksList[state]
    oldest = 0
    commonState = ""
    # use loop and branching to find the most common state
    for i in stateList:
        temp = 0
        for j in range(len(stateList)):
            if i in stateList[j]:
                temp += 1
        # compare the temporary value with current oldest value
        if temp > oldest:
            oldest = temp
            commonState = i

    return commonState
