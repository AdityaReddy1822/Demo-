import random

# Function to calculate the winning number
def calculate_winning_number(numbers):
    average = sum(numbers) / len(numbers)
    return average * 0.8

# Function to determine the winner
def find_winner(players, winning_number):
    closest_player = None
    closest_distance = float('inf')

    for player in players:
        distance = abs(player['chosen_number'] - winning_number)
        if distance < closest_distance:
            closest_distance = distance
            closest_player = player

    return closest_player

# Function to display the scores
def display_scores(players):
    print("\nCurrent Scores:")
    for player in players:
        print(f"{player['name']}: {player['score']} points")

def main():
    print("Welcome to the King of Diamonds game!")
    
    # Step 1: Collect player information
    num_players = int(input("Enter the number of players: "))
    players = []
    
    for i in range(num_players):
        name = input(f"Enter name of Player {i + 1}: ")
        players.append({'name': name, 'score': 3, 'chosen_number': 0})

    # Step 2: Game loop
    while len(players) > 1:
        print("\nNew Round Started!")
        
        # Step 3: Player chooses a number
        for player in players:
            while True:
                try:
                    chosen_number = int(input(f"{player['name']}, choose a number between 0 and 100: "))
                    if 0 <= chosen_number <= 100:
                        player['chosen_number'] = chosen_number
                        break
                    else:
                        print("Please choose a number between 0 and 100.")
                except ValueError:
                    print("Invalid input, please enter an integer.")

        # Step 4: Calculate the winning number
        winning_number = calculate_winning_number([player['chosen_number'] for player in players])
        print(f"\nThe winning number is: {winning_number:.2f}")

        # Step 5: Find the winner
        winner = find_winner(players, winning_number)
        print(f"\nThe winner of this round is {winner['name']} with the closest number: {winner['chosen_number']}")

        # Step 6: Update scores and eliminate players
        for player in players:
            if player != winner:
                player['score'] -= 1
                if player['score'] <= 0:
                    print(f"\n{player['name']} has been eliminated!")
                    players.remove(player)

        # Step 7: Display scores
        display_scores(players)

        # Step 8: Check if only one player remains
        if len(players) == 1:
            print(f"\n{players[0]['name']} is the ultimate winner!")
            break

        # Pause for the next round
        input("\nPress Enter to start the next round...")

if __name__ == "__main__":
    main()
