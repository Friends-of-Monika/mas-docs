## Functions

### def check_prompt(key)

Checks if the prompt's rule passes.

**Parameters:**
- `key` &mdash; select key


**Returns:**<br>
True if prompt's rule passes (or doesnt exist), False if not.

### def get_prompt(key, prompt_key='change')

Gets prompt with the given key and prompt key

**Parameters:**
- `key` &mdash; select key
- `prompt_key` &mdash; key to get prompt


**Returns:**<br>
prompt. "" if invalid

### def get_minitems(key, defval=1)

Gets minimum number of items required to unlock this selector.

**Parameters:**
- `key` &mdash; select key
- `defval` &mdash; default value to return


**Returns:**<br>
minimum number of items to unlock the selector.

### def in_prompt_map(key)

Checks if a key is in the prompt select map

**Parameters:**
- `key` &mdash; select key to check


**Returns:**<br>
True if in the map, FAlse if not

### def iter_prompt()

Creates an interable of prompt keys

**Returns:**<br>
iter (generator) of prompt keys

### def iter_prompt_data()

Creates an iterable of prompt map data

**Returns:**<br>
iter (generator) of tuples: [0]: prompt key [1]: prompt data

### def lock_prompt(key)

Locks ev with the given key

**Parameters:**
- `key` &mdash; select key


### def set_prompt(key, prompt_key='change')

Sets prompt of ev with the given key with one associatd with given prompt key.

**Parameters:**
- `key` &mdash; select key
- `prompt_key` &mdash; key to get propmt. if _ev, then no change


### def unlock_prompt(key)

Unlocks ev with the given key

**Parameters:**
- `key` &mdash; select key


### def startup_prompt_check()

Checks all prompts and adjusts them if needed

### def check_prompt(key)

Checks if the prompt's rule passes.

**Parameters:**
- `key` &mdash; select key


**Returns:**<br>
True if prompt's rule passes (or doesnt exist), False if not.

### def get_prompt(key, prompt_key='change')

Gets prompt with the given key and prompt key

**Parameters:**
- `key` &mdash; select key
- `prompt_key` &mdash; key to get prompt


**Returns:**<br>
prompt. "" if invalid

### def get_minitems(key, defval=1)

Gets minimum number of items required to unlock this selector.

**Parameters:**
- `key` &mdash; select key
- `defval` &mdash; default value to return


**Returns:**<br>
minimum number of items to unlock the selector.

### def in_prompt_map(key)

Checks if a key is in the prompt select map

**Parameters:**
- `key` &mdash; select key to check


**Returns:**<br>
True if in the map, FAlse if not

### def iter_prompt()

Creates an interable of prompt keys

**Returns:**<br>
iter (generator) of prompt keys

### def iter_prompt_data()

Creates an iterable of prompt map data

**Returns:**<br>
iter (generator) of tuples: [0]: prompt key [1]: prompt data

### def lock_prompt(key)

Locks ev with the given key

**Parameters:**
- `key` &mdash; select key


### def set_prompt(key, prompt_key='change')

Sets prompt of ev with the given key with one associatd with given prompt key.

**Parameters:**
- `key` &mdash; select key
- `prompt_key` &mdash; key to get propmt. if _ev, then no change


### def unlock_prompt(key)

Unlocks ev with the given key

**Parameters:**
- `key` &mdash; select key


### def startup_prompt_check()

Checks all prompts and adjusts them if needed

### def selectable_key(selectable)

Returns the display name of a selectable. meant for sorting.

**Parameters:**
- `selectable` &mdash; the selectbale to get key for


**Returns:**<br>
the display name of the selectable

### def create_selectable_remover(acs_type, group, remover_name=None)

Creates a selectable remover for acs

**Parameters:**
- `acs_type` &mdash; acs type of the acs/remover to make
- `group` &mdash; group of selectables this ACS remover should be linked to
- `remover_name` &mdash; the name to use for the remover. If None, we use "Remove"


**Returns:**<br>
remover ACS selectable

### def rm_selectable_remover(remover_sel)

Removes a selectable remover for acs.

**Parameters:**
- `remover_sel` &mdash; remover selectable to remove


### def init_selectable_acs(acs, display_name, thumb, group, visible_when_locked=True, hover_dlg=None, first_select_dlg=None, select_dlg=None, remover=False)

