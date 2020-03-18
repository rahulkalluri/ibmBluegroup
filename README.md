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
flag = ibmBluegroup.userInGroup("intranetID", "group name")
print(flag)
```

If your BlueGroup has spaces in the name, replace blanks with *%20* or *+*. 
```python
from ibmBluegroup import ibmBluegroup

ibmBluegroup = ibmBluegroup()
flag = ibmBluegroup.userInGroup("John.Doe@ibm.com", "Testing+Group")
# OR
# flag = ibmBluegroup.userInGroup("John.Doe@ibm.com", "Testing%20Group")
print(flag)
```
## Python Version

Tested on Python 3.5+.

## License

This library is licensed under the [Apache 2.0 license][license].



[license]: http://www.apache.org/licenses/LICENSE-2.0
