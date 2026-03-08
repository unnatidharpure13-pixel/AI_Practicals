import math

# Board setup
b = [' '] * 9
w = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # Columns
    (0, 4, 8), (2, 4, 6)               # Diagonals
]

print("TIC TAC TOE (Human=X, Computer=O)")
print("1 2 3\n4 5 6\n7 8 9\n")

turn = 'X'

while True:
    # Print board
    print(b[0], "|", b[1], "|", b[2])
    print("--+---+--")
    print(b[3], "|", b[4], "|", b[5])
    print("--+---+--")
    print(b[6], "|", b[7], "|", b[8], "\n")

    # Check for winner
    for a, c, d in w:
        if b[a] == b[c] == b[d] == 'X':
            print("Human wins")
            exit()
        if b[a] == b[c] == b[d] == 'O':
            print("Computer wins")
            exit()

    # Check for draw
    if ' ' not in b:
        print("Draw!")
        exit()

    # Human turn
    if turn == 'X':
        m = int(input("Enter move (1-9): ")) - 1
        if b[m] == ' ':
            b[m] = 'X'
            turn = 'O'
    else:
        # Computer turn
        best = -math.inf
        move = 0
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = 0
                for j in range(9):
                    if b[j] == ' ':
                        b[j] = 'X'
                        if any(b[a] == b[c] == b[d] == 'X' for a, c, d in w):
                            score = -1
                        b[j] = ' '
                b[i] = ' '
                if score > best:
                    best = score
                    move = i
        b[move] = 'O'
        turn = 'X'