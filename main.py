import empire
import races


def play_game():
    player1 = empire.Empire(races.Dwarf)
    player1.establish_city('Turden')

    Turden = player1.get_city('Turden')
    Turden.build_barrack(10)
    Turden.build_mine(3)
    Turden.build_wall(1)
    Turden.build_mine(3)
    Turden.info()


if __name__ == '__main__':
    play_game()
