import time
from collections import defaultdict
from collections.abc import Buffer
from typing import Callable, Optional

from numcodecs.abc import Codec

from .abc import CodecObserver


class WalltimeObserver(CodecObserver):
    codecs: dict[int, Codec]
    encode_times: defaultdict[int, list[float]]
    decode_times: defaultdict[int, list[float]]

    def __init__(self):
        self.codecs = dict()
        self.encode_times = defaultdict(list)
        self.decode_times = defaultdict(list)

    def encode(self, codec: Codec, buf: Buffer) -> Callable[[Buffer], None]:
        encode_start = time.perf_counter()

        def post_encode(encoded: Buffer) -> None:
            self.encode_times[id(codec)].append(time.perf_counter() - encode_start)
            self.codecs[id(codec)] = codec

        return post_encode

    def decode(
        self, codec: Codec, buf: Buffer, out: Optional[Buffer] = None
    ) -> Callable[[Buffer], None]:
        decode_start = time.perf_counter()

        def post_decode(decoded: Buffer) -> None:
            self.decode_times[id(codec)].append(time.perf_counter() - decode_start)
            self.codecs[id(codec)] = codec

        return post_decode

    def results(self) -> dict:
        return dict(
            encode_times={
                repr(self.codecs[c]): ts for c, ts in self.encode_times.items()
            },
            decode_times={
                repr(self.codecs[c]): ts for c, ts in self.decode_times.items()
            },
        )
