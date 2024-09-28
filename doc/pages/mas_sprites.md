## Functions

### def apply_ACSTemplate(acs)

Applies ACS template to the given ACS

**Parameters:**
- `acs` &mdash; acs to apply defaults to


### def apply_ACSTemplates()

RUNTIME ONLY Applies all templates to the available ACS.

### def get_ACSTemplate(acs)

Gets the template for an ACS given the ACS.

**Parameters:**
- `acs` &mdash; acs to get template for


**Returns:**<br>
ACSTemplate associated with the acs, or None if not found

### def get_ACSTemplate_by_type(acs_type)

Gets the template for an ACS given the ACS type

**Parameters:**
- `acs_type` &mdash; acs type to get template for


**Returns:**<br>
ACSTemplate associated with the acs_type or Nonr if not ound

### def add_filter(flt_enum, imx, base=None)

Adds a filter to the global filters You can also use this to override built-in filters.

**Parameters:**
- `flt_enum` &mdash; enum key to use as a filter.
- `imx` &mdash; image matrix to use as filter
- `base` &mdash; filter to use as a backup for this filter. Any images that are unable to be shown for flt_enum will be revert to the base filter. This should also be a FLT_ENUM. This is checked to make sure it is a valid, preexisting enum, so if chaining multiple bases, add them in order. If None, no base is given for the flt. (Default: None)


### def get_filter()

Returns the current filter

**Returns:**<br>
filter to use

### def is_filter(flt)

Checks if the given filter is a valid filter

**Parameters:**
- `flt` &mdash; filter enum to check


**Returns:**<br>
True if valid filter, False if not

### def set_filter(flt_enum)

Sets the current filter if it is valid. Invalid filters are ignored.

**Parameters:**
- `flt_enum` &mdash; filter to set


### def add_filter(flt_enum, imx, base=None)

Adds a filter to the global filters You can also use this to override built-in filters.

**Parameters:**
- `flt_enum` &mdash; enum key to use as a filter.
- `imx` &mdash; image matrix to use as filter
- `base` &mdash; filter to use as a backup for this filter. Any images that are unable to be shown for flt_enum will be revert to the base filter. This should also be a FLT_ENUM. This is checked to make sure it is a valid, preexisting enum, so if chaining multiple bases, add them in order. If None, no base is given for the flt. (Default: None)


### def get_filter()

Returns the current filter

**Returns:**<br>
filter to use

### def is_filter(flt)

Checks if the given filter is a valid filter

**Parameters:**
- `flt` &mdash; filter enum to check


**Returns:**<br>
True if valid filter, False if not

### def set_filter(flt_enum)

Sets the current filter if it is valid. Invalid filters are ignored.

**Parameters:**
- `flt_enum` &mdash; filter to set


### def alt_bcode(v_list, prefix, inc_night)

Adds bcode 0 and bcode 1 versions of the given prefix to the given list.

**Parameters:**
- `prefix` &mdash; string to add bcode to
- `inc_night` &mdash; if True, then we also do night variants of each bcode version, otherwise, just day versions


**Returns:**<br>
v_list - list to add strings to

### def alt_hsplit(v_list, prefix, inc_night)

Adds backhair/front hair versionsof the given prefix to the given list

**Parameters:**
- `prefix` &mdash; string to add bhair/front hair to
- `inc_night` &mdash; if Ture, then we also do night varaints of each bhair fhair version, otherwise just day versions


**Returns:**<br>
v_list - list to add strings to

### def adjust_zoom()

Sets the value zoom to an appropraite amoutn based on the current zoom level.

### def reset_zoom()

Resets the zoom to the default value

### def zoom_out()

zooms out to the farthest zoom level

### def tryparsehair(_hair, default='def')

Returns the given hair if it exists, or the default if not exist

**Parameters:**
- `_hair` &mdash; hair to check for existence
- `default` &mdash; default if hair dont exist


**Returns:**<br>
the hair if it exists, or default if not

### def tryparseclothes(_clothes, default='def')

Returns the given clothes if it exists, or the default if not exist

**Parameters:**
- `_clothes` &mdash; clothes to check for existence
- `default` &mdash; default if clothes dont exist


**Returns:**<br>
the clothes if it exists, or default if not

