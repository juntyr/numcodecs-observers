from collections import defaultdict
from collections.abc import Buffer, Mapping
from dataclasses import dataclass
from typing import Callable, Optional
from types import MappingProxyType

import numpy as np
from numcodecs.abc import Codec

from .abc import CodecObserver
from .hash import HashableCodec


@dataclass
class Bytesize:
    pre: int
    post: int


class ByesizeObserver(CodecObserver):
    _encode_sizes: defaultdict[HashableCodec, list[Bytesize]]
    _decode_sizes: defaultdict[HashableCodec, list[Bytesize]]

    def __init__(self):
        self._encode_sizes = defaultdict(list)
        self._decode_sizes = defaultdict(list)

    @property
    def encode_sizes(self) -> Mapping[HashableCodec, list[Bytesize]]:
        return MappingProxyType(self._encode_sizes)

    @property
    def decode_sizes(self) -> Mapping[HashableCodec, list[Bytesize]]:
        return MappingProxyType(self._decode_sizes)

    def encode(self, codec: Codec, buf_: Buffer) -> Callable[[Buffer], None]:
        def post_encode(encoded: Buffer) -> None:
            buf, encoded = np.asarray(buf_), np.asarray(encoded)

            self._encode_sizes[HashableCodec(codec)].append(
                Bytesize(pre=buf.nbytes, post=encoded.nbytes)
            )

        return post_encode

    def decode(
        self, codec: Codec, buf_: Buffer, out: Optional[Buffer] = None
    ) -> Callable[[Buffer], None]:
        def post_decode(decoded: Buffer) -> None:
            buf, decoded = np.asarray(buf_), np.asarray(decoded)

            self._decode_sizes[HashableCodec(codec)].append(
                Bytesize(pre=buf.nbytes, post=decoded.nbytes)
            )

        return post_decode
