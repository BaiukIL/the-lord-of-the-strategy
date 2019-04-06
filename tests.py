"""
Modules testing module. There are all the tests.
Tests of different race objects differs only in race names, so it has sense to look at one of them.
For example, test_elf_empire and test_dwarf_empire
"""


import unittest
import empire as empire_mod
import city as city_mod
from buildings import barrack
from buildings import wall
from buildings import mine
import races
import army as army_mod
from units import scout
from units import warrior
from units import builder


class TestEmpire(unittest.TestCase):
    def test_elf_empire(self):
        empire = empire_mod.EmpireFactory().create_empire(races.elves)
        self.assertEqual(empire.__class__, empire_mod.ElfEmpire)

        self.assertEqual(empire.what_race(), races.elves)

        self.assertRaisesRegex(KeyError, "Oviar city doesn't exist in {}".format(empire.__class__.__name__),
                               lambda: empire.get_city("Oviar"))

        empire.establish_city("Oviar")
        self.assertEqual(empire.get_city("Oviar").what_race(), races.elves)

        self.assertRaisesRegex(KeyError, "City Oviar has already exists in {} cities".format(empire.__class__.__name__),
                               lambda: empire.establish_city("Oviar"))

        empire.destroy_city("Oviar")
        self.assertRaisesRegex(KeyError, "Oviar city doesn't exist in {}".format(empire.__class__.__name__),
                               lambda: empire.get_city("Oviar"))

    def test_orc_empire(self):
        empire = empire_mod.EmpireFactory().create_empire(races.orcs)
        self.assertEqual(empire.__class__, empire_mod.OrcEmpire)

        self.assertEqual(empire.what_race(), races.orcs)

        self.assertRaisesRegex(KeyError, "Reut city doesn't exist in {}".format(empire.__class__.__name__),
                               lambda: empire.get_city("Reut"))
        empire.establish_city("Reut")
        self.assertEqual(empire.get_city("Reut").what_race(), races.orcs)

        self.assertRaisesRegex(KeyError, "City Reut has already exists in {} cities".format(empire.__class__.__name__),
                               lambda: empire.establish_city("Reut"))

        empire.destroy_city("Reut")
        self.assertRaisesRegex(KeyError, "Reut city doesn't exist in {}".format(empire.__class__.__name__),
                               lambda: empire.get_city("Reut"))

    def test_dwarf_empire(self):
        empire = empire_mod.EmpireFactory().create_empire(races.dwarfs)
        self.assertEqual(empire.__class__, empire_mod.DwarfEmpire)

        self.assertEqual(empire.what_race(), races.dwarfs)
        self.assertRaisesRegex(KeyError, "Durden city doesn't exist in {}".format(empire.__class__.__name__),
                               lambda: empire.get_city("Durden"))

        empire.establish_city("Durden")
        self.assertEqual(empire.get_city("Durden").what_race(), races.dwarfs)
        self.assertRaisesRegex(KeyError, "City Durden has already exists in {} cities".format(empire.__class__.__name__),
                               lambda: empire.establish_city("Durden"))

        empire.destroy_city("Durden")
        self.assertRaisesRegex(KeyError, "Durden city doesn't exist in {}".format(empire.__class__.__name__),
                               lambda: empire.get_city("Durden"))


