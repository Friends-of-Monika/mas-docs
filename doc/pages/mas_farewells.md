## Public functions

### def resetDockstatFlowVars()

Resets all the dockstat flow vars back to the original states (None)

---

### def selectFarewell(check_time=None)

Selects a farewell to be used. This evaluates rules and stuff appropriately.

**Parameters:**
- `check_time` &mdash; time to use when doing date checks If None, we use current datetime (Default: None)


**Returns:**<br>
a single farewell (as an Event) that we want to use

---

### def resetDockstatFlowVars()

Resets all the dockstat flow vars back to the original states (None)

---

### def selectFarewell(check_time=None)

Selects a farewell to be used. This evaluates rules and stuff appropriately.

**Parameters:**
- `check_time` &mdash; time to use when doing date checks If None, we use current datetime (Default: None)


**Returns:**<br>
a single farewell (as an Event) that we want to use

---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _filterFarewell(ev, curr_pri, aff, check_time)

Filters a farewell for the given type, among other things.

**Parameters:**
- `ev` &mdash; ev to filter
- `curr_pri` &mdash; current loweset priority to compare to
- `aff` &mdash; affection to use in aff_range comparisons
- `check_time` &mdash; datetime to check against timed rules


**Returns:**<br>
True if this ev passes the filter, False otherwise

---

### def _filterFarewell(ev, curr_pri, aff, check_time)

Filters a farewell for the given type, among other things.

**Parameters:**
- `ev` &mdash; ev to filter
- `curr_pri` &mdash; current loweset priority to compare to
- `aff` &mdash; affection to use in aff_range comparisons
- `check_time` &mdash; datetime to check against timed rules


**Returns:**<br>
True if this ev passes the filter, False otherwise

---

