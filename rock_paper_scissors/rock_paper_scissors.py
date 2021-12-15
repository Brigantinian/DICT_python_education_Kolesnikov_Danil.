from random import choice

moves = {
    'rock': ['gun', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['fire', 'scissors', 'wolf', 'tree', 'human', 'snake'],
    'scissors': ['gun', 'lightning', 'devil', 'dragon', 'water', 'rock'],
    'gun': ['water', 'air', 'sponge', 'paper', 'devil', 'dragon'],
    'lightning': ['water', 'air', 'sponge', 'paper', 'dragon', 'wolf'],
    'devil': ['water', 'air', 'sponge', 'paper', 'tree', 'wolf'],
    'dragon': ['air', 'sponge', 'paper', 'tree', 'wolf', 'human'],
    'water': ['snake', 'sponge', 'paper', 'tree', 'wolf', 'human'],
    'air': ['snake', 'sponge', 'scissors', 'tree', 'wolf', 'human'],
    'sponge': ['snake', 'scissors', 'tree', 'human', 'rock', 'fire'],
    'wolf': ['snake', 'scissors', 'human', 'rock', 'fire', 'gun'],
    'tree': ['snake', 'scissors', 'rock', 'fire', 'gun', 'lightning'],
    'human': ['scissors', 'rock', 'fire', 'gun', 'lightning', 'devil'],
    'snake': ['rock', 'fire', 'gun', 'lightning', 'devil', 'dragon'],
    'fire': ['fire', 'gun', 'lightning', 'devil', 'dragon', 'water'],  #####
}
chosen_moves = {}


def is_player_won(player_word, computer_word):
    is_win = True
    for word in chosen_moves[player_word]:
        if word == computer_word:
            is_win = False
    return is_win


def get_dashboard():
    dashboard = {}
    f = open("results.txt")
    lines = f.readlines()
    for line in lines:
        data = line.split(':')
        dashboard[data[0]] = int(data[1])
    return dashboard


def write_result(player_name, score):
    dashboard = get_dashboard()
    updated_array = []
    if player_name not in dashboard:
        dashboard[player_name] = 0
    dashboard[player_name] += score
    for player, result in dashboard.items():
        updated_array.append(player)
        updated_array.append(": ")
        updated_array.append(str(result))
        updated_array.append("\n")
    f = open("results.txt", "w")
    f.write("".join(updated_array))


def choose_option():
    chosen_moves.clear()
    print(",".join(moves.keys()))
    player_chose = input()
    player_chose_arr = player_chose.split(" ")

    if not player_chose:
        chosen_moves['rock'] = moves['rock']
        chosen_moves['paper'] = moves['paper']
        chosen_moves['scissors'] = moves['scissors']
    elif len(player_chose_arr) < 3:
        print("You should enter at least 3 values. Try one's more")
        choose_option()
    else:
        for value in player_chose_arr:
            if value not in moves:
                print(f"Incorrect value '{value}', try one's more")
                choose_option()
            else:
                chosen_moves[value] = moves[value]


def start_game():
    print("Welcome To Rock-Paper-Scissors")
    player_name = input("Enter player name: ")
    if not player_name:
        print("You didn't enter your name")
        start_game()
    else:
        choose_option()
        while True:
            try:
                # Input player word
                print("Select opion:")
                print(", ".join(chosen_moves.keys()))
                print("rating")
                print("exit\n")
                player_input = input().strip()
                # Computer word
                computer_input = choice(list(chosen_moves.keys()))
                # Exit
                if player_input == "exit":
                    print("Bye")
                    break
                elif player_input == "rating":
                    print(get_dashboard())
                # Chose winner
                elif player_input == computer_input:
                    print("Draw")
                    print("Computer's choice: ", computer_input)
                    write_result(player_name, 50)
                elif is_player_won(player_input, computer_input):
                    print("Player Wins")
                    print("Computer chose: ", computer_input)
                    write_result(player_name, 100)
                elif not is_player_won(player_input, computer_input):
                    print("Computer Wins")
                    print("Computer chose: ", computer_input)
            except:
                print("Error: incorrect word. Try once more")


if __name__ == "__main__":
    start_game()
