board = [
[0,0,4,3,0,0,2,0,9],
[0,0,5,0,0,9,0,0,1],
[0,7,0,0,6,0,0,4,3],
[0,0,6,0,0,2,0,8,7],
[1,9,0,0,0,7,4,0,0],
[0,5,0,0,8,3,0,0,0],
[6,0,0,0,0,0,1,0,5],
[0,0,3,5,0,8,6,9,0],
[0,4,2,9,1,0,3,0,0]
]


# backtracking algorithm

# create and fill empty_index list with all the indexes as 1d array of places that originally have zeros in them
empty_index = []
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 0:
            empty_index.append((9*(i+1))-(9-j))


# functions to be used in checking algorithm:

# return the row and col of index in board
def get_position(board, index):
    row = index // len(board)
    col = index % len(board)
    return (row, col)


def check_row(board, num, index):
    row = get_position(board, index)[0]

    for i in range(len(board[row])):
        if board[row][i] == num:
            return False

    return True


def check_col(board, num, index):
    col = get_position(board, index)[1]

    for i in range(len(board[col])):
        if board[i][col] == num:
            return False

    return True


def check_square(board, num, index):
    # get which square (starts at 0 not 1)
    square_x = index // len(board) // 3
    square_y = index % len(board) // 3

    for i in range(3):
        for j in range(3):
            if board[i+(3*square_x)][j+(3*square_y)] == num:
                return False

    return True


# backtracking function
# checks if number can go if number can go in
# returns 2 if you have to backtrack
def process_number(num, index, board):
    if check_row(board, num, index) == True and check_col(board, num, index) == True and check_square(board, num, index) == True:
        return True
    else:
        return False
    # else:
    #     if num != 9:
    #         return False
    #     else:
    #         pos = get_position(board, index)
    #         board[pos[0]][pos[1]] == 0
    #         return 2


# nicer printing for the sudoku board
def print_sudoku(board):
    print()
    for i in range(9):
        print_row = ""
        for j in range(len(board[i])):
            print_row = print_row + str(board[i][j]) + " "
            if j == 2 or j == 5:
                print_row = print_row + "|"
        print(print_row)
        if i == 2 or i == 5:
            print("------|------|------")

# print_sudoku(board)



def backtrack(board, iteration, to_iterate):
    pos = get_position(board, iteration[to_iterate])
    # print(pos)
    # print(board)


    # sets previous tested value as lower end in for loop of numbers to test or if a zero is found its set to a zero ( has to do minus one on the lower end if its not a zero since the for loop is zero based )
    # if board[pos[0]][pos[1]] == 0:
    #     lower_end = 0
    # else:
    #     lower_end = board[pos[0]][pos[1]] - 1


    for i in range(9):
        if process_number(i + 1, iteration[to_iterate], board) == True:
            board[pos[0]][pos[1]] = i + 1
            print_sudoku(board)
            if to_iterate == len(iteration) - 1:
                return True
            if backtrack(board, iteration, to_iterate + 1) == True:
                # board[pos[0]][pos[1]] = i + 1
                return True
        else:
            if i == 8:
                board[pos[0]][pos[1]] = 0
                return False


print_sudoku(board)
if backtrack(board, empty_index, 0):
    print()
    print("Solved!")
    print()
else:
    print("Unsolvable!")




# def backtrack(board, iteration, to_iterate):
#     pos = get_position(board, iteration[to_iterate])
#     print(pos)
#     print(board)
#     if board[pos[0]][pos[1]] == 0:
#         lower_end = 0
#     else:
#         lower_end = board[pos[0]][pos[1]] - 1
#     for i in range(lower_end, 9):
#         result = process_number(i+1, iteration[to_iterate], board)
#         if result == True:
#             board[pos[0]][pos[1]] = i + 1
#             backtrack(board, iteration, to_iterate + 1)
#         elif result == 2:
#             print("Backtracking!")
#             board[pos[0]][pos[1]] = 0
#             backtrack(board, iteration, to_iterate - 1)


# def backtrack(board, iteration, to_iterate):
#     pos = get_position(board, iteration[to_iterate])
#     # print(pos)
#     # print(board)
#     if board[pos[0]][pos[1]] == 0:
#         lower_end = 0
#     else:
#         lower_end = board[pos[0]][pos[1]] - 1
#     for i in range(lower_end, 9):
#         result = process_number(i + 1, iteration[to_iterate], board)
#         if result == True:
#             board[pos[0]][pos[1]] = i + 1
#             print(board)
#
#             if to_iterate == len(iteration) - 1:
#                 print(to_iterate, len(iteration))
#
#             backtrack(board, iteration, to_iterate + 1)
#         elif result == 2:
#             print("Backtracking!")
#             board[pos[0]][pos[1]] = 0
#             backtrack(board, iteration, to_iterate - 1)


# def backtrack(board, iteration, to_iterate):
#     if to_iterate > len(iteration):
#         return False
#
#     pos = get_position(board, iteration[to_iterate])
#     print(pos)
#     print(board)
#
#     for i in range(9):
#         if process_number(i+1, iteration[to_iterate], board):
#             board[pos[0]][pos[1]] = i + 1
#             if to_iterate == len(iteration) - 1:
#                 return True
#             if backtrack(board, iteration, to_iterate + 1):
#                 return True
#
#     return False


# try the recursive function method instead of for loops
# def backtrack(board, iteration, to_iterate):
#     if iteration <= len(to_iterate):
#         pos = get_position(board, to_iterate[iteration])
#         for i in range(board[pos[0]][pos[1]], 9):
#             result = process_number(i+1, empty_index[iteration], board)
#             if result == True:
#                 break
#             if result == 2:
#
#                 if iteration > 0:
#                     iteration = iteration - 1
#                 return backtrack(board, iteration, to_iterate)
#         iteration = iteration + 1
#         return backtrack(board, iteration, to_iterate)


# backtrack(board, 0, empty_index)
# print(board)

# test to see that process_number function works which it does:
# print(process_number(7, empty_index[1], board))
