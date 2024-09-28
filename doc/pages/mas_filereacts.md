## Functions

### def addReaction(ev_label, fname, _action=store.EV_ACT_QUEUE, is_good=None, exclude_on=[])

Adds a reaction to the file reactions database.

**Parameters:**
- `ev_label` &mdash; label of this event
- `fname` &mdash; filename to react to
- `_action` &mdash; the EV_ACT to do (Default: EV_ACT_QUEUE)
- `is_good` &mdash; if the gift is good(True), neutral(None) or bad(False) (Default: None)
- `exclude_on` &mdash; keys marking times to exclude this gift


### def build_gift_react_labels(evb_details=[], gsp_details=[], gen_details=[], gift_cntrs=None, ending_label=None, starting_label=None, prepare_data=True)

Processes gift details into a list of labels to show labels to queue/push whatever.

**Parameters:**
- `evb_details` &mdash; list of GiftReactDetails objects of event-based reactions. If empty list, then we don't build event-based reaction labels. (Default: [])
- `gsp_details` &mdash; list of GiftReactDetails objects of generic sprite object reactions. If empty list, then we don't build generic sprite object reaction labels. (Default: [])
- `gen_details` &mdash; list of GiftReactDetails objects of generic gift reactions. If empty list, then we don't build generic gift reaction labels. (Default: [])
- `gift_cntrs` &mdash; MASQuipList of gift connectors to use. If None, then we don't add any connectors. (Default: [])
- `ending_label` &mdash; label to use when finished reacting. (Default: None)
- `starting_label` &mdash; label to use when starting reacting (Default: None)
- `prepare_data` &mdash; True will also setup the appropriate data elements for when dialogue is shown. False will not. (Default: True)


**Returns:**<br>
list of labels. Evb reactions are first, followed by gsp reactions, then gen reactions

### def build_exclusion_list(_key)

Builds a list of excluded gifts based on the key provided

**Parameters:**
- `_key` &mdash; key to build an exclusion list for


**Returns:**<br>
list of giftnames which are excluded by the key

### def check_for_gifts(found_map={}, exclusion_list=[], exclusion_found_map={}, override_react_map=False)

Finds gifts.

**Parameters:**
- `exclusion_list` &mdash; list of giftnames to exclude from the search
- `override_react_map` &mdash; True will skip the last reacted date check, False will not (Default: False)


**Returns:**<br>
found_map - contains all gifts that were found: key: lowercase giftname, no extension val: full giftname wtih extension exclusion_found_map - contains all gifts that were found but are excluded. key: lowercase giftname, no extension val: full giftname with extension list of found giftnames

### def process_gifts(gifts, evb_details=[], gsp_details=[], gen_details=[])

Processes list of giftnames into types of gift

**Parameters:**
- `gifts` &mdash; list of giftnames to process. This is copied so it wont be modified.


**Returns:**<br>
evb_details - list of GiftReactDetails objects regarding event-based reactions spo_details - list of GiftReactDetails objects regarding generic sprite object reactions gen_details - list of GiftReactDetails objects regarding generic gift reactions

### def react_to_gifts(found_map, connect=True)

Reacts to gifts using the standard protocol (no exclusions)

**Parameters:**
- `connect` &mdash; true will apply connectors, FAlse will not


**Returns:**<br>
found_map - map of found reactions key: lowercaes giftname, no extension val: giftname with extension list of labels to be queued/pushed

### def register_gen_grds(details)

registers gifts given a generic GiftReactDetails list

**Parameters:**
- `details` &mdash; list of GiftReactDetails objects to register


### def register_sp_grds(details)

registers gifts given sprite-based GiftReactDetails list

**Parameters:**
- `details` &mdash; list of GiftReactDetails objcts to register


### def delete_file(_filename)

Deletes a file off the found_react map

**Parameters:**
- `_filename` &mdash; the name of the file to delete. If None, we delete one randomly


### def delete_files(_filename_list)

Deletes multiple files off the found_react map

**Parameters:**
- `_filename_list` &mdash; list of filenames to delete.


### def th_delete_file(_filename)

Deletes a file off the threaded found_react map

**Parameters:**
- `_filename` &mdash; the name of the file to delete. If None, we delete one randomly


### def th_delete_files(_filename_list)

Deletes multiple files off the threaded foundreact map

**Parameters:**
- `_filename_list` &mdash; list of ilenames to delete


### def delete_all(_map)

Attempts to delete all files in the given map. Removes files in that map if they dont exist no more

**Parameters:**
- `_map` &mdash; map to delete all


### def get_report_for_date(date=None)

Generates a report for all the gifts given on the input date. The report is in tuple form (total, good_gifts, neutral_gifts, bad_gifts) it contains the totals of each type of gift.

