from core.state import CubeState
import random

def generate_scramble(length: int = 20) -> str:
    notations = ["U", "D", "R", "L", "F", "B"]
    modifiers = ["", "'", "2"]
    opposite = {
        "U": "D", "D": "U",
        "R": "L", "L": "R",
        "F": "B", "B": "F",
    }

    moves = []
    last_notation = None
    second_last_notation = None

    while len(moves) < length:
        notation = random.choice(notations)

        if notation == last_notation: continue

        if last_notation is not None and notation == second_last_notation and opposite[notation] == last_notation: continue

        modifier = random.choice(modifiers)
        moves.append(f"{notation}{modifier}")

        second_last_notation = last_notation
        last_notation = notation

    return " ".join(moves)

print(generate_scramble())