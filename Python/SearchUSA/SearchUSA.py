import networkx as nx
import sys
import math
import matplotlib.pyplot as plt



#  Unity Id (rsdates)
# CSC 520
# NC State Univ
#

# Properties
searchtype= sys.argv[1]
srccityname= sys.argv[2]
destcityname= sys.argv[3]
tempList = []
finalList = []
data = dict()
flag = False
expandCount = 0
expandArray = []
# plt.show()
# Set up graph tree
G=nx.Graph()

G.add_node("albanyGA", latitude=31.58, longitude=84.17)
G.add_node("albanyNY", latitude=42.66, longitude=73.78)
G.add_node("albuquerque", latitude=35.11, longitude=106.61)
G.add_node("atlanta", latitude=33.76, longitude=84.40)
G.add_node("augusta", latitude=33.43, longitude=82.02)
G.add_node("austin", latitude=30.30, longitude=97.75)
G.add_node("bakersfield", latitude=35.36, longitude=119.03)
G.add_node("baltimore", latitude=39.31,  longitude=76.62)
G.add_node("batonRouge", latitude=30.46,  longitude=91.14)
G.add_node("beaumont", latitude=30.08,  longitude=94.13)
G.add_node("boise", latitude=43.61, longitude=116.24)
G.add_node("boston", latitude=42.32, longitude=71.09)
G.add_node("buffalo", latitude=42.90, longitude=78.85)
G.add_node("calgary", latitude=51.00, longitude=114.00)
G.add_node("charlotte", latitude=35.21, longitude=80.83)
G.add_node("chattanooga", latitude=35.05, longitude=85.27)
G.add_node("chicago", latitude=41.84, longitude=87.68)
G.add_node("cincinnati", latitude=39.14, longitude=84.50)
G.add_node("cleveland", latitude=41.48, longitude=81.67)
G.add_node("coloradoSprings", latitude=38.86, longitude=104.79)
G.add_node("columbus", latitude=39.99, longitude=82.99)
G.add_node("dallas", latitude=32.80, longitude=96.79)
G.add_node("dayton", latitude=39.76,  longitude=84.20)
G.add_node("daytonaBeach", latitude=29.21, longitude=81.04)
G.add_node("denver", latitude=39.73, longitude=104.97)
G.add_node("desMoines", latitude=41.59, longitude=93.62)
G.add_node("elPaso", latitude=31.79, longitude=106.42)
G.add_node("eugene", latitude=44.06, longitude=123.11)
G.add_node("europe", latitude=48.87,  longitude=-2.33)
G.add_node("ftWorth", latitude=32.74,  longitude=97.33)
G.add_node("fresno", latitude=36.78, longitude=119.79)
G.add_node("grandJunction", latitude=39.08, longitude=108.56)
G.add_node("greenBay", latitude=44.51, longitude=88.02)
G.add_node("greensboro", latitude=36.08,  longitude=79.82)
G.add_node("houston", latitude=29.76,  longitude=95.38)
G.add_node("indianapolis", latitude=39.79,  longitude=86.15)
G.add_node("jacksonville", latitude=30.32,  longitude=81.66)
G.add_node("japan", latitude=35.68, longitude=220.23)
G.add_node("kansasCity", latitude=39.08, longitude=94.56)
G.add_node("keyWest", latitude=24.56, longitude=81.78)
G.add_node("lafayette", latitude=30.21, longitude=92.03)
G.add_node("lakeCity", latitude=30.19, longitude=82.64)
G.add_node("laredo",  latitude=27.52, longitude=99.49)
G.add_node("lasVegas", latitude=36.19, longitude=115.22)
G.add_node("lincoln", latitude=40.81, longitude=96.68)
G.add_node("littleRock", latitude=34.74,  longitude=92.33)
G.add_node("losAngeles", latitude=34.03, longitude=118.17)
G.add_node("macon", latitude=32.83, longitude=83.65)
G.add_node("medford", latitude=42.33, longitude=122.86)
G.add_node("memphis", latitude=35.12,  longitude=89.97)
G.add_node("mexia", latitude=31.68,  longitude=96.48)
G.add_node("mexico", latitude=19.40,  longitude=99.12)
G.add_node("miami", latitude=25.79,  longitude=80.22)
G.add_node("midland", latitude=43.62, longitude=84.23)
G.add_node("milwaukee", latitude=43.05, longitude=87.96)
G.add_node("minneapolis", latitude=44.96, longitude=93.27)
G.add_node("modesto", latitude=37.66, longitude=120.99)
G.add_node("montreal", latitude=45.50, longitude=73.67)
G.add_node("nashville", latitude=36.15, longitude=86.76)
G.add_node("newHaven", latitude=41.31, longitude=72.92)
G.add_node("newOrleans", latitude=29.97, longitude=90.06)
G.add_node("newYork", latitude=40.70, longitude=73.92)
G.add_node("norfolk", latitude=36.89, longitude=76.26)
G.add_node("oakland", latitude=37.80, longitude=122.23)
G.add_node("oklahomaCity", latitude=35.48, longitude=97.53)
G.add_node("omaha", latitude=41.26, longitude=96.01)
G.add_node("orlando", latitude=28.53, longitude=81.38)
G.add_node("ottawa", latitude=45.42, longitude=75.69)
G.add_node("pensacola", latitude=30.44, longitude=87.21)
G.add_node("philadelphia", latitude=40.72, longitude=76.12)
G.add_node("phoenix", latitude=33.53, longitude=112.08)
G.add_node("pittsburgh", latitude=40.40, longitude=79.84)
G.add_node("pointReyes",  latitude=38.07, longitude=122.81)
G.add_node("portland", latitude=45.52, longitude=122.64)
G.add_node("providence", latitude=41.80, longitude=71.36)
G.add_node("provo", latitude=40.24, longitude=111.66)
G.add_node("raleigh", latitude=35.82, longitude=78.64)
G.add_node("redding", latitude=40.58, longitude=122.37)
G.add_node("reno", latitude=39.53, longitude=119.82)
G.add_node("richmond", latitude=37.54, longitude=77.46)
G.add_node("rochester", latitude=43.17, longitude=77.61)
G.add_node("sacramento", latitude=38.56, longitude=121.47)
G.add_node("salem", latitude=44.93, longitude=123.03)
G.add_node("salinas", latitude=36.68, longitude=121.64)
G.add_node("saltLakeCity", latitude=40.75, longitude=111.89)
G.add_node("sanAntonio", latitude=29.45, longitude=98.51)
G.add_node("sanDiego", latitude=32.78, longitude=117.15)
G.add_node("sanFrancisco", latitude=37.76, longitude=122.44)
G.add_node("sanJose", latitude=37.30, longitude=121.87)
G.add_node("sanLuisObispo", latitude=35.27, longitude=120.66)
G.add_node("santaFe", latitude=35.67, longitude=105.96)
G.add_node("saultSteMarie", latitude=46.49, longitude=84.35)
G.add_node("savannah", latitude=32.05, longitude=81.10)
G.add_node("seattle", latitude=47.63, longitude=122.33)
G.add_node("stLouis", latitude=38.63, longitude=90.24)
G.add_node("stamford", latitude=41.07, longitude=73.54)
G.add_node("stockton", latitude=37.98, longitude=121.30)
G.add_node("tallahassee", latitude=30.45,  longitude=84.27)
G.add_node("tampa", latitude=27.97, longitude=82.46)
G.add_node("thunderBay", latitude=48.38, longitude=89.25)
G.add_node("toledo", latitude=41.67, longitude=83.58)
G.add_node("toronto", latitude=43.65, longitude=79.38)
G.add_node("tucson", latitude=32.21, longitude=110.92)
G.add_node("tulsa", latitude=36.13, longitude=95.94)
G.add_node("uk1", latitude=51.30, longitude=0.00)
G.add_node("uk2", latitude=51.30, longitude=0.00)
G.add_node("vancouver", latitude=49.25, longitude=123.10)
G.add_node("washington", latitude=38.91, longitude=77.01)
G.add_node("westPalmBeach", latitude=26.71, longitude=80.05)
G.add_node("wichita", latitude=37.69, longitude=97.34)
G.add_node("winnipeg", latitude=49.90, longitude=97.13)
G.add_node("yuma", latitude=32.69, longitude=114.62)