class TestCity(unittest.TestCase):
    def test_elf_city(self):
        empire = empire_mod.EmpireFactory().create_empire(races.elves)
        city = city_mod.ElfCity("Oviar", empire)
        self.assertEqual(city.master_empire, empire)
        self.assertEqual(city.what_race(), races.elves)
        city.build_barrack()
        city.build_wall()
        city.build_wall()
        city.build_mine()
        city.info()
        barrack1 = city.buildings[0]
        wall1 = city.buildings[1]
        wall2 = city.buildings[2]
        mine1 = city.buildings[3]
        self.assertEqual(barrack1.__class__, barrack.ElfBarrack)
        self.assertEqual(wall1.__class__, wall.ElfWall)
        self.assertEqual(wall2.__class__, wall.ElfWall)
        self.assertEqual(mine1.__class__, mine.ElfMine)
        city.remove_building(wall1)
        self.assertRaisesRegex(KeyError, "No such building: {} in Oviar".format(wall1),
                               lambda: city.remove_building(wall1))
        city.info()

    def test_orc_city(self):
        empire = empire_mod.EmpireFactory().create_empire(races.orcs)
        city = city_mod.OrcCity("Reut", empire)
        self.assertEqual(city.master_empire, empire)
        self.assertEqual(city.what_race(), races.orcs)
        city.build_barrack()
        city.build_wall()
        city.build_wall()
        city.build_mine()
        city.info()
        barrack1 = city.buildings[0]
        wall1 = city.buildings[1]
        wall2 = city.buildings[2]
        mine1 = city.buildings[3]
        self.assertEqual(barrack1.__class__, barrack.OrcBarrack)
        self.assertEqual(wall1.__class__, wall.OrcWall)
        self.assertEqual(wall2.__class__, wall.OrcWall)
        self.assertEqual(mine1.__class__, mine.OrcMine)
        city.remove_building(wall1)
        self.assertRaisesRegex(KeyError, "No such building: {} in Reut".format(wall1),
                               lambda: city.remove_building(wall1))
        city.info()

    def test_dwarf_city(self):
        empire = empire_mod.EmpireFactory().create_empire(races.dwarfs)
        city = city_mod.DwarfCity("Durden", empire)
        self.assertEqual(city.master_empire, empire)
        self.assertEqual(city.what_race(), races.dwarfs)
        city.build_barrack()
        city.build_wall()
        city.build_wall()
        city.build_mine()
        city.info()
        barrack1 = city.buildings[0]
        wall1 = city.buildings[1]
        wall2 = city.buildings[2]
        mine1 = city.buildings[3]
        self.assertEqual(barrack1.__class__, barrack.DwarfBarrack)
        self.assertEqual(wall1.__class__, wall.DwarfWall)
        self.assertEqual(wall2.__class__, wall.DwarfWall)
        self.assertEqual(mine1.__class__, mine.DwarfMine)
        city.remove_building(wall1)
        self.assertRaisesRegex(KeyError, "No such building: {} in Durden".format(wall1),
                               lambda: city.remove_building(wall1))
        city.info()


class TestArmy(unittest.TestCase):
    def test_elf_army(self):
        empire = empire_mod.EmpireFactory().create_empire(races.elves)
        army = army_mod.ElfArmy(empire)
        self.assertEqual(army.master_empire, empire)
        self.assertEqual(army.what_race(), races.elves)
        scout1 = scout.ElfScout(10, 10)
        scout2 = scout.ElfScout(1, 1)
        warrior1 = warrior.ElfWarrior(10, 10, 5)
        builder1 = builder.ElfBuilder(3, 3)

        self.assertNotIn(scout1, army.units)

        army.recruit_unit(scout1)
        army.recruit_unit(scout2)
        army.recruit_unit(warrior1)
        army.recruit_unit(builder1)

        self.assertRaisesRegex(KeyError, "Unit: {} has already exists in the army ElfArmy".format(builder1),
                               lambda: army.recruit_unit(builder1))

        self.assertIn(scout1, army.units)
        self.assertIn(scout2, army.units)
        self.assertIn(warrior1, army.units)
        self.assertIn(builder1, army.units)

        army.info()

        army.remove_unit(scout1)
        self.assertRaisesRegex(KeyError, "No such unit: {} in the army ElfArmy".format(scout1),
                               lambda: army.remove_unit(scout1))
        army.remove_unit(scout2)

    def test_orc_army(self):
        empire = empire_mod.EmpireFactory().create_empire(races.orcs)
        army = army_mod.OrcArmy(empire)
        self.assertEqual(army.master_empire, empire)
        self.assertEqual(army.what_race(), races.orcs)
        scout1 = scout.OrcScout(10, 10)
        scout2 = scout.OrcScout(1, 1)
        warrior1 = warrior.OrcWarrior(10, 10, 5)
        builder1 = builder.OrcBuilder(3, 3)

        self.assertNotIn(scout1, army.units)

        army.recruit_unit(scout1)
        army.recruit_unit(scout2)
        army.recruit_unit(warrior1)
        army.recruit_unit(builder1)

        self.assertRaisesRegex(KeyError, "Unit: {} has already exists in the army OrcArmy".format(builder1),
                               lambda: army.recruit_unit(builder1))

        self.assertIn(scout1, army.units)
        self.assertIn(scout2, army.units)
        self.assertIn(warrior1, army.units)
        self.assertIn(builder1, army.units)

        army.info()

        army.remove_unit(scout1)
        self.assertRaisesRegex(KeyError, "No such unit: {} in the army OrcArmy".format(scout1),
                               lambda: army.remove_unit(scout1))
        army.remove_unit(scout2)

    def test_dwarf_army(self):
        empire = empire_mod.EmpireFactory().create_empire(races.dwarfs)
        army = army_mod.DwarfArmy(empire)
        self.assertEqual(army.master_empire, empire)
        self.assertEqual(army.what_race(), races.dwarfs)
        scout1 = scout.DwarfScout(10, 10)
        scout2 = scout.DwarfScout(1, 1)
        warrior1 = warrior.DwarfWarrior(10, 10, 5)
        builder1 = builder.DwarfBuilder(3, 3)

        self.assertNotIn(scout1, army.units)

        army.recruit_unit(scout1)
        army.recruit_unit(scout2)
        army.recruit_unit(warrior1)
        army.recruit_unit(builder1)

        self.assertRaisesRegex(KeyError, "Unit: {} has already exists in the army DwarfArmy".format(builder1),
                               lambda: army.recruit_unit(builder1))

        self.assertIn(scout1, army.units)
        self.assertIn(scout2, army.units)
        self.assertIn(warrior1, army.units)
        self.assertIn(builder1, army.units)

        army.info()

        army.remove_unit(scout1)
        self.assertRaisesRegex(KeyError, "No such unit: {} in the army DwarfArmy".format(scout1),
                               lambda: army.remove_unit(scout1))
        army.remove_unit(scout2)


