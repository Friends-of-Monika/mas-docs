## Functions

### def can_use_https()

Checks if we can safely use https in general - this combines several checks, mainly: - ssl - a cert

**Returns:**<br>
True if https can be used.

### def can_use_https()

Checks if we can safely use https in general - this combines several checks, mainly: - ssl - a cert

**Returns:**<br>
True if https can be used.

### def all_none(data=None, lata=None)

Checks if a dict and/or list is all None

**Parameters:**
- `data` &mdash; Dict of data. values are checked for None-ness (Default: None)
- `lata` &mdash; List of data. values are checked for None-ness (Default: None)


**Returns:**<br>
True if all data is None, False otherwise

### def clean_gui_text(text)

Cleans the given text so its suitable for GUI usage

**Parameters:**
- `text` &mdash; text to clean


**Returns:**<br>
cleaned text

### def eqfloat(left, right, places=6)

Float comparisons thatcan handle accuracy errors. This uses checks equivalence within a given amount of decimal places

**Parameters:**
- `left` &mdash; value to compare
- `right` &mdash; other value to compare


**Returns:**<br>
True if values are equal, False if not

### def truncround(value, places=6)

Does "truncated rounding" for floats. This is done via a floatsplit_i that reassembles into a float.

**Parameters:**
- `value` &mdash; float to round
- `places` &mdash; number of decimal places to truncate round to (Default: 6)


**Returns:**<br>
truncate-rounded float

### def floatcombine_i(value, places=6)

Combines output of floatsplit_i back into a float

**Parameters:**
- `value` &mdash; tuple of the following format: [0]: integer part of the float [1]: float part of the float as integer
- `places` &mdash; number of places to apply to the float part (Default: 6)


**Returns:**<br>
float

### def floatsplit(value)

Splits a float into int and float parts (unlike _splitfloat which returns three ints, or floatsplit_i which returns two ints with rounding)

**Parameters:**
- `value` &mdash; float to split


**Returns:**<br>
tuple of the following format: [0] - integer portion of float (int) [1] - float portion of float (float)

### def floatsplit_i(value, places=6)

Similar to floatsplit, but converts the float portion into an int

**Parameters:**
- `value` &mdash; float to split
- `places` &mdash; number of decimal places to keep when converting the float to an int (Default: 6)


**Returns:**<br>
tuple of the following format: [0] - integer portion of float [1] - float portion of float, multiplied by 10^places

### def pdget(key, table, validator=None, defval=None)

Protected Dict GET Gets an item from a dict, using protections to ensure this item is valid

**Parameters:**
- `key` &mdash; key of item to get
- `table` &mdash; dict to get from
- `validator` &mdash; function to call with the item to validate it If None, no validating done (Default: None)
- `defval` &mdash; default value to return if could not get from dict


### def td2hr(duration)

Converts a timedetla to hours (fractional)

**Parameters:**
- `duration` &mdash; timedelta to convert


**Returns:**<br>
hours as float

### def get_localzone()

Wrapper around tzlocal.get_localzone() that won't raise exceptions

**Returns:**<br>
pytz tzinfo object of the local time zone. if system timezone info is configured wrong, then a special-MAS version of a timezone is returned instead. This version works like a static, unchanging timezone, using the time.timezone/altzone values.

### def reload_localzone()

Reloads the cached localzone.

**Returns:**<br>
see get_localzone()

### def local_to_utc(local_dt, latest=True)

Converts the given local datetime into a UTC datetime.

**Parameters:**
- `local_dt` &mdash; datetime to convert, should be naive (no tzinfo)
- `latest` &mdash; True will attempt to reload the local timezone before doing the conversion. If dealing with an old datetime, you might want to pass False (Default: True)


**Returns:**<br>
UTC-based naive datetime (no tzinfo). This is safe for pickling/saving to persistent.

### def utc_to_any(utc_dt, target_tz)

Converts the given UTC datetime into any tz datetime

**Parameters:**
- `utc_dt` &mdash; datetime to convert, should be naive (no tzinfo)
- `target_tz` &mdash; pytz.tzinfo object of the timezone to convert to


**Returns:**<br>
datetime converted to the target timezone. NOTE: DO NOT PICKLE THIS OR SAVE TO PERSISTENT.

### def utc_to_local(utc_dt, latest=True)

Converts the given UTC datetime into a local datetime

