"""
Joyce Sun
jsun02@wesleyan.edu
COMP112-03
Final Project
11 December 2020
"""

import random
gameactive=True

compboard=[] 
userboard=[]
for x in range (5):
    compboard.append (["O"]*5) #sets comp board up into 5x5
for x in range (5):
    userboard.append(["M"]*5)
print ("Let's play Battleship!") #sets user board up into 5x5
def printboard(board):
    '''
    prints the boards
    '''
    for row in board:
        print (" ".join(row))
print ("Computer board")
printboard(compboard) #prints comp board
print ("Your board")
printboard(userboard) #prints user board

def shiprow(compboard):
    '''
    picks a row that the comp's ship is on
    '''
    return random.randint(0,len(compboard)-1)
def shipcolumn(compboard):
    '''
    picks a column that the comp's ship is on
    '''
    return random.randint(0,len(compboard)-1)


def randomguessrows(userboard):
    '''
    generates comp's row guesses
    '''
    return random.randint(0,len(userboard)-1)
def randomguesscolumn(userboard):
    '''
    generates comp's column guesses
    '''
    return random.randint(0, len(userboard)-1)

def check(input):
    '''
    checks to make sure the user's input is valid
    '''
    if str.isdigit(input) == True:
        if (int(input) >= 0 and int(input) <= 4):
            return True
        else:
            return False
    else:
        return False
def checkdirection(input):
    '''
    checks user input to make sure direction choice is valid
    '''
    if input=='horizontal' or input=='vertical':
        return True
    else:
        return False

#allows user to pick ship placement with limitations on length based on their origin point. 
i=1
x=1
rows=[]
cols=[]
usershipplacement=[]
direction= input("In what direction would you like your ship to be(horizontal or vertical)? ")
while (checkdirection(direction)==False):
    direction=input("That's not a valid option! In what direction would you like your ship to be(horizontal or vertical)? ")
if direction=="vertical":
    print("Your ship will drop downwards from your origin point. \nPick the origin point of your ship! Pick a number between 0-4. ")
    #allows user to pick the row for their ship location
    userrow = input("Row: ")
    x+=1
    rows.append(userrow)
    while (check(userrow) == False): #checks user input
        print("That's not a valid row! Pick a number between 0-4")
        userrow = (input("Row: "))
    userrow = int(userrow)
    print("Now pick a column where your ship is located!")
    usercol = input("Column: ")
    while (check(usercol) == False):
        print("That's not a valid column! Pick a number between 0-4")
        usercol = input("Column: ")
    usercol = int(usercol)
    length=input("Pick how long you want your ship to be! Based off of your point of origin, your ship can be from 1-"+ str(5-int(userrow))+" spaces long! ")
    while (check(length) == False):
        print("That's not a valid length!")
        length=input("Pick how long you want your ship to be! Based off of your point of origin, your ship can be from 1-"+ str(5-int(usercol))+" spaces long! ")
    while (int(length)>5-int(userrow)):
        print("A ship that length will not fit on the board!")
        input("Enter the length of your ship! You may choose lengths 1-"+5-int(userrow))
    while i<int(length):
        rows.append(userrow+i)
        i+=1
    for row in rows:
        usershipplacement.append([row, usercol])
        
else:
    print("Your ship will be placed rightward from your origin point. \nPick the origin point of your ship! Pick a number between 0-4. ")
    #allows user to pick the row for their ship location
    usercol = input("Column: ")
    x+=1
    cols.append(usercol)
    while (check(usercol) == False): #checks user input
        print("That's not a valid column! Pick a number between 0-4")
        usercol = (input("Column: "))
    usercol = int(usercol)
    print("Now pick a row where your ship is located!")
    userrow = input("Row: ")
    while (check(userrow) == False):
        print("That's not a valid Row! Pick a number between 0-4")
        userrow = input("Row: ")
    userrow = int(userrow)
    length=input("Pick how long you want your ship to be! Based off of your point of origin, your ship can be from 1-"+ str(5-int(usercol))+" spaces long! ")
    while (check(length) == False):
        print("That's not a valid length!")
        length=input("Pick how long you want your ship to be! Based off of your point of origin, your ship can be from 1-"+ str(5-int(usercol))+" spaces long! ")
    while int(length)>int(5-int(usercol)):
        print("A ship that length will not fit on the board!")
        input("Enter the length of your ship! You may choose lengths 1-"+str(5-int(usercol)))
    while i<int(length):
        cols.append(userrow+i)
        i+=1
    for col in cols:
        usershipplacement.append([userrow, col])

