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


### def _decide_filter()

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `get_filter`.

DEPRECATED Please use get_filter

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='get_filter', should_raise=True)`


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

### def _rslv_flt(flt)

Gets base filter for a flt.

**Parameters:**
- `flt` &mdash; flt to get base filter for


**Returns:**<br>
base flt for flt, or the flt itself if no base

### def set_filter(flt_enum)

Sets the current filter if it is valid. Invalid filters are ignored.

**Parameters:**
- `flt_enum` &mdash; filter to set


### def _test_filter(flt_enum)

Checks if this filter enum can be a filter enum.  Logs to mas log if there are errors

**Parameters:**
- `flt_enum` &mdash; filter enum to test


**Returns:**<br>
True if passed test, False if not

### def add_filter(flt_enum, imx, base=None)

Adds a filter to the global filters You can also use this to override built-in filters.

**Parameters:**
- `flt_enum` &mdash; enum key to use as a filter.
- `imx` &mdash; image matrix to use as filter
- `base` &mdash; filter to use as a backup for this filter. Any images that are unable to be shown for flt_enum will be revert to the base filter. This should also be a FLT_ENUM. This is checked to make sure it is a valid, preexisting enum, so if chaining multiple bases, add them in order. If None, no base is given for the flt. (Default: None)


### def _decide_filter()

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**<br>
> Instead, consider using `get_filter`.

DEPRECATED Please use get_filter

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='get_filter', should_raise=True)`


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

### def _rslv_flt(flt)

Gets base filter for a flt.

**Parameters:**
- `flt` &mdash; flt to get base filter for


**Returns:**<br>
base flt for flt, or the flt itself if no base

### def set_filter(flt_enum)

Sets the current filter if it is valid. Invalid filters are ignored.

**Parameters:**
- `flt_enum` &mdash; filter to set


### def _test_filter(flt_enum)

Checks if this filter enum can be a filter enum.  Logs to mas log if there are errors

**Parameters:**
- `flt_enum` &mdash; filter enum to test


**Returns:**<br>
True if passed test, False if not

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

### def _genLK(keys)

generates a tuple of keys + leanables using the given kens  Leanable Keys are keys prefixed with a lean type like: <lean>|<key>

**Parameters:**
- `keys` &mdash; iterable of keys to use


**Returns:**<br>
tuple of keys + leanable keys

### def _verify_uprightpose(val)

### def _verify_lean(val)

### def _verify_leaningpose(val)

### def _verify_pose(val, allow_none=True)

### def acs_lean_mode(sprite_list, lean)

> [!CAUTION]
> This function is flagged as **deprecated** and **will raise an error.**

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

### def _ms_head(clothing, hair, head)

Creates head string

**Parameters:**
- `clothing` &mdash; type of clothing
- `hair` &mdash; type of hair
- `head` &mdash; type of head


**Returns:**<br>
head string

### def _ms_left(clothing, hair, left)

Creates left side string

**Parameters:**
- `clothing` &mdash; type of clothing
- `hair` &mdash; type of hair
- `left` &mdash; type of left side


**Returns:**<br>
left side stirng

### def _ms_right(clothing, hair, right)

Creates right body string

**Parameters:**
- `clothing` &mdash; type of clothing
- `hair` &mdash; type of hair
- `right` &mdash; type of right side


**Returns:**<br>
right body string

### def _ms_standing(clothing, hair, head, left, right, acs_list)

Creates the custom standing string This is different than the stock ones because of image location

**Parameters:**
- `clothing` &mdash; type of clothing
- `hair` &mdash; type of hair
- `head` &mdash; type of head
- `left` &mdash; type of left side
- `right` &mdash; type of right side
- `acs_list` &mdash; list of MASAccessory objects NOTE: this should the combined list because we don't have layering in standing mode


**Returns:**<br>
custom standing sprite

### def _ms_standingstock(head, left, right, acs_list, single=None)

Creates the stock standing string This is different then the custom ones because of image location  Also no night version atm.

**Parameters:**
- `head` &mdash; type of head
- `left` &mdash; type of left side
- `right` &mdash; type of right side
- `acs_list` &mdash; list of MASAccessory objects NOTE: this should be the combined list because we don't have layering in standing mode
- `single` &mdash; type of single standing picture. (Defualt: None)


**Returns:**<br>
stock standing string

### def _clear_caches()

Clears all caches

### def _add_arms_rk(rk_list, arms, pfx, flt, bcode, clothing_t, leanpose)

Adds render key for multiple MASArm objects, if needed

**Parameters:**
- `arms` &mdash; MASArm objects to add render key for
- `pfx` &mdash; prefix tuple to generate image string with
- `flt` &mdash; filter code to use
- `bcode` &mdash; base code to use
- `clothing_t` &mdash; type of clothing to use
- `leanpose` &mdash; leanpose to use


