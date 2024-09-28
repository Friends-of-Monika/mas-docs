## Functions

### def _add_monika_words(wordlist)

### def copyWordsList(_mode)

Does a deepcopy of the words for the given mode.  Sets the hm_words dict for that mode

**Returns:**<br>
the copied list of words. This is the same reference as hm_words's list. (empty list if mode is invalid)

### def _buildWordList(filepath, _mode)

Builds a list of words given the filepath and mode

**Parameters:**
- `filepath` &mdash; filepath of words to load in
- `_mode` &mdash; mode to build word list for


### def buildEasyList()

Builds the easy word list  Sets hm_words and all_hm_words appropritaley

### def buildNormalList()

Builds the normal word list  Sets hm_words and all_hm_words appropraitely

### def buildHardList()

Builds the hard word list  Sets hm_words and all_hm_words appropraitely

### def addPlayername(_mode)

Adds playername to the given mode if appropriate

**Parameters:**
- `_mode` &mdash; mode to add playername to


### def removePlayername(_mode)

Removes the playername from the given mode if found

**Parameters:**
- `_mode` &mdash; mode to remove in


### def randomSelect(_mode)

Randomly selects and pulls a word from the hm_words, given the mode  Will refill the words list if it is empty

**Parameters:**
- `_mode` &mdash; mode to pull word from


**Returns:**<br>
tuple of the following format: [0]: word [1]: winner (for hint)

### def wordToDisplay(word)

Formats a word so it can be displayed in hangman

**Parameters:**
- `word` &mdash; word to format (string)


**Returns:**<br>
display word

### def _add_monika_words(wordlist)

### def copyWordsList(_mode)

Does a deepcopy of the words for the given mode.  Sets the hm_words dict for that mode

**Returns:**<br>
the copied list of words. This is the same reference as hm_words's list. (empty list if mode is invalid)

### def _buildWordList(filepath, _mode)

Builds a list of words given the filepath and mode

**Parameters:**
- `filepath` &mdash; filepath of words to load in
- `_mode` &mdash; mode to build word list for


### def buildEasyList()

Builds the easy word list  Sets hm_words and all_hm_words appropritaley

### def buildNormalList()

Builds the normal word list  Sets hm_words and all_hm_words appropraitely

### def buildHardList()

Builds the hard word list  Sets hm_words and all_hm_words appropraitely

### def addPlayername(_mode)

Adds playername to the given mode if appropriate

**Parameters:**
- `_mode` &mdash; mode to add playername to


### def removePlayername(_mode)

Removes the playername from the given mode if found

**Parameters:**
- `_mode` &mdash; mode to remove in


### def randomSelect(_mode)

Randomly selects and pulls a word from the hm_words, given the mode  Will refill the words list if it is empty

**Parameters:**
- `_mode` &mdash; mode to pull word from


**Returns:**<br>
tuple of the following format: [0]: word [1]: winner (for hint)

### def wordToDisplay(word)

Formats a word so it can be displayed in hangman

**Parameters:**
- `word` &mdash; word to format (string)


**Returns:**<br>
display word

