from understatapi import UnderstatClient
import pandas as pd

with UnderstatClient() as understat:
    # Get all EPL players for 2024
    league_players = understat.league(league="EPL").get_player_data(season="2024")
    
    # Find Salah by name
    salah_info = next(player for player in league_players if player["player_name"] == "Mohamed Salah")
    
    # Get all shots
    all_shots = understat.player(player=salah_info["id"]).get_shot_data()
    
    # Filter shots for 2024/25 season
    shots_2024_25 = [shot for shot in all_shots if shot["season"] == "2024"]

# Convert to DataFrame and save
df = pd.DataFrame(shots_2024_25)
df.to_csv("mo_salah_2024_understat.csv", index=False)

print("CSV saved as mo_salah_2024_understat.csv")
print("Total shots in 2024/25:", len(shots_2024_25))
