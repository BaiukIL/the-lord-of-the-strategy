from typing import *


class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


# It is not abstract because otherwise inheritance problems occur
# (for instance, when one inherits from this and Singleton):
#   TypeError: metaclass conflict: the metaclass of a derived class must be
#   a (non-strict) subclass of the metaclasses of all its bases.
class Handler:
    """Base handler in CoR"""
    _next_handler: 'Handler' = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler

    def handle_click(self, mouse_pos: Tuple[int, int]) -> bool:
        if self.can_handle(mouse_pos):
            self.handle(mouse_pos)
            return True
        else:
            self.not_handle()
            if self._next_handler is not None:
                return self._next_handler.handle_click(mouse_pos)
            else:
                return False

    def can_handle(self, mouse_pos: Tuple[int, int]) -> bool:
        pass

    def handle(self, mouse_pos: Tuple[int, int]):
        pass

    def not_handle(self):
        """Empty method which can be overridden. It calls when object
        couldn't handle click"""
        pass


class Publisher:

    subscribers: Dict[str, List['Subscriber']]

    def subscribe(self, event, subscriber: 'Subscriber'):
        self.subscribers[event].append(subscriber)

    def unsubscribe(self, event, subscriber: 'Subscriber'):
        self.subscribers[event].remove(subscriber)

    def notify(self, event, *args):
        for subscriber in self.subscribers[event]:
            subscriber.receive_notification(*args)


class Subscriber:
    def receive_notification(self, *args):
        pass
