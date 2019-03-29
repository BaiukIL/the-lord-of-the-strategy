import logging


# "Composite" pattern in the future
class Army:
    def __init__(self, race):
        self.units = list()
        self.race = race

    def info(self):
        print("Army race: {}".format(self.race.__name__))
        print("Army units:")
        for unit in self.units:
            print(" - {}".format(unit))

    def _add_unit(self, unit):
        self.units.append(unit)
        logging.info("{} has joined to {}Empire army".format(unit, self.race.__name__))
