from state import CubeState

inverse_map = {
    "U": "U'", "U'": "U",
    "D": "D'", "D'": "D",
    "R": "R'", "R'": "R",
    "L": "L'", "L'": "L",
    "F": "F'", "F'": "F",
    "B": "B'", "B'": "B",
}

def get_cross_state(cube):
    pos8 = cube.ep.index(8); ori8 = cube.eo[pos8]
    pos9 = cube.ep.index(9); ori9 = cube.eo[pos9]
    pos10 = cube.ep.index(10); ori10 = cube.eo[pos10]
    pos11 = cube.ep.index(11); ori11 = cube.eo[pos11]
    return (pos8, ori8, pos9, ori9, pos10, ori10, pos11, ori11)

