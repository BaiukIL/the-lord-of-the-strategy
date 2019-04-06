from buildings import base_building


class MineBuilder(base_building.BaseBuilder):
    pass


class MineDirector:
    def build_elf_mine(self, builder, city):
        builder.reset(ElfMine())
        builder.set_health(3)
        builder.set_city(city)
        return builder.get()

    def build_orc_mine(self, builder, city):
        builder.reset(OrcMine())
        builder.set_health(3)
        builder.set_city(city)
        return builder.get()

    def build_dwarf_mine(self, builder, city):
        builder.reset(DwarfMine())
        builder.set_health(3)
        builder.set_city(city)
        return builder.get()


class Mine(base_building.Building):
    def mine(self):
        print("{} is mining".format(self.__class__.__name__))


class ElfMine(Mine):
    pass


class OrcMine(Mine):
    pass


class DwarfMine(Mine):
    pass
