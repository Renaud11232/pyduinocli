# pyduinocli [![Build Status](https://travis-ci.org/Renaud11232/pyduinocli.svg?branch=master)](https://travis-ci.org/Renaud11232/pyduinocli)

pyduinocli is a wrapper library around arduino-cli to make the arduino-cli calls easy from a python script.

## pyduinocli goals

* Provide a clear and easy way to use arduino through a python program
* Give the ability to programmatically flash arduino-like boards
* Update 3D printer firmwares automatically

## How to use

### Installation

To install the library simply do
```bash
pip install pyduinocli
```

### How to use

To start using the library simply import the module, create a new Arduino instance and enjoy.

```python
import pyduinocli

arduino = pyduinocli.Arduino("./arduino-cli")
print(arduino.version())
```

## License

See [LICENSE](LICENSE)