**Returns:**<br>
rk_list - render key list to add render keys to

### def _bhli(img_list, hlcode)

Builds a High- Light Image using the base image path

**Parameters:**
- `img_list` &mdash; list of strings that form the base image string NOTE: we assume that the last item in this string is the FILE_EXT. This also assumes highlight codes are always inserted right before the file extension.
- `hlcode` &mdash; highlight code to use. Can be None.


**Returns:**<br>
Image to use for highlight, or None if no highlight.

### def _bhlifp(img_path, hlcode)

Builds a High- Light Image using an image's File Path

**Parameters:**
- `img_path` &mdash; full filepath to an image, including extension.
- `hlcode` &mdash; highlight code to use. Can be None


**Returns:**<br>
Image to use for highlight, or None if no highlight

### def _cgen_im(flt, key, cid, img_base)

Checks cache for an im, GENerates the im if not found

**Parameters:**
- `flt` &mdash; filter to use
- `key` &mdash; key of the image
- `cid` &mdash; cache ID of the cache to use
- `img_base` &mdash; ImageBase to build the image


**Returns:**<br>
Image Manipulator for this render

### def _cgha_im(render_list, flt, render_key)

Checks cache of an image Generates the im if not found, and sets Highlight if needed. Adds IMs to the given render list

**Parameters:**
- `flt` &mdash; filter to use
- `render_key` &mdash; tuple of the following format: [0] - key of the image to generate [1] - cache ID of the cahce to use [2] - ImageBase to build the image [3] - ImageBase to build the highlight
- `st` &mdash; renpy related
- `at` &mdash; renpy related


**Returns:**<br>
render_list - list to add IMs to

### def _cs_im(key, cid, img_base)

Checks cache for an im Stores the img_base if not found

**Parameters:**
- `key` &mdash; key of the image
- `cid` &mdash; cache ID of the cache to use
- `img_base` &mdash; ImageBase to build the image


**Returns:**<br>
ImageBase

### def _dayify(img_key)

Dayifies the given image key. DAying simply replaces the filter portion of the key with "day"

**Parameters:**
- `img_key` &mdash; image key to dayify


**Returns:**<br>
dayified key

### def _gc(cid)

Gets the Cache

**Parameters:**
- `cid` &mdash; cache ID of the cache to get


**Returns:**<br>
cache, or empty dict if cache not found

### def _gen_im(flt, img_base)

GENerates an image maniuplator

**Parameters:**
- `flt` &mdash; filter to use
- `img_base` &mdash; image path or manipulator to use


**Returns:**<br>
generated render key

### def _hlify(key, cid)

Highlightifies the given key. Highlightifying is just prefixing the key with the cid

**Parameters:**
- `key` &mdash; key to highlightify
- `cid` &mdash; cid to use when highlighting


**Returns:**<br>
highlightified key

### def _rk_accessory(rk_list, acs, flt, arm_split, leanpose=None)

Adds accessory render key if needed

**Parameters:**
- `acs` &mdash; MASAccessory object
- `flt` &mdash; filter to apply
- `arm_split` &mdash; see MASAccessory.arm_split for codes. None for no codes at all.
- `leanpose` &mdash; current pose (Default: None)


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_accessory_list(rk_list, acs_list, flt, leanpose=None, arm_split=None)

Adds accessory render keys for a list of accessories

**Parameters:**
- `acs_list` &mdash; list of MASAccessory objects, in order of rendering
- `flt` &mdash; filter to use
- `arm_split` &mdash; affected ACS. If None, we use standard algs.
- `leanpose` &mdash; arms pose for we are currently rendering (Default: None)


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_base_nh(rk_list, barms, leanpose, flt, bcode)

Adds arms base render keys (equiv to _ms_arms_nh_up_base)

**Parameters:**
- `barms` &mdash; tuple of MASArm objects to use
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_base_lean_nh(rk_list, barms, lean, leanpose, flt, bcode)

Adds arms base lean render key (eqiv to _ms_arms_nh_leaning_base)

**Parameters:**
- `barms` &mdash; tuple of MASArm objects to use
- `lean` &mdash; type of lean
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_nh(rk_list, parms, clothing, leanpose, flt, bcode)

Adds arms render key (equiv to _ms_arms_nh_up_arms)

**Parameters:**
- `parms` &mdash; tuple of MASArm objects to use
- `clothing` &mdash; MASClothes object
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_lean_nh(rk_list, parms, clothing, lean, leanpose, flt, bcode)

Adds arms lean render key (equiv to _ms_arms_nh_leaning_arms)

**Parameters:**
- `parms` &mdash; tuple of MASArm objects to use
- `clothing` &mdash; MASClothes object
- `lean` &mdash; type of lean
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_nh_wbase(rk_list, barms, parms, clothing, acs_ase_list, leanpose, lean, flt, bcode)

Adds arms render keys, no hair, with baes