**Parameters:**
- `utc_dt` &mdash; datetime to convert, should be naive (no tzinfo)
- `latest` &mdash; True will attempt to reload the local timezone before doing the conversion. If dealing with an old datetime, you might want to pass False (Default: True)


**Returns:**<br>
localized datetime with tzinfo of this zone (see pytz docs) NOTE: DO NOT PICKLE THIS or SAVE TO PERSISTENT. While pytz can safely pickle, we do not want to force a dependency on the persistent.

### def stdout_as(outstream)

Context manager that can replace stdout temporarily. Use with the with statement (python).

**Decorators:**
- `@contextmanager`


**Parameters:**
- `outstream` &mdash; the stream to temporarily replace sys.stdout with


### def tryparsedt(_datetime, default=None, sep=' ')

Trys to parse a datetime isoformat string into a datetime object

**Parameters:**
- `_datetime` &mdash; datetime iso format string to parse
- `default` &mdash; default value to return if parsing fails
- `sep` &mdash; separator used when converting to isoformat


**Returns:**<br>
datetime object, or default if parsing failed

### def is_file_present(filename)

Checks if a file is present (exists)

### def weightedChoice(choice_weight_tuple_list)

Returns a random item based on weighting.

**Parameters:**
- `choice_weight_tuple_list` &mdash; List of tuples with the form (choice, weighting)


**Returns:**<br>
random choice value picked using choice weights

### def tryparsefloat(value, default=0)

Attempts to parse the given value into a float. Returns the default if that parse failed.

**Parameters:**
- `value` &mdash; value to parse
- `default` &mdash; value to return if parse fails


**Returns:**<br>
a float representation of the given value, or default if the given value could not be parsed into an float

### def bullet_list(_list, bullet='  -')

Converts a list of items into a bulleted list of strings.

**Parameters:**
- `_list` &mdash; list to convert into bulleted list
- `bullet` &mdash; the bullet to use. A space is added between the bullet and the item. (Default: 2 spaces and a dash)


**Returns:**<br>
a list of strings where each string is an item with a bullet.

### def nested_defaultdict(final_factory=None, levels=1)

Generates a nested defaultdict. Basically good for creating an n-level dict of defaults.

**Parameters:**
- `final_factory` &mdash; the constructor/object factory to use for the innermost defaultdict (Default: None)
- `levels` &mdash; the number of nested defaultdicts to use. Must be greater than 0 but less than 10. The default value is equivalent to just calling defaultdict (Default: 1)


**Returns:**<br>
a nested defaultdict implementation

### def add_years(initial_date, years)

**Returns:**<br>
the date with the years added, if it's feb 29th it goes to mar 1st, if feb 29 doesn't exists in the new year

### def add_months(starting_date, months)

Takes a datetime object and add a number of months Handles the case where the new month doesn't have that day

**Parameters:**
- `starting_date` &mdash; date representing the date to add months to
- `months` &mdash; amount of months to add


**Returns:**<br>
datetime.date representing the inputted date with the corresponding months added

### def sod(starting_date)

### def mdnt(starting_date)

Takes a datetime object and returns a new datetime with the same date at midnight

**Parameters:**
- `starting_date` &mdash; date to change


**Returns:**<br>
starting_date but at midnight

### def am3(_datetime)

Takes a datetime object and returns a new datetime with the same date at 3 am.

**Parameters:**
- `_datetime` &mdash; datetime to change


**Returns:**<br>
_datetime but at 3am

### def secInDay()

**Returns:**<br>
number of seconds in a day

### def time2sec(_time)

Converts a time value to seconds

**Parameters:**
- `time` &mdash; datetime.time object to convert


**Returns:**<br>
number of seconds

### def fli_indk(lst, d)

Find List Item

**Parameters:**
- `lst` &mdash; list to cehck
- `d` &mdash; dictionary to check


**Returns:**<br>
The index of the first item in the list that is a key in the dict. There are no checks of if the item can be a valid key. -1 is returned if no item in the list is a key in the dict.

### def insert_sort(sort_list, item, key)

Performs a round of insertion sort. This does least to greatest sorting

**Parameters:**
- `sort_list` &mdash; list to insert + sort
- `item` &mdash; item to sort and insert
- `key` &mdash; function to call using the given item to retrieve sort key


