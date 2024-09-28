# store store

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def mas_override_label(label_to_override, override_label)

Label override function

**Parameters:**
- `label_to_override` &mdash; the label which will be overridden
- `override_label` &mdash; the label to override with


---

### def mas_getSessionLength()

Gets length of current session, IF this cannot be determined, a time delta of 0 is returned

---

### def mas_getAbsenceLength()

Gets time diff between current session start and last session end aka the diff between last session and this if not found, time delta of 0 is returned

---

### def mas_getCurrSeshStart()

Returns the current session start datetime If there is None, we use first session

---

### def mas_getFirstSesh()

Returns the first session datetime.  If we could not get it, datetime.datetime.now() is returnd

---

### def mas_isFirstSeshPast(_date)

Checks if the first session is past the given date

**Parameters:**
- `_date` &mdash; datetime.date to check against


**Returns:**<br>
boolean: - True if first sesh is past given date - False otherwise

---

### def mas_getLastSeshEnd()

Returns datetime of the last session

---

### def mas_getTotalPlaytime()

Gets total playtime.

**Returns:**<br>
total playtime as a timedelta. If not found, we return a time delta of 0

---

### def mas_getTotalSessions()

Gets total sessions  REUTRNS: total number of sessions. If not found, we return 1

---

### def mas_TTDetected()

Checks if time travel was detected

---

### def mas_getWindowTitle()

Returns current windows title set by RenPy

**Returns:**<br>
str

---

### def mas_getAPIKey(feature)

gets the API key for a feature

**Parameters:**
- `feature` &mdash; the string name of the feature to lookup.


**Returns:**<br>
the api key, as a string. Will be null string if no key found

---

### def mas_hasAPIKey(feature)

Checks if a feature has an API key

**Parameters:**
- `feature` &mdash; string name of the feature to check


**Returns:**<br>
true if the feature has an API key, false otherwise

---

### def mas_registerAPIKey(feature, display_name, on_change=None)

Registers a feature that accepts an API key. Features are NOT registered if they already exist.  Can run a function when the api key is changed. This function should return a tuple: [0] - True if the key is valid, False if not [1] - optional error message to show The return value is primarily for setting a key. If no return value is provided, the key is assumed valid. The API key is passed in as the first param. The key will be a null string if the key is being cleared.

**Parameters:**
- `feature` &mdash; the string name of the feature to lookup
- `display_name` &mdash; the display name the feature should use on screen
- `on_change` &mdash; function to run when the API key is changed.


**Returns:**<br>
True if the feature was added, False if not.

---

### def mas_cleanBadUpdateFiles()

Moves any file with the '.new' extension to the correct file

---

### def mas_removeDelayedAction(_id)

Removes a delayed action with the given ID

**Parameters:**
- `_id` &mdash; id of the delayed action to remove


---

### def mas_removeDelayedActions_list(_ids)

Removes a list of delayed actions with given Ids

**Parameters:**
- `_ids` &mdash; list of Ids to remove


---

### def mas_removeDelayedActions()

Multiple argument delayed action removal  Assumes all given args are IDS

---

### def mas_runDelayedActions(flow)

Attempts to run currently held delayed actions for the given flow mode  Delayed actions that are successfully completed are removed from the list

**Parameters:**
- `flow` &mdash; FC constant for the current flow


---

### def mas_addDelayedAction(_id)

Creates a delayed action with the given ID and adds it to the delayed action map (runtime)

**Parameters:**
- `_id` &mdash; id of the delayed action to create


---

### def mas_addDelayedActions_list(_ids)

Creates delayed actions given a list of Ids

**Parameters:**
- `_ids` &mdash; list of IDS to add


---

### def mas_addDelayedActions()

Creates delayed actions given ids as args  assumes each arg is a valid id

---

### def mas_HistLookup(key, year)

Looks up data in the historical archives.

**Parameters:**
- `key` &mdash; data key to look up
- `year` &mdash; year to look up data


**Returns:**<br>
a tuple of the following format: [0]: mas_history lookup constant [1]: retrieved data (which may be None). This is always None if we could not find year or key

---

### def mas_HistLookup_all(key)

Looks up all historical data for a specific key.

**Parameters:**
- `key` &mdash; data key to look up


**Returns:**<br>
dictionary of the following format: year: data tuple from mas_HistLookup

---

### def mas_HistLookup_k(year)

Looks up data in the historical archives

**Parameters:**
- `year` &mdash; year to look up data
- `keys` &mdash; string pieces of a key to search for


**Returns:**<br>
same as mas_HistLookup

---

### def mas_HistLookup_ot(key)

Looks up data overtime in the historical archives.

**Parameters:**
- `key` &mdash; data key to look up
- `years` &mdash; years to look updata


**Returns:**<br>
dict of the following format: year: data tuple from mas_HistLookup

---

### def mas_HistLookup_otl(key, years_list)

Looks up data overtime in the historical archives.

**Parameters:**
- `key` &mdash; data key to look up
- `years_list` &mdash; list of years to lookup data


**Returns:**<br>
dict of the following format: year: data tuple from mas_HistLookup

---

### def mas_HistLookup_otl_k(years_list)

Looks up data overtime in the historical archives

**Parameters:**
- `years_list` &mdash; list of years to lookup data


**Returns:**<br>
See mas_HistLookup_otl

---

### def mas_HistVerify(key, _verify)

Verifies if data at the given key matches the verification value.

**Parameters:**
- `key` &mdash; data key to lookup
- `_verify` &mdash; the data we want to match to
- `years` &mdash; years to look up data (as args) Dont pass in anything if you want to lookup all years since 2017


**Returns:**<br>
tuple of the following format: [0]: true/False if we found data that matched the verification [1]: list of years that matched the verification

---

### def mas_HistVerify_k(years_list, _verify)

Verifies if data at the given key matches the verification value.

**Parameters:**
- `years_list` &mdash; list of years to look up data (as args) Pass an empty list if you want to lookup all years since 2017.
- `_verify` &mdash; the data we want to match to


**Returns:**<br>
see mas_HistVerify

---

### def mas_HistWasFirstValueIn(_verify, year)

Checks if the first year that _verify was found for the keys provided in history matches the year provided

**Parameters:**
- `_verify` &mdash; Value to check for
- `year` &mdash; year to match


**Returns:**<br>
boolean: - True if the first year matches the year provided - False otherwise

---

### def mas_HistGetFirstYearOfValue(_verify)

Gets the first year which has the entry of _verify in the keys provided

**Parameters:**
- `_verify` &mdash; value to check for


**Returns:**<br>
If there's a point where the value we're checking for is found, we return the first year that is met. If not found, we return None

---

### def mas_HistVerifyAll_k(_verify)

Checks if the value of _verify for the keys is in history at any point

**Parameters:**
- `_verify` &mdash; value to check for


**Returns:**<br>
boolean: - True if _verify is in the key built by the provided pieces at all - False otherwise

---

### def mas_HistVerifyLastYear_k(_verify)

Checks history for the value of _verify in the key provided last year

**Parameters:**
- `_verify` &mdash; value to check for


**Returns:**<br>
boolean: - True if _verify is in the key built by the provided pieces last year - False otherwise

---

### def mas_d25SeasonExit_PP(mhs)

Sets a flag to run the D25 exit PP

---

### def is_file_present(filename)

DEPRECIATED  Use mas_utils.is_file_present instead

---

### def dev_mas_unlock_all_sprites()

---

### def dev_mas_clear_spritegift(giftname)

---

### def mas_isCurrentFlt(flt)

Checks if the given filter is the current filter.

**Parameters:**
- `flt` &mdash; filter to check


**Returns:**<br>
True if flt is the current filter, false if not

---

### def MASWeather(weather_id, prompt, sp_day, sp_night=None, precip_type=store.mas_weather.PRECIP_TYPE_DEF, isbg_wf_day=None, isbg_wof_day=None, isbg_wf_night=None, isbg_wof_night=None, entry_pp=None, exit_pp=None, unlocked=False)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `MASFilterableWeather`.

DEPRECATED Old-style MASWeather objects. This is mapped to a MASFilterableWeather with day/night filter settings

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='MASFilterableWeather')`


**Parameters:**
- `weather_id` &mdash; id that defines this weather object NOTE: must be unique
- `prompt` &mdash; button label for this weathe robject
- `sp_day` &mdash; image tag for spaceroom's left window in daytime
- `sp_night` &mdash; image tag for spaceroom's left window in night (Default: None)
- `precip_type` &mdash; type of precipitation, def, rain, overcast, or snow (Default: def)
- `isbg_wf_day` &mdash; ignored
- `isbg_wof_day` &mdash; ignored
- `isbg_wf_night` &mdash; ignored
- `isbg_wof_night` &mdash; ignored
- `entry_pp` &mdash; programming point to execute after switching to this weather (Default: None)
- `exit_pp` &mdash; programming point to execute before leaving this weather (Default: None)
- `unlocked` &mdash; True if this weather object starts unlocked, False otherwise (Default: False)


**Returns:**<br>
MASFitlerableWeather object

---

### def mas_showDecoTag(tag, show_now=False)

Shows a decoration object that is an image tag.

**Parameters:**
- `tag` &mdash; the image tag to show
- `show_now` &mdash; set to True to show immediately (Deafult: False)


---

### def mas_hideDecoTag(tag, hide_now=False)

Hides a decoration object that is an image tag

**Parameters:**
- `tag` &mdash; the image tag to hide
- `hide_now` &mdash; set to True to hide immediately (Default: False)


---

### def mas_isDecoTagEnabled(tag)

Checks if the given deco tag is in the vis store, which means its slated to be visible if it can be.

**Parameters:**
- `tag` &mdash; the image tag to check


**Returns:**<br>
True if the deco is slated to be visible, False if not

---

### def mas_isDecoTagVisible(tag)

Checks if this deco is showing - as in the image associated with this tag is being rendered (including replace tag depending on bg)

**Parameters:**
- `tag` &mdash; the image tag to check


**Returns:**<br>
True if the deco is being shown, false if not

---

### def mas_player_bday_curr(_date=None)

sets date of current year bday, accounting for leap years

---

### def mas_isA01(_date=None)

---

### def mas_isO31(_date=None)

Returns True if the given date is o31

**Parameters:**
- `_date` &mdash; date to check. If None, we use today's date (Default: None)


**Returns:**<br>
True if given date is o31, False otherwise

---

### def mas_o31ShowVisuals()

Shows o31 visuals

---

### def mas_o31HideVisuals()

Hides o31 visuals + vignette

---

### def mas_o31ShowSpriteObjects()

Shows o31 specific sprite objects

---

### def mas_o31HideSpriteObjects()

Hides o31 specific sprite objects

---

### def mas_hasO31DeskAcs()

Checks if we have any o31 desk acs

**Returns:**<br>
boolean

---

### def mas_o31HideDeskAcs()

Removes o31 desk acs

---

### def mas_o31CapGainAff(amount)

CapGainAffection function for o31. See mas_capGainAff for details

---

### def mas_o31CostumeWorn(clothes)

Checks if the given clothes was worn on o31

**Parameters:**
- `clothes` &mdash; Clothes object to check


**Returns:**<br>
year the given clothe was worn if worn on o31, None if never worn on o31.

---

### def mas_o31CostumeWorn_n(clothes_name)

Checks if the given clothes (name) was worn on o31

**Parameters:**
- `clothes_name` &mdash; Clothes name to check


**Returns:**<br>
year the given clothes name was worn if worn on o31, none if never worn on o31.

---

### def mas_o31SelectCostume(selection_pool=None)

Selects an o31 costume to wear. Costumes that have not been worn before are selected first.

**Parameters:**
- `selection_pool` &mdash; pool to select clothes from. If NOne, we get a default list of clothes with costume exprop


**Returns:**<br>
a single MASClothes object of what to wear. None if cannot return anything.

---

### def mas_o31SetCostumeWorn(clothes, year=None)

Sets that a clothing item is worn. Exprop checking is done

**Parameters:**
- `clothes` &mdash; clothes object to set
- `year` &mdash; year that the costume was worn. If NOne, we use current year


---

### def mas_o31SetCostumeWorn_n(clothes_name, year=None)

Sets that a clothing name is worn. NO EXPROP CHECKING IS DONE

**Parameters:**
- `clothes_name` &mdash; name of clothes to set
- `year` &mdash; year that the costume was worn. If None, we use current year


---

### def mas_o31Cleanup()

Cleanup function for o31

---

### def mas_isD25(_date=None)

Returns True if the given date is d25

**Parameters:**
- `_date` &mdash; date to check If None, we use today's date (default: None)


**Returns:**<br>
True if given date is d25, False otherwise

---

### def mas_isD25Eve(_date=None)

Returns True if the given date is d25 eve

**Parameters:**
- `_date` &mdash; date to check If None, we use today's date (Default: None)


**Returns:**<br>
True if given date is d25 eve, False otherwise

---

### def mas_isD25Season(_date=None)

Returns True if the given date is in d25 season. The season goes from dec 11 to jan 5.

**Parameters:**
- `_date` &mdash; date to check If None, we use today's date (Default: None)


**Returns:**<br>
True if given date is in d25 season, False otherwise

---

### def mas_isD25Post(_date=None)

Returns True if the given date is after d25 but still in D25 season. The season goes from dec 1 to jan 5.

**Parameters:**
- `_date` &mdash; date to check If None, we use today's date (Default: None)


**Returns:**<br>
True if given date is in d25 season but after d25, False otherwise.

---

### def mas_isD25PreNYE(_date=None)

Returns True if the given date is in d25 season and before nye.

**Parameters:**
- `_date` &mdash; date to check if None, we use today's date (Default: None)


---

### def mas_isD25PostNYD(_date=None)

Returns True if the given date is in d25 season and after nyd

**Parameters:**
- `_date` &mdash; date to check If None, we use today's date (Default: None)


**Returns:**<br>
True if given date is in d25 season but after nyd, False otherwise

---

### def mas_isD25Outfit(_date=None)

Returns True if the given date is tn the range of days where Monika wears the santa outfit on start.

**Parameters:**
- `_date` &mdash; date to check if None, we use today's date (Default: None)


**Returns:**<br>
True if given date is in the d25 santa outfit range, False otherwise

---

### def mas_isD25Pre(_date=None)

**Parameters:**
- `_date` &mdash; date to check if None, we use today's date (Default: None)


**Returns:**<br>
True if given date is in the D25 season, but before Christmas, False otherwise

---

### def mas_isD25GiftHold(_date=None)

**Parameters:**
- `_date` &mdash; date to check, defaults None, which means today's date is assumed


**Returns:**<br>
boolean - True if within d25c start, to d31 (end of nts range) (The time to hold onto gifts, aka not silently react)

---

### def mas_d25ShowVisuals()

Shows d25 visuals.

---

### def mas_d25HideVisuals()

Hides d25 visuals

---

### def mas_d25ReactToGifts()

Goes thru the gifts stored from the d25 gift season and reacts to them  this also registeres gifts

---

### def mas_d25SilentReactToGifts()

Method to silently 'react' to gifts.  This is to be used if you gave Moni a christmas gift but didn't show up on D25 when she would have opened them in front of you.  This also registeres gifts

---

### def mas_isNYE(_date=None)

Returns True if the given date is new years eve

**Parameters:**
- `_date` &mdash; date to check If None, we use today's date (Default: None)


**Returns:**<br>
True if given date is new years eve, False otherwise

---

### def mas_isNYD(_date=None)

**Parameters:**
- `_date` &mdash; date to check if None, we use today's date (Default: None)


**Returns:**<br>
True if the given date is new years day True if given date is new years day, False otherwise

---

### def mas_isplayer_bday(_date=None, use_date_year=False)

**Parameters:**
- `_date` &mdash; date to check If None, we use today's date (default: None)
- `use_date_year` &mdash; True if we should use the year from _date or not. (Default: False)


**Returns:**<br>
True if given date is player_bday, False otherwise

---

### def strip_mas_birthdate()

strips mas_birthdate of its conditional and action to prevent double birthday sets

---

### def mas_pbdayCapGainAff(amount)

---

### def mas_isF14(_date=None)

---

### def mas_f14CapGainAff(amount)

---

### def getCharacterImage(char, expression='1a')

---

### def mas_getPropFromStyle(style_name, prop_name)

Retrieves a property from a style Recursively checks parent styles until the property is found.

**Parameters:**
- `style_name` &mdash; name of style as string
- `prop_name` &mdash; property to find as string


**Returns:**<br>
value of the propery if we can find it, None if not found

---

### def mas_prefixFrame(frm, prefix)

Generates a frame object with the given prefix substitued into the image. This effectively makes a copy of the given Frame object.

**Parameters:**
- `frm` &mdash; Frame object
- `prefix` &mdash; prefix to replace `prefix_`. "_" will be added if not found


**Returns:**<br>
Frame object, or None if failed to make it

---

### def MASBackground(background_id, prompt, image_day, image_night, image_rain_day=None, image_rain_night=None, image_overcast_day=None, image_overcast_night=None, image_snow_day=None, image_snow_night=None, hide_calendar=False, hide_masks=False, disable_progressive=None, unlocked=False, entry_pp=None, exit_pp=None)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `MASFilterableBackground`.

DEPRECATED Old-style MASBackground objects. This is mapped to a MASFilterableBackground with default (aka pre0.11.3 filters) slice management

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='MASFilterableBackground')`


