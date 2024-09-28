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

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _compareAff(aff_1, aff_2)

See mas_compareAff for explanation

---

### def _compareAffG(affg_1, affg_2)

See mas_compareAffG for explanation

---

### def _betweenAff(aff_low, aff_check, aff_high)

checks if the given affection level is between the given low and high. See mas_betweenAff for explanation

---

### def _isValidAff(aff_check)

Returns true if the given affection is a valid affection state

---

### def _isValidAffRange(aff_range)

Returns True if the given aff range is a valid aff range.

**Parameters:**
- `aff_range` &mdash; tuple of the following format: [0]: lower bound [1]: upper bound


---

### def _m1_script0x2daffection__verify_data()

---

### def _m1_script0x2daffection__set_pers_data(value)

---

### def _m1_script0x2daffection__get_pers_data()

---

### def _m1_script0x2daffection__to_struct()

Packs passed args into a struct

**Returns:**<br>
PY2: str PY3: bytes

---

### def _m1_script0x2daffection__from_struct(struct_)

Upacks passed struct into a tuple of values

**Parameters:**
- `struct_` &mdash; bytes - the struct to unpack


**Returns:**<br>
tuple with values

---

### def _m1_script0x2daffection__hexlify(bytes_)

Converts binary data into a hexadecimal string

---

### def _m1_script0x2daffection__unhexlify(bytes_)

Converts a hexadecimal string into pure binary data

---

### def _m1_script0x2daffection__handle_str2bytes(value)

Verifies we return the expected type, if not, converts it TODO: ME

---

### def _m1_script0x2daffection__intob64(bytes_)

Encodes a string using b64

---

### def _m1_script0x2daffection__fromb64(bytes_)

Decodes an encoded string using b64

---

### def _m1_script0x2daffection__decode_data(data)

Returns decoded data In case the data has been corrupted in a way, returns default values

**Returns:**<br>
- tuple with the data - None if an error happened

---

### def _m1_script0x2daffection__encode_data()

Encodes data If it's unable to encode data, returns None

**Returns:**<br>
- bytes - None if an error happened

---

### def _m1_script0x2daffection__reset_pers_data()

Resets pers data to the default value Dangerous, think twice before using

---

### def _m1_script0x2daffection__get_data()

Returns current data (decoded), ALWAYS use this accessor

**Returns:**<br>
- list with the data - None if an error happened

---

### def _get_aff()

Private getter that handles errors, you should probably use public version

**Returns:**<br>
float - current affection

---

### def _get_today_cap()

Returns today's aff cap

**Returns:**<br>
tuple[float, float] - current aff cap

---

### def _m1_script0x2daffection__validate_timestamp(ts, now_ts)

Verifies the given time against current time

**Parameters:**
- `ts` &mdash; the timestamp to validate
- `now_ts` &mdash; the current time


**Returns:**<br>
float: original timestamp if it's valid or modified timestamp

---

### def _grant_aff(amount, bypass, reason=None)

Grants some affection

**Parameters:**
- `amount` &mdash; float - amount of affection to grant
- `bypass` &mdash; bool - is this bypass gain or not
- `reason` &mdash; str/None - the reason for this bonus, MUST be current topic label or None (Default: None)


---

### def _remove_aff(amount, reason=None)

Removes some affection

**Parameters:**
- `amount` &mdash; float - amount of affection to remove
- `reason` &mdash; str/None - the reason for this lose, MUST be current topic label or None (Default: None)


---

### def _withdraw_aff()

Withdraws some aff daily from the bank to the main pool

---

### def _absence_decay_aff()

Removes some aff during absence

---

### def _reset_aff(reason='RESET')

Resets aff value (and only it) This is a dangerous func, use with care

---

### def _transfer_aff_2nd_gen()

Transfers aff from the first gen to the second gen This may be dangerous, use wisely, don't fook up

---

### def _m1_script0x2daffection__set_aff(amount, reason='SET')

Sets affection to a value

**Parameters:**
- `amount` &mdash; amount to set affection to
- `logmsg` &mdash; msg to show in the log (Default: 'SET')


---

### def _set_aff(value, reason)

---

### def _make_backup(force=False)

Runs backup algo for affection

**Parameters:**
- `force` &mdash; boolean - should we force this?


---

### def _has_mismatch()

Checks if the last backup mismatches with the current aff

---

### def _remove_backups()

Removes all backups

---

### def _restore_backup()

Uses available aff backup Use wisely

**Returns:**<br>
boolean - whether or not a backup was restored

---

### def _compareAff(aff_1, aff_2)

See mas_compareAff for explanation

---

### def _compareAffG(affg_1, affg_2)

See mas_compareAffG for explanation

---

### def _betweenAff(aff_low, aff_check, aff_high)

checks if the given affection level is between the given low and high. See mas_betweenAff for explanation

---

