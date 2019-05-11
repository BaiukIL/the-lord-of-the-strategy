import templates


class Player(metaclass=templates.Singleton):
    def __init__(self, empire):
        self.empire = empire


class AI(Player):
    def lead(self):
        pass
