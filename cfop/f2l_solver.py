import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.state import CubeState
from collections import deque
import os
import pickle

cache_path = os.path.join(os.path.dirname(__file__), "..", "weights", "f2l_table.pkl")

slot_triggers = {4: ["R U R'", "R U' R'", "R U' R'", "F' U' F", "R U R' U'", "R' F R F'", "U", "U'", "U2"], 5: ["L' U' L", "L' U2 L", "L' U2 L", "F U F'", "L' U' L U", "L F' L' F", "U", "U'", "U2"], 6: ["L U L'", "L U' L'", "L U' L'", "B' U' B", "L U L' U'", "U", "U'", "U2"], 7: ["R' U' R", "R' U R", "R' U2 R", "B U B'", "R' U' R U", "U", "U'", "U2"]}

def get_slot_state(cube, slot_idx):
    c_pos = cube.cp.index(slot_idx); c_ori = cube.co[c_pos]
    e_pos = cube.ep.index(slot_idx); e_ori = cube.eo[e_pos]
    return (c_pos, c_ori, e_pos, e_ori)

def invert_alg(alg):
    invert_map = {
        "U": "U'", "U'": "U",
        "U2": "U2",
        "D": "D'", "D'": "D",
        "R": "R'", "R'": "R",
        "L": "L'", "L'": "L",
        "F": "F'", "F'": "F",
        "B": "B'", "B'": "B",
    }
    moves = alg.split()
    inverted = []
    for m in reversed(moves):
        inverted.append(invert_map[m])
    return " ".join(inverted)

def build_slot_table(slot_idx):
    c = CubeState()
    solved = get_slot_state(c, slot_idx)
    table = {solved: None}
    queue = deque([(c, solved)])

    while queue:
        curr_cube, curr_st = queue.popleft()

        for trig in slot_triggers[slot_idx]:
            next_c = curr_cube.copy()
            next_c.apply_algorithm(trig)
            nxt_st = get_slot_state(next_c, slot_idx)

            if nxt_st not in table:
                table[nxt_st] = invert_alg(trig)
                queue.append((next_c, nxt_st))
    return table

def get_f2l_table(path=cache_path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        print("getting f2l map..")
        with open(path, "rb") as f:
            return pickle.load(f)

    print("mapping possible cases..")
    table = {s: build_slot_table(s) for s in [4, 5, 6, 7]}
    with open(path, "wb") as f:
        pickle.dump(table, f)
    print("the map has saved to weights/f2l_table.pkl")
    return table

def solve_slot(cube, slot_idx, table):
    moves = []
    while get_slot_state(cube, slot_idx) != (slot_idx, 0, slot_idx, 0):
        st = get_slot_state(cube, slot_idx)
        c_pos, c_ori, e_pos, e_ori = st
        if c_pos in [4, 5, 6 ,7] and c_pos != slot_idx: alg = slot_triggers[c_pos][0]
        elif e_pos in [4, 5, 6, 7] and e_pos != slot_idx: alg = slot_triggers[e_pos][0]
        else: alg = table[st]
        cube.apply_algorithm(alg)
        moves.append(alg)
    return " ".join(moves)

turn_map = {"": 1, "2": 2, "'": 3}
inv_turn_map = {1: "", 2: "2", 3: "'"}

def simplify_moves(moves_str):
    if not moves_str: return ""
    stack = []

    for m in moves_str.split():
        face = m[0]
        amount = turn_map[m[1::]]

        if stack and stack[-1][0] == face:
            prev_face, prev_amount = stack.pop()
            new_amount = (prev_amount + amount) % 4
            if new_amount != 0:
                stack.append((face, new_amount))
        else:
            stack.append((face, amount))

    return " ".join(f"{face}{inv_turn_map[amt]}" for face, amt in stack)

def solve_f2l(cube, tables):
    all_moves = []
    for slot_idx in [4, 5, 6,7]:
        moves = solve_slot(cube, slot_idx, tables[slot_idx])
        if moves: all_moves.append(moves)
    return simplify_moves(" ".join(all_moves))
        
if __name__ == "__main__":
    table = get_f2l_table()
    print("map is ready! found:", len(table))

    cube = CubeState()
    # cross solved scramble
    scramble = "L2 U' B2 D2 R2 U L2 B2 U2 F2 R' U2 B' U' B2 R' F' U2 F"
    cube.apply_algorithm(scramble)

    print("is f2l solved after scramble?:", get_slot_state(cube, 4))
    solution = solve_f2l(cube, table)
    print("found solution:", solution)
    print("is slot solved?:", get_slot_state(cube, 4))
    print("is f2l solved?:", cube.is_f2l_solved())