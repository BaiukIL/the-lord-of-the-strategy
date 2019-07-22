Game concept
------------------------------------------------------------------------------------------------------------------------

The game is based on races. At first player chooses a race from list:
- Elves
- Orcs
- Dwarfs

and creates empire of this race. (See user_configs.py to change settings)

Every empire differs from others. Thus, Elves units have double speed,
Orcs ones have double damage and Dwarfs objects have double health.

The essential concept of the game is resources. It's like game money which
you can use to build units and buildings. The start resources is 100.

To win, player must destroy enemy city. If player's city is ruined, he's lost.

Interface
------------------------------------------------------------------------------------------------------------------------

Interface is pretty common for strategies, so it's easy to start play.

When game starts you see the default city. You can select if by one click and
unselect by next one. Every selected object has short info placed in the left bottom corner.
While object is selected, there're available commands this object can be
interacted with (If this object belongs to your empire. Otherwise you can only see its info).
Every entity has `upgrade` (red arrow) and `destroy` (black hammer) commands (Currently `upgrade` do nothing).
When you press `destroy` command, destructed object gets you (object_cost / 2) resources of its price back.

To move camera, use WSDA or mouse (in this case just put cursor at the appropriate screen border).
To exit, press ESC.

Note that when unit attacks another object, last one is marked red for a while. Also you should not concern
about unit attack after you've chosen a target, for it follows one on its own. However, when target is dead
or when target is not chosen unit does nothing.

Objects info
------------------------------------------------------------------------------------------------------------------------
Objects pictures are not created, yet are supposed to be added soon.
Now you see white rectangles with appropriate object name instead.
There's a list of game object and their descriptions:
(Notice that listed objects have default characteristics without race bonuses.
For example, while barrack has 20 health points, dwarfs barrack has 40).

**City**.

Description: this is the head object of empire, if it's ruined, game finishes. Any empire city has 30 health points
It's responsible for buildings creation.
- Price: 200
- Health: 30
- Commands:
    - build barrack
    - build mine
    - build wall
- Special skills: None

------------------------------------------------------------------------------------------------------------------------
**Buildings**.

**Barrack**.

Description: Building which is responsible for units creation.
- Price: 20
- Health: 15
- Commands:
    - create builder
    - create warrior
    - create scout
- Special skills: None

**Mine**.

Description: Building which reproduces resources.
- Price: 10
- Health: 10
- Commands: None
- Special skills: Gives 5 extra resources per minute to its empire

**Wall**.

Description: Empty building which can be used to hinder enemy units.
- Price: 5
- Health: 10
- Commands: None
- Special skills: None

------------------------------------------------------------------------------------------------------------------------
**Units**.

**Builder**.

Description: 'Empty' unit which can just move so far.
- Price: 5
- Health: 2
- Speed: 6
- Special skills: None

**Scout**.

Description: Light unit which has low damage but high speed and
can attack from far distance.
- Price: 8
- Health: 3
- Speed: 6
- Damage: 1 (attack delay: 3 sec)
- Special skills: None

**Warrior**.

Description: Heavy unit which has big damage and health but low speed.
- Price: 10
- Health: 5
- Speed: 3
- Damage: 2 (attack delay: 3 sec)
- Special skills: None
