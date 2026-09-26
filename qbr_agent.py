from cfopdb.pll import pll_algorithms
from cfopdb.oll import oll_algorithms
from state import CubeState

class qbragent():
    def solve_oll(self, cube):
        if cube.is_solved(): return ""
        auf_moves = ["", "U", "U2", "U'"]
        cross_moves = ""
        corner_moves = ""

        for pre in auf_moves:
            for name, alg in oll_algorithms.items():
                for post in auf_moves:
                    moves = f"{pre} {alg} {post}".strip()
                    if not cube.is_oll_cross_solved():
                        sim_cube = cube.copy()
                        sim_cube.apply_algorithm(moves)
                        if sim_cube.is_oll_cross_solved():
                            cross_moves = moves
                            cube.apply_algorithm(moves)
                            break

                    if cube.is_oll_cross_solved():
                        sim_cube = cube.copy()
                        sim_cube.apply_algorithm(moves)
                        if sim_cube.is_oll_solved():
                            corner_moves = moves
                            cube.apply_algorithm(moves)
                            break
                        
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
    cube.apply_algorithm("R U R' U R U2 R' U R U R' U' R' F R2 U' R' U' R U R' F' U'")
    agent = qbragent()
    solution = agent.solve(cube)
    print("the moves that agent have found:", solution)
    print("is it solved?:", cube.is_solved())