# edges roads
G.add_edge("albanyNY", "montreal", distance=226)
G.add_edge("albanyNY", "boston", distance=166)
G.add_edge("albanyNY", "rochester", distance=148)
G.add_edge("albanyGA", "tallahassee", distance=120)
G.add_edge("albanyGA", "macon", distance=106)
G.add_edge("albuquerque", "elPaso", distance=267)
G.add_edge("albuquerque", "santaFe", distance=61)
G.add_edge("atlanta", "macon", distance=82)
G.add_edge("atlanta", "chattanooga", distance=117)
G.add_edge("augusta", "charlotte", distance=161)
G.add_edge("augusta", "savannah", distance=131)
G.add_edge("austin", "houston", distance=186)
G.add_edge("austin", "sanAntonio", distance=79)
G.add_edge("bakersfield", "losAngeles", distance=112)
G.add_edge("bakersfield", "fresno", distance=107)
G.add_edge("baltimore", "philadelphia", distance=102)
G.add_edge("baltimore", "washington", distance=45)
G.add_edge("batonRouge", "lafayette", distance=50)
G.add_edge("batonRouge", "newOrleans", distance=80)
G.add_edge("beaumont", "houston", distance=69)
G.add_edge("beaumont", "lafayette", distance=122)
G.add_edge("boise", "saltLakeCity", distance=349)
G.add_edge("boise", "portland", distance=428)
G.add_edge("boston", "providence", distance=51)
G.add_edge("buffalo", "toronto", distance=105)
G.add_edge("buffalo", "rochester", distance=64)
G.add_edge("buffalo", "cleveland", distance=191)
G.add_edge("calgary", "vancouver", distance=605)
G.add_edge("calgary", "winnipeg", distance=829)
G.add_edge("charlotte", "greensboro", distance=91)
G.add_edge("chattanooga", "nashville", distance=129)
G.add_edge("chicago", "milwaukee", distance=90)
G.add_edge("chicago", "midland", distance=279)
G.add_edge("cincinnati", "indianapolis", distance=110)
G.add_edge("cincinnati", "dayton", distance=56)
G.add_edge("cleveland", "pittsburgh", distance=157)
G.add_edge("cleveland", "columbus", distance=142)
G.add_edge("coloradoSprings", "denver", distance=70)
G.add_edge("coloradoSprings", "santaFe", distance=316)
G.add_edge("columbus", "dayton", distance=72)
G.add_edge("dallas", "denver", distance=792)
G.add_edge("dallas", "mexia", distance=83)
G.add_edge("daytonaBeach", "jacksonville", distance=92)
G.add_edge("daytonaBeach", "orlando", distance=54)
G.add_edge("denver", "wichita", distance=523)
G.add_edge("denver", "grandJunction", distance=246)
G.add_edge("desMoines", "omaha", distance=135)
G.add_edge("desMoines", "minneapolis", distance=246)
G.add_edge("elPaso", "sanAntonio", distance=580)
G.add_edge("elPaso", "tucson", distance=320)
G.add_edge("eugene", "salem", distance=63)
G.add_edge("eugene", "medford", distance=165)
G.add_edge("europe", "philadelphia", distance=3939)
G.add_edge("ftWorth", "oklahomaCity", distance=209)
G.add_edge("fresno", "modesto", distance=109)
G.add_edge("grandJunction", "provo", distance=220)
G.add_edge("greenBay", "minneapolis", distance=304)
G.add_edge("greenBay", "milwaukee", distance=117)
G.add_edge("greensboro", "raleigh", distance=74)
G.add_edge("houston", "mexia", distance=165)
G.add_edge("indianapolis", "stLouis", distance=246)
G.add_edge("jacksonville", "savannah", distance=140)
G.add_edge("jacksonville", "lakeCity", distance=113)
G.add_edge("japan", "pointReyes", distance=5131)
G.add_edge("japan", "sanLuisObispo", distance=5451)
G.add_edge("kansasCity", "tulsa", distance=249)
G.add_edge("kansasCity", "stLouis", distance=256)
G.add_edge("kansasCity", "wichita", distance=190)
G.add_edge("keyWest", "tampa", distance=446)
G.add_edge("lakeCity", "tampa", distance=169)
G.add_edge("lakeCity", "tallahassee", distance=104)
G.add_edge("laredo", "sanAntonio", distance=154)
G.add_edge("laredo", "mexico", distance=741)
G.add_edge("lasVegas", "losAngeles", distance=275)
G.add_edge("lasVegas", "saltLakeCity", distance=486)
G.add_edge("lincoln", "wichita", distance=277)
G.add_edge("lincoln", "omaha", distance=58)
G.add_edge("littleRock", "memphis", distance=137)
G.add_edge("littleRock", "tulsa", distance=276)
G.add_edge("losAngeles", "sanDiego", distance=124)
G.add_edge("losAngeles", "sanLuisObispo", distance=182)
G.add_edge("medford", "redding", distance=150)
G.add_edge("memphis", "nashville", distance=210)
G.add_edge("miami", "westPalmBeach", distance=67)
G.add_edge("midland", "toledo", distance=82)
G.add_edge("minneapolis", "winnipeg", distance=463)
G.add_edge("modesto", "stockton", distance=29)
G.add_edge("montreal", "ottawa", distance=132)
G.add_edge("newHaven", "providence", distance=110)
G.add_edge("newHaven", "stamford", distance=92)
G.add_edge("newOrleans", "pensacola", distance=268)
G.add_edge("newYork", "philadelphia", distance=101)
G.add_edge("norfolk", "richmond", distance=92)
G.add_edge("norfolk", "raleigh", distance=174)
G.add_edge("oakland", "sanFrancisco", distance=8)
G.add_edge("oakland", "sanJose", distance=42)
G.add_edge("oklahomaCity", "tulsa", distance=105)
G.add_edge("orlando", "westPalmBeach", distance=168)
G.add_edge("orlando", "tampa", distance=84)
G.add_edge("ottawa", "toronto", distance=269)
G.add_edge("pensacola", "tallahassee", distance=120)
G.add_edge("philadelphia", "pittsburgh", distance=319)
G.add_edge("philadelphia", "newYork", distance=101)
G.add_edge("philadelphia", "uk1", distance=3548)
G.add_edge("philadelphia", "uk2", distance=3548)
G.add_edge("phoenix", "tucson", distance=117)
G.add_edge("phoenix", "yuma", distance=178)
G.add_edge("pointReyes", "redding", distance=215)
G.add_edge("pointReyes", "sacramento", distance=115)
G.add_edge("portland", "seattle", distance=174)
G.add_edge("portland", "salem", distance=47)
G.add_edge("reno", "saltLakeCity", distance=520)
G.add_edge("reno", "sacramento", distance=133)
G.add_edge("richmond", "washington", distance=105)
G.add_edge("sacramento", "sanFrancisco", distance=95)
G.add_edge("sacramento", "stockton", distance=51)
G.add_edge("salinas", "sanJose", distance=31)
G.add_edge("salinas", "sanLuisObispo", distance=137)
G.add_edge("sanDiego", "yuma", distance=172)
G.add_edge("saultSteMarie", "thunderBay", distance=442)
G.add_edge("saultSteMarie", "toronto", distance=436)
G.add_edge("seattle", "vancouver", distance=115)
G.add_edge("thunderBay", "winnipeg", distance=440)