class TestBarrack(unittest.TestCase):
    def test_elf_barrack(self):
        barrack_builder = barrack.BarrackBuilder()
        director = barrack.BarrackDirector()
        barrack1 = director.build_elf_barrack(barrack_builder, None)
        self.assertEqual(barrack1.__class__, barrack.ElfBarrack)
        self.assertEqual(barrack1.create_scout().__class__, scout.ElfScout)
        self.assertEqual(barrack1.create_builder().__class__, builder.ElfBuilder)
        self.assertEqual(barrack1.create_warrior().__class__, warrior.ElfWarrior)
        self.assertEqual(barrack1.health, 10)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: barrack1.decrease_health(20))

        barrack_builder = barrack.BarrackBuilder()
        director = barrack.BarrackDirector()
        barrack2 = director.build_elf_barrack(barrack_builder, None)
        barrack2.increase_health(10)
        self.assertEqual(barrack2.health, 20)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: barrack2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: barrack2.increase_health(-5))
        barrack2.decrease_health(15)
        self.assertTrue(barrack2.is_alive())

    def test_orc_barrack(self):
        barrack_builder = barrack.BarrackBuilder()
        director = barrack.BarrackDirector()
        barrack1 = director.build_orc_barrack(barrack_builder, None)
        self.assertEqual(barrack1.__class__, barrack.OrcBarrack)
        self.assertEqual(barrack1.create_scout().__class__, scout.OrcScout)
        self.assertEqual(barrack1.create_builder().__class__, builder.OrcBuilder)
        self.assertEqual(barrack1.create_warrior().__class__, warrior.OrcWarrior)
        self.assertEqual(barrack1.health, 10)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: barrack1.decrease_health(20))

        barrack_builder = barrack.BarrackBuilder()
        director = barrack.BarrackDirector()
        barrack2 = director.build_orc_barrack(barrack_builder, None)
        barrack2.increase_health(10)
        self.assertEqual(barrack2.health, 20)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: barrack2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: barrack2.increase_health(-5))
        barrack2.decrease_health(15)
        self.assertTrue(barrack2.is_alive())

    def test_dwarf_barrack(self):
        barrack_builder = barrack.BarrackBuilder()
        director = barrack.BarrackDirector()
        barrack1 = director.build_dwarf_barrack(barrack_builder, None)
        self.assertEqual(barrack1.__class__, barrack.DwarfBarrack)
        self.assertEqual(barrack1.create_scout().__class__, scout.DwarfScout)
        self.assertEqual(barrack1.create_builder().__class__, builder.DwarfBuilder)
        self.assertEqual(barrack1.create_warrior().__class__, warrior.DwarfWarrior)
        self.assertEqual(barrack1.health, 10)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: barrack1.decrease_health(20))

        barrack_builder = barrack.BarrackBuilder()
        director = barrack.BarrackDirector()
        barrack2 = director.build_dwarf_barrack(barrack_builder, None)
        barrack2.increase_health(10)
        self.assertEqual(barrack2.health, 20)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: barrack2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: barrack2.increase_health(-5))
        barrack2.decrease_health(15)
        self.assertTrue(barrack2.is_alive())