### def acs_lean_mode(sprite_list, lean)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@store.mas_utils.deprecated(should_raise=True)`


**Parameters:**
- `sprite_list` &mdash; list to add sprites to
- `lean` &mdash; type of lean


### def face_lean_mode(lean)

Returns the appropriate face prefix depending on lean

**Parameters:**
- `lean` &mdash; type of lean


**Returns:**<br>
appropriat eface prefix string

### def create_remover(acs_type, group, mux_types)

Creates a remover ACS

**Parameters:**
- `acs_type` &mdash; acs type for the remover. This is also used in mux_type
- `group` &mdash; group of selectables this ACS remover should be linked to This is used in the naming of the ACS.
- `mux_types` &mdash; list of types to use for mux_type


**Returns:**<br>
remover ACS object

### def get_acs(acs_name)

Gets the ACS object for a given name from the ACS map

**Parameters:**
- `acs_name` &mdash; name of the ACS to get


**Returns:**<br>
ACS object, or None if no acs object with the given name

### def get_acs_of_type(acs_type)

Gets all ACS objects for a given ACS type.

**Parameters:**
- `acs_type` &mdash; type of ACS to get


**Returns:**<br>
list of ACS objects with the given type. list may be empty if no ACS of the given type

### def init_acs(mas_acs)

Initlializes the given MAS accessory into a dictionary map setting

**Parameters:**
- `mas_acs` &mdash; MASAccessory to initialize


### def init_hair(mas_hair)

Initlializes the given MAS hairstyle into a dictionary map setting

**Parameters:**
- `mas_hair` &mdash; MASHair to initialize


### def init_clothes(mas_cloth)

Initlializes the given MAS clothes into a dictionary map setting

**Parameters:**
- `mas_clothes` &mdash; MASClothes to initialize


### def rm_acs(acs)

Deletes an ACS by removing it from the map

**Parameters:**
- `acs` &mdash; ACS to remove


### def lock_exprop_topics(exprop)

Locks topics with the given exprop

**Parameters:**
- `exprop` &mdash; extended property to lock associated topics wtih


### def lock_acstype_topics(acs_type)

Locks topics with the given acs type

**Parameters:**
- `acstype` &mdash; acs type to lock assicated topics with


### def unlock_exprop_topics(exprop)

Unlocks topics with the given exprop

**Parameters:**
- `exprop` &mdash; extended property to unlock associated topics with


### def unlock_acstype_topics(acs_type)

Unlocks topics with the given acs type

**Parameters:**
- `acstype` &mdash; acs type to unlock associated topics with


### def should_disable_lean(lean, arms, character)

Figures out if we need to disable the lean or not based on current character settings

**Parameters:**
- `lean` &mdash; lean type we want to do
- `arms` &mdash; arms type involved with lean
- `character` &mdash; MASMonika object


**Returns:**<br>
True if we should disable lean, False otherwise

### def build_loc()

**Returns:**<br>
location string for the sprite

### def build_loc_val()

**Returns:**<br>
location tuple for a sprite

### def get_sprite(sprite_type, sprite_name)

Returns the sprite object with the given sprite name and sprite type. Or None if we couldn't find one.

### def get_installed_sprites(sprite_type, predicate=None)

Returns ALL available sprite objects

**Parameters:**
- `sprite_type` &mdash; the sprite type constant
- `predicate` &mdash; the predicate function (Default: None)


**Returns:**<br>
list of sprite objects

### def get_installed_acs(predicate=None)

get_installed_sprites for acs objects

**Parameters:**
- `predicate` &mdash; the predicate function (Default: None)


**Returns:**<br>
list of acs sprite objects

### def get_installed_hair(predicate=None)

get_installed_sprites for hair objects

**Parameters:**
- `predicate` &mdash; the predicate function (Default: None)


**Returns:**<br>
list of hair sprite objects

### def get_installed_clothes(predicate=None)

get_installed_sprites for clothes objects

**Parameters:**
- `predicate` &mdash; the predicate function (Default: None)


**Returns:**<br>
list of clothes sprite objects

### def acs_rm_exit_pre_change(temp_space, moni_chr, rm_acs, acs_loc)

Runs before exit point runs for acs

**Parameters:**
- `temp_space` &mdash; temp space
- `moni_chr` &mdash; MASMonika object
- `rm_acs` &mdash; acs we are removing
- `acs_loc` &mdash; acs location to rm this acs from


