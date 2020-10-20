from construct import *


class UnknownEnumError(ConstructError):
    pass


class FixedEnum(Enum):
    """
    Used just like a normal Enum, but fails parsing when an unknown value is found.
    """

    def __getattr__(self, name):
        if name in self.encmapping:
            return self.decmapping[self.encmapping[name]]
        raise AttributeError

    def _decode(self, obj, context, path):
        try:
            return self.decmapping[obj]
        except KeyError:
            raise UnknownEnumError("Incorrect enum value encountered: {} is not in {}".format(obj, self.decmapping))

    def _encode(self, obj, context, path):
        try:
            if isinstance(obj, integertypes):
                if obj not in self.decmapping:
                    raise UnknownEnumError("Incorrect enum value encountered: {} is not in {}".format(
                        obj, self.decmapping), path=path)

                return obj
            return self.encmapping[obj]
        except KeyError:
            raise MappingError("building failed, no mapping for %r" % (obj,), path=path)