**Parameters:**
- `background_id` &mdash;  id that defines the background object NOTE: Must be unique
- `prompt` &mdash;  button label for this bg
- `image_day` &mdash;  the renpy.image object we use for this bg during the day NOTE: Mandatory
- `image_night` &mdash;  the renpy.image object we use for this bg during the night NOTE: Mandatory
- `image_rain_day` &mdash;  the image tag we use for the background while it's raining (day) (Default: None, not required)
- `image_rain_night` &mdash;  the image tag we use for the background while it's raining (night) (Default: None, not required)
- `image_overcast_day` &mdash;  the image tag we use for the background while it's overcast (day) (Default: None, not required)
- `image_overcast_night` &mdash;  the image tag we use for the background while it's overcast (night) (Default: None, not required)
- `image_snow_day` &mdash;  the image tag we use for the background while it's snowing (day) (Default: None, not required)
- `image_snow_night` &mdash;  the image tag we use for the background while it's snowing (night) (Default: None, not required)
- `hide_calendar` &mdash;  whether or not we want to display the calendar (Default: False)
- `hide_masks` &mdash;  weather or not we want to show the windows (Default: False)
- `disable_progressive` &mdash;  weather or not we want to disable progressive weather (Default: None, if hide masks is true and this is not provided, we assume True, otherwise False)
- `unlocked` &mdash;  whether or not this background starts unlocked (Default: False)
- `entry_pp` &mdash;  Entry programming point for the background (Default: None)
- `exit_pp` &mdash;  Exit programming point for this background (Default: None)


**Returns:**<br>
MASFilterableBackground object

---

### def glitchWord(word, odds_space=ODDS_SPACE, odds_other=ODDS_OTHER)

---

### def mas_drawmonika(st, at, character, eyebrows, eyes, nose, mouth, lean=None, arms='steepling', eyebags=None, sweat=None, blush=None, tears=None, emote=None, head='', left='', right='', stock=True, single=None)

DEPRECATED This function has been gutted and only draws standing

**Parameters:**
- `st` &mdash; renpy related
- `at` &mdash; renpy related
- `character` &mdash; MASMonika character object
- `eyebrows` &mdash; type of eyebrows (sitting)
- `eyes` &mdash; type of eyes (sitting)
- `nose` &mdash; type of nose (sitting)
- `mouth` &mdash; type of mouth (sitting)
- `head` &mdash; type of head (standing)
- `left` &mdash; type of left side (standing)
- `right` &mdash; type of right side (standing)
- `lean` &mdash; type of lean (sitting) (Default: None)
- `arms` &mdash; type of arms (sitting) (Default: "steepling")
- `eyebags` &mdash; type of eyebags (sitting) (Default: None)
- `sweat` &mdash; type of sweatdrop (sitting) (Default: None)
- `blush` &mdash; type of blush (sitting) (Default: None)
- `tears` &mdash; type of tears (sitting) (Default: None)
- `emote` &mdash; type of emote (sitting) (Default: None)
- `stock` &mdash; True means we are using stock standing, False means not (standing) (Default: True)
- `single` &mdash; type of single standing image (standing) (Default: None)


---

### def mas_fwm_select(st, at, mfwm)

Selects an image based on current filter and weather.

**Parameters:**
- `st` &mdash; renpy related
- `at` &mdash; renpy related
- `mfwm` &mdash; MASFilterWeatherMap to select image wtih


**Returns:**<br>
dynamic disp output

---

### def mas_fbf_select(st, at, mfmfb)

Selects an image based on current filter, respecting fallback mechanics.

**Parameters:**
- `st` &mdash; renpy related
- `at` &mdash; renpy related
- `mfmfb` &mdash; MASFilterMapFallback object to select image with


**Returns:**<br>
dynamic disp output

---

### def mas_drawmonika_rk(st, at, character, eyebrows, eyes, nose, mouth, lean=None, arms='steepling', eyebags=None, sweat=None, blush=None, tears=None, emote=None, head='a', left='1l', right='1r', stock=True, single=None)

Draws monika dynamically, using render keys See mas_drawmonika for more info.

**Parameters:**
- `st` &mdash; renpy related
- `at` &mdash; renpy related
- `character` &mdash; MASMonika character object
- `eyebrows` &mdash; type of eyebrows (sitting)
- `eyes` &mdash; type of eyes (sitting)
- `nose` &mdash; type of nose (sitting)
- `mouth` &mdash; type of mouth (sitting)
- `head` &mdash; type of head (standing)
- `left` &mdash; type of left side (standing)
- `right` &mdash; type of right side (standing)
- `lean` &mdash; type of lean (sitting) (Default: None)
- `arms` &mdash; type of arms (sitting) (Default: "steepling")
- `eyebags` &mdash; type of eyebags (sitting) (Default: None)
- `sweat` &mdash; type of sweatdrop (sitting) (Default: None)
- `blush` &mdash; type of blush (sitting) (Default: None)
- `tears` &mdash; type of tears (sitting) (Default: None)
- `emote` &mdash; type of emote (sitting) (Default: None)
- `stock` &mdash; True means we are using stock standing, False means not (standing) (Default: True)
- `single` &mdash; type of single standing image (standing) (Default: None)


---

### def mas_drawemptydesk_rk(st, at, character)

draws the table dynamically. includes ACS that should stay on desk.

**Parameters:**
- `st` &mdash; renpy related
- `at` &mdash; renpy realted
- `character` &mdash; MASMonika character object


---

### def mas_checkOverDate(_date)

Checks if the player was gone over the given date entirely (taking you somewhere)

**Parameters:**
- `date` &mdash; a datetime.date of the date we want to see if we've been out all day for


**Returns:**<br>
True if the player and Monika were out together the whole day, False if not.

---

### def mas_capGainAff(amount, aff_gained_var, normal_cap, pbday_cap=None)

Gains affection according to the cap(s) defined

**Parameters:**
- `amount` &mdash;  Amount of affection to gain
- `aff_gained_var` &mdash;  The persistent variable which the total amount gained for the holiday is stored (NOTE: Must be a string)
- `normal_cap` &mdash;  The cap to use when not player bday
- `pbday_cap` &mdash;  The cap to use when it's player bday (NOTE: if not provided, normal_cap is assumed)


---

### def mas_hasSpecialOutfit(_date=None)

Checks if the given date is a special event that has an outfit in the event clothes map

**Parameters:**
- `_date` &mdash; date to check. (Default: None)


**Returns:**<br>
True if given date has a special outfit, False otherwise

---

### def mas_isMonikaBirthday(_date=None)

checks if the given date is monikas birthday Comparison is done solely with month and day

**Parameters:**
- `_date` &mdash; date to check. If not passed in, we use today.


---

### def mas_isMonikaBirthday_dt(_datetime=None, extend_by=0)

checks if the given date is monikas birthday. Takes hours beyond the date into account via the `extend_by` param.

**Parameters:**
- `_datetime` &mdash; datetime to check. If not passed in, we use now.
- `extend_by` &mdash; hours we want to extend past 922 defaults to 0


---

### def mas_getNextMonikaBirthday()

---

### def mas_recognizedBday(_date=None)

Checks if the user recognized monika's birthday at all.

**Returns:**<br>
True if the user recoginzed monika's birthday, False otherwise

---

### def mas_surpriseBdayShowVisuals(cake=False)

Shows bday surprise party visuals

---

### def mas_surpriseBdayHideVisuals(cake=False)

Hides all visuals for surprise party

---

### def mas_confirmedParty()

Checks if the player has confirmed the party

---

### def mas_mbdayCapGainAff(amount)

---

### def RigMouse()

---

### def FileActionMod(name, page=None)

---

### def get_procs()

Retrieves list of processes running right now!  Only works for windows atm

**Returns:**<br>
list of running processes, or an empty list if we couldn't do that

---

### def is_running(proc_list)

Checks if a process in the given list is currently running.

**Returns:**<br>
True if a proccess in proc_list is running, False otherwise

---

### def is_apology_present()

Checks if the 'imsorry' file is in the characters folder.

**Returns:**<br>
True is apology is present, False otherwise

---

### def mas_cvToHM(mins)

Converts the given minutes into hour / minutes

**Parameters:**
- `mins` &mdash; number of minutes


**Returns:**<br>
tuple of the following format: [0] - hours [1] - minutes

---

### def mas_isSTtoAny(_time, _suntime, _hour, _min)

