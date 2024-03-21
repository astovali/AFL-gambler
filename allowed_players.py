import json

import teams

allowed_players: list[teams.Player]

with open("players.json") as file:
    allowed_players = [
        teams.Player(player_info.pop("Player"),player_info)
        for player_info
        in json.load(file)
    ]