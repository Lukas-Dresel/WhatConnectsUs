from construct import *


class NormalizedVectorAdapter(Adapter):
    def _decode(self, obj, context, path):
        return obj.x / 65535.0, obj.y / 65535.0

    def _encode(self, obj, context, path):
        return {'x': int(obj * 65535), 'y': int(obj * 65535) }


NormalizedVector = NormalizedVectorAdapter(Struct(
    "x" / Int16ul,
    "y" / Int16ul,
))