### def _isValidAff(aff_check)

Returns true if the given affection is a valid affection state

---

### def _isValidAffRange(aff_range)

Returns True if the given aff range is a valid aff range.

**Parameters:**
- `aff_range` &mdash; tuple of the following format: [0]: lower bound [1]: upper bound


---

### def _m1_script0x2daffection__verify_data()

---

### def _m1_script0x2daffection__set_pers_data(value)

---

### def _m1_script0x2daffection__get_pers_data()

---

### def _m1_script0x2daffection__to_struct()

Packs passed args into a struct

**Returns:**<br>
PY2: str PY3: bytes

---

### def _m1_script0x2daffection__from_struct(struct_)

Upacks passed struct into a tuple of values

**Parameters:**
- `struct_` &mdash; bytes - the struct to unpack


**Returns:**<br>
tuple with values

---

### def _m1_script0x2daffection__hexlify(bytes_)

Converts binary data into a hexadecimal string

---

### def _m1_script0x2daffection__unhexlify(bytes_)

Converts a hexadecimal string into pure binary data

---

### def _m1_script0x2daffection__handle_str2bytes(value)

Verifies we return the expected type, if not, converts it TODO: ME

---

### def _m1_script0x2daffection__intob64(bytes_)

Encodes a string using b64

---

### def _m1_script0x2daffection__fromb64(bytes_)

Decodes an encoded string using b64

---

### def _m1_script0x2daffection__decode_data(data)

Returns decoded data In case the data has been corrupted in a way, returns default values

**Returns:**<br>
- tuple with the data - None if an error happened

---

### def _m1_script0x2daffection__encode_data()

Encodes data If it's unable to encode data, returns None

**Returns:**<br>
- bytes - None if an error happened

---

### def _m1_script0x2daffection__reset_pers_data()

Resets pers data to the default value Dangerous, think twice before using

---

### def _m1_script0x2daffection__get_data()

Returns current data (decoded), ALWAYS use this accessor

**Returns:**<br>
- list with the data - None if an error happened

---

### def _get_aff()

Private getter that handles errors, you should probably use public version

**Returns:**<br>
float - current affection

---

### def _get_today_cap()

Returns today's aff cap

**Returns:**<br>
tuple[float, float] - current aff cap

---

### def _m1_script0x2daffection__validate_timestamp(ts, now_ts)

Verifies the given time against current time

**Parameters:**
- `ts` &mdash; the timestamp to validate
- `now_ts` &mdash; the current time


**Returns:**<br>
float: original timestamp if it's valid or modified timestamp

---

### def _grant_aff(amount, bypass, reason=None)

Grants some affection

**Parameters:**
- `amount` &mdash; float - amount of affection to grant
- `bypass` &mdash; bool - is this bypass gain or not
- `reason` &mdash; str/None - the reason for this bonus, MUST be current topic label or None (Default: None)


---

### def _remove_aff(amount, reason=None)

Removes some affection

**Parameters:**
- `amount` &mdash; float - amount of affection to remove
- `reason` &mdash; str/None - the reason for this lose, MUST be current topic label or None (Default: None)


---

### def _withdraw_aff()

Withdraws some aff daily from the bank to the main pool

---

### def _absence_decay_aff()

Removes some aff during absence

---

### def _reset_aff(reason='RESET')

Resets aff value (and only it) This is a dangerous func, use with care

---

### def _transfer_aff_2nd_gen()

Transfers aff from the first gen to the second gen This may be dangerous, use wisely, don't fook up

---

### def _m1_script0x2daffection__set_aff(amount, reason='SET')

Sets affection to a value

**Parameters:**
- `amount` &mdash; amount to set affection to
- `logmsg` &mdash; msg to show in the log (Default: 'SET')


---

### def _set_aff(value, reason)

---

### def _make_backup(force=False)

Runs backup algo for affection

**Parameters:**
- `force` &mdash; boolean - should we force this?


---

### def _has_mismatch()

Checks if the last backup mismatches with the current aff

---

### def _remove_backups()

Removes all backups

---

### def _restore_backup()

Uses available aff backup Use wisely

**Returns:**<br>
boolean - whether or not a backup was restored

---

### def _force_exp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

Determines appropriate forced expression for current affection.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def _force_exp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

Determines appropriate forced expression for current affection.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def _brokenToDis()

Runs when transitioning from broken to distressed

---

### def _disToBroken()

Runs when transitioning from distressed to broken

---

### def _disToUpset()

Runs when transitioning from distressed to upset

---

### def _upsetToDis()

Runs when transitioning from upset to distressed

---

### def _upsetToNormal()

Runs when transitioning from upset to normal

---

### def _normalToUpset()

Runs when transitioning from normal to upset

---

### def _normalToHappy()

Runs when transitioning from noraml to happy

---

### def _happyToNormal()

