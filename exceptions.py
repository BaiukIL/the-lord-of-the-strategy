""" This module contains exceptions connected with objects creation. """


class CreationError(Exception):
    """ Base exception. """


class CreationPlaceError(CreationError):
    """ Is raised when object is about to be created in inappropriate place. """


class CreationTimeError(CreationError):
    """ Is raised when object is about to be created before creation time limit expires. """


class CreationResourcesLimitError(CreationError):
    """ Is raised when object is about to be created in the absence of resources. """