def duplicateCheck(list):
    if len(list) == 0: return False
    temp = []
    btemp = []
    for x in list:
        temp.append(x[1])
    return len(temp) != len(set(temp))


# Define functions
def hhat(city1,city2):
    value = 0
    city1Latitude = G.node[city1]['latitude']
    city1Longitude = G.node[city1]['longitude']

    city2Latitude = G.node[city2]['latitude']
    city2Longitude = G.node[city2]['longitude']

    value = math.sqrt(math.pow((69.5 * (city1Latitude - city2Latitude)),2) + (69.5 * math.cos((city1Latitude + city2Latitude)/360 * math.pi) * math.pow((city1Longitude - city2Longitude),2)))
    return value


def a_star(srcCityNode, destCityNode):
    global expandCount
    priorityQueue = [] #initialize priority queue
    initNode = ([srcCityNode], srcCityNode, 0, 0) #creating the initial node tuple
    priorityQueue.append(initNode)
    while priorityQueue:
        rootTuple = priorityQueue.pop(0)
        expandCount = expandCount + 1
        expandArray.append(rootTuple[1])
        pathArray = rootTuple[0]
        lastNode = rootTuple[1]
        runningGScore = rootTuple[3]
        # Check if last node on path is goal node
        if lastNode == destCityNode:
            return pathArray,runningGScore
        # print(rootTuple)
        # Generate successors and calculate G and Hhat and heuristic for each successor path
        for key in sorted(G.neighbors_iter(lastNode)):
            newPathArray = pathArray[:]
            newPathArray.append(key)
            newGScore = runningGScore + G.edge[lastNode][key]['distance']
            computedHHat = hhat(key, destCityNode)
            newHeuristic = newGScore + computedHHat
            newTuple = (newPathArray, key, newHeuristic, newGScore)
            #Before inserting check for duplicates
            if newPathArray[len(newPathArray) - 3] != key and len(newPathArray) >= 3:
                priorityQueue.append(newTuple)
            elif len(newPathArray) < 3:
                priorityQueue.append(newTuple)
            # re-heapify
            priorityQueue.sort(key=lambda x: x[2])
            # print(priorityQueue[0])

        if duplicateCheck(priorityQueue):
            i = 0
            seen = set()
            while i < len(priorityQueue):
                if priorityQueue[i][1] in seen:
                    priorityQueue.pop(i)
                else:
                    seen.add(priorityQueue[i][1])
                i += 1
    return [],0

