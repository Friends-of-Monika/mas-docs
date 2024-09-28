## Functions

### def checkRandSongDelegate()

Handles locking/unlocking of the random song delegate  Ensures that songs cannot be repeated (derandoms the delegate) if the repeat topics flag is disabled and there's no unseen songs And that songs can be repeated if the flag is enabled (re-randoms the delegate)

### def getUnlockedSongs(length=None)

Gets a list of unlocked songs

**Parameters:**
- `length` &mdash; a filter for the type of song we want. "long" for songs of TYPE_LONG "short" for TYPE_SHORT or None for all songs. (Default None)


**Returns:**<br>
list of unlocked all songs of the desired length in tuple format for a scrollable menu

### def getRandomSongs(unseen_only=False)

Gets a list of all random songs

**Parameters:**
- `unseen_only` &mdash; Whether or not the list of random songs should contain unseen only songs


**Returns:**<br>
list of all random songs within aff_range

### def checkSongAnalysisDelegate(curr_aff=None)

Checks to see if the song analysis topic should be unlocked or locked and does the appropriate action

**Parameters:**
- `curr_aff` &mdash; Affection level to ev.checkAffection with. If none, mas_curr_affection is assumed (Default: None)


### def getUnlockedSongAnalyses(curr_aff=None)

Gets a list of all song analysis evs in scrollable menu format

**Parameters:**
- `curr_aff` &mdash; Affection level to ev.checkAffection with. If none, mas_curr_affection is assumed (Default: None)


**Returns:**<br>
List of unlocked song analysis topics in mas_gen_scrollable_menu format

### def hasUnlockedSongAnalyses(curr_aff=None)

Checks if there's any unlocked song analysis topics available

**Parameters:**
- `curr_aff` &mdash; Affection level to ev.checkAffection with. If none, mas_curr_affection is assumed (Default: None)


**Returns:**<br>
boolean: True if we have unlocked song analyses False otherwise

### def hasUnlockedSongs(length=None)

Checks if the player has unlocked a song at any point via the random selection

**Parameters:**
- `length` &mdash; a filter for the type of song we want. "long" for songs of TYPE_LONG "short" for TYPE_SHORT or None for all songs. (Default None)


**Returns:**<br>
True if there's an unlocked song, False otherwise

### def hasRandomSongs(unseen_only=False)

Checks if there are any songs with the random property

**Parameters:**
- `unseen_only` &mdash; Whether or not we should check for only unseen songs


**Returns:**<br>
True if there are songs which are random, False otherwise

### def getPromptSuffix(ev)

Gets the suffix for songs to display in the bookmarks menu

**Parameters:**
- `ev` &mdash; event object to get the prompt suffix for


**Returns:**<br>
Suffix for song prompt

### def checkRandSongDelegate()

Handles locking/unlocking of the random song delegate  Ensures that songs cannot be repeated (derandoms the delegate) if the repeat topics flag is disabled and there's no unseen songs And that songs can be repeated if the flag is enabled (re-randoms the delegate)

### def getUnlockedSongs(length=None)

Gets a list of unlocked songs

**Parameters:**
- `length` &mdash; a filter for the type of song we want. "long" for songs of TYPE_LONG "short" for TYPE_SHORT or None for all songs. (Default None)


**Returns:**<br>
list of unlocked all songs of the desired length in tuple format for a scrollable menu

### def getRandomSongs(unseen_only=False)

Gets a list of all random songs

**Parameters:**
- `unseen_only` &mdash; Whether or not the list of random songs should contain unseen only songs


**Returns:**<br>
list of all random songs within aff_range

### def checkSongAnalysisDelegate(curr_aff=None)

Checks to see if the song analysis topic should be unlocked or locked and does the appropriate action

**Parameters:**
- `curr_aff` &mdash; Affection level to ev.checkAffection with. If none, mas_curr_affection is assumed (Default: None)


### def getUnlockedSongAnalyses(curr_aff=None)

Gets a list of all song analysis evs in scrollable menu format

**Parameters:**
- `curr_aff` &mdash; Affection level to ev.checkAffection with. If none, mas_curr_affection is assumed (Default: None)


**Returns:**<br>
List of unlocked song analysis topics in mas_gen_scrollable_menu format

### def hasUnlockedSongAnalyses(curr_aff=None)

Checks if there's any unlocked song analysis topics available

**Parameters:**
- `curr_aff` &mdash; Affection level to ev.checkAffection with. If none, mas_curr_affection is assumed (Default: None)


**Returns:**<br>
boolean: True if we have unlocked song analyses False otherwise

### def hasUnlockedSongs(length=None)

Checks if the player has unlocked a song at any point via the random selection

**Parameters:**
- `length` &mdash; a filter for the type of song we want. "long" for songs of TYPE_LONG "short" for TYPE_SHORT or None for all songs. (Default None)


**Returns:**<br>
True if there's an unlocked song, False otherwise

### def hasRandomSongs(unseen_only=False)

Checks if there are any songs with the random property

**Parameters:**
- `unseen_only` &mdash; Whether or not we should check for only unseen songs


**Returns:**<br>
True if there are songs which are random, False otherwise

### def getPromptSuffix(ev)

Gets the suffix for songs to display in the bookmarks menu

**Parameters:**
- `ev` &mdash; event object to get the prompt suffix for


**Returns:**<br>
Suffix for song prompt

