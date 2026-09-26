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

cube = CubeState()
print(cube.is_solved())