class CubeState():
    def __init__(self):
        self.cp = list(range(8))
        self.co = [0] * 8
        self.ep = list(range(12))
        self.eo = [0] * 12
        
        '''
        cp:
        u = 0,1,2,3
        d = 4,5,6,7

        ep:
        up floor = 0,1,2,3
        mid floor = 4,5,6,7
        bottom floor = 8,9,10,11

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

        self.ep[0], self.ep[7], self.ep[8], self.ep[4] = (
            self.ep[4],
            self.ep[0],
            self.ep[7],
            self.ep[8],
        )

cube = CubeState()
print('start:', cube.is_solved())

cube.move_r()
print('1x r later:', cube.is_solved())

cube.move_r()
cube.move_r()
cube.move_r()
print('4x r later:', cube.is_solved())