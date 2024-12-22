import math
#grid defaults
class grid:
    x = int
    y = int
    label = str

    def __init__ (self, x, y, label):
        self.x = x
        self.y = y
        self.label = label
gridSymbols = [" + ", " | ", " - ", " * "]
activeGrid = []
usedLabels = []
defaultGridSize = 5
gridBoundaries = [defaultGridSize, defaultGridSize, defaultGridSize, defaultGridSize] # x+, x-, y+, y-

def resetGrid():
    usedLabels.clear()
    activeGrid.clear()
    gridBoundaries = [defaultGridSize, defaultGridSize, defaultGridSize, defaultGridSize] # x+, x-, y+, y-
    activeGrid.append(grid(0,0,gridSymbols[0]))
    for i in range(defaultGridSize):
        activeGrid.append(grid(0, i+1,gridSymbols[1]))
        activeGrid.append(grid(0, -(i+1), gridSymbols[1]))
        activeGrid.append(grid(i+1, 0, gridSymbols[2]))
        activeGrid.append(grid(-(i+1), 0, gridSymbols[2]))
def appendToGrid(x, y, label):
    usedLabels.append(label)
    y = -y
    # on axes
    if x==0 or y==0:
        for i in range(len(activeGrid)):
            if activeGrid[i].x == x and activeGrid[i].y == y:
                activeGrid.pop(i)
                break
    
    if label == "" or label == " ":
        label = "*" #default label
    if len(label) > 1:
        label = label[0]

    #add point
    activeGrid.append(grid(x, y, " " + label + " "))

    #check if boundaries need to be expanded
    if x > 0:
        if x > gridBoundaries[0]:
            for i in range(x-gridBoundaries[0]):
                activeGrid.append(grid(i+1+gridBoundaries[0], 0, gridSymbols[2]))
            gridBoundaries[0] = x
    elif x < 0:
        if abs(x) > gridBoundaries[1]:
            for i in range(abs(x)-gridBoundaries[1]):
                activeGrid.append(grid(-(i+1+gridBoundaries[1]), 0, gridSymbols[2]))
            gridBoundaries[1] = abs(x)
    if y > 0:
        if y > gridBoundaries[2]:
            for i in range(y-gridBoundaries[2]):
                activeGrid.append(grid(0, i+1+gridBoundaries[2], gridSymbols[1]))
            gridBoundaries[2] = y
    elif y < 0:
        if abs(y) > gridBoundaries[3]:
            for i in range(abs(y)-gridBoundaries[3]):
                activeGrid.append(grid(0, -(i+1+gridBoundaries[3]), gridSymbols[1]))
            gridBoundaries[3] = abs(y)
def deletePoint(label):
    if label not in usedLabels:
        print("Point does not exist") 
        return
    for i in range(len(activeGrid)):
        if activeGrid[i-1].label.strip() == label:
            print("Point " + activeGrid[i-1].label.strip() + " Removed!")
            activeGrid.pop(i-1)
    usedLabels.remove(label)
def printGrid():
    for y in range(gridBoundaries[2]+gridBoundaries[3]+1):
        #starts on 0, supposed to start on -(gridBoundaries[3])
        gridy = y-(gridBoundaries[3])
        rowPrinter = []
        for x in range(gridBoundaries[0]+gridBoundaries[1]+1):
            currentPointValid = False
            #starts on 0, supposed to start on -(gridBoundaries[1])
            gridx = x-(gridBoundaries[1])
            # print("scanning " + str(gridx) + " " + str(gridy))
            for i in range(len(activeGrid)):
                if activeGrid[i].x == gridx and activeGrid[i].y == gridy:
                    rowPrinter.append(str(activeGrid[i].label))
                    currentPointValid = True
                    break
            if currentPointValid == False:
                rowPrinter.append("   ")
        print(''.join(rowPrinter).center(gridBoundaries[0]+gridBoundaries[1]+1 * 2))
def pointCoordinateDuplicated(x, y) -> bool:
    for i in range(len(activeGrid)):
        if activeGrid[i].x == x and activeGrid[i].y == -y:
            return True # point EXISTS
    return False
def pointLabelDuplicated(label) -> bool:
    if label in usedLabels: return True # label USED
    else: return False
def splitxy(label) -> tuple:
    for i in range(len(activeGrid)):
        if activeGrid[i-1].label.strip() == label:
            return (activeGrid[i-1].x, activeGrid[i-1].y)
    return None
def twoPointDistance(p1, p2) -> float:
    p1xy = splitxy(p1)
    p1x = p1xy[0]
    p1y = p1xy[1]
    p2xy = splitxy(p2)
    p2x = p2xy[0]
    p2y = p2xy[1]

    xdist = abs(p1x - p2x)
    ydist = abs(p1y - p2y)
    return (xdist**2 + ydist**2)**0.5