Inits the selectable acs

**Parameters:**
- `acs` &mdash; the acs to create a selectable from
- `display_name` &mdash; display name to use
- `thumb` &mdash; thumbnail image
- `group` &mdash; grouping id
- `visible_when_locked` &mdash; True if this should be visible even if locked (Default: True)
- `hover_dlg` &mdash; list of dialogue to say when the item is hovered over (Default: None)
- `first_select_dlg` &mdash; list of dialogue to say when the item is selected for the first time (Default: None)
- `select_dlg` &mdash; list of dialogue to say when the item is selected after the first time (Default: None)
- `remover` &mdash; True if this ACS is a blank one, False otherwise (Default: False)


### def init_selectable_clothes(clothes, display_name, thumb, group, visible_when_locked=True, hover_dlg=None, first_select_dlg=None, select_dlg=None)

Inits the selectable clothes

**Parameters:**
- `clothes` &mdash; the clothes to create selectable from
- `display_name` &mdash; display name to use
- `thumb` &mdash; thumbnail image
- `group` &mdash; grouping id
- `visible_when_locked` &mdash; True if this should be visible even if locked (Default: True)
- `hover_dlg` &mdash; list of dialogue to say when the item is hovered over (Default: None)
- `first_select_dlg` &mdash; list of dialogue to say when the item is selected for the first time (Default: None)
- `select_dlg` &mdash; list of dialogue to say when the item is selected after the first time (Default: None)


### def init_selectable_hair(hair, display_name, thumb, group, visible_when_locked=True, hover_dlg=None, first_select_dlg=None, select_dlg=None)

Inits the selectable hair

**Parameters:**
- `hair` &mdash; the hair to create a selectable from
- `display_name` &mdash; display name to use
- `thumb` &mdash; thumbnail image
- `group` &mdash; grouping id
- `visible_when_locked` &mdash; True if this should be visible even if locked (Default: True)
- `hover_dlg` &mdash; list of dialogue to say when the item is hovered over (Default: None)
- `first_select_dlg` &mdash; list of dialogue to say when the item is selected for the first time (Default: None)
- `select_dlg` &mdash; list of dialogue to say when the item is selected after the first time (Default: None)


### def valid_select_type(sel_con)

Returns True if valid selection constant, False otherwise

**Parameters:**
- `sel_con` &mdash; selection constnat to check


**Returns:**<br>
True if vali dselection constant

### def is_same(old_map_view, new_map_view)

Compares the given select map views for differences.

**Parameters:**
- `old_map_view` &mdash; viewkeys view of the old map
- `new_map_view` &mdash; viewkeys view of the new map


**Returns:**<br>
True if the maps are the same, false if different.

### def save_selectables()

Goes through the selectables and saves their unlocked property.

### def load_selectables()

Loads the persistent data into selectables.

### def filter_acs(unlocked, group=None)

Filters the selectable acs based on criteria

**Parameters:**
- `unlocked` &mdash; True means we only match unlocked selectables
- `group` &mdash; non-None means we match selectables that match this group if None, we don't check group at all. (Default: None)


**Returns:**<br>
list of selectable acs that match criteria

### def filter_clothes(unlocked, group=None)

Filters the selectable clothes based on critera

**Parameters:**
- `unlocked` &mdash; True means we only match unlocked selectables
- `group` &mdash; non-None means we match selectables that match this group if None, we don't check group at all (Default: None)


**Returns:**<br>
list of selectable clothes that match criteria

### def filter_hair(unlocked, group=None)

Filters the selectable hair based on critera

**Parameters:**
- `unlocked` &mdash; True means we only match unlocked selectables
- `group` &mdash; non-None means we match selectables that match this group if None, we don't check group at all (Default: None)


**Returns:**<br>
list of selectable hair that match criteria

### def get_sel(item)

Retrieves the selectable for the given item This uses sprite object type from jsons.

**Parameters:**
- `item` &mdash; sprite objct to find the Selectable for


**Returns:**<br>
selectable for the given item

### def get_sel_acs(acs)

Retrieves the selectable for the given accessory.

**Parameters:**
- `acs` &mdash; MASAccessory object to find selectable for


