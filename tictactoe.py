"""
Tic Tac Toe Player
"""
from queue import Empty

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                Xcount += 1
            elif board[i][j] == O:
                Ocount += 1
    
    if Xcount == Ocount:
        return X
    elif Ocount < Xcount:
        return O
    else:
        return None
        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possibleActions.add((i,j))
    if len(possibleActions) == 0:
        return None
    else:
        return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x,y) = action
    myList = []
    newBoard = []
    for j in range(len(board[x])):
        if j == y:
            myList.append(player(board))
        else:
            myList.append(board[x][j])
            
    for i in range(len(board)):
        if i == x:
            newBoard.append(myList)
        else:
            newBoard.append(board[i])
    
    return newBoard
                
        


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(board[0][0] == board[0][1] == board[0][2]):
        return board[0][0]
    elif(board[0][0] == board[1][0] == board[2][0]):
        return board[1][0]
    elif(board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    elif(board[0][2] == board[1][2] == board[2][2]):
        return board[0][2]
    elif(board[2][0] == board[2][1] == board[2][2]):
        return board[2][0]
    elif(board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    elif(board[1][0] == board[1][1] == board[1][2]):
        return board[1][2]
    elif(board[0][1] == board[1][1] == board[2][1]):
        return board[0][1]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if actions(board) == None or winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def set_util(givenNode, util):
    if givenNode.util is None:
            givenNode.util = util
            return util
    else:
        if player(givenNode.state) == X:
            if givenNode.util < util:
                givenNode.util = util
                return util
            else:
                return givenNode.util
        elif player(givenNode.state) == O:
            if givenNode.util > util:
                givenNode.util = util
                return util
            else:
                return givenNode.util
    
            
            
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]