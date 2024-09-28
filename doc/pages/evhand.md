## Functions

### def addIfNew(items, pool)

### def tuplizeEventLabelList(key_list, db)

### def _isFuture(ev, date=None)

INTERNAL Checks if the start_date of the given event happens after the given time.  IN: ev - Event to check the start_time date - a datetime object used to check against If None is passed it will check against current time (Default: None)  RETURNS: True if the Event's start_date is in the future, False otherwise

### def _isPast(ev, date=None)

INTERNAL Checks if the end_date of the given event happens before the given time.  IN: ev - Event to check the start_time date - a datetime object used to check against If None is passed it will check against current time (Default: None)  RETURNS: True if the Event's end_date is in the past, False otherwise

### def _isPresent(ev)

INTERNAL Checks if current date falls within the given event's start/end date range  IN: ev - Event to check the start_time and end_time  RETURNS: True if current time is inside the  Event's start_date/end_date interval, False otherwise

### def _hideEvent(event, lock=False, derandom=False, depool=False, decond=False)

Internalized hideEvent

### def _hideEventLabel(eventlabel, lock=False, derandom=False, depool=False, decond=False, eventdb=event_database)

Internalized hideEventLabel

### def _lockEvent(ev)

Internalized lockEvent

### def _lockEventLabel(evlabel, eventdb=event_database)

Internalized lockEventLabel

### def _unlockEvent(ev)

Internalized unlockEvent

### def _unlockEventLabel(evlabel, eventdb=event_database)

Internalized unlockEventLabel

### def addYearsetBlacklist(evl, expire_dt)

Adds the given evl to the yearset blacklist, with the given expiration dt

**Parameters:**
- `evl` &mdash; event label
- `expire_dt` &mdash; when the evl should be removed from the blacklist


### def cleanYearsetBlacklist()

Goes through the year setblacklist and removes expired entries

### def isYearsetBlacklisted(evl)

Checks if the given evl is yearset blacklisted. Also checks expiration date and removes if needed.

**Parameters:**
- `evl` &mdash; event label


**Returns:**<br>
True if blacklisted, false if not

### def addIfNew(items, pool)

### def tuplizeEventLabelList(key_list, db)

### def _isFuture(ev, date=None)

INTERNAL Checks if the start_date of the given event happens after the given time.  IN: ev - Event to check the start_time date - a datetime object used to check against If None is passed it will check against current time (Default: None)  RETURNS: True if the Event's start_date is in the future, False otherwise

### def _isPast(ev, date=None)

INTERNAL Checks if the end_date of the given event happens before the given time.  IN: ev - Event to check the start_time date - a datetime object used to check against If None is passed it will check against current time (Default: None)  RETURNS: True if the Event's end_date is in the past, False otherwise

### def _isPresent(ev)

INTERNAL Checks if current date falls within the given event's start/end date range  IN: ev - Event to check the start_time and end_time  RETURNS: True if current time is inside the  Event's start_date/end_date interval, False otherwise

### def _hideEvent(event, lock=False, derandom=False, depool=False, decond=False)

Internalized hideEvent

### def _hideEventLabel(eventlabel, lock=False, derandom=False, depool=False, decond=False, eventdb=event_database)

Internalized hideEventLabel

### def _lockEvent(ev)

Internalized lockEvent

### def _lockEventLabel(evlabel, eventdb=event_database)

Internalized lockEventLabel

### def _unlockEvent(ev)

Internalized unlockEvent

### def _unlockEventLabel(evlabel, eventdb=event_database)

Internalized unlockEventLabel

### def addYearsetBlacklist(evl, expire_dt)

Adds the given evl to the yearset blacklist, with the given expiration dt

**Parameters:**
- `evl` &mdash; event label
- `expire_dt` &mdash; when the evl should be removed from the blacklist


### def cleanYearsetBlacklist()

Goes through the year setblacklist and removes expired entries

### def isYearsetBlacklisted(evl)

Checks if the given evl is yearset blacklisted. Also checks expiration date and removes if needed.

**Parameters:**
- `evl` &mdash; event label


**Returns:**<br>
True if blacklisted, false if not

### def actionPush(ev)

Runs Push Event action for the given event

**Parameters:**
- `ev` &mdash; event to push to event stack


### def actionQueue(ev)

Runs Queue event action for the given event

**Parameters:**
- `ev` &mdash; event to queue to event stack


### def actionUnlock(ev)

Unlocks an event. Also setse the unlock_date to the given unlock time

**Parameters:**
- `ev` &mdash; event to unlock
- `unlock_time` &mdash; time to set unlock_date to


### def actionRandom(ev)

Randos an event.

**Parameters:**
- `ev` &mdash; event to random
- `rebuild_ev` &mdash; True if we wish to notify idle to rebuild events


### def actionPool(ev)

Pools an event.

**Parameters:**
- `ev` &mdash; event to pool


### def actionPush(ev)

Runs Push Event action for the given event

**Parameters:**
- `ev` &mdash; event to push to event stack


### def actionQueue(ev)

Runs Queue event action for the given event

**Parameters:**
- `ev` &mdash; event to queue to event stack


### def actionUnlock(ev)

Unlocks an event. Also setse the unlock_date to the given unlock time

**Parameters:**
- `ev` &mdash; event to unlock
- `unlock_time` &mdash; time to set unlock_date to


### def actionRandom(ev)

Randos an event.

**Parameters:**
- `ev` &mdash; event to random
- `rebuild_ev` &mdash; True if we wish to notify idle to rebuild events


### def actionPool(ev)

Pools an event.

**Parameters:**
- `ev` &mdash; event to pool


