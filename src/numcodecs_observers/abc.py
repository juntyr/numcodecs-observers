"""
This module defines the [`CodecObserver`][numcodecs_observers.abc.CodecObserver] base class, which allows observing encoding and decoding in a [`Codec`][numcodecs.abc.Codec].
"""

__all__ = ["CodecObserver"]

from collections.abc import Buffer
from typing import Optional, Callable

from numcodecs.abc import Codec


class CodecObserver:
    """
    Observer base class, which allows observing encoding and decoding in a
    [`Codec`][numcodecs.abc.Codec].
    """

    def encode(self, codec: Codec, buf: Buffer) -> Callable[[Buffer], None]:
        """ """

        return lambda encoded: None

    def decode(
        self, codec: Codec, buf: Buffer, out: Optional[Buffer] = None
    ) -> Callable[[Buffer], None]:
        """ """

        return lambda decoded: None