**Returns:**<br>
sort_list - list with 1 additonal element, sorted

### def insert_sort_compare(sort_list, item, cmp_func)

Performs a round of insertion sort using comparison function

**Parameters:**
- `sort_list` &mdash; list to insert + sort
- `item` &mdash; item to sort and insert
- `cmp_func` &mdash; function to compare items with. first arg will be item in the list second arg will always be the item being inserted This should return True if the item is not in the correct place False when the item is in the correct place


**Returns:**<br>
sort_list - list with 1 additional element, sorted

### def insert_sort_keyless(sort_list, item)

Performs a round of insertion sort for natural comparison objects. This does least to greatest sorting.

**Parameters:**
- `sort_list` &mdash; list to insert + sort
- `item` &mdash; item to sort and insert


**Returns:**<br>
sort_list - list with 1 additional element, sorted

### def normalize_points(points, offsets, add=True)

normalizes a list of points using the given offsets

**Parameters:**
- `points` &mdash; list of points to normalize
- `offsets` &mdash; Tuple of the following format: [0] - amount to offset x coords [1] - amount to offset y coords
- `add` &mdash; True will add offsets, False will subtract offsets


**Returns:**<br>
list of normalized points

### def nz_count(value_list)

NonZero Count  Counts all non-zero values in the given list

**Parameters:**
- `value_list` &mdash; list to count nonzero values for


**Returns:**<br>
number of nonzero values in list

### def ev_distribute(value_list, amt, nz=False)

EVen Distribute  Evenly distributes the given value to a given value list.

**Parameters:**
- `value_list` &mdash; list of numbers to distribute to
- `amt` &mdash; amount to evenly distribute
- `nz` &mdash; True will make distribution only apply to non-zero values, False will distribute to all (Default: False)


**Returns:**<br>
value_list - even distribution amount added to each appropriate item in this list leftover amount

### def fz_distribute(value_list)

Flipped Zero Distribute  Redistributes values in the given list such that: 1. any index with a value larger than 0 is set to 0 2. any index with a value of 0 now has a nonzero value 3. the nonzero is evenly divided among the appropriate indexes

**Parameters:**
- `value_list` &mdash; list of numbers to flip zero distribute


**Returns:**<br>
value_list - flip-zero distributed list of numbers any leftover amount

### def ip_distribute(value_list, amt_list)

In Place Distribute  Distributes values from one list to the other list, based on index. Mismatched list sizes are allowed. There is no concept of leftovers here.

**Parameters:**
- `value_list` &mdash; list of numbers to distribute to
- `amt_list` &mdash; list of amounts to distribute


**Returns:**<br>
value_list - each corresponding index in amt_list added to corresponding index in value_list

### def lo_distribute(value_list, leftovers, reverse=False, nz=False)

LeftOver Distribute Applies leftovers to the given value list.  If leftovers are larger than the value list, we do ev_distribute first

**Parameters:**
- `value_list` &mdash; list of numbers to distribute to
- `leftovers` &mdash; amount of leftover to distribute
- `reverse` &mdash; True will add in reverse order, false will not (Default: False)
- `nz` &mdash; True will only apply leftovers to non-zero values False will not (Default: False)


**Returns:**<br>
value_list - some items will have leftovers added to them

### def randomblob(size, seed=None)

Generates a blob of StringIO data with the given size

**Parameters:**
- `size` &mdash; size in bytes of the blob to make
- `seed` &mdash; seed to use if None, curent time is used (as per random documentation) (Default: None)


**Returns:**<br>
a cStringIO buffer of the random blob

### def randomblob_fast(size)

Generates a randomb blob of stringIO data more efficientally and with true random using urandom

**Parameters:**
- `size` &mdash; size in bytes of the blob to make


**Returns:**<br>
a cStringIO buffer of the random blob

### def intersperse(_list, _sep)

Intersperses a list with the given separator

### def log_entry(entry_log, value)

Generic entry add to the given log. Stores both time and given value as a tuple: [0]: datetime.now() [1]: value

**Parameters:**
- `entry_log` &mdash; list to log entry to
- `value` &mdash; value to log in this entry


### def sanitize_filename(s)

Sanitizes a filename by removing characters that might have special meaning on certain platforms.

**Parameters:**
- `s` &mdash;  String to sanitize.


**Returns:**<br>
str: Sanitized string, stripped of special characters.

