from cfop.f2l_solver import get_f2l_table, solve_f2l
from cfop.cross_solver import get_cross_table, solve_cross
from cfop.pll import pll_algorithms
from cfop.oll import oll_algorithms
from cfop.oll import twolook_oll_algorithms
from core.state import CubeState

class qbragent():
    def solve_oll(self, cube, twolook: bool = False):
        if cube.is_solved(): return ""
        auf_moves = ["", "U", "U2", "U'"]
        
        if twolook:
            cross_moves = ""
            corner_moves = ""
        
            if not cube.is_oll_cross_solved():
                for pre in auf_moves:
                    for name in ["line", "angle", "dot"]:
                        alg = twolook_oll_algorithms[name]
                        for post in auf_moves:
                            moves = f"{pre} {alg} {post}".strip()
                            sim_cube = cube.copy()
                            sim_cube.apply_algorithm(moves)
                            if sim_cube.is_oll_cross_solved():
                                    cross_moves = moves
                                    cube.apply_algorithm(moves)
                                    break
                        if cross_moves: break
                    if cross_moves: break

            if not cube.is_oll_solved():
                corner_names = ["sune", "anti-sune", "h", "pi", "t", "l", "u"]
                for pre in auf_moves:
                    for name in corner_names:
                        alg = twolook_oll_algorithms[name]
                        for post in auf_moves:
                            moves = f"{pre} {alg} {post}".strip()
                            sim_cube = cube.copy()
                            sim_cube.apply_algorithm(moves)
                            if sim_cube.is_oll_solved():
                                corner_moves = moves
                                cube.apply_algorithm(moves)
                                break
                        if corner_moves: break
                    if corner_moves: break

        else:
            for pre in auf_moves:
                for name, alg in oll_algorithms.items():
                    for post in auf_moves:
                        moves = f"{pre} {alg} {post}".strip()
                        sim_cube = cube.copy()
                        sim_cube.apply_algorithm(moves)
                        if sim_cube.is_oll_solved():
                            cube.apply_algorithm(moves)
                            return moves
            return ""
                        
        return f"{cross_moves} {corner_moves}".strip()

    def solve_pll(self, cube):
        if cube.is_solved(): return ""
        auf_moves = ["", "U", "U2", "U'"]

        for auf in auf_moves:
             sim_cube = cube.copy()
             sim_cube.apply_algorithm(auf)
             if sim_cube.is_solved():
                  cube.apply_algorithm(auf)
                  return auf

        for pre in auf_moves:
            for name, alg in pll_algorithms.items():
                for post in auf_moves:
                        moves = f"{pre} {alg} {post}".strip()
                        sim_cube = cube.copy()
                        sim_cube.apply_algorithm(moves)
                        if sim_cube.is_solved():
                            cube.apply_algorithm(moves)
                            return moves
        return None

    def solve(self, cube):
            oll_moves = self.solve_oll(cube) or ""
            pll_moves = self.solve_pll(cube) or ""
            return f"{oll_moves} {pll_moves}".strip()

    def __init__(self):
        self.cross_table = get_cross_table()
        self.f2l_table = get_f2l_table()

    def solve(self, cube):
         c_moves = solve_cross(cube, self.cross_table)
         f_moves = solve_f2l(cube, self.f2l_table)
         o_moves = self.solve_oll(cube)
         p_moves = self.solve_pll(cube)
         steps = [c_moves, f_moves, o_moves, p_moves]
         return " ".join(m for m in steps if m)

if __name__ == "__main__":
    cube = CubeState()
    cube.apply_algorithm("B' U2 R L2 D L2 U' L2 F2 L2 R2 U B2 L2 B' L U B R' D' R")
    agent = qbragent()
    solution = agent.solve(cube)
    print("the moves that agent have found:", solution)
    print("is the cube solved:", cube.is_solved())