Checks if the given time is within this range: _suntime <= _time < (_hour, _min)

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_suntime` &mdash; suntime to use for lower bound NOTE: suntimes are given in minutes
- `_hour` &mdash; hour to use for upper bound
- `_min` &mdash; minute to use for upper bound


**Returns:**<br>
True if the given time is within bounds of the given suntime and given hour / mins, False otherwise

---

### def mas_isSRtoAny(_time, _hour, _min=0)

Checks if the given time is within Sunrise time to the given _hour and _minute

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for upper bound
- `_min` &mdash; minute to use for upper bound (Default: 0)


**Returns:**<br>
True if the given time is whithin bounds of sunrise and the given hour / mins, False otherwise

---

### def mas_isSStoAny(_time, _hour, _min=0)

Checks if the given time is within sunset to the given _hour and minute

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for upper bound
- `_min` &mdash; minute to use for upper bound (Default: 0)


**Returns:**<br>
True if the given time is within bounds of sunset and the given hour/min, False otherwise

---

### def mas_isMNtoAny(_time, _hour, _min=0)

Checks if the given time is within midnight to the given hour/min.

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for upper bound
- `_min` &mdash; minute to use for upper bound (Default: 0)


**Returns:**<br>
True if the given time is within bounds of midnight and the given hour/min, False otherwise

---

### def mas_isNtoAny(_time, _hour, _min=0)

Checks if the given time is within noon to the given hour/min.

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for upper bound
- `_min` &mdash; minute to use for upper bound (Default: 0)


**Returns:**<br>
True if the given time is within bounds of noon and the given hour /min, False otherwise

---

### def mas_isAnytoST(_time, _hour, _min, _suntime)

Checks if the given time is within this range: (_hour, _min) <= _time < _suntime

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for lower bound
- `_min` &mdash; minute to use for lower bound
- `_suntime` &mdash; suntime to use for upper bound NOTE: suntimes are given in minutes


**Returns:**<br>
True if the given time is within bounds of the given hour / mins and the given suntime, false Otherwise

---

### def mas_isAnytoSR(_time, _hour, _min=0)

Checks if the given time is within a given hour and minute to sunrise time

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for lower bound
- `_min` &mdash; minute to use for lower bound (Default: 0)


**Returns:**<br>
True if the given time is within the bounds of the given hour/min and sunrise, False otherwise

---

### def mas_isAnytoSS(_time, _hour, _min=0)

Checks if the given time is within a given hour/min to sunset time

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for lower bound
- `_min` &mdash; minute to use for lower bound (Default: 0)


**Returns:**<br>
True if the given time is within the bounds of the given hour/min and sunset, False otherwise

---

### def mas_isAnytoMN(_time, _hour, _min=0)

Checks if the given time is within a given hour/min to midnight (next day)

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for lower bound
- `_min` &mdash; mintue to use for lower bound (DEfault: 0)


**Returns:**<br>
True if the given time is within the bounds of the given hour/min and midnight, False otherwise

---

### def mas_isAnytoN(_time, _hour, _min=0)

Checks if the given time is within a given hour/min to noon.

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object
- `_hour` &mdash; hour to use for lower bound
- `_min` &mdash; minute to use for lower bound (Default: 0)


**Returns:**<br>
True if the given tim eis within the bounds of the given hour/min and Noon, False otherwise

---

### def mas_isMNtoSR(_time)

Checks if the given time is within midnight to sunrise

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object


**Returns:**<br>
True if the given time is within midnight to sunrise

---

### def mas_isSRtoN(_time)

Checks if the given time is within sunrise to noon

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object


**Returns:**<br>
True if the given time is witin sunrise to noon

---

### def mas_isNtoSS(_time)

Checks if the given time is within noon to sunset

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object


**Returns:**<br>
True if the given time is within noon to sunset

---

### def mas_isSStoMN(_time)

Checks if the given time is within sunset to midnight

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object


**Returns:**<br>
True if the given time is within sunset to midnight

---

### def mas_isSunny(_time)

DEPRECATED Use mas_isDay instead

---

### def mas_isDay(_time)

Checks if the sun would be up during the given time

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object


**Returns:**<br>
True if it is day time during the given time

---

### def mas_isDayNow()

Checks if the sun would be up right now

**Returns:**<br>
True if the sun would be up now, False if not

---

### def mas_isNight(_time)

Checks if the sun is down during the given time

**Parameters:**
- `_time` &mdash; current time to check NOTE: datetime.time object


**Returns:**<br>
True if it the sun is down during the given time

---

### def mas_isNightNow()

Checks if the sun is down right now

**Returns:**<br>
True if it is night now, False if not

---

### def mas_cvToDHM(mins)

Converts the given minutes into a displayable hour / minutes HH:MM

**Parameters:**
- `mins` &mdash; number of minutes


**Returns:**<br>
string time perfect for displaying

---

### def mas_genDateRange(_start, _end)

Generates a list of datetime.date objects with the given range.

**Parameters:**
- `_start` &mdash; starting date of range
- `_end` &mdash; ending date of range


**Returns:**<br>
list of datetime.date objects between the _start and _end, exclusive. May be empty if invalid start and end dates are given

---

### def mas_EVgenYDT(_start, _end, for_start)

Creates a valid start or end datetime for Event creation, given the start and end datetimes.

**Parameters:**
- `_start` &mdash; datetime that begins this period
- `_end` &mdash; datetime that ends this period
- `for_start` &mdash; True if we want the next valid starting datetime False if we want the next valid ending datetime


**Returns:**<br>
valid datetime for Event creation

---

### def mas_EVgenYD(_start, _end, for_start, _time=datetime.time.min)

Variation of mas_EVgenYDT that accepts datetime.dates. This still returns datetimes though.

**Parameters:**
- `_start` &mdash; date that begins this period
- `_end` &mdash; date that ends this period
- `for_start` &mdash; True if we want the next valid starting datetime False if we want the next valid ending datetime
- `_time` &mdash; time to use with the dates. (Default: datetime.time.min)


**Returns:**<br>
valid datetime for Event creation

---

### def mas_isSpecialDay()

Checks if today is a special day(birthday, anniversary or holiday)

**Returns:**<br>
boolean indicating if today is a special day.

---

### def mas_maxPlaytime()

---

### def mas_isInDateRange(subject, _start, _end, start_inclusive=True, end_inclusive=False)

Checks if the given subject date is within  range of the given start end dates.

**Parameters:**
- `subject` &mdash; subject date to compare
- `_start` &mdash; starting date of the range
- `_end` &mdash; ending date of the range
- `start_inclusive` &mdash; True if start date should be inclusive (Derfault: True)
- `end_inclusive` &mdash; True if end date should be inclusive (Default: False)


**Returns:**<br>
True if the given subject is within date range, False if not

---

### def get_pos(channel='music')

Gets the current position in what's playing on the provided channel

**Parameters:**
- `channel` &mdash; The channel to get the sound position for (Default: 'music')


---

### def delete_all_saves()

Deletes all saved states

---

### def mas_delete_all_chrs()

Deletes all chr files under /characters/ folder. Any encountered errors will be printed to log.

---

### def pause(time=None)

Pauses for the given amount of time

**Parameters:**
- `time` &mdash; The time to pause for. If None, a pause until the user progresses is assumed (Default: None)


---

### def enumerate_steam()

Gets installed steam application IDs from the main steam install directory

**Returns:**<br>
List of application IDs

---

### def mas_isSpring(_date=None)

Checks if given date is during spring iff none passed in, then we assume today  Note: If persistent._mas_pm_live_north_hemisphere is none, we assume northern hemi

**Returns:**<br>
boolean showing whether or not it's spring right now

---

### def mas_isSummer(_date=None)

Checks if given date is during summer iff none passed in, then we assume today  Note: If persistent._mas_pm_live_north_hemisphere is none, we assume northern hemi

**Returns:**<br>
boolean showing whether or not it's summer right now

---

### def mas_isFall(_date=None)

Checks if given date is during fall iff none passed in, then we assume today  Note: If persistent._mas_pm_live_north_hemisphere is none, we assume northern hemi

**Returns:**<br>
boolean showing whether or not it's fall right now

---

### def mas_isWinter(_date=None)

Checks if given date is during winter iff none passed in, then we assume today  Note: If persistent._mas_pm_live_north_hemisphere is none, we assume northern hemi

**Returns:**<br>
boolean showing whether or not it's winter right now

---

### def clearUpdateStructs()

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `mas_versions.clear`.

DEPRECATED Use mas_versions.clear instead

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_versions.clear', should_raise=True)`


---

### def mas_SELisUnlocked(_sprite_item)

Checks if the given sprite item is unlocked

**Parameters:**
- `_sprite_item` &mdash; sprite object to check


**Returns:**<br>
True if the given sprite item is unlocked, false otherwise

---

### def mas_filterUnlockGroup(sp_type, group, unlock_min=None, allow_lock=False)

Unlock selector topic for the given group if appropriate number of selector objects are unlocked.

**Parameters:**
- `sp_type` &mdash; sprite type to filter on
- `group` &mdash; group to use for filtering selectors
- `unlock_min` &mdash; minimum number that has to be unlocked for us to unock the selector topic. IF None, then we use the amount provided by the PROMPT_MAP (Default: None)
- `allow_lock` &mdash; True will lock the selector topic if it fails to be unlocked. (Default: False)


---

### def mas_hasUnlockedClothesWithExprop(exprop, value=None)

Checks if we have unlocked clothes with a specific exprop

**Parameters:**
- `exprop` &mdash; exprop to look for
- `value` &mdash; value the exprop should be. Set to None to ignore.


**Returns:**<br>
boolean: True if we have unlocked clothes with the exprop + value provided False otherwise

---

### def mas_hasLockedClothesWithExprop(exprop, value=None)

Checks if we have locked clothes with a specific exprop

**Parameters:**
- `exprop` &mdash; exprop to look for
- `value` &mdash; value the exprop should be. Set to None to ignore.


**Returns:**<br>
boolean: True if we have locked clothes with the exprop + value provided False otherwise

---

### def remove_seen_labels(pool)

---

### def mas_randomSelectAndRemove(sel_list)

Randomly selects an element from the given list This also removes the element from that list.

**Parameters:**
- `sel_list` &mdash; list to select from


**Returns:**<br>
selected element

---

### def mas_randomSelectAndPush(sel_list)

Randomly selects an element from the the given list and pushes the event This also removes the element from that list.

**Parameters:**
- `sel_list` &mdash; list to select from


---

### def mas_insertSort(sort_list, item, key)

Performs a round of insertion sort. This does least to greatest sorting

**Parameters:**
- `sort_list` &mdash; list to insert + sort
- `item` &mdash; item to sort and insert
- `key` &mdash; function to call using the given item to retrieve sort key


**Returns:**<br>
sort_list - list with 1 additonal element, sorted

---

### def mas_splitSeenEvents(sorted_seen)

Splits the seen_list into seena nd most seen

**Parameters:**
- `sorted_seen` &mdash; list of seen events, sorted by shown_count


**Returns:**<br>
tuple of thef ollowing format: [0] - seen list of events [1] - most seen list of events

---

### def mas_splitRandomEvents(events_dict)

Splits the given random events dict into 2 lists of events

**Returns:**<br>
tuple of the following format: [0] - unseen list of events [1] - seen list of events, sorted by shown_count

---

### def mas_buildEventLists()

Builds the unseen / most seen / seen event lists

**Returns:**<br>
tuple of the following format: [0] - unseen list of events [1] - seen list of events [2] - most seen list of events

---

### def mas_buildSeenEventLists()

Builds the seen / most seen event lists

**Returns:**<br>
tuple of the following format: [0] - seen list of events [1] - most seen list of events

---

### def mas_rebuildEventLists()

Rebuilds the unseen, seen and most seen event lists.

---

### def mas_enableMouseTracking()

---

### def mas_disableMouseTracking()

---

### def mas_isMouseTrackingVisible()

---

### def mas_calDropOverlayShield()

RUNTIME ONLY Enables input for the calendar overlay

---

### def mas_calHideOverlay()

RUNTIME ONLY Hides the calendar overlay

---

### def mas_calIsVisible_ovl()

**Returns:**<br>
True if the calendar ovelray is visible, False otherwise

---

### def mas_calRaiseOverlayShield()

RUNTIME ONLY Disables input for the calendar overlay

---

### def mas_calShowOverlay()

RUNTIME ONLY Shows the calendar overlay

---

### def mas_isLeapYear(year)

Checks if the given year is a leap year, accounting for the error

**Parameters:**
- `year` &mdash; int, year to check


**Returns:**<br>
bool - Whether or not the given year is a leap year

---

### def grant_xp(experience)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `None`.

DEPRECATED This does not do anything anymore. Around for compatibility purposes

**Decorators:**
- `@store.mas_utils.deprecated(should_raise=True)`


---

### def get_level()

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `None`.

DEPRECATED This does not do anything anymore. Around for compatibility purposes

**Decorators:**
- `@store.mas_utils.deprecated(should_raise=True)`


---

### def mas_FreezeGoodAffExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def mas_FreezeBadAffExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def mas_FreezeBothAffExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def mas_UnfreezeBadAffExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def mas_UnfreezeGoodAffExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def mas_UnfreezeBothExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def mas_isBelowZero()

Checks if affection is negative

**Returns:**<br>
boolean

---

### def mas_betweenAff(aff_low, aff_check, aff_high)

Checks if the given affection is between the given affection levels.  If low is actually greater than high, then False is always returned

**Parameters:**
- `aff_low` &mdash; the lower bound of affecton to check with (inclusive) if None, then we assume no lower bound
- `aff_check` &mdash; the affection to check
- `aff_high` &mdash; the upper bound of affection to check with (inclusive) If None, then we assume no upper bound


**Returns:**<br>
True if the given aff check is within the bounds of the given lower and upper affection limits, False otherwise. If low is greater than high, False is returned.

---

### def mas_compareAff(aff_1, aff_2)

Runs compareTo logic on the given affection states

**Parameters:**
- `aff_1` &mdash; an affection state to compare
- `aff_2` &mdash; an affection state to compare


**Returns:**<br>
negative number if aff_1 < aff_2 0 if aff_1 == aff_2 postitive number if aff_1 > aff_2 Returns 0 if a non affection state was provided

---

### def mas_compareAffG(affg_1, affg_2)

Runs compareTo logic on the given affection groups

**Parameters:**
- `affg_1` &mdash; an affection group to compare
- `affg_2` &mdash; an affection group to compare


**Returns:**<br>
negative number if affg_1 < affg_2 0 if affg_1 == affg_2 positive numbre if affg_1 > affg_2 Returns 0 if a non affection group was provided

---

### def mas_isMoniBroken(lower=False, higher=False)

Checks if monika is broken

**Parameters:**
- `lower` &mdash; True means we include everything below this affection state as broken as well (Default: False)
- `higher` &mdash; True means we include everything above this affection state as broken as well (Default: False)


**Returns:**<br>
True if monika is broke, False otherwise

---

### def mas_isMoniDis(lower=False, higher=False)

Checks if monika is distressed

**Parameters:**
- `lower` &mdash; True means we cinlude everything below this affection state as distressed as well NOTE: takes precedence over higher (Default: False)
- `higher` &mdash; True means we include everything above this affection state as distressed as well (Default: FAlse)


**Returns:**<br>
True if monika is distressed, false otherwise

---

### def mas_isMoniUpset(lower=False, higher=False)

Checks if monika is upset

**Parameters:**
- `lower` &mdash; True means we include everything below this affection state as upset as well (Default: False)
- `higher` &mdash; True means we include everything above this affection state as upset as well (Default: False)


**Returns:**<br>
True if monika is upset, false otherwise

---

### def mas_isMoniNormal(lower=False, higher=False)

Checks if monika is normal

