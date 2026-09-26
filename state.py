class CubeState():
    def __init__(self):
        self.cp = list(range(8))
        self.co = [0] * 8
        self.ep = list(range(12))
        self.eo = [0] * 12
        
        '''
        cp (corner permutation):
        u = 0,1,2,3
        d = 4,5,6,7

        ep (edge permutation):
        up floor = 0(ur: white-red), 1(uf: white-green), 2(ul: white-orange), 3(ub: white-blue)
        mid floor = 4(fr: green-red), 5(fl: green-orange), 6(bl: blue-orange), 7(br: blue-red)
        bottom floor = 8(dr: yellow-red), 9(df: yellow-green), 10(dl: yellow-orange), 11(db: yellow-blue)

        co (corner orientation):
        0 = oriented (correct angle)
        1 = twisted clockwise
        2 = twisted counter-clockwise

        eo (edge orientation):
        0: oriented (correct direction)
        1: flipped
        '''

    def is_solved(self) -> bool:
        return (
            self.cp == list(range(8))
            and self.co == [0] * 8
            and self.ep == list(range(12))
            and self.eo == [0] * 12
        )

    def move_u(self) -> None:
        self.cp[0], self.cp[1], self.cp[2], self.cp[3] = (
            self.cp[3],
            self.cp[0],
            self.cp[1],
            self.cp[2],
        )

        self.co[0], self.co[1], self.co[2], self.co[3] = (
            self.co[3],
            self.co[0],
            self.co[1],
            self.co[2],
        )

        self.ep[0], self.ep[1], self.ep[2], self.ep[3] = (
            self.ep[3],
            self.ep[0],
            self.ep[1],
            self.ep[2],
        )

        self.eo[0], self.eo[1], self.eo[2], self.eo[3] = (
            self.eo[3],
            self.eo[0],
            self.eo[1],
            self.eo[2],
        )

    def move_d(self) -> None:
        self.cp[4], self.cp[5], self.cp[6], self.cp[7] = (
            self.cp[5],
            self.cp[6],
            self.cp[7],
            self.cp[4],
        )

        self.co[4], self.co[5], self.co[6], self.co[7] = (
            self.co[5], 
            self.co[6], 
            self.co[7], 
            self.co[4], 
        )

        self.ep[8], self.ep[9], self.ep[10], self.ep[11] = (
            self.ep[9],
            self.ep[10],
            self.ep[11],
            self.ep[8],
        )

        self.eo[8], self.eo[9], self.eo[10], self.eo[11] = (
            self.eo[9],
            self.eo[10],
            self.eo[11],
            self.eo[8],
        )

    def move_r(self) -> None:
        self.cp[0], self.cp[3], self.cp[7], self.cp[4] = (
            self.cp[4],
            self.cp[0],
            self.cp[3],
            self.cp[7],
        )

        self.co[0], self.co[3], self.co[7], self.co[4] = (
            (self.co[4] + 2) % 3,
            (self.co[0] + 1) % 3,
            (self.co[3] + 2) % 3,
            (self.co[7] + 1) % 3,
        )

        self.ep[0], self.ep[7], self.ep[8], self.ep[4] = (
            self.ep[4],
            self.ep[0],
            self.ep[7],
            self.ep[8],
        )

        self.eo[0], self.eo[7], self.eo[8], self.eo[4] = (
            self.eo[4],
            self.eo[0],
            self.eo[7],
            self.eo[8],
        )

    def move_l(self) -> None:
        self.cp[1], self.cp[5], self.cp[6], self.cp[2] = (
            self.cp[2],
            self.cp[1],
            self.cp[5],
            self.cp[6],
        )

        self.co[1], self.co[5], self.co[6], self.co[2] = (
            (self.co[2] + 1) % 3,
            (self.co[1] + 2) % 3,
            (self.co[5] + 1) % 3,
            (self.co[6] + 2) % 3, 
        )

        self.ep[2], self.ep[5], self.ep[10], self.ep[6] = (
            self.ep[6],
            self.ep[2],
            self.ep[5],
            self.ep[10],
        )

        self.eo[2], self.eo[5], self.eo[10], self.eo[6] = (
            self.eo[6],
            self.eo[2],
            self.eo[5],
            self.eo[10],
        )

    def move_m(self) -> None:
        self.ep[1], self.ep[9], self.ep[11], self.ep[3] = (
            self.ep[3],
            self.ep[1],
            self.ep[9],
            self.ep[11],
        )

        self.eo[1], self.eo[9], self.eo[11], self.eo[3] = (
            (self.eo[3] + 1) % 2,
            (self.eo[1] + 1) % 2,
            (self.eo[9] + 1) % 2,
            (self.eo[11] + 1) % 2,
        )

    def move_f(self) -> None:
        self.cp[0], self.cp[4], self.cp[5], self.cp[1] = (
            self.cp[1],
            self.cp[0],
            self.cp[4],
            self.cp[5],
        )

        self.co[0], self.co[4], self.co[5], self.co[1] = (
            (self.co[1] + 1) % 3,
            (self.co[0] + 2) % 3,
            (self.co[4] + 1) % 3,
            (self.co[5] + 2) % 3,
        )

        self.ep[1], self.ep[4], self.ep[9], self.ep[5] = (
            self.ep[5],
            self.ep[1],
            self.ep[4],
            self.ep[9],
        )

        self.eo[1], self.eo[4], self.eo[9], self.eo[5] = (
            (self.eo[5] + 1) % 2,
            (self.eo[1] + 1) % 2,
            (self.eo[4] + 1) % 2,
            (self.eo[9] + 1) % 2,
        )

    def move_b(self) -> None:
        self.cp[2], self.cp[6], self.cp[7], self.cp[3] = (
            self.cp[3],
            self.cp[2],
            self.cp[6],
            self.cp[7],
        )

        self.co[2], self.co[6], self.co[7], self.co[3] = (
            (self.co[3] + 2) % 3,
            (self.co[2] + 1) % 3,
            (self.co[6] + 2) % 3,
            (self.co[7] + 1) % 3,
        )

        self.ep[3], self.ep[6], self.ep[11], self.ep[7] = (
            self.ep[7],
            self.ep[3],
            self.ep[6],
            self.ep[11],
        )

        self.eo[3], self.eo[6], self.eo[11], self.eo[7] = (
            (self.eo[7] + 1) % 2,
            (self.eo[3] + 1) % 2,
            (self.eo[6] + 1) % 2,
            (self.eo[11] + 1) % 2,
        )

    # actually moving the cube
    def apply_move(self, move: str) -> None:
        base_moves = {
                    'U': self.move_u,
                    'D': self.move_d,
                    'R': self.move_r,
                    'L': self.move_l,
                    'M': self.move_m,
                    'F': self.move_f,
                    'B': self.move_b,
                }
        m = move.strip()
        face = m[0]
        if m.endswith("'"):
            count = 3
        elif m.endswith("2"):
            count = 2
        else:
            count = 1
        for _ in range(count):
            base_moves[face]()

    def apply_algorithm(self, alg: str) -> None:
        for move in alg.split():
            self.apply_move(move)

    # copying the cube
    def copy(self):
        new_cube = self.__class__()
        new_cube.cp = self.cp.copy()
        new_cube.co = self.co.copy()
        new_cube.eo = self.eo.copy()
        new_cube.ep = self.ep.copy()
        return new_cube

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__): return False
        return (
            self.cp == other.cp
            and self.co == other.co
            and self.ep == other.ep
            and self.eo == other.eo
        )