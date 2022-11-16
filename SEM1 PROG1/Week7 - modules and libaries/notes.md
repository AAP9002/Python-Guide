# Week 7 - Modules and Libraries
- Creating modules and importing them

## Modules

```python
import module_name
import module_name as abreviation # or this way
```

External code that can be imported

Modules should have an all lowercase name

use doc string

### DOC STRING

PEP 257

this will then be generated into help files automatically

```python
import module_name as abreviation # or this way
help(abreviation)
help(abreviation.function)
```

### Name Spaces

Separate name spaces for the variables and function names.

when importing, a module has its own name space to avoid clashing with names in the main program or other nodules

```python
from module_name import * # import all into same name space
#not recomended as variable and function names may clash

from module_name import function1, function2
```

## Libraries

installing Libraries

```python
pip install -U scikit-learn
```