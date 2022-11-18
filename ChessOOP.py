DIMENSION = 8
NUMFIELDS = DIMENSION*DIMENSION


#Boardtstate the game starts with
boardstate = [['BR','BH','BB','BK','BQ','BB','BH','BR'],
            ['BP','BP','BP','BP','BP','BP','BP','BP'],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['WP','WP','WP','WP','WP','WP','WP','WP'],
            ['WR','WH','WB','WQ','WK','WB','WH','WR']]




fields = []



#Transformation functions between inputs and lists/arrays and back
#chess e.g. a1, h2, f8
#array e.g. 00, 71, 67
#list  e.g.  0, 15, 62

def chessToList(move):
    return int(ord(move[0]))-97+ 8*int(move[1])-8

def chessToArray(move):
    return str(ord(move[0])-97)+str(int(move[1])-1)


def listToChess(move):
    return str(chr(int(move)%8+97))+str((int(move)//8)+1)

def arrayToChess(move):
    return str(chr(int(move[0])+97))+str(int(move[1])+1)

def arrayToList(move):
    return int(move[0])*8+int(move[1])

# Basic class including methods and variables each piece needs
class ChessPiece:
    def __init__(self, name, color, positionX, positionY):
        self.name = name
        self.color = color
        self.positionX = positionX
        self.positionY = positionY
    def printPosition(self):
        print(self.positionX, self.positionY) 

    def checkAvailableSpots(self):
        availableSpots = []
        return availableSpots

    global fields

    def choosePosition(self):
        print("Select spot to move to: ")
        moveTo = input()
        moveTo = chessToArray(moveTo)
        while moveTo not in self.checkAvailableSpots():
            print("Choose an available Spot!"+ str(self.checkAvailableSpots()))
            moveTo = input()
            moveTo = chessToArray(moveTo)
        return int(moveTo)

class Pawn(ChessPiece):
    def __init__(self, name, color, positionX, positionY):
        ChessPiece.__init__(self,name, color, positionX, positionY)
        self.name = name
        self.color = color
        self.positionX = positionX
        self.positionY = positionY
    hasMoved = False
        


    def checkAvailableSpots(self):
        availableSpots = []
        if self.name[0] == "W":
            availableSpots.append()
        if self.name[0] == "B":
            pass
            #if self.position in fields availableSpots.append()

        return availableSpots


class Rook(ChessPiece):
    pass

class Horse(ChessPiece):
    pass

class Bishop(ChessPiece):
    pass

class King(ChessPiece):
    pass

class Queen(ChessPiece):
    pass

class EmptySpot():
    def __init__(self, name, positionX, positionY):
        self.name = name
        self.postionX = positionX
        self.positionY = positionY

pieceClasses = { "P": Pawn, "R": Rook, "H": Horse, "B": Bishop, "K": King, "Q": Queen }

class Chessboard:
#    dimensions = 8
#    numFields = dimensions*dimensions
    pieceList = []
    currentPlayer = "W"
    inactivePlayer = "B"


    def showBoard(self):
        print("    a    b    c    d    e    f    g    h")
        print("  +----+----+----+----+----+----+----+----+")
        
        for i in range(NUMFIELDS):
            if((i+8)%8==0):
                print(int(i/8+1), end= ' ')
            print("|",end =' ')
            print( self.pieceList[i].name,end = ' ')
            if((i+1)%8==0):
                print("|")
                print("  +----+----+----+----+----+----+----+----+")
            
            

    def initiateBoard(self):
        global boardstate
        global fields
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if boardstate[i][j] == "  ":
                    self.pieceList.append(EmptySpot("  ", j,i))
                else:
                    self.pieceList.append(pieceClasses[boardstate[i][j][1]](boardstate[i][j],boardstate[i][j][0], j, i ))
                fields.append(str(j)+str(i))        
        print(fields)

    #Function to move one chess Piece
    def movePiece(self):
        global boardstate #get the globalboardstate
        print("Select Piece to move:")
        chosenPosition = input() #Input should be a chessboard position e.g. a1
        chosenPosition = chessToList(chosenPosition) #turn Input to list value
        while not self.pieceList[chosenPosition].name[0] == self.currentPlayer:
            print("Choose one of your own Pieces! ")
            chosenPosition = input()
            chosenPosition = chessToList(chosenPosition)


        goTo = self.pieceList[chosenPosition].choosePosition() # Select array space to move to
        goTo = arrayToList(goTo)

        #Change position in List
        self.pieceList[chosenPosition], self.pieceList[goTo] = EmptySpot("  ", self.pieceList[chosenPosition].position), self.pieceList[chosenPosition]
        #Change Position in instance
        self.pieceList[goTo].position = goTo
        
        #Change active Player
        temp = self.currentPlayer
        self.currentPlayer = self.inactivePlayer
        self.inactivePlayer = temp

game1 = Chessboard

#while True:
    #game1.showBoard(game1)
    #game1.movePieces(game1)
game1.initiateBoard(game1)
game1.showBoard(game1)
game1.pieceList[63].printPosition()
while True:
    game1.movePiece(game1)
    game1.showBoard(game1)

