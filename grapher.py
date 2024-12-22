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
        if activeGrid[i].label.strip() == label:
            activeGrid.pop(i)
            print("Point " + activeGrid[i].label.strip() + "Removed!")
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
def userLoop():
    fullcommand = str(input("Commands: showGraph, newPoint, deletePoint, reset, exit -> "))
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
    elif command == "reset": 
        resetGrid()
        print("Graph Reset!")
    elif command == "exit": 
        exit()
    else: print("Invalid command")

resetGrid()
print("Welcome to Grapher.py (◕‿◕✿)")
while True:
    userLoop()

            