def uniform(srcCityNode, destCityNode):
    global expandCount
    priorityQueue = []  # initialize priority queue
    initNode = ([srcCityNode], srcCityNode, 0)  # creating the initial node tuple
    priorityQueue.append(initNode)
    while priorityQueue:
        rootTuple = priorityQueue.pop(0)
        expandCount = expandCount + 1
        expandArray.append(rootTuple[1])
        pathArray = rootTuple[0]
        lastNode = rootTuple[1]
        runningGScore = rootTuple[2]
        # Check if last node on path is goal node
        if lastNode == destCityNode:
            return pathArray, runningGScore
        # print(rootTuple)
        # Generate successors and calculate G and Hhat and heuristic for each successor path
        for key in sorted(G.neighbors_iter(lastNode)):
            newPathArray = pathArray[:]
            newPathArray.append(key)
            newGScore = runningGScore + G.edge[lastNode][key]['distance']
            newTuple = (newPathArray, key,newGScore)
            #insert
            if newPathArray[len(newPathArray) - 3] != key and len(newPathArray) >= 3:
                priorityQueue.append(newTuple)
            elif len(newPathArray) < 3:
                priorityQueue.append(newTuple)
            # re-heapify
            priorityQueue.sort(key=lambda x: x[2])
            # print(priorityQueue[0])
        #remove duplicates
        if duplicateCheck(priorityQueue):
            i = 0
            seen = set()
            while i < len(priorityQueue):
                if priorityQueue[i][1] in seen:
                    priorityQueue.pop(i)
                else:
                    seen.add(priorityQueue[i][1])
                i += 1
    return [],0