**Parameters:**
- `barms` &mdash; tuple of MASArm objects for base
- `parms` &mdash; tuple of MASArm objects for pose
- `clothing` &mdash; MASClothes object
- `acs_ase_list` &mdash; acs between arms-base-0 and arms-0
- `leanpose` &mdash; leanpose to pass to accessorylist
- `lean` &mdash; lean to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_base_body_nh(rk_list, flt, bcode)

Adds base body render keys, no hair (equiv of _ms_torso_nh_base)

**Parameters:**
- `flt` &mdash; filter ot use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_base_body_lean_nh(rk_list, lean, flt, bcode)

Adds base body lean render keys, no hair (equivalent of _ms_torsoleaning_nh_base)

**Parameters:**
- `lean` &mdash; type of lean
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_body_nh(rk_list, clothing, flt, bcode)

Adds body render keys, no hair (equiv of _ms_torso_nh)

**Parameters:**
- `clothing` &mdash; MASClothes object
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_body_lean_nh(rk_list, clothing, lean, flt, bcode)

Adds body leaning render keys, no hair (equiv of _ms_torsoleaning_nh)

**Parameters:**
- `clothing` &mdash; MASClothes object
- `lean` &mdash; type of lean
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_body_nh_wbase(rk_list, clothing, acs_bse_list, bcode, flt, leanpose, lean=None)

Adds body render keys, including base and bse acs, no hair

**Parameters:**
- `clothing` &mdash; MASClothes object
- `acs_bse_list` &mdash; acs between base-0 and body-0
- `bcode` &mdash; base code to use
- `flt` &mdash; filter to use
- `leanpose` &mdash; leanpose to pass to accessorylist
- `lean` &mdash; type of lean


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_chair(rk_list, mtc, flt)

Adds chair render key

**Parameters:**
- `mtc` &mdash; MASTableChair object
- `flt` &mdash; filter to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_face(rk_list, eyes, eyebrows, nose, mouth, flt, fpfx, lean, sweat, tears, emote)

Adds face render keys

**Parameters:**
- `eyes` &mdash; type of eyes
- `eyebrows` &mdash; type of eyebrows
- `nose` &mdash; type of nose
- `mouth` &mdash; type of mouth
- `flt` &mdash; filter to use
- `fpfx` &mdash; face prefix to use
- `lean` &mdash; type of lean to use
- `sweat` &mdash; type of sweat drop
- `tears` &mdash; type of tears
- `emote` &mdash; type of emote


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_face_pre(rk_list, flt, fpfx, lean, blush)

Adds face render keys that go before hair

**Parameters:**
- `flt` &mdash; filter to use
- `fpfx` &mdash; face prefix to use
- `lean` &mdash; type of lean to use
- `blush` &mdash; type of blush


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_hair(rk_list, hair, flt, hair_key, lean, leanpose)

Adds hair render key

**Parameters:**
- `hair` &mdash; MASHair object
- `flt` &mdash; filter to use
- `hair_key` &mdash; hair key to use (front/back/mid)
- `lean` &mdash; tyoe of lean
- `leanpose` &mdash; leanpose


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_head(rk_list, flt, lean)

Adds head render keys.

**Parameters:**
- `bcode` &mdash; base code to use
- `flt` &mdash; filter to use
- `lean` &mdash; type of lean


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_table(rk_list, tablechair, show_shadow, flt)

Adds table render key

**Parameters:**
- `table` &mdash; MASTableChair object
- `show_shadow` &mdash; True if shadow should be included, false if not


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_sitting(clothing, hair, base_arms, pose_arms, eyebrows, eyes, nose, mouth, flt, acs_pre_list, acs_bbh_list, acs_bse_list, acs_bba_list, acs_ase_list, acs_bmh_list, acs_mhh_list, acs_bat_list, acs_mat_list, acs_mab_list, acs_bfh_list, acs_afh_list, acs_mid_list, acs_pst_list, leanpose, lean, arms, eyebags, sweat, blush, tears, emote, tablechair, show_shadow)

Creates a list of render keys in order of desired render.