def threePointArea(p1, p2, p3) -> float:
    p1xy = splitxy(p1)
    p1x = p1xy[0]
    p1y = p1xy[1]
    p2xy = splitxy(p2)
    p2x = p2xy[0]
    p2y = p2xy[1]
    p3xy = splitxy(p3)
    p3x = p3xy[0]
    p3y = p3xy[1]

    return 0.5 * abs((p1x*(p2y-p3y)) + (p2x*(p3y-p1y)) + (p3x*(p1y-p2y)))
def pointModulus(label) -> float:
    pxy = splitxy(label)
    px = pxy[0]
    py = pxy[1]
    return (px**2 + py**2)**0.5
def pointArg(label) -> float:
    pxy = splitxy(label)
    px = abs(pxy[0])
    py = abs(pxy[1])
    alpha = math.atan(py/px)
    if pxy[0] < 0 and pxy[1] > 0:
        return math.pi - alpha
    elif pxy[0] < 0 and pxy[1] < 0:
        return math.pi + alpha
    elif pxy[0] > 0 and pxy[1] < 0:
        return 2*math.pi - alpha
    else: return alpha
def pointBaseAngle(label) -> float:
    pxy = splitxy(label)
    px = abs(pxy[0])
    py = abs(pxy[1])
    return math.atan(py/px)

def userLoop():
    print("""Grapher Commands:
    Graph: showGraph, resetGraph
    Points: newPoint, deletePoint
    Calculations: 2PointDistance, 3PointArea, PointModulus, PointArgument, PointBaseAngle
    Exit - Close the program""")
    fullcommand = str(input("Enter Command -> "))
    command = fullcommand.split(" ")[0]
    secondCommand = fullcommand.split(" ")[1] if len(fullcommand.split(" ")) > 1 else None
    thirdCommand = fullcommand.split(" ")[2] if len(fullcommand.split(" ")) > 2 else None
    fourthCommand = fullcommand.split(" ")[3] if len(fullcommand.split(" ")) > 3 else None

    if command == "showgraph" or command == "showGraph" or command == "graph": 
        printGrid()
    elif command == "newpoint" or command == "newPoint":
        if secondCommand != None: x = int(secondCommand)
        else: x = int(input("Enter x coordinate: "))
        if thirdCommand != None: y = int(thirdCommand)
        else: y = int(input("Enter y coordinate: "))
        while pointCoordinateDuplicated(x,y):
            print("Point already exists at coordinates")
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
        if fourthCommand != None: label = str(fourthCommand)
        else: label = str(input("Enter unique label (limited to one character): "))
        while pointLabelDuplicated(label):
            print("Label already exists")
            label = str(input("Enter unique label (limited to one character): "))
        appendToGrid(x, y, label)
        print("Point " + label + " Added!")
    elif command == "deletepoint" or command == "deletePoint": 
        if secondCommand != None: deleteLabel = str(secondCommand)
        else: deleteLabel = str(input("Enter point to delete: "))
        deletePoint(deleteLabel)
    elif command == "reset" or command == "resetgraph": 
        resetGrid()
        print("Graph Reset!")
    elif command == "exit": 
        exit()
    elif command == "2pointdistance" or command == "distance" or command == "2PointDistance":
        if secondCommand != None: p1 = str(secondCommand)
        else: p1 = str(input("Enter name of first point: "))
        if thirdCommand != None: p2 = str(thirdCommand)
        else: p2 = str(input("Enter name of second point: "))
        print("Distance between " + p1 + " and " + p2 + " is " + str(twoPointDistance(p1, p2)))
    elif command == "3pointarea" or command == "area" or command == "3PointArea":
        if secondCommand != None: p1 = str(secondCommand)
        else: p1 = str(input("Enter name of first point: "))
        if thirdCommand != None: p2 = str(thirdCommand)
        else: p2 = str(input("Enter name of second point: "))
        if fourthCommand != None: p3 = str(fourthCommand)
        else: p3 = str(input("Enter name of third point: "))
        print("Area of triangle " + p1 + p2 + p3 + " is " + str(threePointArea(p1, p2, p3)))
    elif command == "pointmodulus" or command == "modulus" or command == "PointModulus":
        if secondCommand != None: p1 = str(secondCommand)
        else: p1 = str(input("Enter name of point: "))
        print("Modulus of " + p1 + " is " + str(pointModulus(p1)))
    elif command == "pointarg" or command == "arg" or command == "angle" or command == "pointargument" or command == "pointangle" or command == "argument" or command == "PointArgument":
        if secondCommand != None: p1 = str(secondCommand)
        else: p1 = str(input("Enter name of point: "))
        print("Argument of " + p1 + " is " + str(pointArg(p1)))
    elif command == "pointbaseangle" or command == "baseangle" or command == "pointalpha" or command == "alpha" or command == "PointBaseAngle":
        if secondCommand != None: p1 = str(secondCommand)
        else: p1 = str(input("Enter name of point: "))
        print("Base angle of " + p1 + " is " + str(pointBaseAngle(p1)))
    else: print("Invalid command")

resetGrid()
print("Welcome to Grapher.py (◕‿◕✿)")
while True:
    userLoop()