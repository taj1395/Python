def display_team_records():
    teams = [
        {"Team ID": 1, "Team Name": "Team Gandalf", "Mascot": "White Wizards"},
        {"Team ID": 2, "Team Name": "Team Sauron", "Mascot": "Orcs"}
    ]

    for team in teams:
        print("- - DISPLAYING TEAM RECORDS")
        print("Team ID:", team["Team ID"])
        print("Team Name:", team["Team Name"])
        print("Mascot:", team["Mascot"])
        print()


def display_player_records():
    players = [
        {"Player ID": 1, "First Name": "Thorin", "Last Name": "Oakenshield", "Team ID": 1},
        {"Player ID": 2, "First Name": "Bilbo", "Last Name": "Baggins", "Team ID": 1},
        {"Player ID": 3, "First Name": "Frodo", "Last Name": "Baggins", "Team ID": 1},
        {"Player ID": 4, "First Name": "Saruman", "Last Name": "The White", "Team ID": 2},
        {"Player ID": 5, "First Name": "Angmar", "Last Name": "Witch-king", "Team ID": 2},
        {"Player ID": 6, "First Name": "Azog", "Last Name": "The Defiler", "Team ID": 2}
    ]

    for player in players:
        print("- - DISPLAYING PLAYER RECORDS")
        print("Player ID:", player["Player ID"])
        print("First Name:", player["First Name"])
        print("Last Name:", player["Last Name"])
        print("Team ID:", player["Team ID"])
        print()


if _name_ == "_main_":
    display_team_records()
    display_player_records()
