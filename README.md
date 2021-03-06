# pyOptional

## Description
Library provided implementation Optional object similar to [Java optional](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html). Using this object, You will never check `if x is None`.

## Install
`pip install pyOptional`

## Usage

### Examples

```python
from pyOptional import Optional

optional_with_value = Optional('ABC')
optional_empty = Optional(None)

print(optional_with_value)
print(optional_empty)
```

**output:**
```
Optional of: ABC
Optional empty
```

### Methods:

#### get()
Returns value or throw `NoneValueError` exception on empty optional
```python
print(optional_with_value.get())
print(optional_empty.get())
```

**output**:
```
ABC
Traceback (most recent call last):
...
pyOptional.exceptions.NoneValueError: Called get on empty optional
```

#### get_or_else(default_value)
Returns value if exists or default_value when empty
```python
print(optional_with_value.get_or_else('XYZ'))
print(optional_empty.get_or_else('XYZ'))
```

**output**:
```
ABC
XYZ
```

#### get_or_else_get(callable_for_generate_default_value)
Returns value if exists, otherwise result of `callable_for_generate_default_value`
```python
def gen_value():
    return 'QWERTY'

print(optional_with_value.get_or_else_get(gen_value))
print(optional_empty.get_or_else_get(gen_value))
print(optional_empty.get_or_else_get(lambda: 'From lambda'))
```

**output**:
```
ABC
QWERTY
From lambda
```

#### get_or_raise(exception_class, *args, **kwargs)
Returns value if exists or raise provided exception
```python
print(optional_with_value.get_or_raise(FileNotFoundError, 'Some message'))
print(optional_empty.get_or_raise(FileNotFoundError, 'Some message'))
```

**output**:
```
ABC
Traceback (most recent call last):
...
FileNotFoundError: Some message
```

#### map(callable_to_transform_value)
Returns optional of other value (result returned by `callable_to_transform_value`) or Optional empty if source Optional was empty
```python
print(optional_with_value.map(lambda val: val*2))
print(optional_empty.map(lambda val: val*2))
```

**output**:
```
Optional of: ABCABC
Optional empty
```

#### flat_map(callable_to_transform_value)
Similar to map, but if source Optional contains another Optionals, result will contain single Optional
```python
nested_val_optional = Optional(Optional(Optional(8)))
nested_empty_optional = Optional(Optional(Optional(None)))
print(nested_val_optional.map(lambda val: val*3))
print('---------------------')
print(nested_empty_optional.map(lambda val: val*3))
print('---------------------')
print(nested_val_optional.flat_map(lambda val: val*3))
print('---------------------')
print(nested_empty_optional.flat_map(lambda val: val*3))
```

**output**:
```
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for *: 'Optional' and 'int'
---------------------
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for *: 'Optional' and 'int'
---------------------
Optional of: 24
---------------------
Optional empty
```

#### if_present(func)
Call func with optional value if exists. If optional is empty, do nothing.

```python
optional_with_value.if_present(lambda val: print('found value ' + val))
optional_empty.if_present(lambda val: print('found value ' + val))
```

**output**:
```
found value ABC
```

#### is_present()
return True if Optional not empty, otherwise False

```python
print(optional_with_value.is_present())
print(optional_empty.is_present())
```

**output**:
```
True
False
```

### Static Methods:

#### empty()
return an empty Optional

```python
print(Optional.empty())
```

**output**:
```
Optional empty
```
