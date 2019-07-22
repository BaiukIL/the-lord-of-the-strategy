###### Patterns
**Creational Patterns**
------------------------------------------------------------------------------------------------------------------------
**Abstract Factory**.

Implementations: game_object/buildings/fabric.py

Think: The idea is that empires are almost similar due to game balance. Thus we have kind of "common empire" which
contains basic game interface (see attached .png file "Empire hierarchy") and all specific races merely differ in
rendering and in few unique methods. The concept of fabrics
(and sound reason) obliges us to keep every race's line separately. Indeed, since player created orc empire
all his objects must behave as orc ones. Thus, every object has to remember what race it is. It can be done in 2 ways:

1. every class has "race" field. It means we have only one base class for every object essence (like empire, city,
 army, etc.). This way, to add unique behavior for elves wall, for instance, we have to make a lot of "if-race" in this method.

2. every class inherits "race" class, so race is set at its name. It means we have many derived classes for every
object essence (like elves_empire, orcs_empire, dwarfs_empire, elf_city...). However, to add unique behavior for elves wall,
for instance, we just have to add a new method in elves_wall class.

In first case is difficult to extend. The other case seems to be copy-and-paste problem, like:

    class ElfEmpire(Empire, races.Elves):
        def __init__(self):
            super().__init__()
            self.army = army.ElfArmy(self)

        def establish_city(self, name):
            if name not in self.cities:
                self.cities[name] = city.ElfCity(name, self)
            else:
                raise KeyError("City {} has already exists in {} cities".format(name, self.__class__.__name__))


    class OrcEmpire(Empire, races.Orcs):
        def __init__(self):
            super().__init__()
            self.army = army.OrcArmy(self)

        def establish_city(self, name):
            if name not in self.cities:
                self.cities[name] = city.OrcCity(name, self)
            else:
                raise KeyError("City {} has already exists in {} cities".format(name, self.__class__.__name__))


    class DwarfEmpire(Empire, races.Dwarfs):
        def __init__(self):
            super().__init__()
            self.army = army.DwarfArmy(self)

        def establish_city(self, name):
            if name not in self.cities:
                self.cities[name] = city.DwarfCity(name, self)
            else:
                raise KeyError("City {} has already exists in {} cities".format(name, self.__class__.__name__))

so our program will bush out very quickly.

However, there's no other choice to structure empire lines in accordance with races (bridge pattern
resolves into the first problem of storing object as a field; decorator pattern resolves into
the second case).

Solution: I've decided to choose the first one because
it makes code more explicit and it is unnecessary to duplicate code in case of addition a new race into the game.
In this case we have single empire and city classes and have to choose explicit race just on the stage of buildings creation.
Thus, we can make an ABSTRACT FACTORY of buildings - Manufacture.
It allows us not to worry about compatibility of empire's objects. Also we can interact
with empires, cities, armies without binding to its implementations (because they have abstract base classes)*.

* There is dynamic typification in python, so we can interact with objects throughout its base class methods without using
factory which returns base class object. However, it does not mean factory is useless: it allows us to
control object's creation.
------------------------------------------------------------------------------------------------------------------------
**Singleton**.

Implementations: Game(), Interface(), AI(), Map() (see game.py, interface/interface.py, AI.py and map.py
respectively).

These classes should have just a single instance available to all game instances.




------------------------------------------------------------------------------------------------------------------------
**Structural Patterns**
------------------------------------------------------------------------------------------------------------------------
**REFUSE Bridge**.

It comes into use when we want to separate abstraction and realization. All connections are on the abstraction level
and it would be great if realizations will be able to change in the future
(for example, if I want to rewrite game onto another framework).
However, it is bad idea to make "realization" field for every entity, for in this case it cannot be used in pygame
object structures (like pygame.sprite.Group), which are very useful. It is impossible because
these structures can only deal with objects derived from pygame.sprite.Sprite. Since my abstractions are not derived from
this class they cannot be used in such structures. Thus bridge pattern as composition of entities is not suitable.

------------------------------------------------------------------------------------------------------------------------
**Composite & Iterator & Visitor**

Implementations: game_objects/army.py

Units have next hierarchy: they can be united in troops, then these troops can be united in bigger troops and so on.
This way we have a tree-like units structure which is great place for composite.
Notice that composite just stores object and sets the hierarchy. To iterate over units we use iterator.
However, it's good idea to add visitor, for iterator should not know about nodes realizations. This
construction allows us to separate logic to classes.

------------------------------------------------------------------------------------------------------------------------
**Facade**.

Implementations: interface/interface.py

Interface is a Facade transformed to singleton which coordinates interface windows work.
It has just a few methods which hide a complex structure relations of different windows
(these: Commands, Selected, Minimap, EmpireInfo, Message).




------------------------------------------------------------------------------------------------------------------------
**Behavioral Patterns**
------------------------------------------------------------------------------------------------------------------------
**REFUSE CoR**.

Situation: we need to handle mouse button press. So we need to figure out what surface can handle this query.
Seems like CoR?
Think: OK, let Selected() be the first handler, Minimap() second, next ... what next? Next we see game objects, placed
on Map(), and commands. If we want to continue our handling-chain we need to align commands and game objects.
However, a great part of objects don't know about other objects and commands don't know anything about each other.
Hereby, by including them in the chain we increase program cohesion, which is bad.
Moreover, if we want to build CoR in this situation, we always need to track if window falls out of the chain and
replace one if it is. Considering that there's a load of disappearing objects, it becomes a tough task.

------------------------------------------------------------------------------------------------------------------------
**Command**.

Implementations: interface/button.py
    
This one uses to store actions (functions) in buttons. Some actions need args and can't be called immediately.
Buttons remember what actions they should react (handle_*_click) and takes the appropriate args of the context.

------------------------------------------------------------------------------------------------------------------------
**State**.

Implementations: interface/window.py

Window can have a few states: `hidden` (don't show on screen; don't react any clicks), `passive` (draws without
borders; ready to react a click and turn to active state) and `active` (draws with borders; if clicked turn to
passive state). It's comfortable to create class for every state and delegate any work connected with state to it.

------------------------------------------------------------------------------------------------------------------------
**REFUSE Observer**.

This pattern already exists in pygame as a `kill` command. When we kill object, all the groups it's consist in
remove the object.

------------------------------------------------------------------------------------------------------------------------
