from itertools import combinations
from random import sample, choice


# random.sample(population, k) - список длиной k из последовательности
# random.choice(sequence) - случайный элемент непустой последовательности.

def board():
    domino = list(map(lambda x: list(x), combinations(range(7),
                                                      2)))  # lambda позволяют функции быть созданной и переданной (зачастую другой функции) в одной строчке кода
    while True:
        player = sample(domino, 7)
        pc = sample(list(filter(lambda x: x not in player, domino)), 7)
        stock_pieces = list(filter(lambda x: x not in (player + pc), domino))
        player_doubles = [bones for bones in player if len(set(bones)) == 1]
        pc_doubles = [bones for bones in pc if len(set(bones)) == 1]
        doubles = player_doubles + pc_doubles
        if doubles:
            max_doubles = max(doubles)
            if max_doubles in player_doubles:
                player.remove(max_doubles)
                first_move = "pc"
            else:
                pc.remove(max_doubles)
                first_move = "player"
                return


def board_status():
    if len(board['player']) == 0:
        return 'The game is over.You win'
    elif len(board['pc']) == 0:
        return 'pc win'
    snake = [num for bones in board['snake'] for num in bones]
    for i in range(7):
        for i in board['snake'][0] and i in board['snake'][-1] and snake.count(i) == 8:
            return "The game is over"
    return "The game is over 2"


def play_board():
    print('-' * 70)
    print('Stock bones:\n', len(board['stock']))
    print('pc bones\n', len(board['pc']))
    print()
    snake = board['snake']
    if len(snake) > 6:
        for i in range(3):
            print(snake[i], end='')
            print(' ', end='')
        for i in range(-3, 0):
            print(snake[i], end='')
    else:
        for j in snake:
            print(j, end='')
    print()
    print("your bones:")
    for i, piece in enumerate(board["player"]):
        print(f'{i + 1}:{piece}')
    print()


def game_move(move):
    try:
       move = int(move)
    except ValueError:
        return False


def make_move(move, player):
    if move == 0:
        stock_piece = choice(board['stock'])
        board['stock'].remove(stock_piece)
        board[player].append(stock_piece)
        return
    ind = (move) - 1
    bones = board[player][ind]
    board[player].remove(bones)
    if move > 0:
        board['snake'].append(bones)
    else:
        board['snake'].insert(0,bones)

board = board()
while