#selects place for comp ship
direction= random.choice(['horizontal', 'vertical'])
srows=[]
scols=[]
compshipplacement=[]
if direction=='horizontal':
    i=1
    c= shipcolumn(compboard)
    r= shiprow(compboard)
    scols.append(c)
    shiplen= random.randint(1, 5-int(c))
    while i<shiplen:
        scols.append(scols[0]+i)
        i+=1
    for col in scols:
        compshipplacement.append([r, col])
else:
    i=1
    r= shiprow(compboard) 
    c= shipcolumn(compboard)
    shiplen= random.randint(1, 5-int(r))
    srows.append(r)
    while i<shiplen:
        srows.append(srows[0]+i)
        i+=1
    for row in srows:
        compshipplacement.append([row, c])
print("\nThe computer's ship is "+str(shiplen)+" spaces and is "+str(direction)+".\n")
print("Computer board")
printboard(compboard)
print("Your board")
printboard(userboard)

    
def userguess():
    '''
    prompts user to guess a row and column on comp's board to find comp's ship
    uses check(input) to make sure user input is correct
    '''
    point=[]
    guessrow = input("Guess a row! Pick a number between 0-4: ")
    while (check(guessrow) == False):
        print("That's not a valid row, pick a number between 0-4")
        guessrow = input("Row: ")
    guessrow = int(guessrow)
    point.append(guessrow)
    guesscol= input("Guess a column! Pick a number between 0-4: ")
    while (check(guesscol) == False):
        print("That's not a valid column, pick a number between 0-4")
        guesscol = input("Column: ")
    guesscol = int(guesscol)
    point.append(guesscol)
    return point

def userguessboard():
    '''
    checks user's guess against current comp board
    directs user if it has already guessed a point
    /a point that doesn't exist
    '''
    uguess = userguess()
    guessrow = uguess[0]
    guesscol = uguess[1]
    while (compboard[guessrow][guesscol]=='X') or (compboard[guessrow][guesscol]=='∆'):
       print ("You already guessed that point")
       uguess = userguess()
       guessrow = uguess[0]
       guesscol = uguess[1]
    if uguess in compshipplacement:
        compboard[guessrow][guesscol]='∆'
        compshipplacement.remove(uguess)
        print("You hit the battleship!")
        printboard(compboard)
        if len(compshipplacement)==0:
            return False
        else:
            return True
    else:
        if ((guessrow < 0 or guessrow > 4) or (guesscol < 0 or guesscol > 4)):
            print ("Sorry, thats not on the board.")
            return True
        elif (compboard[guessrow][guesscol]=='X'):
           print ("You already guessed that point")
           printboard(compboard)
           return True
        else :
            print ("You missed the battleship!")
            compboard[guessrow][guesscol]='X'
            printboard(compboard)
            return True

def compguessboard():
    '''
    checks comp's guess against current user(your) board
    directs comp if it has already guessed a point
    /a point that doesn't exist
    '''
    guessrow = randomguessrows(userboard)
    guesscol = randomguesscolumn(userboard)
    compguess = [guessrow, guesscol]
    while (userboard[guessrow][guesscol]=='O') or (userboard[guessrow][guesscol]=='∆'):
        guessrow = randomguessrows(userboard)
        guesscol = randomguesscolumn(userboard)
        compguess = [guessrow, guesscol]
    if compguess in usershipplacement:
        userboard[guessrow][guesscol]='∆'
        usershipplacement.remove(compguess)
        print("Comp hit the battleship!")
        printboard(userboard)
        if len(usershipplacement)==0:
            return False
        else:
            return True
    else:
        if ((guessrow < 0 or guessrow > 4) or (guesscol < 0 or guesscol > 4)):
            print ("Sorry, thats not on the board.")
            return True
        elif (userboard[guessrow][guesscol]=='O'):
            print ("The computer already guessed that point")
            printboard(userboard)
            return True
        else :
            print ("The computer missed the battleship")
            userboard[guessrow][guesscol]='O'
            printboard(userboard)
            return True

#identifies if game is 'active' and counts number of turns
guesses=1
compguesses=1
while gameactive:
    print("Your turn to guess")
    gameactive=userguessboard()
    if gameactive == False:
        print ("Congrats, you win! You sunk the ship in", guesses, "tries!")
        break
    else:
        guesses+=1
    print("The computer's turn to guess")
    gameactive=compguessboard()
    if gameactive ==False:
        print ("I'm sorry, you lost. The computer sunk your ship in", compguesses, "tries.")
    else:
        compguesses+=1
