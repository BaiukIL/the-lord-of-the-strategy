import health
import logging


class Building(health.Health):
    def __init__(self, strength):
        health.Health.__init__(self, strength)
        logging.info("{} is created".format(self.__class__.__name__))

    def update(self):
        pass
        logging.info("{} has been updated!".format(self.__class__.__name__))

    def _destroy(self):
        pass
        logging.info("{} has been destroyed".format(self.__class__.__name__))


# fabric of units
class Barrack(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def create_scout(self, ):
        raise NotImplementedError

    def create_builder(self):
        raise NotImplementedError

    def create_warrior(self):
        raise NotImplementedError


class Mine(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def mine(self):
        logging.info("{} is mining".format(self.__class__.__name__))


class Wall(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def update(self):
        pass
        logging.info("{} is updated".format(self.__class__.__name__))