class TestWall(unittest.TestCase):
    def test_elf_wall(self):
        wall_builder = wall.WallBuilder()
        director = wall.WallDirector()
        wall1 = director.build_elf_wall(wall_builder, None)
        self.assertEqual(wall1.__class__, wall.ElfWall)
        self.assertEqual(wall1.health, 3)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: wall1.decrease_health(20))

        wall_builder = wall.WallBuilder()
        director = wall.WallDirector()
        wall2 = director.build_elf_wall(wall_builder, None)
        wall2.increase_health(10)
        self.assertEqual(wall2.health, 13)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: wall2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: wall2.increase_health(-5))
        wall2.decrease_health(12)
        self.assertTrue(wall2.is_alive())

    def test_orc_wall(self):
        wall_builder = wall.WallBuilder()
        director = wall.WallDirector()
        wall1 = director.build_orc_wall(wall_builder, None)
        self.assertEqual(wall1.__class__, wall.OrcWall)
        self.assertEqual(wall1.health, 3)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: wall1.decrease_health(20))

        wall_builder = wall.WallBuilder()
        director = wall.WallDirector()
        wall2 = director.build_orc_wall(wall_builder, None)
        wall2.increase_health(10)
        self.assertEqual(wall2.health, 13)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: wall2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: wall2.increase_health(-5))
        wall2.decrease_health(12)
        self.assertTrue(wall2.is_alive())

    def test_dwarf_wall(self):
        wall_builder = wall.WallBuilder()
        director = wall.WallDirector()
        wall1 = director.build_dwarf_wall(wall_builder, None)
        self.assertEqual(wall1.__class__, wall.DwarfWall)
        self.assertEqual(wall1.health, 3)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: wall1.decrease_health(20))

        wall_builder = wall.WallBuilder()
        director = wall.WallDirector()
        wall2 = director.build_dwarf_wall(wall_builder, None)
        wall2.increase_health(10)
        self.assertEqual(wall2.health, 13)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: wall2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: wall2.increase_health(-5))
        wall2.decrease_health(12)
        self.assertTrue(wall2.is_alive())


class TestMine(unittest.TestCase):
    def test_elf_wall(self):
        mine_builder = mine.MineBuilder()
        director = mine.MineDirector()
        mine1 = director.build_elf_mine(mine_builder, None)
        self.assertEqual(mine1.__class__, mine.ElfMine)
        self.assertEqual(mine1.health, 3)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: mine1.decrease_health(20))

        mine_builder = mine.MineBuilder()
        director = mine.MineDirector()
        mine2 = director.build_elf_mine(mine_builder, None)
        mine2.increase_health(10)
        self.assertEqual(mine2.health, 13)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: mine2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: mine2.increase_health(-5))
        mine2.decrease_health(12)
        self.assertTrue(mine2.is_alive())

    def test_orc_mine(self):
        mine_builder = mine.MineBuilder()
        director = mine.MineDirector()
        mine1 = director.build_orc_mine(mine_builder, None)
        self.assertEqual(mine1.__class__, mine.OrcMine)
        self.assertEqual(mine1.health, 3)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: mine1.decrease_health(20))

        mine_builder = mine.MineBuilder()
        director = mine.MineDirector()
        mine2 = director.build_orc_mine(mine_builder, None)
        mine2.increase_health(10)
        self.assertEqual(mine2.health, 13)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: mine2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: mine2.increase_health(-5))
        mine2.decrease_health(12)
        self.assertTrue(mine2.is_alive())

    def test_dwarf_mine(self):
        mine_builder = mine.MineBuilder()
        director = mine.MineDirector()
        mine1 = director.build_dwarf_mine(mine_builder, None)
        self.assertEqual(mine1.__class__, mine.DwarfMine)
        self.assertEqual(mine1.health, 3)
        # city = None --> AttributeError
        self.assertRaises(AttributeError, lambda: mine1.decrease_health(20))

        mine_builder = mine.MineBuilder()
        director = mine.MineDirector()
        mine2 = director.build_dwarf_mine(mine_builder, None)
        mine2.increase_health(10)
        self.assertEqual(mine2.health, 13)
        self.assertRaisesRegex(KeyError, "Can't decrease negative health: -5. Use increase_health for this",
                               lambda: mine2.decrease_health(-5))
        self.assertRaisesRegex(KeyError, "Can't increase negative health: -5. Use decrease_health for this",
                               lambda: mine2.increase_health(-5))
        mine2.decrease_health(12)
        self.assertTrue(mine2.is_alive())


