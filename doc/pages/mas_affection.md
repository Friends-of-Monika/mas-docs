# store mas_affection

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def get_default_data()

Returns default encoded data for aff when first loading the mod

**Returns:**<br>
bytes

---

### def save_aff()

Runs saving logic

---

### def load_aff()

Runs loading logic

---

### def get_default_data()

Returns default encoded data for aff when first loading the mod

**Returns:**<br>
bytes

---

### def save_aff()

Runs saving logic

---

### def load_aff()

Runs loading logic

---

### def audit(attempted_change, change, old, new, frozen=False, bypass=False, ldsv=None)

Audits a change in affection.

**Parameters:**
- `attempted_change` &mdash; the attempted aff change
- `change` &mdash; the amount we are changing by
- `old` &mdash; the old value of affection
- `new` &mdash; what the new affection value will be
- `frozen` &mdash; True means we were frozen, false measn we are not
- `bypass` &mdash; True means we bypassed, false means we did not
- `ldsv` &mdash; Set to the string to use instead of monikatopic NOTE: for load / save operations ONLY


---

### def raw_audit(old, new, change, tag)

Non affection-dependent auditing for general usage.

**Parameters:**
- `old` &mdash; the "old" value
- `new` &mdash; the "new" value
- `change` &mdash; the chnage amount
- `tag` &mdash; a string to label this audit change


---

### def txt_audit(tag, msg)

Generic auditing in the aff log

**Parameters:**
- `tag` &mdash; a string to label thsi audit
- `msg` &mdash; message to show


---

### def audit(attempted_change, change, old, new, frozen=False, bypass=False, ldsv=None)

Audits a change in affection.

**Parameters:**
- `attempted_change` &mdash; the attempted aff change
- `change` &mdash; the amount we are changing by
- `old` &mdash; the old value of affection
- `new` &mdash; what the new affection value will be
- `frozen` &mdash; True means we were frozen, false measn we are not
- `bypass` &mdash; True means we bypassed, false means we did not
- `ldsv` &mdash; Set to the string to use instead of monikatopic NOTE: for load / save operations ONLY


---

### def raw_audit(old, new, change, tag)

Non affection-dependent auditing for general usage.

**Parameters:**
- `old` &mdash; the "old" value
- `new` &mdash; the "new" value
- `change` &mdash; the chnage amount
- `tag` &mdash; a string to label this audit change


---

### def txt_audit(tag, msg)

Generic auditing in the aff log

**Parameters:**
- `tag` &mdash; a string to label thsi audit
- `msg` &mdash; message to show


---

### def runAffPPs(start_aff, end_aff)

Runs programming points to transition from the starting affection to the ending affection

**Parameters:**
- `start_aff` &mdash; starting affection
- `end_aff` &mdash; ending affection


---

### def runAffGPPs(start_affg, end_affg)

Runs programming points to transition from the starting affection group to the ending affection group

**Parameters:**
- `start_affg` &mdash; starting affection group
- `end_affg` &mdash; ending affection group


---

### def talk_quip()

Returns a talk quip based on the current affection

---

### def play_quip()

Returns a play quip based on the current affection

---

### def runAffPPs(start_aff, end_aff)

Runs programming points to transition from the starting affection to the ending affection

**Parameters:**
- `start_aff` &mdash; starting affection
- `end_aff` &mdash; ending affection


---

### def runAffGPPs(start_affg, end_affg)

Runs programming points to transition from the starting affection group to the ending affection group

**Parameters:**
- `start_affg` &mdash; starting affection group
- `end_affg` &mdash; ending affection group


---

### def talk_quip()

Returns a talk quip based on the current affection

---

### def play_quip()

Returns a play quip based on the current affection

---

