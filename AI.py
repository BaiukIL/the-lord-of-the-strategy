import templates
import exceptions


class AI(metaclass=templates.Singleton):
    def __init__(self, empire):
        self.empire = empire

    def strategy(self):
        pass

    def play_step(self):
        for city in self.empire.cities:
            place = city.rect.copy()
            can_create = False
            while not can_create:
                try:
                    city.build_barrack(place.topleft)
                    can_create = True
                except exceptions.CreationPlaceError:
                    place.move_ip(-city.rect.width, 0)
                except exceptions.CreationTimeError:
                    return
                except exceptions.CreationResourcesLimitError:
                    return
