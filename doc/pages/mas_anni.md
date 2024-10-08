# store mas_anni

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def build_anni(years=0, months=0, weeks=0, isstart=True)

Builds an anniversary date.

**Parameters:**
- `years` &mdash; number of years to make this anni date
- `months` &mdash; number of months to make thsi anni date
- `weeks` &mdash; number of weeks to make this anni date
- `isstart` &mdash; True means this should be a starting date, False means ending date


---

### def build_anni_end(years=0, months=0, weeks=0)

Variant of build_anni that auto ends the bool  SEE build_anni for params

---

### def isAnni(milestone=None)

**Returns:**<br>
True if datetime.date.today() is an anniversary date False if today is not an anniversary date

---

### def isAnniWeek()

---

### def isAnniOneMonth()

---

### def isAnniThreeMonth()

---

### def isAnniSixMonth()

---

### def isAnniAny()

---

### def anniCount()

**Returns:**<br>
Integer value representing how many years the player has been with Monika

---

### def pastOneWeek()

**Returns:**<br>
True if current date is past the 1 week threshold False if below the 1 week threshold

---

### def pastOneMonth()

**Returns:**<br>
True if current date is past the 1 month threshold False if below the 1 month threshold

---

### def pastThreeMonths()

**Returns:**<br>
True if current date is past the 3 month threshold False if below the 3 month threshold

---

### def pastSixMonths()

**Returns:**<br>
True if current date is past the 6 month threshold False if below the 6 month threshold

---

### def build_anni(years=0, months=0, weeks=0, isstart=True)

Builds an anniversary date.

**Parameters:**
- `years` &mdash; number of years to make this anni date
- `months` &mdash; number of months to make thsi anni date
- `weeks` &mdash; number of weeks to make this anni date
- `isstart` &mdash; True means this should be a starting date, False means ending date


---

### def build_anni_end(years=0, months=0, weeks=0)

Variant of build_anni that auto ends the bool  SEE build_anni for params

---

### def isAnni(milestone=None)

**Returns:**<br>
True if datetime.date.today() is an anniversary date False if today is not an anniversary date

---

### def isAnniWeek()

---

### def isAnniOneMonth()

---

### def isAnniThreeMonth()

---

### def isAnniSixMonth()

---

### def isAnniAny()

---

### def anniCount()

**Returns:**<br>
Integer value representing how many years the player has been with Monika

---

### def pastOneWeek()

**Returns:**<br>
True if current date is past the 1 week threshold False if below the 1 week threshold

---

### def pastOneMonth()

**Returns:**<br>
True if current date is past the 1 month threshold False if below the 1 month threshold

---

### def pastThreeMonths()

**Returns:**<br>
True if current date is past the 3 month threshold False if below the 3 month threshold

---

### def pastSixMonths()

**Returns:**<br>
True if current date is past the 6 month threshold False if below the 6 month threshold

---

### def add_cal_annis()

Goes through the anniversary database and adds them to the calendar

---

### def clean_cal_annis()

Goes through the calendar and cleans anniversary dates

---

### def reset_annis(new_start_dt)

Reset the anniversaries according to the new start date.

**Parameters:**
- `new_start_dt` &mdash; new start datetime to reset anniversaries


---

### def unlock_past_annis()

Goes through the anniversary database and unlocks the events that already past.

---

### def add_cal_annis()

Goes through the anniversary database and adds them to the calendar

---

### def clean_cal_annis()

Goes through the calendar and cleans anniversary dates

---

### def reset_annis(new_start_dt)

Reset the anniversaries according to the new start date.

**Parameters:**
- `new_start_dt` &mdash; new start datetime to reset anniversaries


---

### def unlock_past_annis()

Goes through the anniversary database and unlocks the events that already past.

---