**Parameters:**
- `lower` &mdash; True means we include everything below this affection state as normal as well (Default: False)
- `higher` &mdash; True means we include evreything above this affection state as normal as well (Default: False)


**Returns:**<br>
True if monika is normal, false otherwise

---

### def mas_isMoniHappy(lower=False, higher=False)

Checks if monika is happy

**Parameters:**
- `lower` &mdash; True means we include everything below this affection state as happy as well (Default: False)
- `higher` &mdash; True means we include everything above this affection state as happy as well (Default: False)


**Returns:**<br>
True if monika is happy, false otherwise

---

### def mas_isMoniAff(lower=False, higher=False)

Checks if monika is affectionate

**Parameters:**
- `lower` &mdash; True means we include everything below this affection state as affectionate as well (Default: FAlse)
- `higher` &mdash; True means we include everything above this affection state as affectionate as well (Default: False)


**Returns:**<br>
True if monika is affectionate, false otherwise

---

### def mas_isMoniEnamored(lower=False, higher=False)

Checks if monika is enamored

**Parameters:**
- `lower` &mdash; True means we include everything below this affection state as enamored as well (Default: False)
- `higher` &mdash; True means we include everything above this affection state as enamored as well (Default: False)


**Returns:**<br>
True if monika is enamored, false otherwise

---

### def mas_isMoniLove(lower=False, higher=False)

Checks if monika is in love

**Parameters:**
- `lower` &mdash; True means we include everything below this affectionate state as love as well (Default: False)
- `higher` &mdash; True means we include everything above this affection state as love as well (Default: False)


**Returns:**<br>
True if monika in love, false otherwise

---

### def mas_isMoniGSad(lower=False, higher=False)

Checks if monika is in sad affection group

**Parameters:**
- `lower` &mdash; True means we include everything below this affection group as sad as well (Default: False)
- `higher` &mdash; True means we include everything above this affection group as sad as well (Default: False)


**Returns:**<br>
True if monika in sad group, false otherwise

---

### def mas_isMoniGNormal(lower=False, higher=False)

Checks if monika is in normal affection group

**Parameters:**
- `lower` &mdash; True means we include everything below this affection group as normal as well (Default: False)
- `higher` &mdash; True means we include everything above this affection group as normal as well (Default: False)


**Returns:**<br>
True if monika is in normal group, false otherwise

---

### def mas_isMoniGHappy(lower=False, higher=False)

Checks if monika is in happy affection group

**Parameters:**
- `lower` &mdash; True means we include everything below this affection group as happy as well (Default: False)
- `higher` &mdash; True means we include everything above this affection group as happy as well (Default: FAlse)


**Returns:**<br>
True if monika is in happy group, false otherwise

---

### def mas_updateAffectionExp(skipPP=False)

---

### def mas_gainAffection(amount=None, modifier=1.0, bypass=False, current_evlabel=None)

Grants some affection whenever something positive happens

**Parameters:**
- `amount` &mdash; float, None - amount of affection to grant, If None, uses the default value for the current aff (Default: None)
- `modifier` &mdash; float - modifier for the amount value (Default: 1.0)
- `bypass` &mdash; bool - whether or not we should bypass the cap, for example during special events (Default: False)
- `current_evlabel` &mdash; str/None - the topic that caused this aff gain, MUST be current topic label or None. You probably DO NOT want to use this (Default: None)


---

### def mas_loseAffection(amount=None, modifier=1.0, reason=None, ev_label=None, apology_active_expiry=datetime.timedelta(hours=3), apology_overall_expiry=datetime.timedelta(weeks=1), current_evlabel=None)

Subtracts some affection whenever something negative happens  A reason can be specified and used for the apology dialogue if the default value is used Monika won't comment on the reason, and slightly will recover affection if None is passed she won't acknowledge that there was need for an apology. DEFAULTS reason to an Empty String mostly because when this one is called is intended to be used for something the player can apologize for, but it's not totally necessary. NEW BITS: prompt: the prompt shown in the menu for apologizing expirydatetime: generic: do we want this to be persistent? or not

**Parameters:**
- `amount` &mdash; float, None - amount of affection to subtract, If None, uses the default value for the current aff (Default: None)
- `modifier` &mdash; float - modifier for the amount value (Default: 1.0)
- `reason` &mdash; int, None, - a constant for the reason for the apology See mas_setApologyReason (Default: None)
- `ev_label` &mdash; string, None - the label for the apology event See mas_setApologyReason (Default: None)
- `apology_active_expiry` &mdash; datetime.timedelta - the amount of session time for the apology to expire (Default: 3 hours)
- `apology_overall_expiry` &mdash; datetime.timedelta - the amount of overall time for the apology to expire (Default: 1 week)
- `current_evlabel` &mdash; str/None - the topic that caused this aff gain, MUST be current topic label or None. You probably DO NOT want to use this (Default: None)


---

### def mas_loseAffectionFraction(fraction=None, min_amount=None, modifier=1.0, reason=None, ev_label=None, apology_active_expiry=datetime.timedelta(hours=3), apology_overall_expiry=datetime.timedelta(weeks=1), current_evlabel=None)

See mas_loseAffection for more info Subtracts portion of affection whenever something negative happens USE VERY WISELY

**Parameters:**
- `fraction` &mdash; float, None - portion of affection to subtracts, If None, uses the default value for the current aff (Default: None)
- `min_amount` &mdash; float, None - minimal amount of affection to substruct, allows to verify that you take at least this amount, but no more than the provided fraction If None, uses the default value for the current aff (Default: None)
- `modifier` &mdash; float - modifier for the amount value NOTE: the modifier is being applied AFTER min_amount (Default: 1.0)


---

### def mas_setAffection()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@store.mas_utils.deprecated()`


---

### def mas_setApologyReason(reason=None, ev_label=None, apology_active_expiry=datetime.timedelta(hours=3), apology_overall_expiry=datetime.timedelta(weeks=1))

Sets a reason for apologizing

**Parameters:**
- `reason` &mdash; The reason for the apology (integer value corresponding to item in the apology_reason_db) (if left None, and an ev_label is present, we assume a non-generic apology)
- `ev_label` &mdash; The apology event we want to unlock (required)
- `apology_active_expiry` &mdash; The amount of session time after which, the apology that was added expires defaults to 3 hours active time
- `apology_overall_expiry` &mdash; The amount of overall time after which, the apology that was added expires defaults to 7 days


---

### def mas_checkAffection()

---

### def mas_cute_message()

---

### def mas_surprise()

Leaves a "surprise" to the player in a txt file

---

### def mas_unlockSurprisePoem(aff_level)

Unlocks a MASPoem for the given aff level

---

### def addReaction(ev_label, fname_list, _action=EV_ACT_QUEUE, is_good=None, exclude_on=[])

Globalied version of the addReaction function in the mas_filereacts store.  Refer to that function for more information

---

### def mas_checkReactions()

Checks for reactions, then queues them

---

### def mas_receivedGift(ev_label)

Globalied version for gift stats tracking

---

### def mas_generateGiftsReport(date=None)

Globalied version for gift stats tracking

---

### def mas_getGiftStatsForDate(label, date=None)

Globalied version to get the stats for a specific gift

**Parameters:**
- `label` &mdash; the gift label identifier.
- `date` &mdash; the date to get the stats for, if None is given will check today's date. (Defaults to None)


**Returns:**<br>
The number of times the gift has been given that date

---

### def mas_getGiftStatsRange(start, end)

Returns status of gifts over a range (needs to be supplied to actually be useful)

**Parameters:**
- `start` &mdash; a start date to check from
- `end` &mdash; an end date to check to


**Returns:**<br>
The gift status of all gifts given over the range

---

### def mas_getSpriteObjInfo(sp_data=None)

Returns sprite info from the sprite reactions list.

**Parameters:**
- `sp_data` &mdash; tuple of the following format: [0] - sprite type [1] - sprite name If None, we use pseudo random select from sprite reacts (Default: None)


---

### def mas_finishSpriteObjInfo(sprite_data, unlock_sel=True)

Finishes the sprite object with the given data.

**Parameters:**
- `sprite_data` &mdash; sprite data tuple from getSpriteObjInfo
- `unlock_sel` &mdash; True will unlock the selector topic, False will not (Default: True)


---

### def mas_giftCapGainAff(amount=None, modifier=1)

---

### def mas_getGiftedDates(giftlabel)

Gets the dates that a gift was gifted

**Parameters:**
- `giftlabel` &mdash; gift reaction label to check when it was last gifted


**Returns:**<br>
list of datetime.dates of the times the gift was given

---

### def mas_lastGiftedInYear(giftlabel, _year)

Checks if the gift for giftlabel was last gifted in _year

**Parameters:**
- `giftlabel` &mdash; gift reaction label to check it's last gifted year
- `_year` &mdash; year to see if it was last gifted in this year


**Returns:**<br>
boolean: - True if last gifted in _year - False otherwise

---

### def dec_musicvol()

Decreases the volume of the music channel by the value defined in songs.vol_bump

---

### def inc_musicvol()

increases the volume of the music channel by the value defined in songs.vol_bump

---

### def mute_music(mute_enabled=True)

Mutes and unmutes the music channel

**Parameters:**
- `mute_enabled` &mdash; True means we are allowed to mute. False means we are not


---

### def mas_play_song(song, fadein=0.0, loop=True, set_per=False, fadeout=0.0, if_changed=False)

literally just plays a song onto the music channel Also sets the currentt track

**Parameters:**
- `song` &mdash; Song to play. If None, the channel is stopped
- `fadein` &mdash; Number of seconds to fade the song in (Default: 0.0)
- `loop` &mdash; True if we should loop the song if possible, False to not loop. (Default: True)
- `set_per` &mdash; True if we should set persistent track, False if not (Default: False)
- `fadeout` &mdash; Number of seconds to fade the song out (Default: 0.0)
- `if_changed` &mdash; Whether or not to only set the song if it's changing (Use to play the same song again without it being restarted) (Default: False)


---

### def play_song()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `mas_play_song`.

**Decorators:**
- `@mas_utils.deprecated(use_instead='mas_play_song')`


---

### def mas_startup_song()

Starts playing either the persistent track  Meant for usage in startup processes.

---

### def select_music()

---

### def mas_resetQuitMsg()

Resets quit messages to the ones appropriate for the current affection.

---

### def mas_setQuitMsg(quit_msg=None, quit_yes=None, quit_no=None)

Sets text for the quit dialogue box

**Parameters:**
- `quit_msg` &mdash; text to show as the quit dialogue box message. Not set if None. (Default: None)
- `quit_yes` &mdash; text to show when YES is clicked in the quit dialogue box. Not set if None. (Default: None)
- `quit_no` &mdash; text to show when NO is clicked in the quit dialogue box. Not set if None. (Default: None)


---

### def dumpPersistentToFile(dumped_persistent, dumppath)

Prints a file containing each dictionary element of a persistent variable

**Parameters:**
- `dumped_persistent` &mdash; a renpy persistent variable
- `dumppath` &mdash; a file path to the text file to be created. Must be a valid write location


---

### def show_dialogue_box()

Jumps to the topic promt menu

---

### def pick_game()

Jumps to the pick a game workflow

---

### def mas_getuser()

Attempts to get the current user

**Returns:**<br>
current user if found, or None if not found

---

### def mas_enable_quitbox()

Enables Monika's quit dialogue warning

---

### def mas_disable_quitbox()

Disables Monika's quit dialogue warning

---

### def mas_enable_quit()

Enables quitting without monika knowing

---

### def mas_disable_quit()

Disables quitting without monika knowing

---

### def mas_drawSpaceroomMasks(dissolve_masks=True)

Draws the appropriate masks according to the current state of the game.

**Parameters:**
- `dissolve_masks` &mdash; True will dissolve masks, False will not (Default; True)


---

### def mas_validate_suntimes()

Validates both persistent and store suntimes are in a valid state. Sunrise is always used as the lead if a reset is needed.

---

### def show_calendar()

RUNTIME ONLY Opens the calendar if we can

---

### def slow_nodismiss(event, interact=True)

Callback for whenever monika talks

**Parameters:**
- `event` &mdash; main thing we can use here, lets us now when in the pipeline we are for display text:
- `begin` &mdash; > start of a say statement
- `show` &mdash; > right before dialogue is shown
- `show_done` &mdash; > right after dialogue is shown
- `slow_done` &mdash; > called after text finishes showing
- `end` &mdash; > end of dialogue (user has interacted) NOTE: dismiss needs to be possible for end to be reached when mouse is clicked after an interaction ends.


---

### def mas_isMorning()

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `mas_isDayNow`.

DEPRECATED Checks if it is day or night via suntimes

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_isDayNow', should_raise=True)`


**Returns:**<br>
True if day, false if not

---

### def mas_progressFilter()

Changes filter according to rules.  Call this when you want to update the filter.

**Returns:**<br>
True upon a filter change, False if not

---

### def mas_shouldChangeTime()

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `None`.

DEPRECATED This no longer makes sense with the filtering system.

**Decorators:**
- `@store.mas_utils.deprecated(should_raise=True)`


---

### def mas_shouldRain()

Rolls some chances to see if we should make it rain

**Returns:**<br>
rain weather to use, or None if we dont want to change weather

---

### def mas_lockHair()

Locks all hair topics

---

### def mas_seasonalCheck()

Determines the current season and runs an appropriate programming point.  If the global for season is currently None, then we instead set the current season.

---

### def mas_enableTextSpeed()

Enables text speed

---

### def mas_disableTextSpeed()

Disables text speed

---

### def mas_resetTextSpeed(ignoredev=False)

Sets text speed to the appropriate one depending on global settings  Rules: 1 - developer always gets text speed (unless ignoredev is True) 2 - text speed enabled if affection above happy 3 - text speed disabled otherwise

---

### def mas_isTextSpeedEnabled()

