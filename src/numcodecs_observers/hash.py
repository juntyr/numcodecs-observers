from collections.abc import Buffer
from typing import Any, Optional

from numcodecs.abc import Codec


class HashableCodec(Codec):
    codec: Codec

    def __init__(self, codec: Codec):
        self.codec = codec

    def encode(self, buf: Buffer) -> Buffer:
        return self.codec.encode(buf)

    def decode(self, buf: Buffer, out: Optional[Buffer] = None) -> Buffer:
        return self.codec.decode(buf, out=out)

    def __hash__(self) -> int:
        return id(self.codec)

    def __eq__(self, other) -> bool:
        if isinstance(other, HashableCodec):
            return id(self.codec) == id(other.codec)

        if isinstance(other, Codec):
            return id(self.codec) == id(other)

        return False

    def __repr__(self) -> str:
        return repr(self.codec)

    def __getattr__(self, name: str) -> Any:
        return getattr(self.codec, name)
