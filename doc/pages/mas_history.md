> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def lookup(key, year)

Looks up data in the historical archives.

**Parameters:**
- `key` &mdash; data key to lookup
- `year` &mdash; year to look up data


**Returns:**<br>
a tuple of the following format: [0]: Lookup constant [1]: retrieved data (which may be None). This is always None if we could not find year or key

---

### def lookup_ot(key)

Looks up data overtime in the historical archives.

**Parameters:**
- `key` &mdash; data key to lookup
- `years` &mdash; years to look up data


**Returns:**<br>
SEE lookup_ot_l

---

### def lookup_otl(key, years_list)

Looks up data overtime in the historical archives.

**Parameters:**
- `key` &mdash; data key to look up
- `years_list` &mdash; list of years to lookup data


**Returns:**<br>
dict of the following format: year: tuple (SEE lookup)

---

### def verify(key, _verify, years_list)

Internali version of mas_HistVerify

---

### def loadMHSData()

Loads persistent MASHistorySaver data into the mhs_db  Also adds MHS to the sorted list and sorts it.

---

### def saveMHSData()

Saves MASHistorySaver data from mhs_db into persistent

---

### def addMHS(mhs)

Adds the given mhs to the database.

**Parameters:**
- `mhs` &mdash; MASHistorySaver object to add


---

### def getMHS(mhs_id)

Gets the MASHistorySaver object with the given id

**Parameters:**
- `mhs_id` &mdash; id of the MASHistorySaver object to get


**Returns:**<br>
MASHistorySaver object, or None if not found

---

### def lookup(key, year)

Looks up data in the historical archives.

**Parameters:**
- `key` &mdash; data key to lookup
- `year` &mdash; year to look up data


**Returns:**<br>
a tuple of the following format: [0]: Lookup constant [1]: retrieved data (which may be None). This is always None if we could not find year or key

---

### def lookup_ot(key)

Looks up data overtime in the historical archives.

**Parameters:**
- `key` &mdash; data key to lookup
- `years` &mdash; years to look up data


**Returns:**<br>
SEE lookup_ot_l

---

### def lookup_otl(key, years_list)

Looks up data overtime in the historical archives.

**Parameters:**
- `key` &mdash; data key to look up
- `years_list` &mdash; list of years to lookup data


**Returns:**<br>
dict of the following format: year: tuple (SEE lookup)

---

### def verify(key, _verify, years_list)

Internali version of mas_HistVerify

---

### def loadMHSData()

Loads persistent MASHistorySaver data into the mhs_db  Also adds MHS to the sorted list and sorts it.

---

### def saveMHSData()

Saves MASHistorySaver data from mhs_db into persistent

---

### def addMHS(mhs)

Adds the given mhs to the database.

**Parameters:**
- `mhs` &mdash; MASHistorySaver object to add


---

### def getMHS(mhs_id)

Gets the MASHistorySaver object with the given id

**Parameters:**
- `mhs_id` &mdash; id of the MASHistorySaver object to get


**Returns:**<br>
MASHistorySaver object, or None if not found

---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _valid_year_range()

generates the range of years that are valid for historical lookups.

**Returns:**<br>
range of years from 2017 to todays year.

---

### def _store(value, key, year)

Stores data in the historical archives.

**Parameters:**
- `value` &mdash; value to store
- `key` &mdash; data key to store value
- `year` &mdash; year to store value


---

### def _store_all(year_data, key)

Stores multiple year's worth of data in the historical archives.

**Parameters:**
- `year_data` &mdash; dictionary of the following format: year: data tuple from mas_HistLookup
- `key` &mdash; data key to store values


---

### def _valid_year_range()

generates the range of years that are valid for historical lookups.

**Returns:**<br>
range of years from 2017 to todays year.

---

### def _store(value, key, year)

Stores data in the historical archives.

**Parameters:**
- `value` &mdash; value to store
- `key` &mdash; data key to store value
- `year` &mdash; year to store value


---

### def _store_all(year_data, key)

Stores multiple year's worth of data in the historical archives.

**Parameters:**
- `year_data` &mdash; dictionary of the following format: year: data tuple from mas_HistLookup
- `key` &mdash; data key to store values


---

### def _bday_exit_pp(mhs)

---

### def _pm_holdme_adj_times(elapsed)

Sets the appropraite persistent vars according to the elasped time for the hold me topic

---

### def _bday_exit_pp(mhs)

---

### def _pm_holdme_adj_times(elapsed)

Sets the appropraite persistent vars according to the elasped time for the hold me topic

---

### def _runMHSAlg()

Runs the historical data saving algorithm

---

### def _runMHSResetAlg()

Runs special resets in the case of TT. Do NOT call if TT not detected.

---

### def _runMHSAlg()

Runs the historical data saving algorithm

---

### def _runMHSResetAlg()

Runs special resets in the case of TT. Do NOT call if TT not detected.

---

