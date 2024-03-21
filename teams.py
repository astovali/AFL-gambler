import random
import sys

class Player:
    def __init__(self, name: str, data: dict):
        self.name = str(name)
        self.data = data
    
    def __repr__(self):
        return f"Player(\"{self.name}\", {self.data})"
    
    def __str__(self):
        return self.name
    
    def __eq__(self, value):
        return self.name == value.name and self.data == value.data
    
    def __hash__(self):
        return (hash(self.name) + hash(tuple(self.data.values()))) % sys.maxsize


class Team:
    def __init__(self, players: frozenset[Player]):
        self.players = players
        self.__hash = random.randint(0, sys.maxsize)
    
    def generate_variations(self, count: int, allowed_players: frozenset[Player], max_variations: int, alpha = 1, beta=5):
        for _ in range(count):
            variations = max_variations * int(random.betavariate(alpha, beta))
            result = set(self.players)
            for player in frozenset(random.sample(list(self.players), variations)):
                result.pop(player)
                result.add(
                    random.choice(
                        list(allowed_players.difference(result)) # Do not add the same player twice to result.
                    )
                )
        
            yield Team(frozenset(result))
    
    def __eq__(self, value):
        return False
    
    def __hash__(self):
        return self.__hash
        


def simulate_match(team_1, team_2) -> int | float:
    """
    Simulates a game between teams 1 and 2.
    Returns a negative number if team 1 wins,
    and a positive number if team 2 wins.

    The magnitude of the number is a metric of how effective one team is
    against the other.

    This function exists because the problem we are trying to solve
    is intransitive. For example, if A beats B and B beats C, it is
    not necessarily implied that A beats C.
    """
    return NotImplemented
