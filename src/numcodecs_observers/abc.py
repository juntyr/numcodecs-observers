__all__ = ["CodecObserver"]

from abc import ABC, abstractmethod
from collections.abc import Buffer
from typing import Optional

from numcodecs.abc import Codec


class CodecObserver(ABC):
    def pre_encode(self, codec: Codec, buf: Buffer) -> None:
        pass

    def post_encode(self, codec: Codec, buf: Buffer, encoded: Buffer) -> None:
        pass

    def pre_decode(
        self, codec: Codec, buf: Buffer, out: Optional[Buffer] = None
    ) -> None:
        pass

    def post_decode(self, codec: Codec, buf: Buffer, decoded: Buffer) -> None:
        pass

    @abstractmethod
    def results(self) -> dict:
        pass