**Parameters:**
- `clothing` &mdash; MASClothes object
- `hair` &mdash; MASHair object
- `base_arms` &mdash; tuple of MASArm objects to use for the base
- `pose_arms` &mdash; tuple of MASArm objects to use for the clothes arms
- `eyebrows` &mdash; type of eyebrows
- `eyes` &mdash; type of eyes
- `nose` &mdash; type of nose
- `mouth` &mdash; type of mouth
- `flt` &mdash; filter to use
- `acs_pre_list` &mdash; sorted list of MASAccessories to draw prior to body
- `acs_bbh_list` &mdash; sroted list of MASAccessories to draw between back hair and body
- `acs_bse_list` &mdash; sorted list of MASAccessories to draw between base body and outfit
- `acs_bba_list` &mdash; sorted list of MASAccessories to draw between body and back arms
- `acs_ase_list` &mdash; sorted list of MASAccessories to draw between base arms and outfit
- `acs_bmh_list` &mdash; sorted list of MASAccessories to draw betrween back arms and mid hair
- `acs_mmh_list` &mdash; sorted list of MASAccessories to draw between mid hair and head
- `acs_bat_list` &mdash; sorted list of MASAccessories to draw before table
- `acs_mat_list` &mdash; sorted list of MASAccessories to draw between middle arms and table
- `acs_mab_list` &mdash; sorted list of MASAccessories to draw between middle arms and boobs
- `acs_bfh_list` &mdash; sorted list of MASAccessories to draw between boobs and front hair
- `acs_afh_list` &mdash; sorted list of MASAccessories to draw between front hair and face
- `acs_mid_list` &mdash; sorted list of MASAccessories to draw between body and arms
- `acs_pst_list` &mdash; sorted list of MASAccessories to draw after arms
- `leanpose` &mdash; lean and arms together
- `lean` &mdash; type of lean
- `arms` &mdash; type of arms
- `eyebags` &mdash; type of eyebags
- `sweat` &mdash; type of sweatdrop
- `blush` &mdash; type of blush
- `tears` &mdash; type of tears
- `emote` &mdash; type of emote
- `tablechair` &mdash; MASTableChair object
- `show_shadow` &mdash; True will show shadow, false will not


**Returns:**<br>
list of render keys

### def _clear_caches()

Clears all caches

### def _add_arms_rk(rk_list, arms, pfx, flt, bcode, clothing_t, leanpose)

Adds render key for multiple MASArm objects, if needed

**Parameters:**
- `arms` &mdash; MASArm objects to add render key for
- `pfx` &mdash; prefix tuple to generate image string with
- `flt` &mdash; filter code to use
- `bcode` &mdash; base code to use
- `clothing_t` &mdash; type of clothing to use
- `leanpose` &mdash; leanpose to use


**Returns:**<br>
rk_list - render key list to add render keys to

### def _bhli(img_list, hlcode)

Builds a High- Light Image using the base image path

**Parameters:**
- `img_list` &mdash; list of strings that form the base image string NOTE: we assume that the last item in this string is the FILE_EXT. This also assumes highlight codes are always inserted right before the file extension.
- `hlcode` &mdash; highlight code to use. Can be None.


**Returns:**<br>
Image to use for highlight, or None if no highlight.

### def _bhlifp(img_path, hlcode)

Builds a High- Light Image using an image's File Path

**Parameters:**
- `img_path` &mdash; full filepath to an image, including extension.
- `hlcode` &mdash; highlight code to use. Can be None


**Returns:**<br>
Image to use for highlight, or None if no highlight

### def _cgen_im(flt, key, cid, img_base)

Checks cache for an im, GENerates the im if not found

**Parameters:**
- `flt` &mdash; filter to use
- `key` &mdash; key of the image
- `cid` &mdash; cache ID of the cache to use
- `img_base` &mdash; ImageBase to build the image


**Returns:**<br>
Image Manipulator for this render

### def _cgha_im(render_list, flt, render_key)

Checks cache of an image Generates the im if not found, and sets Highlight if needed. Adds IMs to the given render list

**Parameters:**
- `flt` &mdash; filter to use
- `render_key` &mdash; tuple of the following format: [0] - key of the image to generate [1] - cache ID of the cahce to use [2] - ImageBase to build the image [3] - ImageBase to build the highlight
- `st` &mdash; renpy related
- `at` &mdash; renpy related


**Returns:**<br>
render_list - list to add IMs to

### def _cs_im(key, cid, img_base)

Checks cache for an im Stores the img_base if not found

**Parameters:**
- `key` &mdash; key of the image
- `cid` &mdash; cache ID of the cache to use
- `img_base` &mdash; ImageBase to build the image


**Returns:**<br>
ImageBase

### def _dayify(img_key)

Dayifies the given image key. DAying simply replaces the filter portion of the key with "day"

**Parameters:**
- `img_key` &mdash; image key to dayify


**Returns:**<br>
dayified key

### def _gc(cid)

Gets the Cache

**Parameters:**
- `cid` &mdash; cache ID of the cache to get


**Returns:**<br>
cache, or empty dict if cache not found

### def _gen_im(flt, img_base)

GENerates an image maniuplator

**Parameters:**
- `flt` &mdash; filter to use
- `img_base` &mdash; image path or manipulator to use


**Returns:**<br>
generated render key

### def _hlify(key, cid)

Highlightifies the given key. Highlightifying is just prefixing the key with the cid

**Parameters:**
- `key` &mdash; key to highlightify
- `cid` &mdash; cid to use when highlighting


**Returns:**<br>
highlightified key

