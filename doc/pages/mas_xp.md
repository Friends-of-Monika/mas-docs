# store mas_xp

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def calc()

Calculates xp gained since last call to calc  Sets globals as needed

**Returns:**<br>
amt of xp gained since last call to calc

---

### def calc_by_hours(duration, start_rate)

Calculates toatl xp gain given a duration (in hours) and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amt of time to grant xp for (hours)
- `start_rate` &mdash; the rate to start calculating with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

---

### def calc_by_time(duration, start_rate)

Calculates total xp gain given a duration and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amount of time to grant xp for (timedelta)
- `start_rate` &mdash; the rate to start calctuing with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

---

### def grant()

Grants xp based on current state. Meant for use by ch30 code

---

### def level()

Gets current level

**Returns:**<br>
current level

---

### def set_xp_rate()

Sets xp rate based on session time today Also resets reset date if appropriate

---

### def calc()

Calculates xp gained since last call to calc  Sets globals as needed

**Returns:**<br>
amt of xp gained since last call to calc

---

### def calc_by_hours(duration, start_rate)

Calculates toatl xp gain given a duration (in hours) and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amt of time to grant xp for (hours)
- `start_rate` &mdash; the rate to start calculating with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

---

### def calc_by_time(duration, start_rate)

Calculates total xp gain given a duration and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amount of time to grant xp for (timedelta)
- `start_rate` &mdash; the rate to start calctuing with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

---

### def grant()

Grants xp based on current state. Meant for use by ch30 code

---

### def level()

Gets current level

**Returns:**<br>
current level

---

### def set_xp_rate()

Sets xp rate based on session time today Also resets reset date if appropriate

---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _calc(xp_rate, start, end, hrx)

Calculates xp gained within a range

**Parameters:**
- `xp_rate` &mdash; starting rate to calc xp with
- `start` &mdash; datetime to begin calculating xp with
- `end` &mdash; datetime to end calculating xp with
- `hrx` &mdash; hours today that have already been applied to xp


**Returns:**<br>
tuple: [0] - xp gained [1] - new xp_rate to use [2] - new amount of hours that we have applied xp rate to

---

### def _grant(xp, xptnl)

Internal version of grant. dont use

**Parameters:**
- `xp` &mdash; amount of xp to grant
- `xptnl` &mdash; current xp to next level


**Returns:**<br>
tuple: [0] - lvls gained [1] - new xp tnl

---

### def _grant_on_pt()

Grants xp by calcuating avgs using the current playtime

**Returns:**<br>
tuple: [0] - lvls gained [1] - new xp tnl

---

### def _grant_xp(xp)

Grant abitrary xp. You better have a good reason to use this.

**Parameters:**
- `xp` &mdash; arbitrary xp to grant


---

### def _level(xp)

gets level using based on an amt of xp

**Parameters:**
- `xp` &mdash; amt of xp to calculate level for


**Returns:**<br>
level based on xp

---

### def _level_rxp(xp)

Gets gained levels and remaining xp

**Parameters:**
- `xp` &mdash; amt of xp to calculate level for


**Returns:**<br>
tuple of the following format: [0] - lvls gained [1] - remainig xp

---

### def _calc(xp_rate, start, end, hrx)

Calculates xp gained within a range

**Parameters:**
- `xp_rate` &mdash; starting rate to calc xp with
- `start` &mdash; datetime to begin calculating xp with
- `end` &mdash; datetime to end calculating xp with
- `hrx` &mdash; hours today that have already been applied to xp


**Returns:**<br>
tuple: [0] - xp gained [1] - new xp_rate to use [2] - new amount of hours that we have applied xp rate to

---

### def _grant(xp, xptnl)

Internal version of grant. dont use

**Parameters:**
- `xp` &mdash; amount of xp to grant
- `xptnl` &mdash; current xp to next level


**Returns:**<br>
tuple: [0] - lvls gained [1] - new xp tnl

---

### def _grant_on_pt()

Grants xp by calcuating avgs using the current playtime

**Returns:**<br>
tuple: [0] - lvls gained [1] - new xp tnl

---

### def _grant_xp(xp)

Grant abitrary xp. You better have a good reason to use this.

**Parameters:**
- `xp` &mdash; arbitrary xp to grant


---

### def _level(xp)

gets level using based on an amt of xp

**Parameters:**
- `xp` &mdash; amt of xp to calculate level for


**Returns:**<br>
level based on xp

---

### def _level_rxp(xp)

Gets gained levels and remaining xp

**Parameters:**
- `xp` &mdash; amt of xp to calculate level for


**Returns:**<br>
tuple of the following format: [0] - lvls gained [1] - remainig xp

---

