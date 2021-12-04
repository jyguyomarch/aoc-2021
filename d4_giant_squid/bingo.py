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

for board in boards:
    print(board)

# Play Bingo
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
            winning_draw = draw
            break
    if winning_board_sum > 0: break

for board in boards:
    print(board)

print(f'Last draw number: {winning_draw}')
print(f'Winning board sum: {winning_board_sum}')
print(f'Final Score: {winning_board_sum * winning_draw}')
