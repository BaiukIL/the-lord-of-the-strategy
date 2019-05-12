

class CreationError(Exception):
    pass


class CreationPlaceError(CreationError):
    pass


class CreationTimeError(CreationError):
    pass


class CreationResourcesLimitError(CreationError):
    pass
