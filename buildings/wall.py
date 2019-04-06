from buildings import base_building


class WallBuilder(base_building.BaseBuilder):
    pass


class WallDirector:
    def build_elf_wall(self, builder, city):
        builder.reset(ElfWall())
        builder.set_health(3)
        builder.set_city(city)
        return builder.get()

    def build_orc_wall(self, builder, city):
        builder.reset(OrcWall())
        builder.set_health(3)
        builder.set_city(city)
        return builder.get()

    def build_dwarf_wall(self, builder, city):
        pass
        builder.reset(DwarfWall())
        builder.set_health(3)
        builder.set_city(city)
        return builder.get()


class Wall(base_building.Building):
    pass


class ElfWall(Wall):
    pass


class OrcWall(Wall):
    pass


class DwarfWall(Wall):
    pass