### def _rk_accessory(rk_list, acs, flt, arm_split, leanpose=None)

Adds accessory render key if needed

**Parameters:**
- `acs` &mdash; MASAccessory object
- `flt` &mdash; filter to apply
- `arm_split` &mdash; see MASAccessory.arm_split for codes. None for no codes at all.
- `leanpose` &mdash; current pose (Default: None)


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_accessory_list(rk_list, acs_list, flt, leanpose=None, arm_split=None)

Adds accessory render keys for a list of accessories

**Parameters:**
- `acs_list` &mdash; list of MASAccessory objects, in order of rendering
- `flt` &mdash; filter to use
- `arm_split` &mdash; affected ACS. If None, we use standard algs.
- `leanpose` &mdash; arms pose for we are currently rendering (Default: None)


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_base_nh(rk_list, barms, leanpose, flt, bcode)

Adds arms base render keys (equiv to _ms_arms_nh_up_base)

**Parameters:**
- `barms` &mdash; tuple of MASArm objects to use
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_base_lean_nh(rk_list, barms, lean, leanpose, flt, bcode)

Adds arms base lean render key (eqiv to _ms_arms_nh_leaning_base)

**Parameters:**
- `barms` &mdash; tuple of MASArm objects to use
- `lean` &mdash; type of lean
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_nh(rk_list, parms, clothing, leanpose, flt, bcode)

Adds arms render key (equiv to _ms_arms_nh_up_arms)

**Parameters:**
- `parms` &mdash; tuple of MASArm objects to use
- `clothing` &mdash; MASClothes object
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_lean_nh(rk_list, parms, clothing, lean, leanpose, flt, bcode)

Adds arms lean render key (equiv to _ms_arms_nh_leaning_arms)

**Parameters:**
- `parms` &mdash; tuple of MASArm objects to use
- `clothing` &mdash; MASClothes object
- `lean` &mdash; type of lean
- `leanpose` &mdash; leanpose to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_arms_nh_wbase(rk_list, barms, parms, clothing, acs_ase_list, leanpose, lean, flt, bcode)

Adds arms render keys, no hair, with baes

**Parameters:**
- `barms` &mdash; tuple of MASArm objects for base
- `parms` &mdash; tuple of MASArm objects for pose
- `clothing` &mdash; MASClothes object
- `acs_ase_list` &mdash; acs between arms-base-0 and arms-0
- `leanpose` &mdash; leanpose to pass to accessorylist
- `lean` &mdash; lean to use
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_base_body_nh(rk_list, flt, bcode)

Adds base body render keys, no hair (equiv of _ms_torso_nh_base)

**Parameters:**
- `flt` &mdash; filter ot use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_base_body_lean_nh(rk_list, lean, flt, bcode)

Adds base body lean render keys, no hair (equivalent of _ms_torsoleaning_nh_base)

**Parameters:**
- `lean` &mdash; type of lean
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_body_nh(rk_list, clothing, flt, bcode)

Adds body render keys, no hair (equiv of _ms_torso_nh)

**Parameters:**
- `clothing` &mdash; MASClothes object
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_body_lean_nh(rk_list, clothing, lean, flt, bcode)

Adds body leaning render keys, no hair (equiv of _ms_torsoleaning_nh)

**Parameters:**
- `clothing` &mdash; MASClothes object
- `lean` &mdash; type of lean
- `flt` &mdash; filter to use
- `bcode` &mdash; base code to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_body_nh_wbase(rk_list, clothing, acs_bse_list, bcode, flt, leanpose, lean=None)

Adds body render keys, including base and bse acs, no hair

**Parameters:**
- `clothing` &mdash; MASClothes object
- `acs_bse_list` &mdash; acs between base-0 and body-0
- `bcode` &mdash; base code to use
- `flt` &mdash; filter to use
- `leanpose` &mdash; leanpose to pass to accessorylist
- `lean` &mdash; type of lean


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_chair(rk_list, mtc, flt)

Adds chair render key

**Parameters:**
- `mtc` &mdash; MASTableChair object
- `flt` &mdash; filter to use


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_face(rk_list, eyes, eyebrows, nose, mouth, flt, fpfx, lean, sweat, tears, emote)

Adds face render keys

**Parameters:**
- `eyes` &mdash; type of eyes
- `eyebrows` &mdash; type of eyebrows
- `nose` &mdash; type of nose
- `mouth` &mdash; type of mouth
- `flt` &mdash; filter to use
- `fpfx` &mdash; face prefix to use
- `lean` &mdash; type of lean to use
- `sweat` &mdash; type of sweat drop
- `tears` &mdash; type of tears
- `emote` &mdash; type of emote


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_face_pre(rk_list, flt, fpfx, lean, blush)

Adds face render keys that go before hair

