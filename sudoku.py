# Example sudoku board.
# board = [
# [0,0,4,3,0,0,2,0,9],
# [0,0,5,0,0,9,0,0,1],
# [0,7,0,0,6,0,0,4,3],
# [0,0,6,0,0,2,0,8,7],
# [1,9,0,0,0,7,4,0,0],
# [0,5,0,0,8,3,0,0,0],
# [6,0,0,0,0,0,1,0,5],
# [0,0,3,5,0,8,6,9,0],
# [0,4,2,9,1,0,3,0,0]
# ]

board = [
[0,0,0,0,6,9,2,4,0],
[7,0,0,1,4,3,0,8,0],
[0,0,6,0,0,0,0,0,0],
[0,7,0,0,8,5,0,0,9],
[0,3,0,0,0,0,0,1,0],
[9,0,0,3,1,0,0,5,0],
[0,0,0,0,0,0,4,0,0],
[0,9,0,4,7,2,0,0,3],
[0,4,1,8,9,0,0,0,0]
]

# board = [
# [5,3,0,0,7,0,0,0,0],
# [6,0,0,1,9,5,0,0,0],
# [0,9,8,0,0,0,0,6,0],
# [8,0,0,0,6,0,0,0,3],
# [4,0,0,8,0,3,0,0,1],
# [7,0,0,0,2,0,0,0,6],
# [0,6,0,0,0,0,2,8,0],
# [0,0,0,4,1,9,0,0,5],
# [0,0,0,0,8,0,0,7,9]
# ]


# This function creates and returns a list of all the indexes in the sudoku board that do not have any pre-set numbers.
def create_empty_index_list(board):
    empty_index = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_index.append((9*(i+1))-(9-j))
    return empty_index



# Return the row and col of index in board as an array: [row, col]
# Input must be zero index based so a normal sudoku with 81 numbers (9x9) should have its input start with 0 and end at 80 instead of starting at 1 and ending at 81!
def get_position(index):
    board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    row = index // len(board)
    col = index % len(board)
    return (row, col)



# Function to check if given number is to be found in the row of given index
def check_row(board, num, index):
    row = get_position(index)[0]

    for i in range(len(board[row])):
        if board[row][i] == num:
            return False

    return True



# Function to check if given number is to be found in the column of given index
def check_col(board, num, index):
    col = get_position(index)[1]

    for i in range(len(board[col])):
        if board[i][col] == num:
            return False

    return True



# Function to check if given number is to be found in the typical sudoku "square", the 3x3 ones found on sudokus.
# The function figures out which square to check by given index.
def check_square(board, num, index):
    # get which square (starts at 0 not 1)
    square_x = index // len(board) // 3
    square_y = index % len(board) // 3

    for i in range(3):
        for j in range(3):
            if board[i+(3*square_x)][j+(3*square_y)] == num:
                return False

    return True



# Returns True if number can go in, returns false if number cannot be put into that particular index.
def process_number(num, index, board):
    if check_row(board, num, index) == True and check_col(board, num, index) == True and check_square(board, num, index) == True:
        return True
    else:
        return False



# Prints out the sudoku board in a nicer fashion in the CLI.
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



# This function handles the actual solving of the sudoku puzzle by using a tactic called backtracking.
def backtrack(board, iteration, to_iterate):
    pos = get_position(iteration[to_iterate])

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
                board[pos[0]][pos[1]] = 0
        else:
            if i == 8:
                # board[pos[0]][pos[1]] = 0
                return False


# This function handles the output of the backtrack() function.
# This function will also call the pritn_sudoku() function which prints the un-solved sudoku board in the CLI in a cleaner and easier to read way for the sudoku thats being solved.
# This function is also responsible for calling the function create_empty_index_list() which creates and returns a list of all the indexes in the sudoku that have no pre-set number.
# Depending on the output of the backtrack() function this function will either print "Solvable" or "Unsolvable" when the program is finished.
def solve(sudoku):
    print_sudoku(sudoku)
    empty_index = create_empty_index_list(sudoku)
    if len(empty_index) == 0:
        print("Unsolvable")
    elif backtrack(sudoku, empty_index, 0):
        print()
        print("Solved!")
        print()
    else:
        print()
        print("Unsolvable!")
        print()


# This function will handle input gathering if you want to solve your own sudoku
# This function will return a 1D array of the input that it has recieved.
def get_input_for_sudoku():
    exit_values = ["stop", "exit", "q", "quit", "n"]
    print()
    print("Solve a sudoku:")
    print()
    sudoku_to_solve = []
    for i in range(81):

        input_checking = True
        while input_checking:
            pos = get_position(i)
            inputt = input(f"Input for ROW/COL {pos[0] + 1}/{pos[1] + 1}: ")

            if inputt.isdigit():
                inputt = int(inputt)
                if inputt <= 9:
                    sudoku_to_solve.append(inputt)
                    input_checking = False
                else:
                    print("Error, input must be 9 or below!")
            elif inputt.lower() in exit_values:
                return False
            else:
                print("Error, input must be an integer!")
    return sudoku_to_solve



# This function will transform the "1D" array produced by the get_input_for_sudoku() function and reshape it into an array that works with the backtracking and position checking functions.
# Input array shape must be (81) output shape will then be (9,9)
def transform_from_1d(input):
    sudoku_board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    if len(input) == 81:
        for i in range(len(input)):
            pos = get_position(i)
            sudoku_board[pos[0]][pos[1]] = input[i]
        return sudoku_board
    else:
        return False



# This while loop is used to loop the program so you can solve multiple sudokus without having to re-run the program.
# Prints important information for every run.
exit_values = ["stop", "exit", "q", "quit", "n", "exity", "quity"]
program_is_running = True
while program_is_running:
    print()
    print("Welcome to the Smart Sudoku Solver!")
    print("To see this program solve an example sudoku please enter \"example\"!")
    print("If you want to solve your own sudoku, enter \"solve\"!")
    print("The sudoku solver will print multiple sudoku boards in quick succession.")
    print("If the sudoku is solvable the last printed sudoku board is the solved and finished one!")
    print("While entering your own sudoku board enter a \"0\" for empty spaces.")
    command = input(": ")
    if command.lower() == "example":
        solve(board)
    elif command.lower() in exit_values:
        program_is_running = False
    elif command.lower() == "solve":
        sudoku_1d = get_input_for_sudoku()
        sudoku = transform_from_1d(sudoku_1d)
        solve(sudoku)
