from abc import ABC, abstractmethod


# CoR Base Handler
class BaseHandler(ABC):
    _next: 'BaseHandler' = None

    def set_next(self, handler) -> 'BaseHandler':
        self._next = handler
        return handler

    def handle(self, args) -> bool:
        handled = self._handle(args)
        if self._next is not None:
            return self._next.handle(args[1:])
        return handled

    @abstractmethod
    def _handle(self, args) -> bool:
        pass
