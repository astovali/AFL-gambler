import itertools
import random
import types

import teams
from allowed_players import allowed_players


def tournament(group_a: list[teams.Team], group_b: list[teams.Team]):
    """
    Simulate a tournament between two populations of teams.

    Returns a tuple (scores_a, scores_b), where scores_a and scores_b are
    dicts containing the cumulative scores of each team in group_a or group_b.
    """
    scores_a = dict.fromkeys(group_a)
    scores_b = dict.fromkeys(group_b)

    for team_a, team_b in itertools.product(group_a, group_b):
        outcome = teams.simulate_match(team_a, team_b)
        scores_a[team_a] -= outcome
        scores_b[team_b] += outcome
    
    return scores_a, scores_b


def generate_variations(team: teams.Team, allowed_players: teams.Player, count: int):
    """
    Generate `count` variations of the team `team`.
    """
    return team.generate_variations(count, allowed_players, 10, alpha=1, beta=5)


def select_and_vary(
        scores: dict[teams.Player:int|float],
        generate_variation: types.FunctionType,
        allowed_players: list[teams.Player]
        ):
    """
    Select the best team in the population and generate variations of it.
    There will be as many variations as teams in the original group `scores`
    """
    best_team = max(scores, key=lambda team: scores[team])
    return generate_variations(best_team, allowed_players, len(scores))

if __name__ == "__main__":
    pass