## Functions

### def addIfNew(items, pool)

### def tuplizeEventLabelList(key_list, db)

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


