## Functions

### def writelog(msg)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `log.info, log.warning, log.error, log.exception`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='log.info, log.warning, log.error, log.exception')`


### def writelogs(msgs)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@store.mas_utils.deprecated()`


### def writelog(msg)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `log.info, log.warning, log.error, log.exception`.

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='log.info, log.warning, log.error, log.exception')`


### def writelogs(msgs)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `None`.

**Decorators:**
- `@store.mas_utils.deprecated()`


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


### def processGifts()

Processes giftnames that were loaded, adding/removing them from certain dicts.

### def runSpriteObjAlg()

### def runSpriteObjAlg()

