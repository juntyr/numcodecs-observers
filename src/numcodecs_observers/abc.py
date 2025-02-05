__all__ = ["CodecObserver"]

from collections.abc import Buffer
from typing import Optional, Callable

from numcodecs.abc import Codec


class CodecObserver:
    def encode(self, codec: Codec, buf: Buffer) -> Callable[[Buffer], None]:
        return lambda encoded: None

    def decode(
        self, codec: Codec, buf: Buffer, out: Optional[Buffer] = None
    ) -> Callable[[Buffer], None]:
        return lambda decoded: None
