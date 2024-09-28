## Functions

### def getZodiacSign(date)

Gets a zodiac sign for a date Idea from https://stackoverflow.com/questions/3274597

**Parameters:**
- `date` &mdash; datetime.date


**Returns:**<br>
string with the sign

### def genFriendlyDispDate(_datetime)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `genFriendlyDispDate_d`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='genFriendlyDispDate_d')`


**Parameters:**
- `_datetime` &mdash; datetime object to create good display date


### def genFriendlyDispDate_d(_date)

Generates a display date using the given date This creates a display date in the format: Month Day, Year However, this is somewhat variable.  If it is the same as the current year, the year is not provided. If the date is whithin a year of the current date, year is not provided. If the year is last year and greater than a year of the current date, "last year on <month> <day>" If the year is within 2-10 years ago, then "x years ago on <month> <day>" is used. Otherwise, the actual 4 digit year is used.  If the days / months are the same, then "x years ago to this date" is used.

**Parameters:**
- `_date` &mdash; date object to create good display date


**Returns:**<br>
tuple of the following format: [0]: nicely formatted display date, suitable for conversation [1]: timedelta between today and the given _date

### def genFormalDispDate(_date)

Generates a display date using the given date  This is considered "formal", in that it's not really realisitc when used in normal conversation. For example, if today is august 24, you don't say 'this happened august 24th, 2016', you normally would say 'this happened x years ago today'.

**Parameters:**
- `_date` &mdash; date object to create good display date


**Returns:**<br>
tuple of the following format: [0]: nicely formtted display date, suitable for text [1]: timedelta between today and the given _date

### def saveCalendarDatabase(encoder)

Saves the passed database as a json file named db.mcal

### def loadCalendarDatabase()

Returns the database read from the file renpy.config.savedir + '/db.mcal' as a dict

**Returns:**<br>
a dict containing the events for the calendar

### def addEvent(ev)

Adds an event to the calendar accoridng to its start_date and end_date properties. If start_date is not set in the given event, this function will do nothing.

**Parameters:**
- `ev` &mdash; event to add


### def addEvent_evd(ev, _date)

Adds an event to the calendar at a preicse date.

**Parameters:**
- `ev` &mdash; event to add
- `_date` &mdash; datetime.date to add to


### def addEvent_evdt(ev, _datetime)

Adds an event to the calendar at a precise datetime.

**Parameters:**
- `ev` &mdash; event to add


### def addRepeatable(identifier, display_label, month, day, year_param)

Adds a repeatable to the calendar at a precise month / day Sanity checks are done for month / day

**Parameters:**
- `identifier` &mdash; label of the event that it's unique
- `display_label` &mdash; label that will be displayed
- `month` &mdash; month to add to
- `day` &mdash; day to add to
- `year_param` &mdash; data to put in the year part of the tuple


### def addRepeatable_d(identifier, display_label, _date, year_param)

Adds a repeatable to the calendar at precise datetime.date

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to add
- `display_label` &mdash; label that will be displayed
- `_date` &mdash; datetime.date to add to
- `year_param` &mdash; data to put in the year part of the tuple


### def addRepeatable_dt(identifier, display_label, _datetime, year_param)

Adds a repeatable to the calendar at a precise datetime

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to add
- `display_label` &mdash; label that will be displayed
- `_datetime` &mdash; datetime to add to
- `year_param` &mdash; data to put in the year part of the tuple


### def removeEvent(ev)

Removes an event from the calendar using it's start_date and end_date properties.

**Parameters:**
- `ev` &mdash; event to remove


### def removeEvent_eld(ev_label, _date)

Removes an event from the calendar at a precise date.

**Parameters:**
- `ev_label` &mdash; eventlabel of the event to remove
- `_date` &mdash; datetime.date we should look at for event removal


### def removeEvent_evd(ev, _date)

Removes an event from the calendar at a precise date.

**Parameters:**
- `ev` &mdash; event to remove
- `_date` &mdash; datetime.date we should look at for event removal


### def removeEvent_eldt(ev_label, _datetime)

Removes an event from the calendar at a precise datetime.

