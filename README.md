# numcodecs-combinators

A stack of codecs, which makes up a combined codec.

On encoding, the codecs are applied to encode from left to right, i.e.
```python
CodecStack(a, b, c).encode(buf)
```
computes
```python
c.encode(b.encode(a.encode(buf)))
```

On decoding, the codecs are applied to decode from right to left, i.e.
```python
CodecStack(a, b, c).decode(buf)
```
computes
```python
a.decode(b.decode(c.decode(buf)))
```

The `CodecStack` provides the additional `encode_decode(buf)` method that
computes
```python
stack.decode(stack.encode(buf))
```
but makes use of knowing the shapes and dtypes of all intermediary encoding
stages.