**Returns:**<br>
the selectable for this acs, or None if not found.

### def get_sel_clothes(clothes)

Retrieves the selectable for the given clothes

**Parameters:**
- `clothes` &mdash; MASClothes object to find selectable for


**Returns:**<br>
the selectable for these clothes, or None if not found

### def get_sel_hair(hair)

Retrieves the selectable for the given hair

**Parameters:**
- `hair` &mdash; MASHair object to find selectbale for


**Returns:**<br>
the selectable for this hair, or none if not found

### def is_hairacs_compatible(hair, acs_sel)

Wrapper around mas_sprites.is_hairacs_compatible that uses an ACS selector.

**Parameters:**
- `hair` &mdash; hair to check
- `acs_sel` &mdash; ACS selector to check


**Returns:**<br>
True if hair+acs is compatible, False if not

### def is_clotheshair_compatible(clothes, hair_sel)

Wrapper around mas_sprites.is_clotheshair_compatible that uses a hair selector.

**Parameters:**
- `clothes` &mdash; clothes to check
- `hair_sel` &mdash; hair selector to check


**Returns:**<br>
True if clothes+hair is compatible, false if not

### def lock_acs(acs)

Locks the given accessory's selectable

**Parameters:**
- `acs` &mdash; MASAccessory object to lock


### def lock_clothes(clothes)

Locks the given clothes' selectable

**Parameters:**
- `clothes` &mdash; MASClothes object to lock


### def lock_hair(hair)

locks the given hair's selectable

**Parameters:**
- `hair` &mdash; MASHair object to lock


### def set_compat_acs(acs_sels, hair)

Checks compatibility of the given list of acs selectors to the given hair sprite object and sets appropriate flags

**Parameters:**
- `acs_sels` &mdash; list of acs selectors to check
- `hair` &mdash; hair sprite object to check


**Returns:**<br>
acs_sels - acs selectors with modified flags for compatibility

### def set_compat_hair(hair_sels, clothes)

Checks compatiblity of the given list of hair selectors to the given clothing sprite object and sets appropriate flags.

**Parameters:**
- `hair_sels` &mdash; list of hair selectors to check
- `clothes` &mdash; clothing sprite object to check


**Returns:**<br>
hair_sels - hair selectors with modified flags for compatibility

### def unlock_acs(acs)

Unlocks the given accessory's selectable

**Parameters:**
- `acs` &mdash; MASAccessory object to unlock


### def unlock_clothes(clothes)

Unlocks the given clothes' selectable

**Parameters:**
- `clothes` &mdash; MASClothes object to unlock


### def unlock_hair(hair)

Unlocks the given hair's selectable

**Parameters:**
- `hair` &mdash; MASHair object to unlock


### def unlock_selector(group)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `unlock_prompt`.

