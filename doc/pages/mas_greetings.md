## Functions

### def selectGreeting(gre_type=None, check_time=None)

Selects a greeting to be used. This evaluates rules and stuff appropriately.

**Parameters:**
- `gre_type` &mdash; greeting type to use (Default: None)
- `check_time` &mdash; time to use when doing date checks If None, we use current datetime (Default: None)


**Returns:**<br>
a single greeting (as an Event) that we want to use

### def checkTimeout(gre_type)

Checks if we should clear the current greeting type because of a timeout.

**Parameters:**
- `gre_type` &mdash; greeting type we are checking


**Returns:**<br>
passed in gre_type, or None if timeout occured.

### def selectGreeting(gre_type=None, check_time=None)

Selects a greeting to be used. This evaluates rules and stuff appropriately.

**Parameters:**
- `gre_type` &mdash; greeting type to use (Default: None)
- `check_time` &mdash; time to use when doing date checks If None, we use current datetime (Default: None)


**Returns:**<br>
a single greeting (as an Event) that we want to use

### def checkTimeout(gre_type)

Checks if we should clear the current greeting type because of a timeout.

**Parameters:**
- `gre_type` &mdash; greeting type we are checking


**Returns:**<br>
passed in gre_type, or None if timeout occured.