def greedy(srcCityNode, destCityNode):
    global expandCount
    priorityQueue = []  # initialize priority queue
    initNode = ([srcCityNode], srcCityNode, 0, 0)  # creating the initial node tuple
    priorityQueue.append(initNode)
    while priorityQueue:
        rootTuple = priorityQueue.pop(0)
        expandCount = expandCount + 1
        expandArray.append(rootTuple[1])
        pathArray = rootTuple[0]
        lastNode = rootTuple[1]
        runningGScore = rootTuple[2]
        # Check if last node on path is goal node
        if lastNode == destCityNode:
            return pathArray, runningGScore
        # print(rootTuple)
        # Generate successors and calculate G and Hhat and heuristic for each successor path
        for key in sorted(G.neighbors_iter(lastNode)):
            newPathArray = pathArray[:]
            newPathArray.append(key)
            newGScore = runningGScore + G.edge[lastNode][key]['distance']
            computedHHat = hhat(key, destCityNode)
            newTuple = (newPathArray, key, newGScore, computedHHat)
            if newPathArray[len(newPathArray) - 3] != key and len(newPathArray) >= 3:
                priorityQueue.append(newTuple)
            elif len(newPathArray) < 3:
                priorityQueue.append(newTuple)
        # re-heapify
        priorityQueue.sort(key=lambda x: x[3])
    return [], 0