Runs when transitinong from happy to normal

---

### def _happyToAff()

Runs when transitioning from happy to affectionate

---

### def _affToHappy()

Runs when transitioning from affectionate to happy

---

### def _affToEnamored()

Runs when transitioning from affectionate to enamored

---

### def _enamoredToAff()

Runs when transitioning from enamored to affectionate

---

### def _enamoredToLove()

Runs when transitioning from enamored to love

---

### def _loveToEnamored()

Runs when transitioning from love to enamored

---

### def _gSadToNormal()

Runs when transitioning from sad group to normal group

---

### def _gNormalToSad()

Runs when transitioning from normal group to sad group

---

### def _gNormalToHappy()

Runs when transitioning from normal group to happy group

---

### def _gHappyToNormal()

Runs when transitioning from happy group to normal group

---

### def _isMoniState(aff_1, aff_2, lower=False, higher=False)

Compares the given affection values according to the affection state system  By default, this will check if aff_1 == aff_2

**Parameters:**
- `aff_1` &mdash; affection to compare
- `aff_2` &mdash; affection to compare
- `lower` &mdash; True means we want to check aff_1 <= aff_2
- `higher` &mdash; True means we want to check aff_1 >= aff_2


**Returns:**<br>
True if the given affections pass the test we want to do. False otherwise

---

### def _isMoniStateG(affg_1, affg_2, lower=False, higher=False)

Compares the given affection groups according to the affection group system  By default, this will check if affg_1 == affg_2

**Parameters:**
- `affg_1` &mdash; affection group to compare
- `affg_2` &mdash; affection group to compare
- `lower` &mdash; True means we want to check affg_1 <= affg_2
- `higher` &mdash; True means we want to check affg_1 >= affg_2


**Returns:**<br>
true if the given affections pass the test we want to do. False otherwise

---

### def _init_talk_quips()

Initializes the talk quiplists

---

### def _init_play_quips()

Initializes the play quipliust

---

### def _dict_quip(_quips)

Returns a quip based on the current affection using the given quip dict

**Parameters:**
- `_quips` &mdash; quip dict to pull from


**Returns:**<br>
quip or empty string if failure

---

### def _brokenToDis()

Runs when transitioning from broken to distressed

---

### def _disToBroken()

Runs when transitioning from distressed to broken

---

### def _disToUpset()

Runs when transitioning from distressed to upset

---

### def _upsetToDis()

Runs when transitioning from upset to distressed

---

### def _upsetToNormal()

Runs when transitioning from upset to normal

---

### def _normalToUpset()

Runs when transitioning from normal to upset

---

### def _normalToHappy()

Runs when transitioning from noraml to happy

---

### def _happyToNormal()

Runs when transitinong from happy to normal

---

### def _happyToAff()

Runs when transitioning from happy to affectionate

---

### def _affToHappy()

Runs when transitioning from affectionate to happy

---

### def _affToEnamored()

Runs when transitioning from affectionate to enamored

---

### def _enamoredToAff()

Runs when transitioning from enamored to affectionate

---

### def _enamoredToLove()

Runs when transitioning from enamored to love

---

### def _loveToEnamored()

Runs when transitioning from love to enamored

---

### def _gSadToNormal()

Runs when transitioning from sad group to normal group

---

### def _gNormalToSad()

Runs when transitioning from normal group to sad group

---

### def _gNormalToHappy()

Runs when transitioning from normal group to happy group

---

### def _gHappyToNormal()

Runs when transitioning from happy group to normal group

---

### def _isMoniState(aff_1, aff_2, lower=False, higher=False)

Compares the given affection values according to the affection state system  By default, this will check if aff_1 == aff_2

**Parameters:**
- `aff_1` &mdash; affection to compare
- `aff_2` &mdash; affection to compare
- `lower` &mdash; True means we want to check aff_1 <= aff_2
- `higher` &mdash; True means we want to check aff_1 >= aff_2


**Returns:**<br>
True if the given affections pass the test we want to do. False otherwise

---

### def _isMoniStateG(affg_1, affg_2, lower=False, higher=False)

Compares the given affection groups according to the affection group system  By default, this will check if affg_1 == affg_2

**Parameters:**
- `affg_1` &mdash; affection group to compare
- `affg_2` &mdash; affection group to compare
- `lower` &mdash; True means we want to check affg_1 <= affg_2
- `higher` &mdash; True means we want to check affg_1 >= affg_2


**Returns:**<br>
true if the given affections pass the test we want to do. False otherwise

---

### def _init_talk_quips()

Initializes the talk quiplists

---

### def _init_play_quips()

Initializes the play quipliust

---

### def _dict_quip(_quips)

Returns a quip based on the current affection using the given quip dict

**Parameters:**
- `_quips` &mdash; quip dict to pull from


**Returns:**<br>
quip or empty string if failure

---

