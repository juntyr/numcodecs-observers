import numcodecs_combinators
import numcodecs_observers
import numcodecs
import numpy as np


def test_perf():
    observers = [
        numcodecs_observers.bytesize.ByesizeObserver(),
        numcodecs_observers.walltime.WalltimeObserver(),
    ]
    stack = numcodecs_combinators.stack.CodecStack(
        numcodecs.BitRound(keepbits=6), numcodecs.Zlib(level=7)
    )

    data = np.random.normal(size=(100, 100))

    with numcodecs_observers.observe(stack, observers) as stack_:
        stack_.encode_decode(data)

    print([o.results() for o in observers])
