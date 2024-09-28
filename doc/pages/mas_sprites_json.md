## Functions

### def _add_hair_to_verify(hairname, verimap, name)

### def writelog(msg)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `log.info, log.warning, log.error, log.exception`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='log.info, log.warning, log.error, log.exception')`


### def writelogs(msgs)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**

**Decorators:**
- `@store.mas_utils.deprecated()`


### def _verify_sptype(val, allow_none=True)

### def _add_hair_to_verify(hairname, verimap, name)

### def writelog(msg)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `log.info, log.warning, log.error, log.exception`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='log.info, log.warning, log.error, log.exception')`


### def writelogs(msgs)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**

**Decorators:**
- `@store.mas_utils.deprecated()`


### def _verify_sptype(val, allow_none=True)

### def parsewritelog(msg_data)

write log using specially formatted data.

**Parameters:**
- `msg_data` &mdash; tuple of the following format: [0] - log constant [1] - indentation level [2] - msg to write


**Returns:**<br>
True if an ERR constant was found, False if not

### def parsewritelogs(msgs_data)

Write logs using specially formatted data

**Parameters:**
- `msgs_data` &mdash; list of tuples of the following format: [0] - log constant [1] - indentation level [2] - msg to write


**Returns:**<br>
True if an ERR constnat was found, False if not

### def _replace_hair_map(sp_name, hair_to_replace)

Replaces the hair vals of the given sprite object with the given name of the given hair with defaults.

**Parameters:**
- `sp_name` &mdash; name of the clothing sprite object to replace hair map values in
- `hair_to_replace` &mdash; hair name to replace with defaults


### def _remove_sel_list(name, sel_list)

Removes selectable from selectbale list  Only intended for json usage. DO not use elsewhere. In general, you should NEVER need to remove a selectable from the selectable list.

### def _reset_sp_obj(sp_obj)

Uninits the given sprite object. This is meant only for json sprite usage if we need to back out.

**Parameters:**
- `sp_obj` &mdash; sprite object to remove


### def _build_loadstrs(sp_obj, sel_obj=None)

Builds list of strings that need to be verified via loadable.

**Parameters:**
- `sp_obj` &mdash; sprite object to build strings from
- `sel_obj` &mdash; selectable to build thumb string from. Ignored if None (Default: None)


**Returns:**<br>
list of strings that would need to be loadable verified

### def _check_giftname(giftname, sp_type, sp_name, msg_log, ind_lvl)

Initializes the giftname with the sprite info

