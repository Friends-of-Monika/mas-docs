## Public functions

### def selectGreeting(gre_type=None, check_time=None)

Selects a greeting to be used. This evaluates rules and stuff appropriately.

**Parameters:**
- `gre_type` &mdash; greeting type to use (Default: None)
- `check_time` &mdash; time to use when doing date checks If None, we use current datetime (Default: None)


**Returns:**<br>
a single greeting (as an Event) that we want to use

---

### def checkTimeout(gre_type)

Checks if we should clear the current greeting type because of a timeout.

**Parameters:**
- `gre_type` &mdash; greeting type we are checking


**Returns:**<br>
passed in gre_type, or None if timeout occured.

---

### def selectGreeting(gre_type=None, check_time=None)

Selects a greeting to be used. This evaluates rules and stuff appropriately.

**Parameters:**
- `gre_type` &mdash; greeting type to use (Default: None)
- `check_time` &mdash; time to use when doing date checks If None, we use current datetime (Default: None)


**Returns:**<br>
a single greeting (as an Event) that we want to use

---

### def checkTimeout(gre_type)

Checks if we should clear the current greeting type because of a timeout.

**Parameters:**
- `gre_type` &mdash; greeting type we are checking


**Returns:**<br>
passed in gre_type, or None if timeout occured.

---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _filterGreeting(ev, curr_pri, aff, check_time, gre_type=None)

Filters a greeting for the given type, among other things.

**Parameters:**
- `ev` &mdash; ev to filter
- `curr_pri` &mdash; current loweset priority to compare to
- `aff` &mdash; affection to use in aff_range comparisons
- `check_time` &mdash; datetime to check against timed rules
- `gre_type` &mdash; type of greeting we want. We just do a basic in check for category. We no longer do combinations (Default: None)


**Returns:**<br>
True if this ev passes the filter, False otherwise

---

### def _filterGreeting(ev, curr_pri, aff, check_time, gre_type=None)

Filters a greeting for the given type, among other things.

**Parameters:**
- `ev` &mdash; ev to filter
- `curr_pri` &mdash; current loweset priority to compare to
- `aff` &mdash; affection to use in aff_range comparisons
- `check_time` &mdash; datetime to check against timed rules
- `gre_type` &mdash; type of greeting we want. We just do a basic in check for category. We no longer do combinations (Default: None)


**Returns:**<br>
True if this ev passes the filter, False otherwise

---

