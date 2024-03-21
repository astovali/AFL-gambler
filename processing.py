import csv
import json

with (
        open("afl-player-stats-2024.csv") as file,
        open("players.json", mode="w") as dump_file
    ):
    table = csv.DictReader(file)
    dump_me = [row for row in table]

    json.dump(dump_me, dump_file)
