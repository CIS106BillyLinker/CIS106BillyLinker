def write_players_to_file():
    players = [
        ("John Doe", 0.320),
        ("Jane Smith", 0.275),
        ("Alice Johnson", 0.290),
        ("Bob Brown", 0.310),
        ("Charlie Davis", 0.300),
        ("Diana Prince", 0.340),
        ("Ethan Hunt", 0.265),
        ("Fiona Apple", 0.280),
        ("George Lucas", 0.295),
        ("Hannah Montana", 0.330)
    ]

    with open('players.txt', 'w') as file:
        for player in players:
            file.write(f"{player[0]},{player[1]}\n")

def display_players():
    with open('players.txt', 'r') as file:
        for line in file:
            name, average = line.strip().split(',')
            print(f"Player: {name}, Batting Average: {average}")

def search_player(last_name):
    with open('players.txt', 'r') as file:
        for line in file:
            name, average = line.strip().split(',')
            if last_name in name.split()[-1]:
                print(f"Found: {name}, Batting Average: {average}")
                return
    print("Player not found.")

def main():
    write_players_to_file()
    display_players()

    while True:
        last_name = input("Enter a last name to search for (or 'exit' to quit): ")
        if last_name.lower() == 'exit':
            break
        search_player(last_name)

if __name__ == "__main__":
    main()
