"""Decorators"""


class ElfBuildingUnique:
    @staticmethod
    def increase_health(method):
        def wrap(*args, **kwargs):
            pass
        return wrap


class OrcBuildingUnique:
    @ElfBuildingUnique.increase_health
    def some_method(self):
        pass


class DwarfBuildingUnique:
    pass
