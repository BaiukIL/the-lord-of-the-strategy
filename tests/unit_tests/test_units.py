import unittest
import image
from interface.interface import Interface
from game import Game
from game_objects import races, empire
from game_objects.units import warrior


class TestWarrior(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.DWARFS)
        self.other_empire = empire.Empire(races.ELVES)
        Interface(self.empire, self.other_empire)
        Game(self.empire, self.other_empire)
        self.warrior = warrior.OrcWarrior(empire=self.empire,
                                          cost=10,
                                          health=11,
                                          speed=10,
                                          damage=20,
                                          fight_distance=300,
                                          size=(100, 100),
                                          image=image.get_image(self.empire).WARRIOR)

    def test_default(self):
        self.assertEqual(self.warrior.empire, self.empire)
        self.assertEqual(self.warrior.cost, 10)
        self.assertEqual(self.warrior.health, 11)
        self.assertEqual(self.warrior.max_speed, 10)
        self.assertEqual(self.warrior.damage, 20)
        self.assertEqual(self.warrior.fight_distance, 300)
        self.assertEqual(self.warrior.rect.size, (100, 100))
        self.assertEqual(self.warrior.destination, self.warrior.rect.center)

    def test_move(self):
        self.assertEqual(self.warrior.rect.center, (50, 50))
        self.warrior.set_move_to((1000, 1000))
        self.assertEqual(self.warrior.destination, (1000, 1000))
        self.warrior.set_move_to((100, 50))
        self.assertEqual(self.warrior.destination, (100, 50))
        self.assertEqual(list(self.warrior.speed), [10, 0])
        self.warrior.move()
        self.assertEqual(self.warrior.destination, (100, 50))
        self.assertEqual(self.warrior.rect.center, (60, 50))
        self.warrior.set_move_to((60, 100))
        self.warrior.move()
        self.assertEqual(self.warrior.rect.center, (60, 60))
        self.warrior.stop_move()
        self.assertEqual(self.warrior.destination, (60, 60))

    def test_attack(self):
        other_unit = warrior.ElfWarrior(empire=self.empire,
                                        cost=1,
                                        health=1,
                                        speed=1,
                                        damage=2,
                                        fight_distance=300,
                                        size=(100, 100),
                                        image=image.get_image(self.empire).WARRIOR)
        other_unit.rect.center = (1000, 50)
        self.warrior.attack_target.add(other_unit)
        self.warrior.update()
        self.assertEqual(self.warrior.rect.center, (60, 50))

    def tearDown(self) -> None:
        # if we don't kill created objects, they will left if Game().objects
        # (it happens because Game() is singleton) and some create problems will occur
        for obj in Game().objects:
            obj.kill()


# Scout does not differ from Warrior so far so see Warrior tests
class TestScout(unittest.TestCase):
    pass


# Builder does not differ from unit so far which is extended by warrior
#  (i.e. warrior tests covers unit.Unit tests), so see warrior tests
class TestBuilder(unittest.TestCase):
    pass