**Parameters:**
- `ev_label` &mdash; eventlabel of the event to remove
- `_datetime` &mdash; datetime we should look at for event removal


### def removeEvent_evdt(ev, _datetime)

Removes and event from the calendar at a precise datetime.

**Parameters:**
- `ev` &mdash; event to remove
- `_datetime` &mdash; datetime.date we should look at for removal


### def removeEvent_el(ev_label, month=None, day=None, remove_all=False)

Removes an event from the calendar.

**Parameters:**
- `ev_label` &mdash; eventlabel of the event to remove
- `month` &mdash; If given (and a valid month), will only check the calendar in the given month. (Default: None)
- `day` &mdash; If given (and a valid day), will only check the calendar for the given day for each month (Default: None)
- `remove_all` &mdash; True means we remove every single occurence of the given eventlabel. False means we only remove the first one we find. (Default: False)


### def removeEvent_ev(ev, month=None, day=None, remove_all=False)

Removes an event from the calendar.  SEE removeEvent_el for important NOTES regarding this function.

**Parameters:**
- `ev` &mdash; event to remove
- `month` &mdash; SEE removeEvent_el
- `day` &mdash; SEE removeEvent_el
- `remove_all` &mdash; SEE removeEvent_el


### def removeRepeatable(identifier, month=None, day=None)

Removes a repeatable from the calendar.

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to remove
- `month` &mdash; If given (and a valid month), will only check the calendar in the given month. (Default: None)
- `day` &mdash; If given (and a valid day), will only check the calendar for the given day for reach month (Default: None)


### def removeRepeatable_d(identifier, _date)

Removes a repeatable from teh calendar at a precise datetime.date

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to remove
- `_date` &mdash; datetime.date we should look at for removal


### def removeRepeatable_dt(identifier, _datetime)

Removes a repeatable from teh calendar at aprecise datetime

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to remove
- `_datetime` &mdash; datetime we should look at for removal


### def getZodiacSign(date)

Gets a zodiac sign for a date Idea from https://stackoverflow.com/questions/3274597

**Parameters:**
- `date` &mdash; datetime.date


**Returns:**<br>
string with the sign

### def genFriendlyDispDate(_datetime)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `genFriendlyDispDate_d`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='genFriendlyDispDate_d')`


**Parameters:**
- `_datetime` &mdash; datetime object to create good display date


### def genFriendlyDispDate_d(_date)

Generates a display date using the given date This creates a display date in the format: Month Day, Year However, this is somewhat variable.  If it is the same as the current year, the year is not provided. If the date is whithin a year of the current date, year is not provided. If the year is last year and greater than a year of the current date, "last year on <month> <day>" If the year is within 2-10 years ago, then "x years ago on <month> <day>" is used. Otherwise, the actual 4 digit year is used.  If the days / months are the same, then "x years ago to this date" is used.

**Parameters:**
- `_date` &mdash; date object to create good display date


**Returns:**<br>
tuple of the following format: [0]: nicely formatted display date, suitable for conversation [1]: timedelta between today and the given _date

### def genFormalDispDate(_date)

Generates a display date using the given date  This is considered "formal", in that it's not really realisitc when used in normal conversation. For example, if today is august 24, you don't say 'this happened august 24th, 2016', you normally would say 'this happened x years ago today'.

**Parameters:**
- `_date` &mdash; date object to create good display date


**Returns:**<br>
tuple of the following format: [0]: nicely formtted display date, suitable for text [1]: timedelta between today and the given _date

### def saveCalendarDatabase(encoder)

Saves the passed database as a json file named db.mcal

### def loadCalendarDatabase()

Returns the database read from the file renpy.config.savedir + '/db.mcal' as a dict

**Returns:**<br>
a dict containing the events for the calendar

### def addEvent(ev)

Adds an event to the calendar accoridng to its start_date and end_date properties. If start_date is not set in the given event, this function will do nothing.

**Parameters:**
- `ev` &mdash; event to add


### def addEvent_evd(ev, _date)

Adds an event to the calendar at a preicse date.

**Parameters:**
- `ev` &mdash; event to add
- `_date` &mdash; datetime.date to add to


### def addEvent_evdt(ev, _datetime)