Returns true if text speed is enabled

---

### def mas_check_player_derand()

Checks the player derandom lists for events that are not random and derandoms them

---

### def mas_get_player_bookmarks(bookmarked_evls)

Gets topics which are bookmarked by the player Also cleans events which no longer exist

**Parameters:**
- `bookmarked_evls` &mdash; appropriate persistent variable holding the bookmarked eventlabels


**Returns:**<br>
List of bookmarked topics as evs

---

### def mas_get_player_derandoms(derandomed_evls)

Gets topics which are derandomed by the player (in check-scrollable-menu format) Also cleans out events which no longer exist

**Parameters:**
- `derandomed_evls` &mdash; appropriate variable holding the derandomed eventlabels


**Returns:**<br>
List of player derandomed topics in mas_check_scrollable_menu form

---

### def mas_safeToRefDokis()

Checks if it is safe for us to reference the dokis in a potentially sensitive matter. The user must have responded to the question regarding dokis - if the user hasn't responded, then we assume it is NEVER safe to reference dokis.

**Returns:**<br>
True if safe to reference dokis

---

### def mas_set_pronouns(key=None)

Sets gender specific word replacements  Few examples: "It is his pen." (if the player's gender is declared as male) "It is her pen." (if the player's gender is declared as female) "It is their pen." (if player's gender is not declared)  For all available pronouns/words check the keys in MAS_PRONOUN_GENDER_MAP

**Parameters:**
- `key` &mdash; Optional[Literal["M", "F", "X"]] - key (perhaps current gender) to set the pronouns for If None, uses persistent.gender


---

### def mas_getTimeFile(filestring)

Returns the filestring pointing to the right asset for day/night

**Returns:**<br>
filestring pointing to the right path

---

### def mas_swapStyle(base_name, dark_name, morning_flag)

Swaps the single style between default and dark variants.

**Parameters:**
- `morning_flag` &mdash; Light/dark mode switch


---

### def mas_hasDarkStyle(style_name)

Check if selected style has a dark alternative.

---

### def mas_isDarkStyle(style_name)

Check if selected style is a dark style.

---

### def mas_isTextDarkStyle(style_name)

Check if selected style is a text_dark style.

---

### def mas_darkMode(morning_flag=False)

Swaps all styles to dark/light mode provided on the input

**Parameters:**
- `morning_flag` &mdash; if True, light mode, if False, dark mode


---

### def mas_passedILY(pass_time)

Checks whether we are within the appropriate time since the last time Monika told the player 'ily' which is stored in persistent._mas_last_monika_ily

**Parameters:**
- `pass_time` &mdash; a timedelta corresponding to the time limit we want to check against


**Returns:**<br>
boolean indicating if we are within the time limit

---

### def mas_ILY(set_time=None)

Sets persistent._mas_last_monika_ily (the last time Monika said ily) to a given time

**Parameters:**
- `set_time` &mdash; the time we want to set persistent._mas_last_monika_ily to defaults to datetime.datetime.now()


---

### def mas_shouldKiss(chance, cooldown=datetime.timedelta(hours=1), special_day_bypass=False)

Checks if Monika should give the player a random kiss  CONDITIONS: 1. Enamored+ affection 2. Player already had their first kiss with Monika 3. Random chance that changes depending on the chance and special_day_bypass vars 4. Enough time has passed since the last kiss

**Parameters:**
- `chance` &mdash;  the chance to receive a kiss from Monika
- `cooldown` &mdash;  a datetime.timedelta representing the amount of time after the last kiss the next random kiss will be allowed (Default: 1 hour)
- `special_day_bypass` &mdash;  whether a special day should bypass the chance (Default=False)


**Returns:**<br>
boolean: - True if the above conditions are met - False otherwise

---

### def mas_open_extra_menu()

Jumps to the extra menu workflow

---

### def zoom_smoothly(trans, st, at)

Transition function used in mas_smooth_transition takes the standard parameters on functions used on transforms see https://www.renpy.org/doc/html/atl.html#function-statement

---

### def mas_checkApologies()

---

### def removeTopicID(topicID)

Removes one topic from the _seen_ever variable topics list if it exists in either var (persistent is also checked for existence)

**Parameters:**
- `topicID` &mdash; the topicID to remove


---

### def mas_eraseTopic(topicID, per_eventDB=persistent.event_database)

Erases an event from both lockdb and Event database This should also handle lockdb data as well. TopicIDs that are not in the given eventDB are silently ignored. (LockDB data will be erased if found)

**Parameters:**
- `topicID` &mdash; topic ID / label
- `per_eventDB` &mdash; persistent database this topic is in


---

### def mas_transferTopic(old_topicID, new_topicID, per_eventDB)

DEPREACTED  NOTE: This can cause data corruption. DO NOT USE.  Transfers a topic's data from the old topic ID to the new one int he given database as well as the lock database.  NOTE: If the new topic ID already exists in the given databases, the data is OVERWRITTEN  IN: old_topicID - old topic ID to transfer new_topicID - new topic ID to receieve per_eventDB - persistent databse this topic is in

---

### def mas_transferTopicSeen(old_topicID, new_topicID)

Tranfers persistent seen ever data. This is separate because of complex topic adjustments

**Parameters:**
- `old_topicID` &mdash; old topic ID to tranfer
- `new_topicID` &mdash; new topic ID to receieve


---

### def adjustTopicIDs(changedIDs, updating_persistent=persistent)

Changes labels in persistent._seen_ever to new IDs in the changedIDs dict

**Parameters:**
- `oldList` &mdash; the list of old Ids to change
- `changedIDs` &mdash; dict of changed ids:
- `key` &mdash; > old ID
- `value` &mdash; > new ID


---

### def updateTopicIDs(version_number, updating_persistent=persistent)

Updates topic IDS between versions by performing a two step process: adjust exisitng IDS to match the new IDS then add newIDs to the persistent randomtopics

**Parameters:**
- `version_number` &mdash; the version number we are updating to


---

### def updateGameFrom(startVers)

Updates the game, starting at the given start version

**Parameters:**
- `startVers` &mdash; the version number in the parsed format ('v#####')


---

### def safeDel(varname)

Safely deletes variables from persistent

**Parameters:**
- `varname` &mdash; name of the variable to delete from persistent as string


---

### def mas_DropShield_core()

Enables: - Talk button + hotkey - Extra button + hotkey - Music button + hotkey + volume keys + mute key - Play button + hotkey - Calendar overlay - Escape key

---

### def mas_RaiseShield_core()

Disables: - Talk button + hotkey - Extra button + hotkey - Music button + hotkey + volume keys + mute key - Play button + hotkey - Calendar overlay - Escape key

---

### def mas_DropShield_dlg()

Enables: - Talk button + hotkey - Extra button + hotkey - Play button + hotkey - Calendar overlay  Disables: - Derandom hotkey - bookmark hotkey  Unsets: - dialogue workflow flag  Intended Flow: - Monika stops talking

---

### def mas_RaiseShield_dlg()

Disables: - Talk button + hotkey - Extra button + hotkey - Play button + hotkey - Calendar overlay  Enables: - Derandom hotkey - bookmark hotkey  Sets: - dialogue workflow flag  Intended Flow: - Monika starts talking

---

### def mas_DropShield_mumu()

Enables: - Talk button + hotkey - Extra button + hotkey - Music button - Play button + hotkey - Calendar overlay  Intended Flow: - The Music menu is closed

---

### def mas_RaiseShield_mumu()

Disables: - Talk button + hotkey - Extra button + hotkey - Music button - Play button + hotkey - Calendar overlay  Intended Flow: - The Music menu is opened

---

### def mas_DropShield_idle()

Enables: - Talk hotkey - Extra hotkey - Music hotkey - Play button + hotkey - Music controller hotkeys  Intended Flow: - Idle mode ends

---

### def mas_RaiseShield_idle()

Disables: - Talk hotkey - Extra hotkey - Music hotkey - Play button + hotkey - Music controller hotkeys  Intended Flow: - Idle mode starts

---

### def mas_DropShield_timedtext()

Enables: - text speed - escape key - Music button + hotkey - Music Menu - Calendar overlay - Window hiding - dismiss  Shows: - hotkey buttons

---

### def mas_RaiseShield_timedtext()

Disables: - text speed - escape key - Music button + hotkey - Music Menu - Calendar overlay - Window hiding - dismiss  Hides: - hotkey buttons

---

### def mas_MUMUDropShield()

Enables: - Music button + hotkey - Music Menu  Intended Flow: - Whenever the music menu-based interactions need to be enabled

---

### def mas_MUMURaiseShield()

Disables: - Music button + hotkey - Music Menu  Intended Flow: - Whenever the music menu-based interactions need to be disabled

---

### def mas_MUINDropShield()

Enables: - Music button + hotkey - Music Menu - Music controller keys  Intended Flow: - Whenever all music-based interactions need to be enabled

---

### def mas_MUINRaiseShield()

Disables: - Music button + hotkey - Music Menu - Music controller keys  Intended Flow: - Whenever all music-based interactions need to be disabled

---

### def mas_dlgToIdleShield()

Enables: - Talk button - Extra button - Calendar overlay  Disables: - Music hotkey  Unsets: - dialogue workflow flag  Intended flow: - when transitioning from a dialogue workflow to idle mode

---

### def mas_coreToIdleShield()

Enables: - Talk button - Extra button - Music button - Calendar overlay - Escape key  Intended flow: - when transitiong from core sheilds to idle shields

---

### def mas_mumuToIdleShield()

Enables: - Talk button - Extra button - Music button - songs - calendar overlay  Intended Flow: - when transitioning from music menu to idle mode

---

### def mas_canCheckActiveWindow()

Checks if we can check the active window (simplifies conditionals)

---

### def mas_getActiveWindowHandle()

Gets the active window name

**Returns:**<br>
The active window handle if found. If it is not possible to get, we return an empty string

---

### def mas_display_notif(title, body, group=None, skip_checks=False)

Notification creation method

**Parameters:**
- `title` &mdash; Notification heading text
- `body` &mdash; A list of items which would go in the notif body (one is picked at random)
- `group` &mdash; Notification group (for checking if we have this enabled) (Default: None)
- `skip_checks` &mdash; Whether or not we skips checks (Default: False)


**Returns:**<br>
bool indicating status (notif shown or not (by check))

---

### def mas_isFocused()

Checks if MAS is the focused window

---

### def mas_isInActiveWindow(regexp, active_window_handle=None)

Checks if ALL keywords are in the active window name

**Parameters:**
- `regexp` &mdash;  Regex pattern to identify the window
- `active_window_handle` &mdash;  String representing the handle of the active window If None, it's fetched (Default: None)


---

### def mas_clearNotifs()

Clears all tray icons (also action center on win10)

---

### def mas_checkForWindowReacts()

Runs through events in the windowreact_db to see if we have a reaction, and if so, queue it

---

### def mas_resetWindowReacts(excluded=persistent._mas_windowreacts_no_unlock_list)

Runs through events in the windowreact_db to unlock them

---

### def mas_updateFilterDict()

Updates the filter dict with the groups in the groups list for the settings menu

---

### def mas_addBlacklistReact(ev_label)

Adds the given ev_label to the no unlock list

---

### def mas_removeBlacklistReact(ev_label)

Removes the given ev_label to the no unlock list if exists

---

### def mas_notifsEnabledForGroup(group)

Checks if notifications are enabled, and if enabled for the specified group

---

### def mas_unlockFailedWRS(ev_label=None)

Unlocks a wrs again provided that it showed, but failed to show (failed checks in the notif label)

---

### def mas_prepForReload()

Handles clearing wrs notifs and unregistering the wndclass to allow 'reload' to work properly

---

### def mas_HKRaiseShield()

RUNTIME ONLY Disables main hotkeys and music controller keys

---

### def mas_HKDropShield()

RUNTIME ONLY Enables the main hotkeys and music controller keys

---

### def mas_HKRaiseShield_main()

RUNTIME ONLY Disables main hotkeys

---

### def mas_HKDropShield_main()

RUNTIME ONLY Enables main hotkeys

---

### def mas_HKIsEnabled()

**Returns:**<br>
True if all the main hotkeys are enabled, False otherwise

---

### def mas_HKCanQuietMusic()

**Returns:**<br>
True if we can lower or stop the music, False if not

---

### def mas_HKIsSettingsClosed()

**Returns:**<br>
True if the settings is closed, False otherwise

---

### def mas_HKAllowHotkey()

ALWAYS CHECK THIS WHEN DOING ANYTHING THAT BREAKS FLOW.  Otherwise you may break the game if the game menu opens while something else breaks the context.

**Returns:**<br>
True if hotkey is allowed to be used now, False otherwise

---

### def enable_esc()

Enables the escape key so you can go to the game menu

---

### def disable_esc()

disables the escape key so you cant go to game menu

---

### def set_keymaps()

---

### def HKBHideButtons()

---

### def HKBShowButtons()

---

### def mas_HKBRaiseShield()

RUNTIME ONLY Disables the hotkey buttons

---

### def mas_HKBDropShield()

RUNTIME ONLY Enables the hotkey buttons

---

### def mas_HKBIsEnabled()

**Returns:**<br>
True if all the buttons are enabled, False otherwise

---

### def mas_HKBIsVisible()

**Returns:**<br>
True if teh Hotkey buttons are visible, False otherwise

---

### def MovieOverlayHideButtons()

---

### def MovieOverlayShowButtons()

---

### def mas_derandom_topic(ev_label=None)

Function for the derandom hotkey, 'x'

**Parameters:**
- `ev_label` &mdash; label of the event we want to derandom. (Optional. If None, persistent.current_monikatopic is used) (Default: None)


---

### def mas_bookmark_topic(ev_label=None)

Function for the bookmark hotkey, 'b'

**Parameters:**
- `ev_label` &mdash; label of the event we want to bookmark. (Optional, defaults to persistent.current_monikatopic)


---

### def mas_hasBookmarks(persist_var=None)

Checks to see if we have bookmarks to show  Bookmarks are restricted to Normal+ affection and to topics that are unlocked and are available based on current affection

**Parameters:**
- `persist_var` &mdash; appropriate variable holding the bookedmarked eventlabels. If None, persistent._mas_player_bookmarked is assumed (Default: None)


**Returns:**<br>
boolean: True if there are bookmarks in the curent var False otherwise

---

### def mas_setupIdleMode(brb_label=None, brb_callback_label=None)

Setups idle mode

**Parameters:**
- `brb_label` &mdash; the label of this brb event, if None, use the current label (Default: None)
- `brb_callback_label` &mdash; the callback label of this brb event, if None, we build it here (Default: None)


---

### def mas_resetIdleMode(clear_idle_data=True)

Resets idle mode  This is meant to basically clear idle mode for holidays or other things that hijack main flow

**Parameters:**
- `clear_idle_data` &mdash; whether or not clear persistent idle data (Default: True)


**Returns:**<br>
string with idle callback label or None if it was reset before

---

### def replace_text(s)

---

### def game_menu_check()

---

### def force_integer_multiplier(width, height)

---

### def addEvent(event, eventdb=None, skipCalendar=True, restartBlacklist=False, markSeen=False, code='EVE')

Adds an event object to the given eventdb dict Properly checksfor label and conditional statements This function ensures that a bad item is not added to the database

**Parameters:**
- `event` &mdash; the Event object to add to database
- `eventdb` &mdash; The Event databse (dict) we want to add to NOTE: DEPRECATED. Use code instead. NOTE: this can still be used for custom adds. (Default: None)
- `skipCalendar` &mdash; flag that marks wheter or not calendar check should be skipped (Default: True)
- `restartBlacklist` &mdash; True if this topic should be added to the restart blacklist (Default: False)
- `markSeen` &mdash; True if this topic should be `True` in persistent._seen_ever. (Default: False)
- `code` &mdash; code of the event database to add to. (Default: EVE) - event database


---

### def hideEventLabel(eventlabel, lock=False, derandom=False, depool=False, decond=False, eventdb=evhand.event_database)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `mas_hideEVL`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_hideEVL', should_raise=True)`


---

### def hideEvent(event, lock=False, derandom=False, depool=False, decond=False)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `mas_hideEvent`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_hideEvent')`


---

### def mas_hideEvent(ev, lock=False, derandom=False, depool=False, decond=False)

Hide an event by Falsing its unlocked/random/pool props

**Parameters:**
- `ev` &mdash; event object we want to hide
- `lock` &mdash; True if we want to lock this event, False if not (Default: False)
- `derandom` &mdash; True fi we want to unrandom this Event, False if not (Default: False)
- `depool` &mdash; True if we want to unpool this event, Flase if not (Default: False)
- `decond` &mdash; True if we want to remove the conditional, False if not (Default: False)


---

### def mas_hideEventLabel(ev_label, lock=False, derandom=False, depool=False, decond=False, eventdb=evhand.event_database)

Hide an event label by Falsing its unlocked/random/pool props

**Parameters:**
- `ev_label` &mdash; label of the event we wnat to hide
- `lock` &mdash; True if we want to lock this event, False if not (Default: False)
- `derandom` &mdash; True fi we want to unrandom this Event, False if not (Default: False)
- `depool` &mdash; True if we want to unpool this event, Flase if not (Default: False)
- `decond` &mdash; True if we want to remove the conditional, False if not (Default: False)
- `eventdb` &mdash; event databsae ev_label is in (Default: evhand.event_database)


---

### def mas_showEvent(ev, unlock=False, _random=False, _pool=False)

Show an event by Truing its unlock/ranomd/pool props

**Parameters:**
- `ev` &mdash; event to show
- `unlock` &mdash; True if we want to unlock this event, False if not (Default: False)
- `_random` &mdash; True if we want to random this event, Flase otherwise (Default: False)
- `_pool` &mdash; True if we want to pool this event, False otherwise (Default: False)


---

### def mas_showEventLabel(ev_label, unlock=False, _random=False, _pool=False, eventdb=evhand.event_database)

Shows an event label, by Truing the unlocked, random, and pool properties.

**Parameters:**
- `ev_label` &mdash; label of event to show
- `unlock` &mdash; True if we want to unlock this event, False if not (DEfault: False)
- `_random` &mdash; True if we want to random this event, False if not (Default: False)
- `_pool` &mdash; True if we want to pool this event, False if not (Default: False)
- `eventdb` &mdash; eventdatabase this label belongs to (Default: evhannd.event_database)


---

### def lockEvent(ev)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `mas_lockEvent`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_lockEvent', should_raise=True)`


**Parameters:**
- `ev` &mdash; the event object to lock


---

### def lockEventLabel(evlabel, eventdb=evhand.event_database)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `mas_lockEventLabel`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_lockEventLabel', should_raise=True)`


**Parameters:**
- `evlabel` &mdash; event label of the event to lock
- `eventdb` &mdash; Event database to find this label


---

### def mas_lockEvent(ev)

Locks the given event object

**Parameters:**
- `ev` &mdash; the event object to lock


---

### def mas_lockEventLabel(evlabel, eventdb=evhand.event_database)

Locks the given event label

**Parameters:**
- `evlabel` &mdash; event label of the event to lock
- `eventdb` &mdash; Event database to find this label


---

### def pushEvent(event_label, skipeval=False, notify=False)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `MASEventList.push`.

This pushes high priority or time sensitive events onto the top of the event list

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='MASEventList.push')`


**Parameters:**
- `skipmidloopeval` &mdash; do we want to skip the mid loop eval to prevent other rogue events from interrupting. (Defaults: False)
- `notify` &mdash; True will trigger a notification if appropriate. False will not (Default: False)


---

### def queueEvent(event_label, notify=False)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `MASEventList.queue`.

This adds low priority or order-sensitive events onto the bottom of the event list. This is slow, but rarely called and list should be small.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='MASEventList.queue')`


