#--- Day 4: Giant Squid ---
#https://adventofcode.com/2021/day/4

def mark_board(board, num):
    new_board = []
    for row in board:
        new_row = []
        new_board.append(new_row)
        for x in row:
            if x == num:
                new_row.append(-1)
            else:
                new_row.append(x)
    return new_board

def winning_board(board):
    # Return sum of unmarked numbers if winning, 0 otherwise
    # Check rows
    for row in board:
        if sum(row) == -5:
            return sum_board(board)
    # Check columns
    for i in range(5):
        if board[0][i] == -1 and board[1][i] == -1 and board[2][i] == -1 and board[3][i] == -1 and board[4][i] == -1:
            return sum_board(board)
    return 0

def sum_board(board):
    sum_total = 0
    for row in board:
        sum_total += sum([x for x in row if x != -1])
    return sum_total

# Get Data
f = open('d4_giant_squid/bingo_input.txt','r')
lines = f.read().splitlines()

# Parse draw numbers
draw_numbers = [int(num) for num in lines.pop(0).split(',')]

# Parse boards
boards = []
board_tmp = []
for line in lines:
    if line != '':
        board_tmp.append([int(x) for x in line.split(' ') if x != ''])
        if len(board_tmp) == 5:
            boards.append(board_tmp.copy())
            board_tmp.clear()

# Play Bingo
#list of tuples (board, winning sum, draw number)
winning_list = []
winning_draw = -1
winning_board_sum = -1
for draw in draw_numbers:
    # Loop over boards
    board_position = 0
    for board in boards:
        # Mark board
        boards[board_position] = mark_board(board, draw)
        board_position += 1
    for board in boards:
        # Check board for win
        winning_board_sum = winning_board(board)
        if winning_board_sum > 0:
            winning_list.append((board, winning_board_sum, draw))
            winning_draw = draw
    for board, board_sum, draw_num in winning_list:
        try:
            boards.remove(board)
        except ValueError:
            #ignore board was already removed
            pass

first_board, first_board_sum, first_draw_num = winning_list[0]
print(f'First win draw number: {first_draw_num}')
print(f'First winning board sum: {first_board_sum}')
print(f'First win Final Score: {first_board_sum * first_draw_num}')

last_board, last_board_sum, last_draw_num = winning_list[-1]
print(f'Last win draw number: {last_draw_num}')
print(f'Lastt winning board sum: {last_board_sum}')
print(f'Last win Final Score: {last_board_sum * last_draw_num}')