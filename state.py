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

        self.ep[0], self.ep[1], self.ep[2], self.ep[3] = (
            self.ep[3],
            self.ep[0],
            self.ep[1],
            self.ep[2],
        )

    def move_d(self) -> None:
        self.cp[4], self.cp[5], self.cp[6], self.cp[7] = (
            self.cp[5],
            self.cp[6],
            self.cp[7],
            self.cp[4],
        )

        self.ep[8], self.ep[9], self.ep[10], self.ep[11] = (
            self.ep[9],
            self.ep[10],
            self.ep[11],
            self.ep[8],
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

cube = CubeState()
print('start:', cube.is_solved())

cube.move_b()
print('1x move later:', cube.is_solved())

cube.move_b()
print('2x move later:', cube.is_solved())

cube.move_b()
cube.move_b()
print('4x move later:', cube.is_solved())