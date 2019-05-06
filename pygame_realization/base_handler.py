from abc import ABC, abstractmethod


# CoR Base Handler
class BaseHandler:
    _next_handler: 'BaseHandler' = None

    def set_next(self, handler) -> 'BaseHandler':
        self._next_handler = handler
        return handler

    def handle_click(self, *args):
        if self.can_handle(*args):
            self.handle()
        else:
            if self._next_handler is not None:
                self._next_handler.handle_click(*args)

    def can_handle(self, *args) -> bool:
        pass

    def handle(self, *args):
        pass
