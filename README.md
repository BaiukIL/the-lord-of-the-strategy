# The Lord of the Strategy
Computer strategy game written in Python 3.6.

Currently it is ready to play.
To start play just clone the project and run: `:~/path-to-project$ python play_game.py`


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

    The only 
        empire can win: 
            the most powerful one.
            
    Build cities,
      muster army,
        mine gold, 
          but remember: 
            enemy is upcoming...
See how-to-play and other game info at docs.
