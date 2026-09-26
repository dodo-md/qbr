class CubeState():
    def __init__(self):
        self.cp = list(range(8))
        self.co = [0] * 8
        self.ep = list(range(12))
        self.eo = [0] * 12

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

cube = CubeState()
print('start:', cube.is_solved())

cube.move_u()
print('1x u later:', cube.is_solved())

cube.move_u()
cube.move_u()
cube.move_u()
print('4x u later:', cube.is_solved())