"""
This module defines the [`HashableCodec`][numcodecs_observers.hash.HashableCodec] helper class, which wraps an existing [`Codec`][numcodecs.abc.Codec] and makes it [`hash`][hash]able.
"""

__all__ = ["HashableCodec"]

from typing import Any, Callable, Optional

from numcodecs.abc import Codec
from numcodecs_combinators.abc import CodecCombinatorMixin
from typing_extensions import Buffer  # MSPV 3.12


class HashableCodec(Codec, CodecCombinatorMixin):
    """
    Helper class to wrap an existing [`Codec`][numcodecs.abc.Codec] and make
    it [`hash`][hash]able.

    This class overrides the [`__hash__`][object.__hash__] and
    [`__eq__`][object.__eq__] methods to use the codec instance's [`id`][id].
    """

    __slots__: tuple[str, ...] = ("codec",)
    codec: Codec
    """ The wrapped codec. """

    def __init__(self, codec: Codec):
        self.codec = codec

    @property
    def codec_id(self) -> None | str:  # type: ignore
        return self.codec.codec_id

    def encode(self, buf: Buffer) -> Buffer:
        return self.codec.encode(buf)

    def decode(self, buf: Buffer, out: Optional[Buffer] = None) -> Buffer:
        return self.codec.decode(buf, out=out)

    def get_config(self) -> dict:
        return self.codec.get_config()

    @classmethod
    def from_config(cls, config):
        raise NotImplementedError()

    def map(self, mapper: Callable[[Codec], Codec]) -> Codec:
        # Explicitly don't wrap the mapped inner codec with HashableCodec, as
        #  HashableCodec should only be applied manually at the top-level
        return mapper(self.codec)

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