# TODO remember to reset the expand count after calling search algorithm function

def viewCommaSeperatedList(list):
    view = ", ".join(list)
    return view

def resetExpandArrayANDExpandCount():
    global expandArray
    global expandCount

    expandArray = []
    expandCount = 0

if searchtype == "ASTAR" or searchtype == "astar":
    tuple = a_star(srccityname, destcityname)
    list = tuple[0]
    totalDistance = tuple[1]
    print('Expanded Nodes: ', viewCommaSeperatedList(expandArray))
    print('Number of nodes expanded: ', expandCount)
    print('Solution Path: ', viewCommaSeperatedList(list))
    print('Solution Path Node Count: ', len(list))
    print('Distance from source to destination: ', totalDistance)
    resetExpandArrayANDExpandCount()

if searchtype == "UNIFORM" or searchtype == "uniform":
    tuple = uniform(srccityname, destcityname)
    list = tuple[0]
    totalDistance = tuple[1]
    print('Expanded Nodes: ', viewCommaSeperatedList(expandArray))
    print('Number of nodes expanded: ', expandCount)
    print('Solution Path: ', viewCommaSeperatedList(list))
    print('Solution Path Node Count: ', len(list))
    print('Distance from source to destination: ', totalDistance)
    resetExpandArrayANDExpandCount()

if searchtype == "GREEDY" or searchtype == "greedy":
    tuple = greedy(srccityname, destcityname)
    list = tuple[0]
    totalDistance = tuple[1]
    print('Expanded Nodes: ', viewCommaSeperatedList(expandArray))
    print('Number of nodes expanded: ', expandCount)
    print('Solution Path: ', viewCommaSeperatedList(list))
    print('Solution Path Node Count: ', len(list))
    print('Distance from source to destination: ', totalDistance)
    resetExpandArrayANDExpandCount()

if searchtype != "UNIFORM" and searchtype != "uniform" and searchtype != "ASTAR" and searchtype != "astar" and searchtype != "GREEDY" and searchtype != "greedy":
    print("Invalid search type")
