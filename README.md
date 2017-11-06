# IBM Bluegroup Python SDK

## Installation

To install, use `pip`:

```bash
pip install --upgrade ibmBluegroup
```

## Usage

```python
from ibmBluegroup import ibmBluegroup

ibmBluegroup = ibmBluegroup()
flag = ibmBluegroup.userInGroup("intrenetID", "group name")
print(flag)
```

Tip: please use '%20' replace all blanks of group name.

## Python Version

Tested on: Python from 3.5.

## License

This library is licensed under the [Apache 2.0 license][license].



[license]: http://www.apache.org/licenses/LICENSE-2.0
