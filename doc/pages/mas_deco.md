# store mas_deco

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def add_deco(s_name, obj)

Adds deco object to the deco db. Raises an exception if there are duplicates. All deco objects get prefixed wtih text to prevent collisions with standard sprite objects.

**Parameters:**
- `s_name` &mdash; shorthand name to apply to this deco object
- `obj` &mdash; MASDecoration object to add to the deco db


---

### def get_deco(name)

Gets a deco object by name. This accepts shortname or regular deco name

**Parameters:**
- `name` &mdash; can either be shortname or actual deco name


**Returns:**<br>
MASDecoration object, or None if not valid name

---

### def add_deco(s_name, obj)

Adds deco object to the deco db. Raises an exception if there are duplicates. All deco objects get prefixed wtih text to prevent collisions with standard sprite objects.

**Parameters:**
- `s_name` &mdash; shorthand name to apply to this deco object
- `obj` &mdash; MASDecoration object to add to the deco db


---

### def get_deco(name)

Gets a deco object by name. This accepts shortname or regular deco name

**Parameters:**
- `name` &mdash; can either be shortname or actual deco name


**Returns:**<br>
MASDecoration object, or None if not valid name

---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _add_it_deco(obj)

Adds a MASImageTagDecoration object to the deco db. Raises exceptions if a duplicate was found OR if the object is not a MASImageTagDecoration.

**Parameters:**
- `obj` &mdash; MASImageTagDecoration object to add to the deco db


---

### def _add_it_deco(obj)

Adds a MASImageTagDecoration object to the deco db. Raises exceptions if a duplicate was found OR if the object is not a MASImageTagDecoration.

**Parameters:**
- `obj` &mdash; MASImageTagDecoration object to add to the deco db


---

