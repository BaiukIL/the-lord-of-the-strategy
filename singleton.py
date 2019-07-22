""" This module contains `Singleton` - Python realization of singleton. """


class Singleton(type):
    """ Python realization of singleton.
    Class inherits from this becomes singleton (i.e. no more than one instance of it class
    can exist).
    Usage example:

        class A(metaclass=singleton.Singleton):
            def __init__(self, number):
                pass

    Now after creating `A` instance:
        a = A(10)
    Every time we call `A()` we will access to `a` variable.
    It works correct even though python linter shows warning like:

     - No value for argument 'number' in constructor call of A class.
    """

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
