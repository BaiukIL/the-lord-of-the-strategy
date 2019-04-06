from units import unit


class Scout(unit.Unit):
    pass


class ElfScout(unit.ElfUnit, Scout):
    pass


class OrcScout(unit.OrcUnit, Scout):
    pass


class DwarfScout(unit.DwarfUnit, Scout):
    pass
