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

if __name__ == "__main__":
    cube = CubeState()
    cube.apply_algorithm("R D B2 R2 U' R2 D B2 D2 B2 L' B R' B2 L B' U2")
    agent = qbragent()
    solution = agent.solve_oll(cube)
    print("the moves that agent have found:", solution)
    print("is oll solved?:", cube.is_oll_solved())
    print("is oll cross solved?:", cube.is_oll_cross_solved())