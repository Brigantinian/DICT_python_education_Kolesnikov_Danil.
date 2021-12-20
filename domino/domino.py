import random

stash = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
    [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
    [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
    [3, 3], [3, 4], [3, 5], [3, 6],
    [4, 4], [4, 5], [4, 6],
    [5, 5], [5, 6],
    [6, 6]
]
players = {}
board = []


def get_bones(player_name, count):
    for i in range(0, count):
        bone_idx = random.randint(0, len(stash) - 1)
        players[player_name].append(stash[bone_idx])
        del stash[bone_idx]


def lowest_double():
    lowest_double_value = None
    first_move_player = None
    for player_name in players:
        for bone in players[player_name]:
            if bone[0] == bone[1] and (lowest_double_value is None or bone[0] < lowest_double_value):
                lowest_double_value = bone[0]
                first_move_player = player_name
    if lowest_double_value is None:
        first_move_player = random.choice(list(players))
    return first_move_player


def print_player_board(player_name):
    print("Chose option:")
    idx = 0
    for bone in players[player_name]:
        print(f"{idx}: {bone}")
        idx += 1


def player_move(player_name, idx):
    bone = players[player_name][idx]
    if len(board) == 0 or board[len(board) - 1][1] == bone[0]:
        board.append(players[player_name][idx])
        del players[player_name][idx]
        return True
    else:
        return False


def computer_move(can_stash):
    should_go_to_stash = True
    moved = False
    for bone_idx, _ in enumerate(players['computer']):
        if not moved:
            move_result = player_move('computer', bone_idx)
            if move_result:
                moved = True
                should_go_to_stash = False
    if should_go_to_stash and can_stash:
        get_bones('computer', 1)
        # "len(players['computer'] - 1" ==> after stash last item drops in the end of list
        move_after_stash_result = player_move('computer', len(players['computer']) - 1)
        if not move_after_stash_result:
            print('Computer passed')
    elif should_go_to_stash and not can_stash:
        print('Computer passed')
    else:
        print("Computer made a move")


def game():
    # Create computer player
    players['computer'] = []
    # Create human player
    player_name_choice = input('Enter player name: ')
    players[player_name_choice] = []
    # Give bones
    for player_name in list(players):
        get_bones(player_name, 7)
    # Have player already been in stash
    was_in_stash = False
    # Computer moves first
    move_turn = lowest_double()
    # Game stated
    while True:
        try:
            # Can player go to stash
            can_go_to_stash = True if len(stash) > 0 else False
            if move_turn == 'computer':
                computer_move(can_go_to_stash)
                move_turn = player_name_choice
                print(board)
            else:
                # Print board
                print_player_board(player_name_choice)
                if can_go_to_stash and not was_in_stash:
                    print("- stash")
                else:
                    print("- pass")
                # Player move
                player_move_choice = input("Chose on of the options upset: ")

                if player_move_choice == "stash" and can_go_to_stash and not was_in_stash:
                    get_bones(player_name_choice, 1)
                    was_in_stash = True
                elif player_move_choice == "pass" and (not can_go_to_stash or was_in_stash):
                    print("Passed")
                    move_turn = 'computer'
                    was_in_stash = False
                elif int(player_move_choice) < len(players[player_name_choice]):
                    player_move_result = player_move(player_name_choice, int(player_move_choice))
                    if player_move_result:
                        move_turn = 'computer'
                        was_in_stash = False
                    else:
                        print("You can't move this bone")
                else:
                    print("Incorrect input. Try one's more")
                # Show board
                print(board)

            if len(stash) == 0:
                print("No more bones in stash")
                print("Game ended")
                break
            print(players)
        except:
            print("Incorrect input. Try one's more")


if __name__ == "__main__":
 game()