### def acs_rm_exit_pst_change(temp_space, moni_chr, rm_acs, acs_loc)

Runs after exit point runs runs for acs

**Parameters:**
- `temp_space` &mdash; temp space
- `moni_chr` &mdash; MASMonika object
- `rm_acs` &mdash; acs we are removing
- `acs_loc` &mdash; acs location to rm this acs from


### def acs_rm_exit_pst_removal(temp_space, moni_chr, rm_acs, acs_loc)

Runs after the ACS is removed

**Parameters:**
- `temp_space` &mdash; temp space
- `moni_chr` &mdash; MASMonika object
- `rm_acs` &mdash; acs we are removing
- `acs_loc` &mdash; acs location the ACS was removed from


### def acs_wear_mux_pre_change(temp_space, moni_chr, new_acs, acs_loc)

Runs before mux type acs are removed

**Parameters:**
- `temp_space` &mdash; temp space
- `moni_chr` &mdash; MASMonika object
- `new_acs` &mdash; acs we are adding
- `acs_loc` &mdash; acs location to wear this acs


### def acs_wear_mux_pst_change(temp_space, moni_chr, new_acs, acs_loc)

Runs after mux type acs removed, before insertion

**Parameters:**
- `moni_chr` &mdash; MASMonika object
- `new_acs` &mdash; acs we are adding
- `acs_loc` &mdash; acs location to wear this acs


### def acs_wear_entry_pre_change(temp_space, moni_chr, new_acs, acs_loc)

Runs after insertion, before entry pooint

**Parameters:**
- `temp_space` &mdash; temp space
- `moni_chr` &mdash; MASmonika object
- `new_acs` &mdash; acs we are adding
- `acs_loc` &mdash; acs location to wear this acs


### def acs_wear_entry_pst_change(temp_space, moni_chr, new_acs, acs_loc)

Runs after entry point

**Parameters:**
- `temp_space` &mdash; temp space
- `moni_chr` &mdash; MASMonika object
- `new_acs` &mdash; acs we are adding
- `acs_loc` &mdash; acs location to wear this acs


### def clothes_exit_pre_change(temp_space, moni_chr, prev_cloth, new_cloth)

Runs pre clothes change code. This code is ran prior to clothes being changed and prior to exit prog point

**Parameters:**
- `temp_space` &mdash; temporary dictionary space
- `moni_chr` &mdash; MASMonika object
- `prev_cloth` &mdash; current clothes
- `new_cloth` &mdash; clothes we are changing to


### def clothes_exit_pst_change(temp_space, moni_chr, prev_cloth, new_cloth)

Runs after exit prog point is ran, before the actual change.

**Parameters:**
- `temp_space` &mdash; temp dict space
- `moni_chr` &mdash; MASMonika object
- `prev_cloth` &mdash; current clothes
- `new_cloth` &mdash; clothes we are changing to


### def clothes_entry_pre_change(temp_space, moni_chr, prev_cloth, new_cloth)

Runs after change, before entry prog point.

**Parameters:**
- `temp_space` &mdash; temp dict space
- `moni_chr` &mdash; MASMonika object
- `prev_cloth` &mdash; current clothes
- `new_cloth` &mdash; clothes we are changing to


### def clothes_entry_pst_change(temp_space, moni_chr, prev_cloth, new_cloth)

Runs after entry prog point

**Parameters:**
- `temp_space` &mdash; temp dict space
- `moni_chr` &mdash; MASMonika object
- `prev_cloth` &mdash; current clothes
- `new_cloth` &mdash; clothes we are changing to


### def hair_exit_pre_change(temp_space, moni_chr, prev_hair, new_hair)

Runs pre hair change code. This code is ran prior to hair being changed and prior to exit prog point.

**Parameters:**
- `temp_space` &mdash; temporary dictionary space
- `moni_chr` &mdash; MASMonika object
- `prev_hair` &mdash; current hair
- `new_hair` &mdash; hair we are changing to


### def hair_exit_pst_change(temp_space, moni_chr, prev_hair, new_hair)

Runs after exit prog point is ran, before the actual change.

