# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.
#
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.
#
# Return the number of pawns the rook can capture in one move.
#
# Example 1:
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# In this example the rook is able to capture all the pawns.
#
# Example 2:
# Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation:
# Bishops are blocking the rook to capture any pawn.
#
# Example 3:
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation:
# The rook can capture the pawns at positions b5, d6 and f5.

# def numRookCaptures(board):
#     Rpos, ppos, Bpos, Rcap = {}, {}, {}, {}
#     for x in range(len(board)):
#         if 'R' in board[x]:
#             try:
#                 Rpos[x] = []
#                 Rpos[x] += [a for a, b in enumerate(board[x]) if b == 'R']
#             except KeyError:
#                 continue
#         # if 'B' in board[x]:
#         #     try:
#         #         Bpos[x] = []
#         #         Bpos[x] += [a for a, b in enumerate(board[x]) if b == 'B']
#         #     except KeyError:
#         #         continue
#         # if 'p' in board[x]:
#         #     try:
#         #         ppos[x] = []
#         #         ppos[x] += [a for a, b in enumerate(board[x]) if b == 'p']
#         #     except KeyError:
#         #         continue
#
#     print(Rpos)
#     print(ppos)
#     print(Bpos)
#     for x Rpos.items():


def numRookCaptures(board):
    Rpos = []
    for x in range(len(board)):
        if 'R' in board[x]:
            Rpos.append(x)
            Rpos.append(board[x].index('R'))
            break

    count = 0

    # check horizontal left
    leftmark = Rpos[1]
    while leftmark > 0:
        leftmark -= 1
        if board[Rpos[0]][leftmark] == 'B':
            break
        elif board[Rpos[0]][leftmark] == 'p':
            count += 1
            break

    # check horizontal right
    rightmark = Rpos[1]
    while rightmark < len(board[0]) - 1:
        rightmark += 1
        if board[Rpos[0]][rightmark] == 'B':
            break
        elif board[Rpos[0]][rightmark] == 'p':
            count += 1
            break

    #check vertical up
    upmark = Rpos[0]
    while upmark > 0:
        upmark -= 1
        if board[upmark][Rpos[1]] == 'B':
            break
        elif board[upmark][Rpos[1]] == 'p':
            count += 1
            break

    # check vertical down
    downmark = Rpos[0]
    while downmark < len(board) - 1:
        downmark += 1
        if board[downmark][Rpos[1]] == 'B':
            break
        elif board[downmark][Rpos[1]] == 'p':
            count += 1
            break

    return count


print(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))