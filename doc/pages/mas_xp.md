## Functions

### def calc()

Calculates xp gained since last call to calc  Sets globals as needed

**Returns:**<br>
amt of xp gained since last call to calc

### def calc_by_hours(duration, start_rate)

Calculates toatl xp gain given a duration (in hours) and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amt of time to grant xp for (hours)
- `start_rate` &mdash; the rate to start calculating with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

### def calc_by_time(duration, start_rate)

Calculates total xp gain given a duration and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amount of time to grant xp for (timedelta)
- `start_rate` &mdash; the rate to start calctuing with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

### def grant()

Grants xp based on current state. Meant for use by ch30 code

### def level()

Gets current level

**Returns:**<br>
current level

### def set_xp_rate()

Sets xp rate based on session time today Also resets reset date if appropriate

### def calc()

Calculates xp gained since last call to calc  Sets globals as needed

**Returns:**<br>
amt of xp gained since last call to calc

### def calc_by_hours(duration, start_rate)

Calculates toatl xp gain given a duration (in hours) and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amt of time to grant xp for (hours)
- `start_rate` &mdash; the rate to start calculating with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

### def calc_by_time(duration, start_rate)

Calculates total xp gain given a duration and starting rate using the new XP model

**Parameters:**
- `duration` &mdash; amount of time to grant xp for (timedelta)
- `start_rate` &mdash; the rate to start calctuing with


**Returns:**<br>
tuple of the following format: [0] - amt of xp gained (float) [1] - new rate (float)

### def grant()

Grants xp based on current state. Meant for use by ch30 code

### def level()

Gets current level

**Returns:**<br>
current level

### def set_xp_rate()

Sets xp rate based on session time today Also resets reset date if appropriate

