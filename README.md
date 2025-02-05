[![image](https://img.shields.io/github/actions/workflow/status/juntyr/numcodecs-observers/ci.yml?branch=main)](https://github.com/juntyr/numcodecs-observers/actions/workflows/ci.yml?query=branch%3Amain)
[![image](https://img.shields.io/pypi/v/numcodecs-observers.svg)](https://pypi.python.org/pypi/numcodecs-observers)
[![image](https://img.shields.io/pypi/l/numcodecs-observers.svg)](https://github.com/juntyr/numcodecs-observers/blob/main/LICENSE)
[![image](https://img.shields.io/pypi/pyversions/numcodecs-observers.svg)](https://pypi.python.org/pypi/numcodecs-observers)
[![image](https://readthedocs.org/projects/numcodecs-observers/badge/?version=latest)](https://numcodecs-observers.readthedocs.io/en/latest/?badge=latest)

# numcodecs-observers

Observe encoding and decoding in the [`numcodecs`] buffer compression API.

The following observers, implementing the `CodecObserver` class are provided:

- `ByesizeObserver`: measure the byte size of the data before and after encoding / decoding
- `WalltimeObserver`: measure the walltime taken to encode / decode

[`numcodecs`]: https://numcodecs.readthedocs.io/en/stable/

## License

Licensed under the Mozilla Public License, Version 2.0 ([LICENSE](LICENSE) or https://www.mozilla.org/en-US/MPL/2.0/).


## Funding

The `numcodecs-observers` package has been developed as part of [ESiWACE3](https://www.esiwace.eu), the third phase of the Centre of Excellence in Simulation of Weather and Climate in Europe.

Funded by the European Union. This work has received funding from the European High Performance Computing Joint Undertaking (JU) under grant agreement No 101093054.
