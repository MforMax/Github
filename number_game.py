import time

def counting_game():
    current_number = 1
    player = 1

    print("Welcome to the Number game terminal.")
    time.sleep(3)
    print("Rules:")
    time.sleep(2)
    print("- The game starts at 1.")
    time.sleep(2)
    print("- Each player can choose 1, 2, or 3 numbers per turn (in order).")
    time.sleep(2)
    print("The player who says 15 looses the game.")
    time.sleep(2)

    while current_number <= 15:
        print(f"\nCurrent number is: {current_number - 1}")
        print(f"Player {player}'s turn.")

        while True:
            try:
                count = int(input("How many numbers would you like to choose (1-3)? "))
                if count in [1, 2, 3]:
                    break
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        chosen_numbers = []
        for i in range(count):
            if current_number <= 15:
                chosen_numbers.append(current_number)
                current_number += 1

        print(f"Player {player} chooses: {chosen_numbers}")

        if check_lose_on_13(player, chosen_numbers):
            break

        if check_lose_on_14(player, chosen_numbers):
            break

        if 15 in chosen_numbers:
            print(f"\nPlayer {player} said 15!")
            print(f"Player {3 - player} wins the game!")
            break

def check_lose_on_13(player, chosen_numbers):
    """If player says 13, they lose."""
    if 13 in chosen_numbers:
        print(f"\nPlayer {player} said 13!")
        print(f"Player {player} loses the game!")
        print(f"Player {3 - player} wins!")
        return True
    return False


def check_lose_on_14(player, chosen_numbers):
    """If player says 14, the other player loses."""
    if 14 in chosen_numbers:
        print(f"\nPlayer {player} said 14!")
        print(f"Player {player} wins the game!")
        print(f"Player {3 - player} loses because they must say 15.")
        return True
    return False
        
    player = 2 if player == 1 else 1


counting_game()