**Parameters:**
- `flt` &mdash; filter to use
- `fpfx` &mdash; face prefix to use
- `lean` &mdash; type of lean to use
- `blush` &mdash; type of blush


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_hair(rk_list, hair, flt, hair_key, lean, leanpose)

Adds hair render key

**Parameters:**
- `hair` &mdash; MASHair object
- `flt` &mdash; filter to use
- `hair_key` &mdash; hair key to use (front/back/mid)
- `lean` &mdash; tyoe of lean
- `leanpose` &mdash; leanpose


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_head(rk_list, flt, lean)

Adds head render keys.

**Parameters:**
- `bcode` &mdash; base code to use
- `flt` &mdash; filter to use
- `lean` &mdash; type of lean


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_table(rk_list, tablechair, show_shadow, flt)

Adds table render key

**Parameters:**
- `table` &mdash; MASTableChair object
- `show_shadow` &mdash; True if shadow should be included, false if not


**Returns:**<br>
rk_list - list to add render keys to

### def _rk_sitting(clothing, hair, base_arms, pose_arms, eyebrows, eyes, nose, mouth, flt, acs_pre_list, acs_bbh_list, acs_bse_list, acs_bba_list, acs_ase_list, acs_bmh_list, acs_mhh_list, acs_bat_list, acs_mat_list, acs_mab_list, acs_bfh_list, acs_afh_list, acs_mid_list, acs_pst_list, leanpose, lean, arms, eyebags, sweat, blush, tears, emote, tablechair, show_shadow)

Creates a list of render keys in order of desired render.

**Parameters:**
- `clothing` &mdash; MASClothes object
- `hair` &mdash; MASHair object
- `base_arms` &mdash; tuple of MASArm objects to use for the base
- `pose_arms` &mdash; tuple of MASArm objects to use for the clothes arms
- `eyebrows` &mdash; type of eyebrows
- `eyes` &mdash; type of eyes
- `nose` &mdash; type of nose
- `mouth` &mdash; type of mouth
- `flt` &mdash; filter to use
- `acs_pre_list` &mdash; sorted list of MASAccessories to draw prior to body
- `acs_bbh_list` &mdash; sroted list of MASAccessories to draw between back hair and body
- `acs_bse_list` &mdash; sorted list of MASAccessories to draw between base body and outfit
- `acs_bba_list` &mdash; sorted list of MASAccessories to draw between body and back arms
- `acs_ase_list` &mdash; sorted list of MASAccessories to draw between base arms and outfit
- `acs_bmh_list` &mdash; sorted list of MASAccessories to draw betrween back arms and mid hair
- `acs_mmh_list` &mdash; sorted list of MASAccessories to draw between mid hair and head
- `acs_bat_list` &mdash; sorted list of MASAccessories to draw before table
- `acs_mat_list` &mdash; sorted list of MASAccessories to draw between middle arms and table
- `acs_mab_list` &mdash; sorted list of MASAccessories to draw between middle arms and boobs
- `acs_bfh_list` &mdash; sorted list of MASAccessories to draw between boobs and front hair
- `acs_afh_list` &mdash; sorted list of MASAccessories to draw between front hair and face
- `acs_mid_list` &mdash; sorted list of MASAccessories to draw between body and arms
- `acs_pst_list` &mdash; sorted list of MASAccessories to draw after arms
- `leanpose` &mdash; lean and arms together
- `lean` &mdash; type of lean
- `arms` &mdash; type of arms
- `eyebags` &mdash; type of eyebags
- `sweat` &mdash; type of sweatdrop
- `blush` &mdash; type of blush
- `tears` &mdash; type of tears
- `emote` &mdash; type of emote
- `tablechair` &mdash; MASTableChair object
- `show_shadow` &mdash; True will show shadow, false will not


**Returns:**<br>
list of render keys

### def _acs_wear_if_found(_moni_chr, acs_name)

Wears the acs if the acs exists

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `acs_name` &mdash; name of the accessory


### def _acs_wear_if_gifted(_moni_chr, acs_name)

Wears the acs if it exists and has been gifted/reacted. It has been gifted/reacted if the selectable is unlocked.

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `acs_name` &mdash; name of the accessory


### def _acs_wear_if_in_tempstorage(_moni_chr, key)

Wears the acs in tempstorage at the given key, if any.

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `key` &mdash; key in tempstorage


### def _acs_wear_if_in_tempstorage_s(_moni_chr, key)

Wears a single acs in tempstorage at the given key, if any.

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `key` &mdash; key in tempstorage


### def _acs_wear_if_wearing_acs(_moni_chr, acs, acs_to_wear)

Wears the given acs if wearing another acs.

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `acs` &mdash; acs to check if wearing
- `acs_to_wear` &mdash; acs to wear if wearing acs


### def _acs_wear_if_wearing_type(_moni_chr, acs_type, acs_to_wear)

Wears the given acs if wearing an acs of the given type.

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `acs_type` &mdash; acs type to check if wearing
- `acs_to_wear` &mdash; acs to wear if wearing acs type