### def addReaction(ev_label, fname, _action=store.EV_ACT_QUEUE, is_good=None, exclude_on=[])

Adds a reaction to the file reactions database.

**Parameters:**
- `ev_label` &mdash; label of this event
- `fname` &mdash; filename to react to
- `_action` &mdash; the EV_ACT to do (Default: EV_ACT_QUEUE)
- `is_good` &mdash; if the gift is good(True), neutral(None) or bad(False) (Default: None)
- `exclude_on` &mdash; keys marking times to exclude this gift


### def build_gift_react_labels(evb_details=[], gsp_details=[], gen_details=[], gift_cntrs=None, ending_label=None, starting_label=None, prepare_data=True)

Processes gift details into a list of labels to show labels to queue/push whatever.

**Parameters:**
- `evb_details` &mdash; list of GiftReactDetails objects of event-based reactions. If empty list, then we don't build event-based reaction labels. (Default: [])
- `gsp_details` &mdash; list of GiftReactDetails objects of generic sprite object reactions. If empty list, then we don't build generic sprite object reaction labels. (Default: [])
- `gen_details` &mdash; list of GiftReactDetails objects of generic gift reactions. If empty list, then we don't build generic gift reaction labels. (Default: [])
- `gift_cntrs` &mdash; MASQuipList of gift connectors to use. If None, then we don't add any connectors. (Default: [])
- `ending_label` &mdash; label to use when finished reacting. (Default: None)
- `starting_label` &mdash; label to use when starting reacting (Default: None)
- `prepare_data` &mdash; True will also setup the appropriate data elements for when dialogue is shown. False will not. (Default: True)


**Returns:**<br>
list of labels. Evb reactions are first, followed by gsp reactions, then gen reactions

### def build_exclusion_list(_key)

Builds a list of excluded gifts based on the key provided

**Parameters:**
- `_key` &mdash; key to build an exclusion list for


**Returns:**<br>
list of giftnames which are excluded by the key

### def check_for_gifts(found_map={}, exclusion_list=[], exclusion_found_map={}, override_react_map=False)

Finds gifts.

**Parameters:**
- `exclusion_list` &mdash; list of giftnames to exclude from the search
- `override_react_map` &mdash; True will skip the last reacted date check, False will not (Default: False)


**Returns:**<br>
found_map - contains all gifts that were found: key: lowercase giftname, no extension val: full giftname wtih extension exclusion_found_map - contains all gifts that were found but are excluded. key: lowercase giftname, no extension val: full giftname with extension list of found giftnames

### def process_gifts(gifts, evb_details=[], gsp_details=[], gen_details=[])

Processes list of giftnames into types of gift

**Parameters:**
- `gifts` &mdash; list of giftnames to process. This is copied so it wont be modified.


**Returns:**<br>
evb_details - list of GiftReactDetails objects regarding event-based reactions spo_details - list of GiftReactDetails objects regarding generic sprite object reactions gen_details - list of GiftReactDetails objects regarding generic gift reactions

### def react_to_gifts(found_map, connect=True)

Reacts to gifts using the standard protocol (no exclusions)

**Parameters:**
- `connect` &mdash; true will apply connectors, FAlse will not


**Returns:**<br>
found_map - map of found reactions key: lowercaes giftname, no extension val: giftname with extension list of labels to be queued/pushed

### def register_gen_grds(details)

registers gifts given a generic GiftReactDetails list

**Parameters:**
- `details` &mdash; list of GiftReactDetails objects to register


### def register_sp_grds(details)

registers gifts given sprite-based GiftReactDetails list

**Parameters:**
- `details` &mdash; list of GiftReactDetails objcts to register


### def delete_file(_filename)

Deletes a file off the found_react map

**Parameters:**
- `_filename` &mdash; the name of the file to delete. If None, we delete one randomly


### def delete_files(_filename_list)

Deletes multiple files off the found_react map

**Parameters:**
- `_filename_list` &mdash; list of filenames to delete.


### def th_delete_file(_filename)

Deletes a file off the threaded found_react map

**Parameters:**
- `_filename` &mdash; the name of the file to delete. If None, we delete one randomly


### def th_delete_files(_filename_list)

Deletes multiple files off the threaded foundreact map

**Parameters:**
- `_filename_list` &mdash; list of ilenames to delete


### def delete_all(_map)

Attempts to delete all files in the given map. Removes files in that map if they dont exist no more

**Parameters:**
- `_map` &mdash; map to delete all


### def get_report_for_date(date=None)

Generates a report for all the gifts given on the input date. The report is in tuple form (total, good_gifts, neutral_gifts, bad_gifts) it contains the totals of each type of gift.

