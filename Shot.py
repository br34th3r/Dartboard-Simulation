class Shot:
    def __init__(self, board):
        self.x, self.y = board.shoot()

    def getX(self):
        return self.x

    def getY(self):
        return self.y