**Parameters:**
- `temp_space` &mdash; temp dict space
- `moni_chr` &mdash; MASMonika object
- `prev_hair` &mdash; current hair
- `new_hair` &mdash; hair we are changing to


### def hair_entry_pre_change(temp_space, moni_chr, prev_hair, new_hair)

Runs after change, before entry prog point.

**Parameters:**
- `temp_space` &mdash; temp dict space
- `moni_chr` &mdash; MASMonika object
- `preV_hair` &mdash; current hair
- `new_hair` &mdash; hair we are changing to


### def hair_entry_pst_change(temp_space, moni_chr, prev_hair, new_hair)

Runs after entry prog point

**Parameters:**
- `temp_space` &mdash; temp dict space
- `moni_chr` &mdash; MASMonika object
- `prev_hair` &mdash; current hair
- `new_hair` &mdash; hair we are changing to


### def is_hairacs_compatible(hair, acs)

Checks if the given hair is compatible with the given acs

**Parameters:**
- `hair` &mdash; hair to check
- `acs` &mdash; acs to check


**Returns:**<br>
True if hair+acs is compatible, False if not

### def is_clotheshair_compatible(clothes, hair)

Checks if the given clothes is compatible with the given hair

**Parameters:**
- `clothes` &mdash; clothes to check
- `hair` &mdash; hair to check


**Returns:**<br>
True if clothes+hair is comaptible, False if not

### def use_bma(arm_id)

Returns base MASArm for an armid

**Parameters:**
- `arm_id` &mdash; numerical digit for an arm. Corresponds to NUM_ARMS


**Returns:**<br>
base MASArm for this arm, or None if no Arm

### def use_bmpm(posenum)

Returns tuple of MASArms for a pose num

**Parameters:**
- `posenum` &mdash; numerical digit for a pose. This corresponds to NUM_POSE.


**Returns:**<br>
base MASArms for this poes, or None if no arms

### def use_bmpm_s(leanpose)

Version of use_bpam that uses leanpose

**Parameters:**
- `leanpose` &mdash; leanpose string


**Returns:**<br>
base MASArms for this pose, or None if no arms

### def show_empty_desk()

shows empty desk

### def register_image(name, d)

Thanks for nothing, RenPy  Registers the existence of an image with `name`, and that the image used displayable d.

**Parameters:**
- `name` &mdash; tuple of strings (tag, attributes)
- `d` &mdash; displayables


### def needs_closed_eye_variant(exp)

Checks if an exp needs a closed eye variation

**Parameters:**
- `exp` &mdash; spritecode to check


**Returns:**<br>
boolean - True if the given spritecode needs a closed eye variant, False otherwise

### def is_wink_sprite(exp)

Checks if an exp is a wink sprite

**Parameters:**
- `exp` &mdash; spritecode to check


**Returns:**<br>
boolean - True if this is a wink sprite, False otherwise

### def is_follow_sprite(exp)

Checks if an exp is a follow sprite

**Parameters:**
- `exp` &mdash; spritecode to check


**Returns:**<br>
boolean - True if this is a follow sprite, False otherwise

### def needs_tear_atl(exp)

Checks if this spritecode needs a streaming tears atl

**Parameters:**
- `exp` &mdash; spritecode to check


**Returns:**<br>
boolean - True if so, False otherwise

### def replace_eyes(exp, replacement_eyes)

Returns the sprite string for the closed eye variant

**Parameters:**
- `exp` &mdash; exp to replace eyes
- `replacement_eyes` &mdash; spritecode part representing the replacement eyes


**Returns:**<br>
closed eye representation of the given spritecode

### def generate_static_sprite(exp)

Creates the DynamicDisplayable object for the given exp

**Parameters:**
- `exp` &mdash; exp to make a closed eye version of


### def generate_follow_sprite(exp)

Creates the follow version of the given sprite

### def add_static_sprite_alias(exp)

Registers an alias for static sprites

### def generate_normal_sprite(exp)

Generates sprites for standard open/closed eye variants  DOES NOT HANDLE WINKS

**Parameters:**
- `exp` &mdash; spritecode to generate sprites for


### def generate_wink_sprite(exp)

Generates wink sprites and their prerequisites

### def generate_images(exp)

Generates sprites, aliases, and their prerequisites and adds them to the renpy.display.image.images map

**Parameters:**
- `exp` &mdash; spritecode to generate