Adds an event to the calendar at a precise datetime.

**Parameters:**
- `ev` &mdash; event to add


### def addRepeatable(identifier, display_label, month, day, year_param)

Adds a repeatable to the calendar at a precise month / day Sanity checks are done for month / day

**Parameters:**
- `identifier` &mdash; label of the event that it's unique
- `display_label` &mdash; label that will be displayed
- `month` &mdash; month to add to
- `day` &mdash; day to add to
- `year_param` &mdash; data to put in the year part of the tuple


### def addRepeatable_d(identifier, display_label, _date, year_param)

Adds a repeatable to the calendar at precise datetime.date

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to add
- `display_label` &mdash; label that will be displayed
- `_date` &mdash; datetime.date to add to
- `year_param` &mdash; data to put in the year part of the tuple


### def addRepeatable_dt(identifier, display_label, _datetime, year_param)

Adds a repeatable to the calendar at a precise datetime

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to add
- `display_label` &mdash; label that will be displayed
- `_datetime` &mdash; datetime to add to
- `year_param` &mdash; data to put in the year part of the tuple


### def removeEvent(ev)

Removes an event from the calendar using it's start_date and end_date properties.

**Parameters:**
- `ev` &mdash; event to remove


### def removeEvent_eld(ev_label, _date)

Removes an event from the calendar at a precise date.

**Parameters:**
- `ev_label` &mdash; eventlabel of the event to remove
- `_date` &mdash; datetime.date we should look at for event removal


### def removeEvent_evd(ev, _date)

Removes an event from the calendar at a precise date.

**Parameters:**
- `ev` &mdash; event to remove
- `_date` &mdash; datetime.date we should look at for event removal


### def removeEvent_eldt(ev_label, _datetime)

Removes an event from the calendar at a precise datetime.

**Parameters:**
- `ev_label` &mdash; eventlabel of the event to remove
- `_datetime` &mdash; datetime we should look at for event removal


### def removeEvent_evdt(ev, _datetime)

Removes and event from the calendar at a precise datetime.

**Parameters:**
- `ev` &mdash; event to remove
- `_datetime` &mdash; datetime.date we should look at for removal


### def removeEvent_el(ev_label, month=None, day=None, remove_all=False)

Removes an event from the calendar.

**Parameters:**
- `ev_label` &mdash; eventlabel of the event to remove
- `month` &mdash; If given (and a valid month), will only check the calendar in the given month. (Default: None)
- `day` &mdash; If given (and a valid day), will only check the calendar for the given day for each month (Default: None)
- `remove_all` &mdash; True means we remove every single occurence of the given eventlabel. False means we only remove the first one we find. (Default: False)


### def removeEvent_ev(ev, month=None, day=None, remove_all=False)

Removes an event from the calendar.  SEE removeEvent_el for important NOTES regarding this function.

**Parameters:**
- `ev` &mdash; event to remove
- `month` &mdash; SEE removeEvent_el
- `day` &mdash; SEE removeEvent_el
- `remove_all` &mdash; SEE removeEvent_el


### def removeRepeatable(identifier, month=None, day=None)

Removes a repeatable from the calendar.

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to remove
- `month` &mdash; If given (and a valid month), will only check the calendar in the given month. (Default: None)
- `day` &mdash; If given (and a valid day), will only check the calendar for the given day for reach month (Default: None)


### def removeRepeatable_d(identifier, _date)

Removes a repeatable from teh calendar at a precise datetime.date

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to remove
- `_date` &mdash; datetime.date we should look at for removal


### def removeRepeatable_dt(identifier, _datetime)

Removes a repeatable from teh calendar at aprecise datetime

**Parameters:**
- `identifier` &mdash; identifier of the repeatable to remove
- `_datetime` &mdash; datetime we should look at for removal


### def addSeasonEvents()

Adds season change events to the calendar. If the changed param is True it changes the old events.

**Parameters:**
- `changed` &mdash; flag to specify that we need to change the old events from the calendar


### def addSeasonEvents()

Adds season change events to the calendar. If the changed param is True it changes the old events.

**Parameters:**
- `changed` &mdash; flag to specify that we need to change the old events from the calendar