DEPRECATED - Use unlock_prompt instead Unlocks the selector of the given group.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='unlock_prompt', should_raise=True)`


**Parameters:**
- `group` &mdash; group to unlock selector topic.


### def json_sprite_unlock(sp_obj, unlock_label=True)

RUNTIME ONLY Unlocks selectable for the given sprite, as ewll as the selector topic for that sprite.

**Parameters:**
- `sp_obj` &mdash; sprite object to unlock selectbale+
- `unlock_label` &mdash; True will unlock the selector lable, False will not (Default: True)


### def selector_adj_ranged_callback(adj)

This is called by an adjustment of the twopane menu when its range is being changed (set)

**Parameters:**
- `adj` &mdash; the adj object


### def selector_search_callback(search_query)

The selector screen input callback.

**Parameters:**
- `search_query` &mdash; search query to filter and sort by


### def mas_item_name_format(item_name)

Formats acs name to be sentence case, with spaces, and pluralized

**Parameters:**
- `item_name` &mdash; the text to be formatted


**Returns:**<br>
item_name - formatted

### def selectable_key(selectable)

Returns the display name of a selectable. meant for sorting.

**Parameters:**
- `selectable` &mdash; the selectbale to get key for


**Returns:**<br>
the display name of the selectable

### def create_selectable_remover(acs_type, group, remover_name=None)

Creates a selectable remover for acs

**Parameters:**
- `acs_type` &mdash; acs type of the acs/remover to make
- `group` &mdash; group of selectables this ACS remover should be linked to
- `remover_name` &mdash; the name to use for the remover. If None, we use "Remove"


**Returns:**<br>
remover ACS selectable

### def rm_selectable_remover(remover_sel)

Removes a selectable remover for acs.

**Parameters:**
- `remover_sel` &mdash; remover selectable to remove


### def init_selectable_acs(acs, display_name, thumb, group, visible_when_locked=True, hover_dlg=None, first_select_dlg=None, select_dlg=None, remover=False)

Inits the selectable acs

**Parameters:**
- `acs` &mdash; the acs to create a selectable from
- `display_name` &mdash; display name to use
- `thumb` &mdash; thumbnail image
- `group` &mdash; grouping id
- `visible_when_locked` &mdash; True if this should be visible even if locked (Default: True)
- `hover_dlg` &mdash; list of dialogue to say when the item is hovered over (Default: None)
- `first_select_dlg` &mdash; list of dialogue to say when the item is selected for the first time (Default: None)
- `select_dlg` &mdash; list of dialogue to say when the item is selected after the first time (Default: None)
- `remover` &mdash; True if this ACS is a blank one, False otherwise (Default: False)


### def init_selectable_clothes(clothes, display_name, thumb, group, visible_when_locked=True, hover_dlg=None, first_select_dlg=None, select_dlg=None)

Inits the selectable clothes

**Parameters:**
- `clothes` &mdash; the clothes to create selectable from
- `display_name` &mdash; display name to use
- `thumb` &mdash; thumbnail image
- `group` &mdash; grouping id
- `visible_when_locked` &mdash; True if this should be visible even if locked (Default: True)
- `hover_dlg` &mdash; list of dialogue to say when the item is hovered over (Default: None)
- `first_select_dlg` &mdash; list of dialogue to say when the item is selected for the first time (Default: None)
- `select_dlg` &mdash; list of dialogue to say when the item is selected after the first time (Default: None)


### def init_selectable_hair(hair, display_name, thumb, group, visible_when_locked=True, hover_dlg=None, first_select_dlg=None, select_dlg=None)

Inits the selectable hair

**Parameters:**
- `hair` &mdash; the hair to create a selectable from
- `display_name` &mdash; display name to use
- `thumb` &mdash; thumbnail image
- `group` &mdash; grouping id
- `visible_when_locked` &mdash; True if this should be visible even if locked (Default: True)
- `hover_dlg` &mdash; list of dialogue to say when the item is hovered over (Default: None)
- `first_select_dlg` &mdash; list of dialogue to say when the item is selected for the first time (Default: None)
- `select_dlg` &mdash; list of dialogue to say when the item is selected after the first time (Default: None)


### def valid_select_type(sel_con)

Returns True if valid selection constant, False otherwise

**Parameters:**
- `sel_con` &mdash; selection constnat to check


**Returns:**<br>
True if vali dselection constant

### def is_same(old_map_view, new_map_view)

Compares the given select map views for differences.

**Parameters:**
- `old_map_view` &mdash; viewkeys view of the old map
- `new_map_view` &mdash; viewkeys view of the new map


**Returns:**<br>
True if the maps are the same, false if different.

### def save_selectables()

Goes through the selectables and saves their unlocked property.

### def load_selectables()

Loads the persistent data into selectables.

### def filter_acs(unlocked, group=None)

Filters the selectable acs based on criteria

**Parameters:**
- `unlocked` &mdash; True means we only match unlocked selectables
- `group` &mdash; non-None means we match selectables that match this group if None, we don't check group at all. (Default: None)


**Returns:**<br>
list of selectable acs that match criteria

### def filter_clothes(unlocked, group=None)

Filters the selectable clothes based on critera

**Parameters:**
- `unlocked` &mdash; True means we only match unlocked selectables
- `group` &mdash; non-None means we match selectables that match this group if None, we don't check group at all (Default: None)


**Returns:**<br>
list of selectable clothes that match criteria

### def filter_hair(unlocked, group=None)

Filters the selectable hair based on critera

**Parameters:**
- `unlocked` &mdash; True means we only match unlocked selectables
- `group` &mdash; non-None means we match selectables that match this group if None, we don't check group at all (Default: None)


**Returns:**<br>
list of selectable hair that match criteria

### def get_sel(item)

Retrieves the selectable for the given item This uses sprite object type from jsons.

**Parameters:**
- `item` &mdash; sprite objct to find the Selectable for


**Returns:**<br>
selectable for the given item

### def get_sel_acs(acs)

Retrieves the selectable for the given accessory.

**Parameters:**
- `acs` &mdash; MASAccessory object to find selectable for


**Returns:**<br>
the selectable for this acs, or None if not found.

### def get_sel_clothes(clothes)

Retrieves the selectable for the given clothes

**Parameters:**
- `clothes` &mdash; MASClothes object to find selectable for


**Returns:**<br>
the selectable for these clothes, or None if not found

### def get_sel_hair(hair)

Retrieves the selectable for the given hair

**Parameters:**
- `hair` &mdash; MASHair object to find selectbale for


**Returns:**<br>
the selectable for this hair, or none if not found

### def is_hairacs_compatible(hair, acs_sel)

Wrapper around mas_sprites.is_hairacs_compatible that uses an ACS selector.

**Parameters:**
- `hair` &mdash; hair to check
- `acs_sel` &mdash; ACS selector to check


**Returns:**<br>
True if hair+acs is compatible, False if not

### def is_clotheshair_compatible(clothes, hair_sel)

Wrapper around mas_sprites.is_clotheshair_compatible that uses a hair selector.

**Parameters:**
- `clothes` &mdash; clothes to check
- `hair_sel` &mdash; hair selector to check


**Returns:**<br>
True if clothes+hair is compatible, false if not

### def lock_acs(acs)

Locks the given accessory's selectable

**Parameters:**
- `acs` &mdash; MASAccessory object to lock


### def lock_clothes(clothes)

Locks the given clothes' selectable

**Parameters:**
- `clothes` &mdash; MASClothes object to lock


### def lock_hair(hair)

locks the given hair's selectable

**Parameters:**
- `hair` &mdash; MASHair object to lock


### def set_compat_acs(acs_sels, hair)

Checks compatibility of the given list of acs selectors to the given hair sprite object and sets appropriate flags

**Parameters:**
- `acs_sels` &mdash; list of acs selectors to check
- `hair` &mdash; hair sprite object to check


**Returns:**<br>
acs_sels - acs selectors with modified flags for compatibility

### def set_compat_hair(hair_sels, clothes)

Checks compatiblity of the given list of hair selectors to the given clothing sprite object and sets appropriate flags.

**Parameters:**
- `hair_sels` &mdash; list of hair selectors to check
- `clothes` &mdash; clothing sprite object to check


**Returns:**<br>
hair_sels - hair selectors with modified flags for compatibility

### def unlock_acs(acs)

Unlocks the given accessory's selectable

**Parameters:**
- `acs` &mdash; MASAccessory object to unlock


### def unlock_clothes(clothes)

Unlocks the given clothes' selectable

**Parameters:**
- `clothes` &mdash; MASClothes object to unlock


### def unlock_hair(hair)

Unlocks the given hair's selectable

**Parameters:**
- `hair` &mdash; MASHair object to unlock


### def unlock_selector(group)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `unlock_prompt`.

DEPRECATED - Use unlock_prompt instead Unlocks the selector of the given group.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='unlock_prompt', should_raise=True)`


**Parameters:**
- `group` &mdash; group to unlock selector topic.


### def json_sprite_unlock(sp_obj, unlock_label=True)

RUNTIME ONLY Unlocks selectable for the given sprite, as ewll as the selector topic for that sprite.

**Parameters:**
- `sp_obj` &mdash; sprite object to unlock selectbale+
- `unlock_label` &mdash; True will unlock the selector lable, False will not (Default: True)


### def selector_adj_ranged_callback(adj)

This is called by an adjustment of the twopane menu when its range is being changed (set)

**Parameters:**
- `adj` &mdash; the adj object


### def selector_search_callback(search_query)

The selector screen input callback.

**Parameters:**
- `search_query` &mdash; search query to filter and sort by


### def mas_item_name_format(item_name)

Formats acs name to be sentence case, with spaces, and pluralized

**Parameters:**
- `item_name` &mdash; the text to be formatted


**Returns:**<br>
item_name - formatted