**Parameters:**
- `notify` &mdash; True will trigger a notification if appropriate, False will not (Default: False)


---

### def unlockEvent(ev)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `mas_unlockEvent`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_unlockEvent', should_raise=True)`


**Parameters:**
- `ev` &mdash; the event object to unlock


---

### def unlockEventLabel(evlabel, eventdb=evhand.event_database)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `mas_unlockEventLabel`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='mas_unlockEventLabel')`


**Parameters:**
- `evlabel` &mdash; event label of the event to lock
- `eventdb` &mdash; Event database to find this label


---

### def mas_unlockEvent(ev)

Unlocks the given evnet object

**Parameters:**
- `ev` &mdash; the event object to unlock


---

### def mas_unlockEventLabel(evlabel, eventdb=evhand.event_database)

Unlocks the given event label

**Parameters:**
- `evlabel` &mdash; event label of the event to lock
- `eventdb` &mdash; Event database to find this label


---

### def isFuture(ev, date=None)

Checks if the start_date of the given event happens after the given time.

**Parameters:**
- `ev` &mdash; Event to check the start_time
- `date` &mdash; a datetime object used to check against If None is passed it will check against current time (Default: None)


**Returns:**<br>
True if the Event's start_date is in the future, False otherwise

---

### def isPast(ev, date=None)

Checks if the end_date of the given event happens before the given time.

**Parameters:**
- `ev` &mdash; Event to check the start_time
- `date` &mdash; a datetime object used to check against If None is passed it will check against current time (Default: None)


**Returns:**<br>
True if the Event's end_date is in the past, False otherwise

---

### def isPresent(ev)

Checks if current date falls within the given event's start/end date range

**Parameters:**
- `ev` &mdash; Event to check the start_time and end_time


**Returns:**<br>
True if current time is inside the  Event's start_date/end_date interval, False otherwise

---

### def popEvent(remove=True)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `MASEventList.pop`.