### def _acs_wear_if_not_wearing_type(_moni_chr, acs_type, acs_to_wear)

Wears the given acs if NOT wearing an acs of the given type.

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `acs_type` &mdash; asc type to check if not wearing
- `acs_to_wear` &mdash; acs to wear if not wearing acs type


### def _acs_remove_if_found(_moni_chr, acs_name)

REmoves an acs if the name exists

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `acs_name` &mdash; name of the accessory to remove


### def _acs_ribbon_save_and_remove(_moni_chr)

Removes ribbon acs and aves them to temp storage.

**Parameters:**
- `_moni_chr` &mdash; MASMonika object


### def _acs_ribbon_like_save_and_remove(_moni_chr)

Removes ribbon-like acs and saves them to temp storage, if found

**Parameters:**
- `_moni_chr` &mdash; MASMonika object


### def _acs_save_and_remove_exprop(_moni_chr, exprop, key, lock_topics)

Removes acs with given exprop, saving them to temp storage with given key. Also locks topics with the exprop if desired

**Parameters:**
- `_moni_chr` &mdash; MASMonika object
- `exprop` &mdash; exprop to remove and save acs
- `key` &mdash; key to use for temp storage
- `lock_topics` &mdash; True will lock topics associated with this exprop False will not


### def _hair_unlock_select_if_needed()

Unlocks the hairdown selector if enough hair is unlocked.

### def _clothes_baked_entry(_moni_chr)

Clothes baked entry

### def _hair_def_entry(_moni_chr)

Entry programming point for ponytail

### def _hair_def_exit(_moni_chr)

Exit programming point for ponytail

### def _hair_down_entry(_moni_chr)

Entry programming point for hair down

### def _hair_down_exit(_moni_chr)

Exit programming point for hair down

### def _hair_bun_entry(_moni_chr)

Entry programming point for hair bun

### def _hair_orcaramelo_bunbraid_exit(_moni_chr)

Exit prog point for bunbraid

### def _hair_braided_entry(_moni_chr)

Entry prog point for braided hair

### def _hair_braided_exit(_moni_chr)

Exit prog point for braided hair

### def _hair_wet_entry(_moni_chr)

Entry prog point for wet hair

### def _clothes_def_entry(_moni_chr)

Entry programming point for def clothes

### def _clothes_def_exit(_moni_chr)

Exit programming point for def clothes

### def _clothes_rin_exit(_moni_chr)

Exit programming point for rin clothes

### def _clothes_marisa_exit(_moni_chr)

Exit programming point for marisa clothes

### def _clothes_orcaramelo_hatsune_miku_entry(_moni_chr)

Entry pp for orcaramelo miku

### def _clothes_orcaramelo_hatsune_miku_exit(_moni_chr)

Exit pp for orcaramelo miku

### def _clothes_orcaramelo_sakuya_izayoi_entry(_moni_chr)

Entry pp for orcaramelo sakuya

### def _clothes_orcaramelo_sakuya_izayoi_exit(_moni_chr)

Exit pp for orcaramelo sakuya

### def _clothes_dress_newyears_entry(_moni_chr)

entry progpoint for dress_newyears

### def _clothes_dress_newyears_exit(_moni_chr)

exit progpoint for dress_newyears

### def _clothes_sundress_white_exit(_moni_chr)

Exit programming point for sundress white

### def _clothes_velius94_dress_whitenavyblue_entry(_moni_chr)

Entry prog point for navyblue dress

### def _clothes_bath_towel_white_entry(_moni_chr)

Entry prog point for bath towel

### def _clothes_bath_towel_white_exit(_moni_chr)

Exit prog point for bath towel

### def _clothes_briaryoung_shuchiin_academy_uniform_entry(_moni_chr)

Entry prog point for the shuchiin academy uniform

### def _clothes_briaryoung_shuchiin_academy_uniform_exit(_moni_chr)

Exit prog point for the shuchiin academy uniform

### def _clothes_hatana_2b_entry(_moni_chr)

Entry pp for hatana 2b

### def _clothes_hatana_2b_exit(_moni_chr)

Exit prog point for hatana 2b

### def _acs_quetzalplushie_entry(_moni_chr)

Entry programming point for quetzal plushie acs

### def _acs_quetzalplushie_exit(_moni_chr)

Exit programming point for quetzal plushie acs

### def _acs_center_quetzalplushie_entry(_moni_chr)

Entry programming point for quetzal plushie (mid version) acs

### def _acs_center_quetzalplushie_exit(_moni_chr)

Exit programming point for quetzal plushie (mid version) acs

### def _acs_quetzalplushie_santahat_entry(_moni_chr)

Entry programming point for quetzal plushie santa hat acs

### def _acs_center_quetzalplushie_santahat_entry(_moni_chr)

