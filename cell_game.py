""" cell """
import numpy as np

def generate_board(rows, cols):
    """ generate a board with givin size """
    aux = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if np.random.random() < 0.5:
                aux[i][j] = 1
    return aux

def calculate_dead_alive(board, posx, posy):
    """ calculate of cell is dead on alive in next generation """
    alive = 0
    for aux in ((x, y) for x in [-1, 0, 1]  for y in [-1, 0, 1]):
        if aux == (0, 0):
            continue
        pos = np.array((posx, posy)) + np.array(aux)
        if min(pos) < 0 or max(pos) >= board.shape[0]:
            continue
        alive += board[pos[0]][pos[1]]
    if board[posx][posy]:
        # alive cell
        if alive in (2, 3):
            return True
    else:
        # dead cell
        if alive == 3:
            return True
    return False

def new_generation(board):
    """ calculates new based on board """
    # size = board.shape
    new = np.zeros(board.shape)
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if calculate_dead_alive(board, row, col):
                new[row][col] = 1
            else:
                new[row][col] = 0
    return new
