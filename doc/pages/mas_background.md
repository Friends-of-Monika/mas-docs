## Functions

### def build()

Builds all background objects using current time settings.

---### def buildupdate()

Builds all background objects and updates current time settings. This properly saves prev_flt.

---### def default_MBGFM()

Generates a MASBackgroundFilterManager using the default (aka pre0.11.3) settings.

**Returns:**<br>
MASBackgroundFilterManager object

---### def loadMBGData()

Loads persistent MASBackground data into the weather map

---### def saveMBGData()

Saves MASBackground data from bg map into persistent

---### def getUnlockedBGCount()

Gets the number of unlocked backgrounds

---### def hasXUnlockedBGs(min_amt_unlocked)

Checks if we have at least min_amt_unlocked bgs unlocked

**Parameters:**
- `min_amt_unlocked` &mdash; minimum number of BGs which should be unlocked to return true


**Returns:**<br>
True if we have at least min_amt_unlocked BGs unlocked, False otherwise

---### def getBackground(id_)

Returns a bg object

**Parameters:**
- `id_` &mdash; str - background id


**Returns:**<br>
background object or None if not found

---### def unlockBackground(id_)

Unlocks a bg

**Parameters:**
- `id_` &mdash; str - background id


---### def lockBackground(id_)

Locks a bg

**Parameters:**
- `id_` &mdash; str - background id


---### def isBackgroundUnlocked(id_)

Checks if a background is unlocked

**Parameters:**
- `id_` &mdash; str - background id


**Returns:**<br>
boolean

---### def log_bg(bg_obj, exc_info=None)

Logs the given BG object to standard bg log

**Parameters:**
- `bg_obj` &mdash; bg object to log
- `exc_info` &mdash; exception info. Should be tuple: [0] - exception type [1] - exception value [2] - traceback (Default: None)


---### def build()

Builds all background objects using current time settings.

---### def buildupdate()

Builds all background objects and updates current time settings. This properly saves prev_flt.

---### def default_MBGFM()

Generates a MASBackgroundFilterManager using the default (aka pre0.11.3) settings.

**Returns:**<br>
MASBackgroundFilterManager object

---### def loadMBGData()

Loads persistent MASBackground data into the weather map

---### def saveMBGData()

Saves MASBackground data from bg map into persistent

---### def getUnlockedBGCount()

Gets the number of unlocked backgrounds

---### def hasXUnlockedBGs(min_amt_unlocked)

Checks if we have at least min_amt_unlocked bgs unlocked

**Parameters:**
- `min_amt_unlocked` &mdash; minimum number of BGs which should be unlocked to return true


**Returns:**<br>
True if we have at least min_amt_unlocked BGs unlocked, False otherwise

---### def getBackground(id_)

Returns a bg object

**Parameters:**
- `id_` &mdash; str - background id


**Returns:**<br>
background object or None if not found

---### def unlockBackground(id_)

Unlocks a bg

**Parameters:**
- `id_` &mdash; str - background id


---### def lockBackground(id_)

Locks a bg

**Parameters:**
- `id_` &mdash; str - background id


---### def isBackgroundUnlocked(id_)

Checks if a background is unlocked

**Parameters:**
- `id_` &mdash; str - background id


**Returns:**<br>
boolean

---### def log_bg(bg_obj, exc_info=None)

Logs the given BG object to standard bg log

**Parameters:**
- `bg_obj` &mdash; bg object to log
- `exc_info` &mdash; exception info. Should be tuple: [0] - exception type [1] - exception value [2] - traceback (Default: None)


---### def run_gbl_flt_change(old_flt, new_flt, curr_time)

Runs global filter change progpoint, logging for errors

---### def run_gbl_flt_change(old_flt, new_flt, curr_time)

Runs global filter change progpoint, logging for errors

---### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

#### def _toggleBackgroundUnlock(id_, value)

Locks/unlocks a bg

**Parameters:**
- `id_` &mdash; str - background id
- `value` &mdash; bool - the value for the unlocked field


---#### def _toggleBackgroundUnlock(id_, value)

Locks/unlocks a bg

**Parameters:**
- `id_` &mdash; str - background id
- `value` &mdash; bool - the value for the unlocked field


---#### def _gbl_flt_change(old_flt, new_flt, curr_time)

Runs when a filter change occurs

**Parameters:**
- `old_flt` &mdash; outgoing filter. Will be None on startup.
- `new_flt` &mdash; incoming filter.
- `curr_time` &mdash; current time as datetime.time


---#### def _gbl_chunk_change(old_chunk, new_chunk, curr_time)

Runs when a chunk change occurs

**Parameters:**
- `old_chunk` &mdash; outgoing chunk, will be None on startup
- `new_flt` &mdash; incoming chunk
- `curr_time` &mdash; current time as datetime.time


---#### def _def_background_entry(_old)

Entry programming point for default background

---#### def _def_background_exit(_new)

Exit programming point for default background

---#### def _gbl_flt_change(old_flt, new_flt, curr_time)

Runs when a filter change occurs

**Parameters:**
- `old_flt` &mdash; outgoing filter. Will be None on startup.
- `new_flt` &mdash; incoming filter.
- `curr_time` &mdash; current time as datetime.time


---#### def _gbl_chunk_change(old_chunk, new_chunk, curr_time)

Runs when a chunk change occurs

**Parameters:**
- `old_chunk` &mdash; outgoing chunk, will be None on startup
- `new_flt` &mdash; incoming chunk
- `curr_time` &mdash; current time as datetime.time


---#### def _def_background_entry(_old)

Entry programming point for default background

---#### def _def_background_exit(_new)

Exit programming point for default background

---