class TestScout(unittest.TestCase):
    def test_elf_scout(self):
        scout1 = scout.ElfScout(10, 3)
        self.assertEqual(scout1.health, 10)
        self.assertEqual(scout1.speed, 3)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: scout.ElfScout(-3, 0))

        self.assertTrue(scout1.can_move())
        self.assertTrue(scout1.is_alive())
        self.assertEqual(scout1.what_race(), races.elves)

        scout1.decrease_health(4)
        self.assertEqual(scout1.health, 6)
        scout1.decrease_speed(10)
        self.assertEqual(scout1.speed, 0)
        scout1.increase_speed(10)
        self.assertEqual(scout1.speed, 10)

    def test_orc_scout(self):
        scout1 = scout.OrcScout(10, 3)
        self.assertEqual(scout1.health, 10)
        self.assertEqual(scout1.speed, 3)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: scout.OrcScout(-3, 0))

        self.assertTrue(scout1.can_move())
        self.assertTrue(scout1.is_alive())
        self.assertEqual(scout1.what_race(), races.orcs)

        scout1.decrease_health(4)
        self.assertEqual(scout1.health, 6)
        scout1.decrease_speed(10)
        self.assertEqual(scout1.speed, 0)
        scout1.increase_speed(10)
        self.assertEqual(scout1.speed, 10)

    def test_dwarf_scout(self):
        scout1 = scout.DwarfScout(10, 3)
        self.assertEqual(scout1.health, 10)
        self.assertEqual(scout1.speed, 3)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: scout.DwarfScout(-3, 0))

        self.assertTrue(scout1.can_move())
        self.assertTrue(scout1.is_alive())
        self.assertEqual(scout1.what_race(), races.dwarfs)

        scout1.decrease_health(4)
        self.assertEqual(scout1.health, 6)
        scout1.decrease_speed(10)
        self.assertEqual(scout1.speed, 0)
        scout1.increase_speed(10)
        self.assertEqual(scout1.speed, 10)


# TestBuilder is similar to TestScout
class TestBuilder(unittest.TestCase):
    def test_elf_builder(self):
        builder1 = builder.ElfBuilder(10, 3)
        self.assertEqual(builder1.health, 10)
        self.assertEqual(builder1.speed, 3)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: builder.ElfBuilder(-3, 0))

        self.assertTrue(builder1.can_move())
        self.assertTrue(builder1.is_alive())
        self.assertEqual(builder1.what_race(), races.elves)

        builder1.decrease_health(4)
        self.assertEqual(builder1.health, 6)
        builder1.decrease_speed(10)
        self.assertEqual(builder1.speed, 0)
        builder1.increase_speed(10)
        self.assertEqual(builder1.speed, 10)

    def test_orc_builder(self):
        builder1 = builder.OrcBuilder(10, 3)
        self.assertEqual(builder1.health, 10)
        self.assertEqual(builder1.speed, 3)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: builder.OrcBuilder(-3, 0))

        self.assertTrue(builder1.can_move())
        self.assertTrue(builder1.is_alive())
        self.assertEqual(builder1.what_race(), races.orcs)

        builder1.decrease_health(4)
        self.assertEqual(builder1.health, 6)
        builder1.decrease_speed(10)
        self.assertEqual(builder1.speed, 0)
        builder1.increase_speed(10)
        self.assertEqual(builder1.speed, 10)

    def test_dwarf_builder(self):
        builder1 = builder.DwarfBuilder(10, 3)
        self.assertEqual(builder1.health, 10)
        self.assertEqual(builder1.speed, 3)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: builder.DwarfBuilder(-3, 0))

        self.assertTrue(builder1.can_move())
        self.assertTrue(builder1.is_alive())
        self.assertEqual(builder1.what_race(), races.dwarfs)

        builder1.decrease_health(4)
        self.assertEqual(builder1.health, 6)
        builder1.decrease_speed(10)
        self.assertEqual(builder1.speed, 0)
        builder1.increase_speed(10)
        self.assertEqual(builder1.speed, 10)


