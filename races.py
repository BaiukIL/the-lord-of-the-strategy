elves = 'elves'
orcs = 'orcs'
dwarfs = 'dwarfs'


class Race:
    def what_race(self):
        raise NotImplementedError


class Elves(Race):
    def what_race(self):
        return elves


class Orcs(Race):
    def what_race(self):
        return orcs


class Dwarfs(Race):
    def what_race(self):
        return dwarfs
