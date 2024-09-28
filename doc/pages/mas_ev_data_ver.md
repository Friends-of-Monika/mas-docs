# store mas_ev_data_ver

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def verify_event_data(per_db)

Verifies event data of the given persistent data. Entries that are invalid are removed. We only check the bits of data that we have, so data lines with smaller sizes are only validated for what they have.

**Parameters:**
- `per_db` &mdash; persistent database to verify


---

### def verify_event_data(per_db)

Verifies event data of the given persistent data. Entries that are invalid are removed. We only check the bits of data that we have, so data lines with smaller sizes are only validated for what they have.

**Parameters:**
- `per_db` &mdash; persistent database to verify


---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _strict_can_pickle(val)

Checks if this value can be pickled safely into persistent.  This is VERY strict. we only allow types, not isinstance checks. no ducks here  This will check structures recursively and will catch recursion errors.

**Parameters:**
- `val` &mdash; value to check


**Returns:**<br>
tuple of the following format: [0] - True if the value can be safely pickled, False if recursion error or not picklable. [1] - True if recursion error, False otherwise

---

### def _m1_event0x2dhandler__strict_can_pickle(val)

Recursive strict pickle check. See _strict_can_pickle for more info.  Will raise recursion error if appropriate.

**Parameters:**
- `val` &mdash; value to check


**Returns:**<br>
True if value can be safely pickled, False otherwise.

---

### def _verify_bool(val, allow_none=True)

---

### def _verify_dict(val, allow_none=True)

---

### def _verify_list(val, allow_none=True)

---

### def _verify_dt(val, allow_none=True)

---

### def _verify_dt_nn(val)

---

### def _verify_evact(val, allow_none=True)

---

### def _verify_int(val, allow_none=True)

---

### def _verify_int_nn(val)

---

### def _verify_str(val, allow_none=True)

---

### def _verify_td(val, allow_none=True)

---

### def _verify_td_nn(val)

---

### def _verify_tuli(val, allow_none=True)

---

### def _verify_tuli_nn(val)

---

### def _verify_tuli_aff(val, allow_none=True)

---

### def _verify_item(val, _type, allow_none=True)

Verifies the given value has the given type/instance

**Parameters:**
- `val` &mdash; value to verify
- `_type` &mdash; type to check
- `allow_none` &mdash; If True, None should be considered good value, false means bad value (Default: True)


**Returns:**<br>
True if the given value has the given type/instance, false otherwise

---

### def _strict_can_pickle(val)

Checks if this value can be pickled safely into persistent.  This is VERY strict. we only allow types, not isinstance checks. no ducks here  This will check structures recursively and will catch recursion errors.

**Parameters:**
- `val` &mdash; value to check


**Returns:**<br>
tuple of the following format: [0] - True if the value can be safely pickled, False if recursion error or not picklable. [1] - True if recursion error, False otherwise

---

### def _m1_event0x2dhandler__strict_can_pickle(val)

Recursive strict pickle check. See _strict_can_pickle for more info.  Will raise recursion error if appropriate.

**Parameters:**
- `val` &mdash; value to check


**Returns:**<br>
True if value can be safely pickled, False otherwise.

---

### def _verify_bool(val, allow_none=True)

---

### def _verify_dict(val, allow_none=True)

---

### def _verify_list(val, allow_none=True)

---

### def _verify_dt(val, allow_none=True)

---

### def _verify_dt_nn(val)

---

### def _verify_evact(val, allow_none=True)

---

### def _verify_int(val, allow_none=True)

---

### def _verify_int_nn(val)

---

### def _verify_str(val, allow_none=True)

---

### def _verify_td(val, allow_none=True)

---

### def _verify_td_nn(val)

---

### def _verify_tuli(val, allow_none=True)

---

### def _verify_tuli_nn(val)

---

### def _verify_tuli_aff(val, allow_none=True)

---

### def _verify_item(val, _type, allow_none=True)

Verifies the given value has the given type/instance

**Parameters:**
- `val` &mdash; value to verify
- `_type` &mdash; type to check
- `allow_none` &mdash; If True, None should be considered good value, false means bad value (Default: True)


**Returns:**<br>
True if the given value has the given type/instance, false otherwise

---

### def _verify_per_mtime()

verifies persistent data and ensure mod times are not in the future

---

### def _verify_per_mtime()

verifies persistent data and ensure mod times are not in the future

---

### def _verify_data_line(ev_line)

Verifies event data for a single tuple of data.

**Parameters:**
- `ev_line` &mdash; single line of data to verify


**Returns:**<br>
True if passed verification, False if not

---

### def _verify_data_line(ev_line)

Verifies event data for a single tuple of data.

**Parameters:**
- `ev_line` &mdash; single line of data to verify


**Returns:**<br>
True if passed verification, False if not

---