class TestWarrior(unittest.TestCase):
    def test_elf_warrior(self):
        warrior1 = warrior.ElfWarrior(10, 3, 1)
        self.assertEqual(warrior1.health, 10)
        self.assertEqual(warrior1.speed, 3)
        self.assertEqual(warrior1.damage, 1)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: warrior.ElfWarrior(-3, 0, 0))

        self.assertTrue(warrior1.can_move())
        self.assertTrue(warrior1.is_alive())
        self.assertTrue(warrior1.can_hit())
        self.assertEqual(warrior1.what_race(), races.elves)

        warrior1.decrease_health(4)
        self.assertEqual(warrior1.health, 6)
        warrior1.decrease_speed(10)
        self.assertEqual(warrior1.speed, 0)
        warrior1.increase_speed(10)
        self.assertEqual(warrior1.speed, 10)
        warrior1.decrease_damage(5)
        self.assertEqual(warrior1.damage, 0)
        warrior1.increase_damage(1)
        self.assertEqual(warrior1.damage, 1)

        warrior2 = warrior.ElfWarrior(3, 0, 1)
        warrior1.hit(warrior2)
        self.assertEqual(warrior2.health, 2)
        warrior1.hit(warrior2)
        self.assertEqual(warrior2.health, 1)
        warrior1.hit(warrior2)
        self.assertFalse(warrior2.is_alive())

    def test_orc_warrior(self):
        warrior1 = warrior.OrcWarrior(10, 3, 1)
        self.assertEqual(warrior1.health, 10)
        self.assertEqual(warrior1.speed, 3)
        self.assertEqual(warrior1.damage, 1)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: warrior.OrcWarrior(-3, 0, 0))

        self.assertTrue(warrior1.can_move())
        self.assertTrue(warrior1.is_alive())
        self.assertTrue(warrior1.can_hit())
        self.assertEqual(warrior1.what_race(), races.orcs)

        warrior1.decrease_health(4)
        self.assertEqual(warrior1.health, 6)
        warrior1.decrease_speed(10)
        self.assertEqual(warrior1.speed, 0)
        warrior1.increase_speed(10)
        self.assertEqual(warrior1.speed, 10)
        warrior1.decrease_damage(5)
        self.assertEqual(warrior1.damage, 0)
        warrior1.increase_damage(1)
        self.assertEqual(warrior1.damage, 1)

        warrior2 = warrior.OrcWarrior(3, 0, 1)
        warrior1.hit(warrior2)
        self.assertEqual(warrior2.health, 2)
        warrior1.hit(warrior2)
        self.assertEqual(warrior2.health, 1)
        warrior1.hit(warrior2)
        self.assertFalse(warrior2.is_alive())

    def test_dwarf_warrior(self):
        warrior1 = warrior.DwarfWarrior(10, 3, 1)
        self.assertEqual(warrior1.health, 10)
        self.assertEqual(warrior1.speed, 3)
        self.assertEqual(warrior1.damage, 1)
        self.assertRaisesRegex(Exception, "Can't create object with negative or zero health: -3",
                               lambda: warrior.DwarfWarrior(-3, 0, 0))

        self.assertTrue(warrior1.can_move())
        self.assertTrue(warrior1.is_alive())
        self.assertTrue(warrior1.can_hit())
        self.assertEqual(warrior1.what_race(), races.dwarfs)

        warrior1.decrease_health(4)
        self.assertEqual(warrior1.health, 6)
        warrior1.decrease_speed(10)
        self.assertEqual(warrior1.speed, 0)
        warrior1.increase_speed(10)
        self.assertEqual(warrior1.speed, 10)
        warrior1.decrease_damage(5)
        self.assertEqual(warrior1.damage, 0)
        warrior1.increase_damage(1)
        self.assertEqual(warrior1.damage, 1)

        warrior2 = warrior.DwarfWarrior(3, 0, 1)
        warrior1.hit(warrior2)
        self.assertEqual(warrior2.health, 2)
        warrior1.hit(warrior2)
        self.assertEqual(warrior2.health, 1)
        warrior1.hit(warrior2)
        self.assertFalse(warrior2.is_alive())