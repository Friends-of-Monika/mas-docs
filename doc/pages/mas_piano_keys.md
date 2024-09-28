## Functions

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

