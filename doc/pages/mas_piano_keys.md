## Functions

### def _findKeymap(value)

Finds the key that points to value in the keymap. Effectively a dict value search

**Parameters:**
- `value` &mdash; value to find


**Returns:**<br>
key in persistent._mas_piano_keymaps that returns value, or None if value not found

### def _setKeymap(key, new)

Sets a keymap. Checks for existing keymap and will remove it. Will NOT set the keymap if key == new

**Parameters:**
- `key` &mdash; the key we are mapping
- `new` &mdash; the new key item to map to


**Returns:**<br>
tuple of the following format: [0] - new key that was set (could be None) [1] - old key that was originally set (could be None)

### def _strtoN(note)

Converts a stringified note to a regular note

**Parameters:**
- `note` &mdash; note string to convert


**Returns:**<br>
piano note version, or None if this wasnt a real ntoe

### def _strtoN_list(note_list)

Versin of strtoN that can handle a full list

**Parameters:**
- `note_list` &mdash; list of notes to convert


**Returns:**<br>
list of piano notes. or None if at least note wasnt real

### def _labelCheck(key, _params, jobj)

specialized json label checking function

**Parameters:**
- `key` &mdash; key of label to check
- `_params` &mdash; params dict, also using key
- `jobj` &mdash; json object, also using key


### def _intCheck_nl(key, _params, jobj, warn_msg)

Specialized json int checking function

**Parameters:**
- `key` &mdash; key of the integer to check
- `_params` &mdash; params dict, also using key
- `jobj` &mdash; json object, also using key
- `warn_msg` &mdash; warning message


### def _noteCheck(key, _params, _warns, jobj, warn_msg)

Specialized json note list checking function

**Parameters:**
- `key` &mdash; key of notes to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warnings list
- `jobj` &mdash; json object, also using key
- `warn_msg` &mdash; message to use for warning


### def _scCheck(key, _params, _warns, jobj, warn_msg)

Specialized json spritecode / expression checking function

**Parameters:**
- `key` &mdash; key of sprite code to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object, also using key
- `warn_msg` &mdash; message to use for warning


### def _floatCheck(key, _params, _warns, jobj, warn_msg)

Specialized json float checking function

**Parameters:**
- `key` &mdash; key of the float to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object also using keuy
- `warn_msg` &mdash; message to use for warning


### def _intCheck(key, _params, _warns, jobj, warn_msg)

Specialized json int checking function

**Parameters:**
- `key` &mdash; key of the int to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object also using keuy
- `warn_msg` &mdash; message to use for warning


### def _boolCheck(key, _params, _warns, jobj, warn_msg)

Specialized json bool checking function

**Parameters:**
- `key` &mdash; key of the bool to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object also using keuy
- `warn_msg` &mdash; message to use for warning


### def _findKeymap(value)

Finds the key that points to value in the keymap. Effectively a dict value search

**Parameters:**
- `value` &mdash; value to find


**Returns:**<br>
key in persistent._mas_piano_keymaps that returns value, or None if value not found

### def _setKeymap(key, new)

Sets a keymap. Checks for existing keymap and will remove it. Will NOT set the keymap if key == new

**Parameters:**
- `key` &mdash; the key we are mapping
- `new` &mdash; the new key item to map to


**Returns:**<br>
tuple of the following format: [0] - new key that was set (could be None) [1] - old key that was originally set (could be None)

### def _strtoN(note)

Converts a stringified note to a regular note

**Parameters:**
- `note` &mdash; note string to convert


**Returns:**<br>
piano note version, or None if this wasnt a real ntoe

### def _strtoN_list(note_list)

Versin of strtoN that can handle a full list

**Parameters:**
- `note_list` &mdash; list of notes to convert


**Returns:**<br>
list of piano notes. or None if at least note wasnt real

### def _labelCheck(key, _params, jobj)

specialized json label checking function

**Parameters:**
- `key` &mdash; key of label to check
- `_params` &mdash; params dict, also using key
- `jobj` &mdash; json object, also using key


### def _intCheck_nl(key, _params, jobj, warn_msg)

Specialized json int checking function

**Parameters:**
- `key` &mdash; key of the integer to check
- `_params` &mdash; params dict, also using key
- `jobj` &mdash; json object, also using key
- `warn_msg` &mdash; warning message


### def _noteCheck(key, _params, _warns, jobj, warn_msg)

Specialized json note list checking function

**Parameters:**
- `key` &mdash; key of notes to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warnings list
- `jobj` &mdash; json object, also using key
- `warn_msg` &mdash; message to use for warning


### def _scCheck(key, _params, _warns, jobj, warn_msg)

Specialized json spritecode / expression checking function

**Parameters:**
- `key` &mdash; key of sprite code to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object, also using key
- `warn_msg` &mdash; message to use for warning


### def _floatCheck(key, _params, _warns, jobj, warn_msg)

Specialized json float checking function

**Parameters:**
- `key` &mdash; key of the float to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object also using keuy
- `warn_msg` &mdash; message to use for warning


### def _intCheck(key, _params, _warns, jobj, warn_msg)

Specialized json int checking function

**Parameters:**
- `key` &mdash; key of the int to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object also using keuy
- `warn_msg` &mdash; message to use for warning


### def _boolCheck(key, _params, _warns, jobj, warn_msg)

Specialized json bool checking function

**Parameters:**
- `key` &mdash; key of the bool to check
- `_params` &mdash; params dict, also using key
- `_warns` &mdash; warning list
- `jobj` &mdash; json object also using keuy
- `warn_msg` &mdash; message to use for warning


### def addSong(filepath, add_main=False)

Adds a song to the pnml db, given its json filepath

**Parameters:**
- `filepath` &mdash; filepath to the JSON we want to load in - Assumed to be clean and ready to go
- `add_main` &mdash; True means we should add this to the main pnml db too (Default: False)


### def addCustomSongs()

Adds the custom songs (if we find any) to the game

### def addStockSongs()

Adds the stock songs to the game

### def addSong(filepath, add_main=False)

Adds a song to the pnml db, given its json filepath

**Parameters:**
- `filepath` &mdash; filepath to the JSON we want to load in - Assumed to be clean and ready to go
- `add_main` &mdash; True means we should add this to the main pnml db too (Default: False)


### def addCustomSongs()

Adds the custom songs (if we find any) to the game

### def addStockSongs()

Adds the stock songs to the game

### def getSongChoices()

Creates a list of tuples appropriate to display as a piano song selection menu.

**Returns:**<br>
Tuple of the following format: [0]: list of tuples for song selection. May be an empty list [1]: Last item (the nvm) for the song selection

### def getSongChoices()

Creates a list of tuples appropriate to display as a piano song selection menu.

**Returns:**<br>
Tuple of the following format: [0]: list of tuples for song selection. May be an empty list [1]: Last item (the nvm) for the song selection

