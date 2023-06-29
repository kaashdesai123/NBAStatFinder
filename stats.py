from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, teamyearbyyearstats
import pandas as pd

def get_player_stats(player_name):
    nba_players = players.get_players()
    player_info = [player for player in nba_players if player['full_name'].lower() == player_name.lower()]
    if not player_info:
        print("Player not found.")
        return

    career = playercareerstats.PlayerCareerStats(player_id=player_info[0]['id'])
    career_df = career.get_data_frames()[0]
    print(career_df)

def compare_players(player1_name, player2_name):
    print(f"Stats for {player1_name}:")
    get_player_stats(player1_name)
    print(f"\nStats for {player2_name}:")
    get_player_stats(player2_name)

def get_team_stats(team_name):
    nba_teams = teams.get_teams()
    team_info = [team for team in nba_teams if team['full_name'].lower() == team_name.lower()]
    if not team_info:
        print("Team not found.")
        return

    team_stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team_info[0]['id'])
    team_stats_df = team_stats.get_data_frames()[0]
    print(team_stats_df)

def main_menu():
    while True:
        print("\n1. Get player stats\n2. Compare two players\n3. Get team stats\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            player_name = input("Enter player's full name: ")
            get_player_stats(player_name)
        elif choice == '2':
            player1_name = input("Enter first player's full name: ")
            player2_name = input("Enter second player's full name: ")
            compare_players(player1_name, player2_name)
        elif choice == '3':
            team_name = input("Enter team's full name: ")
            get_team_stats(team_name)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
