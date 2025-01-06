def print_board(lst):
    st = '''
    {} | {} | {}
    ----------
    {} | {} | {}
    ----------
    {} | {} | {}
'''.format(*lst)
    print(st)

def check_winner(choices, turns):
    # Check rows
    for i in range(0, 9, 3):
        if choices[i] == choices[i+1] == choices[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if choices[i] == choices[i+3] == choices[i+6] != ' ':
            return True
    # Check diagonals
    if choices[0] == choices[4] == choices[8] != ' ':
        return True
    if choices[2] == choices[4] == choices[6] != ' ':
        return True
    return False

choices = [' ' for _ in range(9)]
print('Welcome to Tic Tac Toe')
print_board(choices)
turns = 'X'

while 1:
    mv = int(input(f'Its your turn {turns}, your move [0-8]: '))
    if 0 <= mv <= 8 and choices[mv] == ' ':
        choices[mv] = turns
        print_board(choices)
        if hhhcheck_winner(choices, turns):
            print(f'You won {turns}!')
            break
        if ' ' not in choices:
            print('The game is a tie!')
            break
        turns = 'X' if turns == '0' else '0'
    else:
        print('Invalid move, try again.')
