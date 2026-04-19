import numcodecs
import numcodecs_combinators
import numpy as np

import numcodecs_observers


def test_perf():
    nbytes = numcodecs_observers.bytesize.BytesizeObserver()
    timing = numcodecs_observers.walltime.WalltimeObserver()

    stack = numcodecs_combinators.stack.CodecStack(
        numcodecs.BitRound(keepbits=6), numcodecs.Zlib(level=7)
    )

    data = np.random.normal(size=(100, 100))

    with numcodecs_observers.observe(stack, [nbytes, timing]) as stack_:
        stack_.encode_decode(data)

    print(nbytes.encode_sizes)
    print(nbytes.decode_sizes)
    print(timing.encode_times)
    print(timing.decode_times)


def test_observing_wrap():
    codec = numcodecs.Zlib(level=7)

    with numcodecs_observers.observe(codec, []) as codec_:
        assert codec_.codec_id == codec.codec_id
        assert str(codec_.get_config()) == str(codec.get_config())


def test_hashable_wrap():
    codec = numcodecs.Zlib(level=7)
    codec_ = numcodecs_observers.hash.HashableCodec(codec)

    assert codec_.codec_id == codec.codec_id
    assert str(codec_.get_config()) == str(codec.get_config())
