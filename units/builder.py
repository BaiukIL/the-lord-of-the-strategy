from units import unit


class Builder(unit.Unit):
    pass


class ElfBuilder(unit.ElfUnit, Builder):
    pass


class OrcBuilder(unit.OrcUnit, Builder):
    pass


class DwarfBuilder(unit.DwarfUnit, Builder):
    pass
