from collections import defaultdict
from collections.abc import Buffer
from dataclasses import dataclass
from typing import Callable, Optional

import numpy as np
from numcodecs.abc import Codec

from .abc import CodecObserver


@dataclass
class Bytesize:
    pre: int
    post: int


class ByesizeObserver(CodecObserver):
    codecs: dict[int, Codec]
    encode_sizes: defaultdict[int, list[Bytesize]]
    decode_sizes: defaultdict[int, list[Bytesize]]

    def __init__(self):
        self.codecs = dict()
        self.encode_sizes = defaultdict(list)
        self.decode_sizes = defaultdict(list)

    def encode(self, codec: Codec, buf_: Buffer) -> Callable[[Buffer], None]:
        def post_encode(encoded: Buffer) -> None:
            buf, encoded = np.asarray(buf_), np.asarray(encoded)

            self.encode_sizes[id(codec)].append(
                Bytesize(pre=buf.nbytes, post=encoded.nbytes)
            )
            self.codecs[id(codec)] = codec

        return post_encode

    def decode(
        self, codec: Codec, buf_: Buffer, out: Optional[Buffer] = None
    ) -> Callable[[Buffer], None]:
        def post_decode(decoded: Buffer) -> None:
            buf, decoded = np.asarray(buf_), np.asarray(decoded)

            self.decode_sizes[id(codec)].append(
                Bytesize(pre=buf.nbytes, post=decoded.nbytes)
            )
            self.codecs[id(codec)] = codec

        return post_decode

    def results(self) -> dict:
        return dict(
            encode_sizes={
                repr(self.codecs[c]): ts for c, ts in self.encode_sizes.items()
            },
            decode_sizes={
                repr(self.codecs[c]): ts for c, ts in self.decode_sizes.items()
            },
        )
