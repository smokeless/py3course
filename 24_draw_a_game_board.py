'''
Time for some fake graphics! Let’s say we want to draw game boards
that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Obviously,
they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw,
and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed previously on this blog
'''
def getInput()->int:
    print('Input the size of the board.')
    someInt = input('>> ')
    try:
        int(someInt)
    except ValueError:
        print('Please input an integer.')
    return int(someInt)


def drawBoard(boardSize: int ):
    horizon = ' --- '
    vert    = '|    '
    horizon = horizon * boardSize
    vert    = vert    * (boardSize + 1)
    for i in range(boardSize):
        print(horizon)
        if i != boardSize:
            print(vert)
    print(horizon)

uIn = getInput()
drawBoard(uIn)