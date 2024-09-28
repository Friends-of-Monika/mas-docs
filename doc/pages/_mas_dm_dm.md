## Public functions

### def add_idxs(_db, _key, _exp_len)

Adds indexes to the given key

**Parameters:**
- `_db` &mdash; database to add indexes to
- `_key` &mdash; key of the item to add indexes to
- `_exp_len` &mdash; the length the item should have prior to addition Pass in less than 0 to ignore length checks


---

### def add_idxs_db(_db, _exp_len)

Adds indexes to items in the given db

**Parameters:**
- `_db` &mdash; database to add indexes to
- `_exp_len` &mdash; the length the item shoudl have prior to additoin Pass in 0 or less to ignore length checks


---

### def rm_idxs(_db, _key, _exp_len)

removes indexes off the given key off the given db

**Parameters:**
- `_db` &mdash; database to remove indexes off of
- `_key` &mdash; key of the item to remove indexes off of
- `_exp_len` &mdash; the length the item should have prior to removal. Pass in 0 or less to ignore length checks.


---

### def rm_idxs_db(_db, _exp_len)

Removes indexes off items in the given db

**Parameters:**
- `_db` &mdash; database to remove indexes off of
- `_exp_len` &mdash; the length the item should have prior to removal Pass in 0 or less to ignore length checks


---

### def run(start_ver, end_ver)

Runs the data migration algorithms.

**Parameters:**
- `start_ver` &mdash; start version to start
- `end_ver` &mdash; ending version number


---

### def add_idxs(_db, _key, _exp_len)

Adds indexes to the given key

**Parameters:**
- `_db` &mdash; database to add indexes to
- `_key` &mdash; key of the item to add indexes to
- `_exp_len` &mdash; the length the item should have prior to addition Pass in less than 0 to ignore length checks


---

### def add_idxs_db(_db, _exp_len)

Adds indexes to items in the given db

**Parameters:**
- `_db` &mdash; database to add indexes to
- `_exp_len` &mdash; the length the item shoudl have prior to additoin Pass in 0 or less to ignore length checks


---

### def rm_idxs(_db, _key, _exp_len)

removes indexes off the given key off the given db

**Parameters:**
- `_db` &mdash; database to remove indexes off of
- `_key` &mdash; key of the item to remove indexes off of
- `_exp_len` &mdash; the length the item should have prior to removal. Pass in 0 or less to ignore length checks.


---

### def rm_idxs_db(_db, _exp_len)

Removes indexes off items in the given db

**Parameters:**
- `_db` &mdash; database to remove indexes off of
- `_exp_len` &mdash; the length the item should have prior to removal Pass in 0 or less to ignore length checks


---

### def run(start_ver, end_ver)

Runs the data migration algorithms.

**Parameters:**
- `start_ver` &mdash; start version to start
- `end_ver` &mdash; ending version number


---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _m1_zz_dm__add_idxs(_db, _key, _exp_len, idx_d_list)

INTERNAL ONLY adds indexes to the given key to the given db

---

### def _m1_zz_dm__rm_idxs(_db, _key, _exp_len, idx_list)

INTERNAL ONLY removes indexes off the given key off the given db

---

### def _m1_zz_dm__dm_1_to_2_helper(curr_len)

---

### def _dm_1_to_2()

Data migration from version 1 to 2  GOALS: - remove rules property from events and shrink the tuples.

---

### def _dm_0811_to_2()

Data migration from version 0811-0814 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_089_to_2()

Data migration from version 089-0810 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_082_to_2()

Data migration from version 082-088 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_080_to_2()

Data migration from version 080-081 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_073_to_2()

Data migration from version 0o73-074 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_2_to_1()

Data migration from version 2 to 1  GOALS: - add rules property to events, expand tuples

---

### def _determine_version()

This returns an  appropriate dm version based on version

---

### def _m1_zz_dm__lessthan(val_a, val_b)

---

### def _m1_zz_dm__morethan(val_a, val_b)

---

### def _find_dm_fun(piv_ver, adj_ver, direction)

Iterates until we find a dm function and returns it.

**Parameters:**
- `piv_ver` &mdash; the verion number we dont want to change when searching
- `adj_ver` &mdash; the verison number we change when searching
- `direction` &mdash; the direction to change adj_ver


**Returns:**<br>
tuple of the following format: [0]: data migration function found, Or none if not found [1]: value of adj_ver when data migration found

---

### def _m1_zz_dm__add_idxs(_db, _key, _exp_len, idx_d_list)

INTERNAL ONLY adds indexes to the given key to the given db

---

### def _m1_zz_dm__rm_idxs(_db, _key, _exp_len, idx_list)

INTERNAL ONLY removes indexes off the given key off the given db

---

### def _m1_zz_dm__dm_1_to_2_helper(curr_len)

---

### def _dm_1_to_2()

Data migration from version 1 to 2  GOALS: - remove rules property from events and shrink the tuples.

---

### def _dm_0811_to_2()

Data migration from version 0811-0814 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_089_to_2()

Data migration from version 089-0810 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_082_to_2()

Data migration from version 082-088 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_080_to_2()

Data migration from version 080-081 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_073_to_2()

Data migration from version 0o73-074 to 2  GOALS: - remove rules property from events and shrink the tuples

---

### def _dm_2_to_1()

Data migration from version 2 to 1  GOALS: - add rules property to events, expand tuples

---

### def _determine_version()

This returns an  appropriate dm version based on version

---

### def _m1_zz_dm__lessthan(val_a, val_b)

---

### def _m1_zz_dm__morethan(val_a, val_b)

---

### def _find_dm_fun(piv_ver, adj_ver, direction)

Iterates until we find a dm function and returns it.

**Parameters:**
- `piv_ver` &mdash; the verion number we dont want to change when searching
- `adj_ver` &mdash; the verison number we change when searching
- `direction` &mdash; the direction to change adj_ver


**Returns:**<br>
tuple of the following format: [0]: data migration function found, Or none if not found [1]: value of adj_ver when data migration found

---