DO NOT USE.  Use MASEventList.pop instead (not exactly the same)

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='MASEventList.pop', should_raise=True)`


---

### def seen_event(event_label)

Please use mas_seenEvent, this function hasn't been deprecated only because it's used a lot in event conditionals and I don't want to update them all

---

### def mas_seenEvent(event_label)

This checks if an event has either been seen or is already in the event list.

---

### def mas_findEVL(event_label)

Finds index of the given event label in the even tlist

**Parameters:**
- `event_label` &mdash; event lable to check


**Returns:**<br>
index of the event in teh even tlist, -1 if not found

---

### def mas_inEVL(event_label)

This checks if an event is in the event list

**Parameters:**
- `event_label` &mdash; event lable to check


**Returns:**<br>
True if in event list, False if not

---

### def mas_rmEVL(event_label)

REmoves an event from the event list if it exists

---

### def mas_rmallEVL(event_label)

Removes all events with athe given label

---

### def restartEvent()

This checks if there is a persistent topic, and if there was push it back on the stack with a little comment.

---

### def mas_isRstBlk(topic_label)

Checks if the event with the current label is blacklistd from being restarted

**Parameters:**
- `topic_label` &mdash; label of the event we are trying to restart


---

### def mas_cleanEventList()

Iterates through the event list and removes items which shouldn't be restarted

---

### def mas_cleanJustSeen(eventlist, db)

Cleans the given event list of just seen items (withitn the THRESHOLD) retunrs not just seen items

**Parameters:**
- `eventlist` &mdash; list of event labels to pick from
- `db` &mdash; database these events are tied to


**Returns:**<br>
cleaned list of events (stuff not in the time THREASHOLD)

---

### def mas_cleanJustSeenEV(ev_list)

Cleans the given event list (of events) of just seen items (within the THRESHOLD). Returns not just seen items. Basically the same as mas_cleanJustSeen, except for Event object lists

**Parameters:**
- `ev_list` &mdash; list of event objects


**Returns:**<br>
cleaned list of events (stuff not in the tiem THRESHOLD)

---

### def mas_unlockPrompt(count=1)

Unlocks a pool event

**Parameters:**
- `count` &mdash; number of pool events to unlock (Default: 1)


**Returns:**<br>
True if an event was unlocked. False otherwise

---

### def mas_getBackground(background_id, default=None)

Gets a MASFilterableBackground by id

**Parameters:**
- `background_id` &mdash; id of the background to get
- `default` &mdash; default to return if not found


**Returns:**<br>
MASFilterableBackground if found, None otherwise

---

### def mas_getCurrentBackgroundId(default=None)

Returns the id of the current background

**Parameters:**
- `default` &mdash; the fallback value to return (Default: None)


**Returns:**<br>
string - the bg id or default if not found

---

### def mas_isBackgroundUnlocked(id_)

Checks if a background with the given id is unlocked

**Parameters:**
- `id_` &mdash; str - the background id


**Returns:**<br>
boolean

---

### def mas_check_event_types(per_db, str_buffer=None, str_rep=True)

Goes through given persistent database for events and double checks types. Returns a string report.

**Parameters:**
- `per_db` &mdash; persistent db of events to check types of
- `str_buffer` &mdash; the string buffer we should write to. If None, we do NO reporting.
- `str_rep` &mdash; UNUSED


**Returns:**<br>
string report int he given buffer

---

### def mas_largest_persistent_item()

Determines largest item in persistent

**Returns:**<br>
tuple of the following format: [0] - key of item [1] - size of item

---

### def mas_per_dump(item_key)

Dumps something from persistent

**Parameters:**
- `item_key` &mdash; the string name of the item to dump


---

### def mas_per_dump_dict(dkey)

Dumps an output of a persistent dict

**Parameters:**
- `dkey` &mdash; the string name of the dict to dump


---

### def mas_per_dump_list(lkey)

Dumps an output of a persistent list

**Parameters:**
- `lkey` &mdash; the string name of the list to dump


---

### def dev_api_key_tester(key)

---

### def dev_api_key_tester_error(key)

---

### def dev_api_key_tester_returns_not_tuple(key)

---

### def dev_api_key_tester_returns_not_long_enough(key)

---

### def dev_api_key_tester_false_not_valid_error_msg(key)

---

### def dev_register_multipleAPI(count)

For testing - use to register a ton of api keys

**Parameters:**
- `count` &mdash; number of keys to register


---

### def mas_canShowIslands(flt=None)

Global check for whether or not we can show the islands event This only checks the technical side, NOT event unlocks

**Parameters:**
- `flt` &mdash; the filter to use in check If None, we fetch the current filter If False, we don't check the fitler at all (Default: None)


**Returns:**<br>
boolean

---

### def mas_startupPlushieLogic(chance=4)

Runs a simple random check for the quetzal plushie.

**Parameters:**
- `chance` &mdash; value that determines the chance of that determines if the plushie will appear Defualts to 4


---

### def mas_incMoniReload()

Increments the monika reload counter unless its at max

---

### def mas_isFirstSeshDay(_date=None)

Checks if _date is the day of first session

**Parameters:**
- `_date` &mdash; date to compare against


---

### def mas_hasRPYFiles()

Checks if there are rpy files in the gamedir

---

### def mas_getRPYFiles()

Gets a list of rpy files in the gamedir

---

### def mas_is18Over(_date=None)

Checks if player is over 18

**Parameters:**
- `_date` &mdash; date to check


**Returns:**<br>
boolean: - True if player is over 18 - False otherwise

---

### def mas_getPlayerAge(_date=None)

Gets the player age

**Parameters:**
- `_date` &mdash; the datetime.date to get the player age at


**Returns:**<br>
integer representing the player's current age or None if we don't have player's bday

---

### def mas_canShowRisque(aff_thresh=2000, grace=None)

Checks if we can show something risque  Conditions for this: 1. Player has had first kiss (No point going for risque things if this hasn't been met yet) 2. Player is over 18 3. Aff condition (raw)

**Parameters:**
- `aff_thresh` &mdash;  - Raw affection value to be greater than or equal to
- `grace` &mdash;  - a grace period passed in as a timedelta defaults to 1 week


**Returns:**<br>
boolean: - True if the above conditions are satisfied - False if not

---

### def mas_timePastSince(timekeeper, passed_time, _now=None)

Checks if a certain amount of time has passed since the time in the timekeeper

**Parameters:**
- `timekeeper` &mdash;  variable holding the time we last checked whatever it restricts (can be datetime.datetime or datetime.date)
- `passed_time` &mdash;  datetime.timedelta of the amount of time which should have passed since the last check in order to return True
- `_now` &mdash;  time to check against (If none, now is assumed, (Default: None))


**Returns:**<br>
boolean: - True if it has been passed_time units past timekeeper - False otherwise

---

### def mas_pastOneDay(timekeeper, _now=None)

One day time past version of mas_timePastSince()

**Parameters:**
- `timekeeper` &mdash; variable holding the time since last event
- `_now` &mdash; time to check against (Default: None)


---

### def mas_setTODVars()

Sets the mas_globals.time_of_day variable

---

### def mas_seenLabels(label_list, seen_all=False)

List format for renpy.seen_label. Allows checking if we've seen multiple labels at once

**Parameters:**
- `label_list` &mdash; list of labels we want to check if we've seen
- `seen_all` &mdash; True if all labels in label_list must have been seen in order for this function to return True.


**Returns:**<br>
boolean: - True if we have seen the inputted labels and met the seen_all criteria - False otherwise

---

### def mas_a_an_str(ref_str, ignore_case=True)

Takes in a reference string and returns it back with an 'a' prefix or 'an' prefix depending on starting letter

**Parameters:**
- `ref_str` &mdash; string in question to prefix
- `ignore_case` &mdash; whether or not we should ignore capitalization of a/an and not adjust the capitalization of ref_str (Default: True)


**Returns:**<br>
string prefixed with a/an

---

### def mas_a_an(ref_str, ignore_case=True)

Takes in a reference string and returns either a/an based on the first letter of the word

**Parameters:**
- `ref_str` &mdash; string in question to prefix
- `ignore_case` &mdash; whether or not we should ignore capitalization of a/an and just use lowercase (Default: True)


**Returns:**<br>
a/an based on the ref string

---

### def mas_setEventPause(seconds=60)

Sets a pause 'til next event

**Parameters:**
- `seconds` &mdash; the number of seconds to pause for. Can be None to remove pause (Default: 60)


---

### def mas_getCurrentMoniExp(layer='master')

Returns Monika's current expression

**Parameters:**
- `layer` &mdash; the layer to check for Monika's displayable You probably shouldn't change this (Default: 'master')


**Returns:**<br>
string with sprite code or None if we couldn't get the exp (e.g. if Monika isn't on the screen)

---

### def FinishEnterName()

---

### def mas_lastSeenInYear(ev_label, year=None)

Checks whether or not the even was last seen in the year provided

**Parameters:**
- `ev_label` &mdash; label of the event we want to check
- `year` &mdash; the year we want to check if it's been last seen in


**Returns:**<br>
boolean - True if last seen this year, False otherwise

---

### def mas_lastSeenLastYear(ev_label)

Checks if the event corresponding to ev_label was last seen last year

---

### def mas_after_bath_cleanup_change_outfit()

After bath cleanup change outfit code

---

### def mas_generateShoppingList(low_cons_list=None)

Generates a list of consumables we're low on in the form of a 'shopping list' and exports it to the characters folder

**Parameters:**
- `low_cons_list` &mdash; List of MASConsumable objects that we're low on


---

### def mas_getConsumable(consumable_id)

Gets a consumable object by type and id

**Parameters:**
- `consumable_id` &mdash; id of the consumable


**Returns:**<br>
Consumable object: If found, MASConsumable If not found, None

---

### def mas_useThermos()

Gets Monika to put her drink into a thermos when taking her somewhere if it is eligible

---

### def mas_getEV(ev_label)

Global get function that retreives an event given the label  Designed to be used as a wrapper around the mas_all_ev_db dict

**Parameters:**
- `ev_label` &mdash; eventlabel to find event for


**Returns:**<br>
the event object you were looking for, or None if not found

---

### def mas_checkEVL(ev_label, predicate)

Checks event properties using a lambda

**Parameters:**
- `ev_label` &mdash; ev_label representing the event to check properties for
- `predicate` &mdash; predicate function (accepting an ev as the argument) for the test(s)


**Returns:**<br>
True if predicate function returns True, False otherwise

---

### def mas_getEVLPropValue(ev_label, prop, default=None)

Safely gets an ev prop value

**Parameters:**
- `ev_label` &mdash; eventlabel corresponding to the event object to get the property from
- `prop` &mdash; property name to get
- `default` &mdash; default value to return if ev not found/prop not found (Default: None)


**Returns:**<br>
Value of the given property name, or default if not found/no ev exists

---

### def mas_setEVLPropValues(ev_label)

Sets ev prop values in bulk if the ev exists

**Parameters:**
- `ev_label` &mdash; ev_label representing the event to set properties for
- `kwargs` &mdash; propname=new_value. Represents the value to set to the property


**Returns:**<br>
True if the property/ies was/were set False if not (ev does not exist)

---

### def mas_isPoolEVL(ev_label)

Checks if the event for the given event label is pool

**Parameters:**
- `ev_label` &mdash; eventlabel corresponding to the event we wish to check if is pooled


**Returns:**<br>
True if the ev is pooled, False if not, or the ev doesn't exist

---

### def mas_isRandomEVL(ev_label)

Checks if the event for the given event label is random

**Parameters:**
- `ev_label` &mdash; eventlabel corresponding to the event we wish to check if is random


**Returns:**<br>
True if the ev is random, False if not, or the ev doesn't exist

---

### def mas_isUnlockedEVL(ev_label)

Checks if the event for the given event label is unlocked

**Parameters:**
- `ev_label` &mdash; eventlabel corresponding to the event we wish to check if is unlocked


**Returns:**<br>
True if the ev is unlocked, False if not, or the ev doesn't exist

---

### def mas_getEVL_last_seen(ev_label, default=None)

Gets the last_seen from the event corresponding to the given eventlabel  If the event doesn't exist, the default is returned

**Parameters:**
- `ev_label` &mdash; eventlabel for the event we wish to get last_seen from
- `default` &mdash; value to return if the event object doesn't exist


**Returns:**<br>
The last_seen of the ev, or the default if the event doesn't exist

---

### def mas_getEVL_shown_count(ev_label, default=0)

Gets the shown_count from the event corresponding to the given eventlabel  If the event doesn't exist, the default is returned

**Parameters:**
- `ev_label` &mdash; eventlabel for the event we wish to get shown_count from
- `default` &mdash; value to return if the event object doesn't exist


**Returns:**<br>
The shown_count of the ev, or the default if the event doesn't exist

---

### def mas_inRulesEVL(ev_label)

Checks if keys are in the event's rules dict

**Parameters:**
- `ev_label` &mdash; eventlabel for the event we wish to check rule keys for


**Returns:**<br>
True if all rule keys provided are in an event object's rules dict False if the event doesn't exist or any provided keys aren't present in the rules dict

---

### def mas_assignModifyEVLPropValue(ev_label, propname, operation, value)

Does an assign-modify operation

**Parameters:**
- `ev_label` &mdash; eventlabel representing the event that will have a property assign/modified
- `propname` &mdash; property name to do the assign-modify operation on
- `operation` &mdash; operator to assign/modify with. (Any of the following: +=, -=, *=, /= (as a string))
- `value` &mdash; value to use in the operation


**Returns:**<br>
True if event values were assign/modified successfully False otherwise

---

### def mas_getEVCL(ev_label)

Global get function that retrieves the calendar label for an event given the eventlabel. This is mainly to help with calendar.

**Parameters:**
- `ev_label` &mdash; eventlabel to find calendar label for


**Returns:**<br>
the calendar label you were looking for, or "Unknown Event" if not found.

---

### def mas_hideEVL(ev_label, code, lock=False, derandom=False, depool=False, decond=False)

Hides an event given label and code.

**Parameters:**
- `ev_label` &mdash; label of event to hide
- `code` &mdash; string code of the db this ev_label belongs to
- `lock` &mdash; True if we want to lock this event (Default: False)
- `derandom` &mdash; True if we want to de random this event (Default: False)
- `depool` &mdash; True if we want to de pool this event (Default: False)
- `decond` &mdash; True if we want to remove conditoinal for this event (Default: False)


---

### def mas_showEVL(ev_label, code, unlock=False, _random=False, _pool=False)

Shows an event given label and code.

**Parameters:**
- `ev_label` &mdash; label of event to show
- `code` &mdash; string code of the db this ev_label belongs to
- `unlock` &mdash; True if we want to unlock this Event (Default: False)
- `_random` &mdash; True if we want to random this event (Default: False)
- `_pool` &mdash; True if we want to random thsi event (Default: False)


---

### def mas_protectedShowEVL(ev_label, code, unlock=False, _random=False, _pool=False)

Shows an event given label and code.  Does checking if the actions should happen

**Parameters:**
- `ev_label` &mdash; label of event to show
- `code` &mdash; string code of the db this ev_label belongs to
- `unlock` &mdash; True if we want to unlock this Event (Default: False)
- `_random` &mdash; True if we want to random this event (Default: False)
- `_pool` &mdash; True if we want to random thsi event (Default: False)


---

### def mas_lockEVL(ev_label, code)

Locks an event given label and code.

**Parameters:**
- `ev_label` &mdash; label of event to show
- `code` &mdash; string code of the db this ev_label belongs to


---

### def mas_unlockEVL(ev_label, code)

Unlocks an event given label and code.

**Parameters:**
- `ev_label` &mdash; label of event to show
- `code` &mdash; string code of the db this ev_label belongs to


---

### def mas_stripEVL(ev_label, list_pop=False, remove_dates=True)

Strips the conditional and action properties from an event given its label start_date and end_date will be removed if remove_dates is True Also removes the event from the event list if present (optional)

**Parameters:**
- `ev_label` &mdash; label of event to strip
- `list_pop` &mdash; True if we want to remove the event from the event list (Default: False)
- `remove_dates` &mdash; True if we want to remove start/end_dates from the event (Default: True)


---

### def mas_flagEVL(ev_label, code, flags)

Applies flags to the given event

**Parameters:**
- `ev_label` &mdash; label of the event to flag
- `code` &mdash; string code of the db this ev_label belongs to
- `flags` &mdash; flags to apply


---

### def mas_unflagEVL(ev_label, code, flags)

Unflags flags from the given event

**Parameters:**
- `ev_label` &mdash; label of the event to unflag
- `code` &mdash; string code of the db this ev_label belongs to
- `flags` &mdash; flags to unset


---

### def mas_transferTopicData(new_topic_evl, old_topic_evl, old_topic_ev_db, transfer_unlocked=True, transfer_shown_count=True, transfer_seen_data=True, transfer_last_seen=True, erase_topic=True)

Transfers topic data from ev to ev

**Parameters:**
- `new_topic_evl` &mdash; new topic's eventlabel
- `old_topic_evl` &mdash; old topic's eventlabel
- `old_topic_ev_db` &mdash; event database containing the old topic
- `transfer_unlocked` &mdash; whether or not we should transfer the unlocked property of the old topic
- `transfer_shown_count` &mdash; whether or not we should transfer the shown_count property of the old topic
- `transfer_seen_data` &mdash; whether or not we should transfer the _seen_ever state of the old topic
- `transfer_last_seen` &mdash; whether or not we should transfer the last_seen property of the old topic
- `erase_topic` &mdash; whether or not we should erase this topic after transferring data


---

### def mas_isGameUnlocked(gamename)

Checks if the given game is unlocked.

**Parameters:**
- `gamename` &mdash; name of the game to check


**Returns:**<br>
True if the game is unlocked, False if not, or the game doesn't exist

---

### def mas_unlockGame(gamename)

Unlocks the given game.

**Parameters:**
- `gamename` &mdash; name of the game to unlock


---

### def mas_lockGame(gamename)

Locks the given game.

**Parameters:**
- `gamename` &mdash; name of the game to lock


---

### def mas_addClothesToHolidayMap(clothes, key=None)

Adds the given clothes to the holiday clothes map

**Parameters:**
- `clothes` &mdash; clothing item to add
- `key` &mdash; dateime.date to use as key. If None, we use today


---

### def mas_addClothesToHolidayMapRange(clothes, start_date, end_date)

Adds the given clothes to the holiday clothes map over the day range provided

**Parameters:**
- `clothes` &mdash; clothing item to add
- `start_date` &mdash; datetime.date to start adding to the map on
- `end_date` &mdash; datetime.date to stop adding to the map on


---

### def mas_doesBackgroundHaveHolidayDeco(deco_tags, background_id=None)

Checks if a background has support for the given deco tag(s)

**Parameters:**
- `deco_tags` &mdash; list of deco tags to check for
- `background_id` &mdash; id of the background to check if it supports deco If None, mas_current_background's id is used (Default: None)


---

### def mas_backgroundUpdateCheck()

This launches the background update thread

---

### def mas_get_player_nickname(capitalize=False, exclude_names=[], _default=None, regex_replace_with_nullstr=None)

Picks a nickname for the player at random based on accepted nicknames

**Parameters:**
- `capitalize` &mdash; Whether or not we should capitalize the first character (Default: False)
- `exclude_names` &mdash; List of names to be excluded in the selection pool for nicknames (Default: Empty list)
- `_default` &mdash; Default name to return if affection < affectionate or no nicknames have been set/allowed If None, the player's name is assumed (Default: None)
- `regex_replace_with_nullstr` &mdash; Regex str to use to identify parts of a nickname which should be replaced with an empty string. If None, this is ignored (Default: None)


---

### def mas_input(prompt, default='', allow=None, exclude='{}', length=None, with_none=None, pixel_width=None, screen='input', screen_kwargs={})

Calling this function pops up a window asking the player to enter some text.

**Parameters:**
- `prompt` &mdash; a string giving a prompt to display to the player
- `default` &mdash; a string giving the initial text that will be edited by the player (Default: "")
- `allow` &mdash; a string giving a list of characters that will be allowed in the text (Default: None)
- `exclude` &mdash; if a character is present in this string, it is not allowed in the text (Default: "{}")
- `length` &mdash; an integer giving the maximum length of the input string (Default: None)
- `with_none` &mdash; the transition to use (Default: None)
- `pixel_width` &mdash; if not None, the input is limited to being this many pixels wide, in the font used by the input to display text (Default: None)
- `screen` &mdash; the name of the screen that takes input. If not given, the 'input' screen is used (Default: "input")
- `screen_kwargs` &mdash; the keyword arguments to pass in to the screen NOTE: passing in the prompt argument is not mandatory here (Default: {})


**Returns:**<br>
entered string

---

### def mas_getMousePos()

Gets the mouse position in terms of physical screen size

**Returns:**<br>
tuple, (x, y) coordinates representing the mouse position

---

### def mas_quipExp(exp_code)

Allows expressions to be inserted into quips directly via function substitution  (This is effectively a renpy.show that returns '' instead of None)

**Parameters:**
- `exp_code` &mdash; code of the expression as str (ex: '1hua')


---

### def mas_chgCalEVul(number_of_days)

Changes the conditionals / actions / and more of the monika start date topic so it unlocks after the given number of days

**Parameters:**
- `number_of_days` &mdash; number of days before unlocking the monika start date topic


---

### def mas_test_sitting()

---

### def mas_supertest()

---

### def mas_matrix_cache_report()

---

### def mas_build_mbgfm(mn_sr_size, mn_sr_d, sr_ss_size, sr_ss_d, ss_mn_size, ss_mn_d, ml_min, ml_max, pr_min, pr_max, mx_min, mx_max)

Generates a MASBackgroundFilterManager using sample number of slice sizes.

**Parameters:**
- `mn_sr_size` &mdash; how many slices to use for the mn_sr chunk
- `mn_sr_d` &mdash; passed to the is_day param
- `sr_ss_size` &mdash; how many slices to use for the sr_ss chunk
- `sr_ss_d` &mdash; passed to the is_day param
- `ss_mn_size` &mdash; how many slices to use for the ss_mn chunk
- `ss_mn_d` &mdash; passed to the is_day param
- `ml_min` &mdash; minimum minlength time to use in seconds NOTE: if larger than ml_max, ml_max takes precedence
- `ml_max` &mdash; max minlength time to use in seconds
- `pr_min` &mdash; min priority to use (must be 1-10) NOTE: if larger than pr_max, pr_max takes precedence
- `pr_max` &mdash; max priority to use (must be 1-10)
- `mx_min` &mdash; minimum maxlength time to use in seconds NOTE: if larger than mx_max, mx_max takes precdence
- `mx_max` &mdash; minimum maxlength time to use in seconds


**Returns:**<br>
MASBackgroundFilterManager object with the given settings

---

### def mas_qb_mbgfm()

---

### def mas_qb_mbgfm_otm()

---

### def mas_qb_mbgfm_irl()

once slice for everything except day, which uses a 5 minute sunrise and sunset

---

### def mas_OVLDropShield()

RUNTIME ONLY Enables all overlay screens. This is like "dropping a shield" because it allows user interactions with the overlays.

---

### def mas_OVLHide()

RUNTIME ONLY Hides all overlay screens.

---

### def mas_OVLRaiseShield()

RUNTIME ONLY Disables all overlay screens. This is like "raising a shield" because it prevents user interactions with the overlays.

---

### def mas_OVLShow()

RUNTIME ONLY Shows all overlay screens.

---

### def mas_setWeather(_weather)

Sets the initial weather. This is meant for startup/ch30_reset

**Parameters:**
- `_weather` &mdash; weather to set to.


---

### def mas_changeWeather(new_weather, by_user=None, set_persistent=False, new_bg=None)

Changes weather without doing scene changes

**Parameters:**
- `new_weather` &mdash; weather to change to
- `by_user` &mdash; flag for if user changes weather or not
- `set_persistent` &mdash; whether or not we want to make this weather persistent
- `new_bg` &mdash; MASFilterableBackground which will be switched to along with weather change. If none, mas_current_background is used. (Default: None)


---

### def mas_startupWeather()

Runs a weather startup alg, checking whether or not persistent weather should be used Sets weather accordingly

---

### def mas_setBackground(_background)

Sets the initial bg  Does not do anything if the current bg is same.

**Parameters:**
- `_background` &mdash;  The background we're changing to. Assumes this is already built.


---

### def mas_changeBackground(new_background, by_user=None, set_persistent=False)

changes the background w/o any scene changes. Will not run progpoints or do any actual bg changes if the current background is already set to the background we are changing to.

**Parameters:**
- `new_background` &mdash;  The background we're changing to
- `by_user` &mdash;  True if the user switched the background themselves
- `set_persistent` &mdash;  True if we want this to be persistent


**Returns:**<br>
MASBackgroundChangeInfo object of the changes that occured.

---

### def mas_startupBackground()

Sets up the spaceroom to start up in the background you left in if it is unlocked and still exists

---

### def mas_checkBackgroundChangeDelegate()

Checks to see if the background change delegate should be locked or unlocked and changes its state accordingly  Key rule: at least 2 available backgrounds

---

### def mas_remove_event()

Removes an event from the persistent database and lock DB

---

### def mas_remove_event_list(label_list)

Does the same as mas_remove_event, but with a list

---

### def pnmlLoadTuples()

Loads piano note match lists from the saved data, wich is assumed to be in the proper format. No checking is done.

---

### def pnmlSaveTuples()

Saves piano not match list into a pickleable format.

---

### def mas_reset_d25()

Removes d25 events  Quits the game

---

### def mas_reset_nye()

Remogse nye events  Quist tehe game

---

### def mas_reset_ptods()

Removes all PTODS from the lockDB and per_eventDB this basically allows them to be refreshed on next load.

---

### def mas_ptod_warptime()

Emulates moving forward 1 day by changing all currently unlocked python tips to have an unlock date of yesterday

---

### def mas_ptod_unlocktip()

Unlocks tips with the given numbers. This does not do warp time.

---

### def mas_eventDataDump()

Data dump for purely events stats

---

### def mas_unstableDataDump()

This is a function called on startup and performs data dumps.  Please add your data dump to a different file than dumps.log if its a large dump.  Thank you.

---

### def mas_progressionDataDump()

Dumps progression data as a string

---

### def mas_sessionDataDump()

Dumps session data as a string

---

### def mas_varDataDump()

Dumps other kinds of data.

---

### def mas_dataDumpFlag()

Checks if the data dump flag (file) exists

---

### def mas_eventDataDump()

Data dump for purely events stats

---

### def mas_unstableDataDump()

This is a function called on startup and performs data dumps.  Please add your data dump to a different file than dumps.log if its a large dump.  Thank you.

---

### def mas_progressionDataDump()

Dumps progression data as a string

---

### def mas_sessionDataDump()

Dumps session data as a string

---

### def mas_varDataDump()

Dumps other kinds of data.

---

### def mas_dataDumpFlag()

Checks if the data dump flag (file) exists

---

### def label_callback(name, abnormal)

Function to run plugin functions and store the last label

---

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _m1_zz_submods__run(_function, args)

Private function to run a function in the global store

---

### def __mas__extractNumbers(partname, filelist)

Extracts a list of the number parts of the given file list  Also sorts them nicely

**Parameters:**
- `partname` &mdash; part of the filename prior to the numbers
- `filelist` &mdash; list of filenames


---

### def __mas__backupAndDelete(loaddir, org_fname, savedir=None, numnum=None)

Does a file backup / and iterative deletion.

**Parameters:**
- `loaddir` &mdash; directory we are copying files from
- `org_fname` &mdash; filename of the original file / aka file to copy
- `savedir` &mdash; directory we are copying files to (and deleting old files) If None, we use loaddir instead (Default: None)
- `numnum` &mdash; if passed in, use this number instead of figuring out the next numbernumber. (Default: None)


**Returns:**<br>
tuple of the following format: [0]: numbernumber we just made [1]: numbernumber we deleted (None means no deletion)

---

### def __mas__memoryBackup()

Backs up both persistent and calendar info

---

### def __mas__memoryCleanup()

Cleans up persistent data by removing uncessary parts.

---

### def _mas_getBadFiles()

Searches through the entire mod_assets folder for any file with the '.new' extension and returns their paths

**Returns:**<br>
a list containing the file names, list will be empty if there was no 'bad' files

---

### def _mas_AffSave()

Runs saving algo for affection

---

### def _mas_AffLoad()

Runs loading algo for affection

---

### def _mas_getAffection()

Tries to return current affection

**Returns:**<br>
float

---

### def _mas_getBadExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `_get_current_aff_lose`.

**Decorators:**
- `@mas_utils.deprecated(use_instead='_get_current_aff_lose')`


---

### def _mas_getGoodExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `_get_current_aff_gain`.

**Decorators:**
- `@mas_utils.deprecated(use_instead='_get_current_aff_gain')`


---

### def _mas_getTodayExp()

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@mas_utils.deprecated()`


