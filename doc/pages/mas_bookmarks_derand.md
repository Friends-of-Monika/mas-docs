## Public functions

### def resetDefaultValues()

Resets the globals to their default values

---

### def getLabelPrefix(test_str)

Checks if test_str starts with anything in the list of prefixes, and if so, returns the matching prefix

**Parameters:**
- `test_str` &mdash; string to test


**Returns:**<br>
string: - label_prefix if test_string starts with a prefix in list_prefixes - empty string otherwise

---

### def getDerandomedEVLs()

Gets a list of derandomed eventlabels

**Returns:**<br>
list of derandomed eventlabels

---

### def shouldRandom(eventlabel)

Checks if we should random the given eventlabel This is determined by whether or not the event is in any derandom list

**Returns:**<br>
boolean: True if we should random this event, False otherwise

---

### def wrappedGainAffection(amount=None, modifier=1.0, bypass=False)

Wrapper function for mas_gainAffection which allows it to be used in event rules at init 5  See mas_gainAffection for documentation

---

### def removeDerand(eventlabel)

Removes a derandomed eventlabel from ALL derandom dbs

**Parameters:**
- `eventlabel` &mdash; Eventlabel to remove


---

### def resetDefaultValues()

Resets the globals to their default values

---

### def getLabelPrefix(test_str)

Checks if test_str starts with anything in the list of prefixes, and if so, returns the matching prefix

**Parameters:**
- `test_str` &mdash; string to test


**Returns:**<br>
string: - label_prefix if test_string starts with a prefix in list_prefixes - empty string otherwise

---

### def getDerandomedEVLs()

Gets a list of derandomed eventlabels

**Returns:**<br>
list of derandomed eventlabels

---

### def shouldRandom(eventlabel)

Checks if we should random the given eventlabel This is determined by whether or not the event is in any derandom list

**Returns:**<br>
boolean: True if we should random this event, False otherwise

---

### def wrappedGainAffection(amount=None, modifier=1.0, bypass=False)

Wrapper function for mas_gainAffection which allows it to be used in event rules at init 5  See mas_gainAffection for documentation

---

### def removeDerand(eventlabel)

Removes a derandomed eventlabel from ALL derandom dbs

**Parameters:**
- `eventlabel` &mdash; Eventlabel to remove


---