Entry programming point for quetzal plushie santa hat (mid version) acs

### def _acs_quetzalplushie_antlers_entry(_moni_chr)

Entry programming point for quetzal plushie antlers acs

### def _acs_heartchoc_entry(_moni_chr)

Entry programming point for heartchoc acs

### def _acs_heartchoc_exit(_moni_chr)

Exit programming point for heartchoc acs

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

### def _hair__testingxcp_entry(_moni_chr)

### def _hair__testingxcp_exit(_moni_chr)

### def _clothes__testingxcp_entry(_moni_chr)

### def _clothes__testingxcp_exit(_moni_chr)

### def _acs__testingxcp_entry(_moni_chr)

### def _acs__testingxcp_exit(_moni_chr)

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


### def _verify_fwm_db()

Verifies that data in the FW_DB is correct. MASFilterWeatherMaps are valid if: 1. if the MFWM is fallback-based: a) All filters provided include a fallback filter with PRECIP_TYPE_DEF set. 2. If the MFWM is standard: a) All filters contain a PRECIP_TYPE_DEF set.  Raises all errors.

### def _verify_mfwm(mfwm_id, mfwm)

Verifies a MASFilterWeatherMap object.  Raises all errors.

**Parameters:**
- `mfwm_id` &mdash; ID of the MASFilterWeatherMap object
- `mfwm` &mdash; MASFilterWeatherMap object to verify


### def _mfwm_find_fb_def(mfwm, flt, flt_defs)

Finds fallbacks from a starting flt that are covered with a default precip type.

**Parameters:**
- `mfwm` &mdash; MASFilterWeatherMap object we are checking
- `flt` &mdash; filter we are checking for fallbacks
- `flt_defs` &mdash; dict containing keys of filters that already have known defaults in their fallback chains.


**Returns:**<br>
flt_defs - additional filters with known defaults are added to this dict as we go through the fallback chain of the given flt. True if we found a non-None default precip type. False if not

### def _find_circ_fb(flt, memo)

Tries to find circular fallbacks. Assumes that the current flt has not been placed into memo yet.

**Parameters:**
- `flt` &mdash; flt we are checking
- `memo` &mdash; dict of all flts we traversed here


**Returns:**<br>
memo - if False is returned, all keys in this memo are deemed to be non-circular fallbacks. True if circular fallback is found, False otherwise

### def _find_next_fb(flt, memo, ordered_memo)

Finds next filter and stores in memo and ordered memo

**Parameters:**
- `flt` &mdash; filter to find next filter for


**Returns:**<br>
memo - dict to add the next filter as a key if not None ordered memo - list to append the next filter if not None the next filter, or None if no next filter.

### def _verify_flt_fb()

Verifies that there are no circular fallbacks in the filter fallback dict.  Raises an error if circular fallbacks are found

### def _verify_fwm_db()

Verifies that data in the FW_DB is correct. MASFilterWeatherMaps are valid if: 1. if the MFWM is fallback-based: a) All filters provided include a fallback filter with PRECIP_TYPE_DEF set. 2. If the MFWM is standard: a) All filters contain a PRECIP_TYPE_DEF set.  Raises all errors.

### def _verify_mfwm(mfwm_id, mfwm)

Verifies a MASFilterWeatherMap object.  Raises all errors.

**Parameters:**
- `mfwm_id` &mdash; ID of the MASFilterWeatherMap object
- `mfwm` &mdash; MASFilterWeatherMap object to verify


### def _mfwm_find_fb_def(mfwm, flt, flt_defs)

Finds fallbacks from a starting flt that are covered with a default precip type.

**Parameters:**
- `mfwm` &mdash; MASFilterWeatherMap object we are checking
- `flt` &mdash; filter we are checking for fallbacks
- `flt_defs` &mdash; dict containing keys of filters that already have known defaults in their fallback chains.


**Returns:**<br>
flt_defs - additional filters with known defaults are added to this dict as we go through the fallback chain of the given flt. True if we found a non-None default precip type. False if not

### def _find_circ_fb(flt, memo)

Tries to find circular fallbacks. Assumes that the current flt has not been placed into memo yet.

**Parameters:**
- `flt` &mdash; flt we are checking
- `memo` &mdash; dict of all flts we traversed here


**Returns:**<br>
memo - if False is returned, all keys in this memo are deemed to be non-circular fallbacks. True if circular fallback is found, False otherwise

### def _find_next_fb(flt, memo, ordered_memo)

Finds next filter and stores in memo and ordered memo

**Parameters:**
- `flt` &mdash; filter to find next filter for


**Returns:**<br>
memo - dict to add the next filter as a key if not None ordered memo - list to append the next filter if not None the next filter, or None if no next filter.

### def _verify_flt_fb()

Verifies that there are no circular fallbacks in the filter fallback dict.  Raises an error if circular fallbacks are found