---

### def _get_current_aff_gain()

---

### def _get_current_aff_lose()

---

### def _get_current_aff_fraction_lose()

---

### def _mas_revertFreshStart()

Revert affection to before the fresh start

---

### def _mas_shatterAffection()

Sets affection to the lowest value

---

### def _mas_doFreshStart()

Resets affection

---

### def _m1_script0x2daffection__long_absence_check()

---

### def _mas_AffStartup()

---

### def _write_txt(path, text, update=False)

Writes the text file in the specified path using basedir as starting path

**Parameters:**
- `path` &mdash; String path to the file this function will write it will always start at basedir
- `text` &mdash; actual text for the txt file
- `update` &mdash; if it should override the file if it exists defaults to False


---

### def _Shake(start, time, child=None, dist=100.0)

---

### def _mas_hk_mute_music()

hotkey specific muting / unmuting music channel

---

### def _mas_hk_inc_musicvol()

hotkey specific music volume increasing

---

### def _mas_hk_dec_musicvol()

hotkey specific music volume decreasing

---

### def _mas_hk_show_dialogue_box()

hotkey specific show dialgoue box

---

### def _mas_hk_open_extra_menu()

hotkey specific open extras menu

---

### def _mas_hk_pick_game()

hotkey specific pick game

---

### def _mas_hk_select_music()

Runs the select music function if we are allowed to. INTENDED FOR HOTKEY USAGE ONLY

---

### def _mas_hk_derandom_topic()

hotkey specific derandom topics

---

### def _mas_hk_bookmark_topic()

hotkey specific bookmark topics

---

### def _mas_game_menu_start(scope)

Runs code prior to opening the game menu in any way.

**Returns:**<br>
scope - use this dict as temp space

---

### def _mas_game_menu_end(scope)

Runs code after exiting the game menu in any way.

**Parameters:**
- `scope` &mdash; temp space used in `_mas_game_menu_start`


---

### def _mas_game_menu()

Wrapper aound _invoke_game_menu that follows additional ui rules

---

### def _mas_quick_menu_cb(screen_name)

Opens game menu to the appropraite quick screen.

---

### def _mas_hide_windows()

Wrapper around the _hide_windows label that hides windows

---

### def _mas_check_ev_type_bool(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type_dict(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type_dt(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type_evact(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type_int(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type_str(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type_tuli(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type_tuli_aff(val, name, report, delim=' | ', str_rep=True)

---

### def _mas_check_ev_type(ev, str_rep=True)

Checks typers of the given event, then returns a string report

**Parameters:**
- `ev` &mdash; event to check


**Returns:**<br>
single line string report

---

### def _mas_check_ev_type_per(ev_line, str_rep=True)

Checks typers of the given event line, then returns a string report

**Parameters:**
- `ev_line` &mdash; line of persistent tuple data to check


**Returns:**<br>
single line string report

---

### def _mas_backgroundUpdateCheck()

THIS IS A PRIVATE FUNCTION Background update check

---

### def _mas_resetVersionUpdates()

Resets all version update script's seen status

---

### def _mas_build_fake_slices(flt_pfx, size, ml_min, ml_max, pr_min, pr_max, mx_min, mx_max)

Builds fake slices with the given size

**Parameters:**
- `flt_pfx` &mdash; prefix to use for each slice filter
- `size` &mdash; number of slices to make
- `ml_min` &mdash; min minlength time to use in seconds
- `ml_max` &mdash; max minlength time ot use in seconds
- `pr_min` &mdash; min priority to use
- `pr_max` &mdash; max priority to use
- `mx_min` &mdash; min maxlength time to use in seconds
- `mx_max` &mdash; max maxlength time ot use in seconds


**Returns:**<br>
list of created slices.

---

### def _mas_build_random_fake_slice(flt, ml_min, ml_max, pr_min, pr_max, mx_min, mx_max)

Builds a fake slice with the given filter name and randomized minlength and pr based on the given values

**Parameters:**
- `flt` &mdash; filter name to use


**Returns:**<br>
MASBackgroundFilterSlice object

---

### def _mas_qb_alg_test(spread=False)

Test alg and write output to log

**Parameters:**
- `spread` &mdash; pass True to use expand_sld instead of expand_once


---

### def _mas_qb_fast_a(abc)

Pass in a mbgfm, unbuilt

---

### def _mas_qb_fast()

Makes somethign and writes it out

---

### def _m1_zz_submods__build_override_label_to_base_label_map()

Populates a lookup dict for all label overrides which are in effect

**Decorators:**
- `@store.mas_submod_utils.functionplugin('ch30_reset', priority=-999)`


---

