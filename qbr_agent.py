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
        if cube.is_solved(): return ""
        auf_moves = ["", "U", "U2", "U'"]

        for pre in auf_moves:
            for name, alg in 

if __name__ == "__main__":
    cube = CubeState()
    cube.apply_algorithm("R U R' U R U2 R' F R U R' U' F' U2 F U R U' R' F'")
    agent = qbragent()
    solution = agent.solve_oll(cube)
    print("the moves that agent have found:", solution)
    print("is oll solved?:", cube.is_oll_solved())