**Parameters:**
- `giftname` &mdash; giftname we want to use
- `sp_type` &mdash; sprite type we want to init
- `sp_name` &mdash; name of the sprite object to associated with this gift (use the sprite's name property == ID)
- `ind_lvl` &mdash; indentation level to use


**Returns:**<br>
msg_log - list to log messages to

### def _init_giftname(giftname, sp_type, sp_name)

Initializes the giftname with the sprite info does not check for valid giftname.

**Parameters:**
- `giftname` &mdash; giftname we want to use
- `sp_type` &mdash; sprite type we want to init
- `sp_name` &mdash; name of the sprite object to associate with this gift


### def _process_giftname()

Process the gift maps by cleaning the persistent vars

### def _process_progpoint(sp_type, name, save_obj, msg_log, ind_lvl, progname)

Attempts to find a prop point for a sprite object with the given sp_type and name

**Parameters:**
- `sp_type` &mdash; sprite object type
- `name` &mdash; name of sprite object
- `ind_lvl` &mdash; indent level
- `progname` &mdash; name of progpoint (do not include suffix)


**Returns:**<br>
save_obj - dict to save progpoint to msg_log - list to save messages to

### def _test_loadables(sp_obj, msg_log, ind_lvl)

Tests loadable images and errs if an image is not loadable.

**Parameters:**
- `sp_obj` &mdash; sprite object to test
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
msg_log - list to add messages to

### def _validate_type(json_obj, msg_log, ind_lvl)

Validates the type of this json object.  Logs errors. Also pops type off

**Parameters:**
- `json_obj` &mdash; json object to validate
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
msg_log - list to add messages to SP constant if valid type, None otherwise

### def _validate_mux_type(json_obj, msg_log, indent_lvl)

Validates mux_type of this json object

**Parameters:**
- `json_obj` &mdash; json object to validate
- `indent_lvl` &mdash; indtenation lvl to use


**Returns:**<br>
msg_log - list to save error messages to if nothing was addeed to this list, the mux_type is valid mux_type found. May be None

### def _validate_iterstr(jobj, save_obj, propname, required, allow_none, msg_log, indent_lvl)

Validates an iterable if it consists solely of strings  an empty list is considered bad.

**Parameters:**
- `jobj` &mdash; json object to parse
- `propname` &mdash; property name for error messages
- `required` &mdash; True if this property is required, False if not
- `allow_none` &mdash; True if None is valid value, False if not
- `indent_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save to msg_log - list to save messages to True if good, False if bad

### def _validate_params(jobj, save_obj, param_dict, required, msg_log, indent_lvl)

Validates a list of parameters, while also saving said params into given save object.  Errors/Warnings are logged to given lists

**Parameters:**
- `jobj` &mdash; json object to parse
- `param_dict` &mdash; dict of params + verification functiosn
- `required` &mdash; True if the given params are required, False otherwise.
- `indent_lvl` &mdash; indentation level to use


**Returns:**<br>
save_obj - dict to save data to msg_log - log to save messages to True if success, False if not

### def _validate_acs(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates ACS-specific properties, as well as acs pose map  Props validated: - rec_layer - priority - acs_type - dlg_desc - dlg_plural - mux_type - pose_map - giftname - arm_split - highlight

**Parameters:**
- `jobj` &mdash; json object to pasrse
- `obj_based` &mdash; dict of object-based items (contains pose_map)
- `indent_lvl` &mdash; indentation lvl to use


**Returns:**<br>
save_obj - dict to save data to msg_log - list to add messages to True if validation success, False if not

### def _validate_fallbacks(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates fallback related properties and pose map  Props validated: - fallback - pose_map

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items (contains pose_map)
- `indent_lvl` &mdash; indentation lvl to use


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messages to True if success, False if not

### def _validate_hair(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates HAIR related properties  Props validated: - unlock - highlight

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items
- `indent_lvl` &mdash; indentation lvl


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messagse to True on success, False if not

### def _validate_clothes(jobj, save_obj, obj_based, sp_name, dry_run, msg_log, indent_lvl, post_proc_data)

Validates CLOTHES related properties  Props validated: - hair_map - giftname - pose_arms - highlight - outfit_hair - outfit_acs

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of objected-baesd items (contains split)
- `sp_name` &mdash; name of the clothes we are validating
- `dry_run` &mdash; true if we are dry running, False if not
- `indent_lvl` &mdash; indentation lvl


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messages to post_proc_data - dict to store data for post proccessing True if good, False if not

### def _validate_ex_props(jobj, save_obj, obj_based, msg_log, ind_lvl)

Validates ex_props proprety  Props validated: - ex_props

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items (contains ex_props)
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messages to

### def _validate_highlight(obj_based, save_obj, msg_log, ind_lvl, hl_keys)

Validates highlight objects  Props validated: - highlight

**Parameters:**
- `obj_based` &mdash; dict of object-based props
- `hl_keys` &mdash; the keys that this highlight object should be using
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save data to msg_log - list to add messages to True if valid, False if not

### def _validate_highlight_core(jobj, save_obj, msg_log, ind_lvl, hl_keys)

Primary portion of highlight validation. This is so it can be used seamlessly with highlight split object validation logs.  Props validated: - highlight

**Parameters:**
- `jobj` &mdash; json object to parse
- `hl_keys` &mdash; the keys this highlight object should be using


**Returns:**<br>
save_obj - dict to save data to msg_log - list to add messages to True if valid, False if not

### def _validate_selectable(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates selectable  Props validated: - select_info

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items (contains select_info)
- `indent_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save data to msg_log - list to write messages to True if success, false if failure

### def addSpriteObject(filepath, post_proc_data)

Adds a sprite object, given its json filepath

**Parameters:**
- `filepath` &mdash; filepath to the JSON we want to load


**Returns:**<br>
post_proc_data - dict to store post processing data in

### def addSpriteObjects(post_proc_data)

Adds sprite objects if we find any  Also does delayed validation rules: - hair

**Returns:**<br>
post_proc_data - data to be used in post processing code (should be a dict)

### def initSpriteObjectProc()

Prepares internal data for sprite object processing

### def verifyHairs()

Verifies all hair items that we encountered

### def processOutfitExtras(post_proc_data)

Processes outfit extras for sprites

**Parameters:**
- `post_proc_data` &mdash; data set by the sprite object add alg


### def _addGift(giftname, indent_lvl)

Adds the reaction for this gift, using the correct label depending on gift label existence.

**Parameters:**
- `giftname` &mdash; giftname to add reaction for
- `indent_lvl` &mdash; indentation level to use


### def processGifts()

Processes giftnames that were loaded, adding/removing them from certain dicts.

### def parsewritelog(msg_data)

write log using specially formatted data.

**Parameters:**
- `msg_data` &mdash; tuple of the following format: [0] - log constant [1] - indentation level [2] - msg to write


**Returns:**<br>
True if an ERR constant was found, False if not

### def parsewritelogs(msgs_data)

Write logs using specially formatted data

**Parameters:**
- `msgs_data` &mdash; list of tuples of the following format: [0] - log constant [1] - indentation level [2] - msg to write


**Returns:**<br>
True if an ERR constnat was found, False if not

### def _replace_hair_map(sp_name, hair_to_replace)

Replaces the hair vals of the given sprite object with the given name of the given hair with defaults.

**Parameters:**
- `sp_name` &mdash; name of the clothing sprite object to replace hair map values in
- `hair_to_replace` &mdash; hair name to replace with defaults


### def _remove_sel_list(name, sel_list)

Removes selectable from selectbale list  Only intended for json usage. DO not use elsewhere. In general, you should NEVER need to remove a selectable from the selectable list.

### def _reset_sp_obj(sp_obj)

Uninits the given sprite object. This is meant only for json sprite usage if we need to back out.

**Parameters:**
- `sp_obj` &mdash; sprite object to remove


### def _build_loadstrs(sp_obj, sel_obj=None)

Builds list of strings that need to be verified via loadable.

**Parameters:**
- `sp_obj` &mdash; sprite object to build strings from
- `sel_obj` &mdash; selectable to build thumb string from. Ignored if None (Default: None)


**Returns:**<br>
list of strings that would need to be loadable verified

### def _check_giftname(giftname, sp_type, sp_name, msg_log, ind_lvl)

Initializes the giftname with the sprite info

**Parameters:**
- `giftname` &mdash; giftname we want to use
- `sp_type` &mdash; sprite type we want to init
- `sp_name` &mdash; name of the sprite object to associated with this gift (use the sprite's name property == ID)
- `ind_lvl` &mdash; indentation level to use


**Returns:**<br>
msg_log - list to log messages to

### def _init_giftname(giftname, sp_type, sp_name)

Initializes the giftname with the sprite info does not check for valid giftname.

**Parameters:**
- `giftname` &mdash; giftname we want to use
- `sp_type` &mdash; sprite type we want to init
- `sp_name` &mdash; name of the sprite object to associate with this gift


### def _process_giftname()

Process the gift maps by cleaning the persistent vars

### def _process_progpoint(sp_type, name, save_obj, msg_log, ind_lvl, progname)

Attempts to find a prop point for a sprite object with the given sp_type and name

**Parameters:**
- `sp_type` &mdash; sprite object type
- `name` &mdash; name of sprite object
- `ind_lvl` &mdash; indent level
- `progname` &mdash; name of progpoint (do not include suffix)


**Returns:**<br>
save_obj - dict to save progpoint to msg_log - list to save messages to

### def _test_loadables(sp_obj, msg_log, ind_lvl)

Tests loadable images and errs if an image is not loadable.

**Parameters:**
- `sp_obj` &mdash; sprite object to test
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
msg_log - list to add messages to

### def _validate_type(json_obj, msg_log, ind_lvl)

Validates the type of this json object.  Logs errors. Also pops type off

**Parameters:**
- `json_obj` &mdash; json object to validate
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
msg_log - list to add messages to SP constant if valid type, None otherwise

### def _validate_mux_type(json_obj, msg_log, indent_lvl)

Validates mux_type of this json object

**Parameters:**
- `json_obj` &mdash; json object to validate
- `indent_lvl` &mdash; indtenation lvl to use


**Returns:**<br>
msg_log - list to save error messages to if nothing was addeed to this list, the mux_type is valid mux_type found. May be None

### def _validate_iterstr(jobj, save_obj, propname, required, allow_none, msg_log, indent_lvl)

Validates an iterable if it consists solely of strings  an empty list is considered bad.

**Parameters:**
- `jobj` &mdash; json object to parse
- `propname` &mdash; property name for error messages
- `required` &mdash; True if this property is required, False if not
- `allow_none` &mdash; True if None is valid value, False if not
- `indent_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save to msg_log - list to save messages to True if good, False if bad

### def _validate_params(jobj, save_obj, param_dict, required, msg_log, indent_lvl)

Validates a list of parameters, while also saving said params into given save object.  Errors/Warnings are logged to given lists

**Parameters:**
- `jobj` &mdash; json object to parse
- `param_dict` &mdash; dict of params + verification functiosn
- `required` &mdash; True if the given params are required, False otherwise.
- `indent_lvl` &mdash; indentation level to use


**Returns:**<br>
save_obj - dict to save data to msg_log - log to save messages to True if success, False if not

### def _validate_acs(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates ACS-specific properties, as well as acs pose map  Props validated: - rec_layer - priority - acs_type - dlg_desc - dlg_plural - mux_type - pose_map - giftname - arm_split - highlight

**Parameters:**
- `jobj` &mdash; json object to pasrse
- `obj_based` &mdash; dict of object-based items (contains pose_map)
- `indent_lvl` &mdash; indentation lvl to use


**Returns:**<br>
save_obj - dict to save data to msg_log - list to add messages to True if validation success, False if not

### def _validate_fallbacks(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates fallback related properties and pose map  Props validated: - fallback - pose_map

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items (contains pose_map)
- `indent_lvl` &mdash; indentation lvl to use


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messages to True if success, False if not

### def _validate_hair(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates HAIR related properties  Props validated: - unlock - highlight

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items
- `indent_lvl` &mdash; indentation lvl


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messagse to True on success, False if not

### def _validate_clothes(jobj, save_obj, obj_based, sp_name, dry_run, msg_log, indent_lvl, post_proc_data)

Validates CLOTHES related properties  Props validated: - hair_map - giftname - pose_arms - highlight - outfit_hair - outfit_acs

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of objected-baesd items (contains split)
- `sp_name` &mdash; name of the clothes we are validating
- `dry_run` &mdash; true if we are dry running, False if not
- `indent_lvl` &mdash; indentation lvl


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messages to post_proc_data - dict to store data for post proccessing True if good, False if not

### def _validate_ex_props(jobj, save_obj, obj_based, msg_log, ind_lvl)

Validates ex_props proprety  Props validated: - ex_props

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items (contains ex_props)
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save data to msg_log - list to save messages to

### def _validate_highlight(obj_based, save_obj, msg_log, ind_lvl, hl_keys)

Validates highlight objects  Props validated: - highlight

**Parameters:**
- `obj_based` &mdash; dict of object-based props
- `hl_keys` &mdash; the keys that this highlight object should be using
- `ind_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save data to msg_log - list to add messages to True if valid, False if not

### def _validate_highlight_core(jobj, save_obj, msg_log, ind_lvl, hl_keys)

Primary portion of highlight validation. This is so it can be used seamlessly with highlight split object validation logs.  Props validated: - highlight

**Parameters:**
- `jobj` &mdash; json object to parse
- `hl_keys` &mdash; the keys this highlight object should be using


**Returns:**<br>
save_obj - dict to save data to msg_log - list to add messages to True if valid, False if not

### def _validate_selectable(jobj, save_obj, obj_based, msg_log, indent_lvl)

Validates selectable  Props validated: - select_info

**Parameters:**
- `jobj` &mdash; json object to parse
- `obj_based` &mdash; dict of object-based items (contains select_info)
- `indent_lvl` &mdash; indentation level


**Returns:**<br>
save_obj - dict to save data to msg_log - list to write messages to True if success, false if failure

### def addSpriteObject(filepath, post_proc_data)

Adds a sprite object, given its json filepath

**Parameters:**
- `filepath` &mdash; filepath to the JSON we want to load


**Returns:**<br>
post_proc_data - dict to store post processing data in

### def addSpriteObjects(post_proc_data)

Adds sprite objects if we find any  Also does delayed validation rules: - hair

**Returns:**<br>
post_proc_data - data to be used in post processing code (should be a dict)

### def initSpriteObjectProc()

Prepares internal data for sprite object processing

### def verifyHairs()

Verifies all hair items that we encountered

### def processOutfitExtras(post_proc_data)

Processes outfit extras for sprites

**Parameters:**
- `post_proc_data` &mdash; data set by the sprite object add alg


### def _addGift(giftname, indent_lvl)

Adds the reaction for this gift, using the correct label depending on gift label existence.

**Parameters:**
- `giftname` &mdash; giftname to add reaction for
- `indent_lvl` &mdash; indentation level to use


### def processGifts()

Processes giftnames that were loaded, adding/removing them from certain dicts.

### def runSpriteObjAlg()

### def runSpriteObjAlg()

