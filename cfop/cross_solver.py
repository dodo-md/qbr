from core.state import CubeState
from collections import deque

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

def build_cross_table():
    c = CubeState()
    solved = get_cross_state(c)
    table = {solved: None}
    queue = deque([(c, solved)])

    while queue:
        curr_cube, curr_st = queue.popleft()

        for m in inverse_map.keys():
            next_c = curr_cube.copy()
            next_c.apply_move(m)
            nxt_st = get_cross_state(next_c)

            if nxt_st not in table:
                table[nxt_st] = inverse_map[m]
                queue.append((next_c, nxt_st))

    return table

def solve_cross(cube, table):
    moves = []
    while not cube.is_cross_solved():
        st = get_cross_state(cube)
        m = table[st]
        cube.apply_move(m)
        moves.append(m)
    return " ".join(moves)

if __name__ == "__main__":
    print("mapping 190.080 cases..")
    table = build_cross_table()
    print("map is ready! found:", len(table))

    cube = CubeState()
    # wca scramble
    cube.apply_algorithm("D' L2 R2 B2 L2 R2 U B2 U2 F2 L2 D2 L D2 B R2 F U B2 R2 U'")
    print("is cross solved after scramble?:", cube.is_cross_solved())

    solution = solve_cross(cube, table)
    print("found solution:", solution)
    print("is cross solved?:", cube.is_cross_solved())