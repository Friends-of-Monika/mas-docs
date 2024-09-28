## Functions

### def is_platform_good_for_chess()

---### def is_platform_good_for_chess()

---### def getGameEVByPrompt(gamename)

Gets the game ev using the prompt of its event (gamename)

**Parameters:**
- `gamename` &mdash; Name of the game we want to get


**Returns:**<br>
event object for the game entered if found. None if not found

---### def getGameEVByPrompt(gamename)

Gets the game ev using the prompt of its event (gamename)

**Parameters:**
- `gamename` &mdash; Name of the game we want to get


**Returns:**<br>
event object for the game entered if found. None if not found

---### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

#### def _total_games_played(exclude_list=[])

Returns the total number of games played by adding up the shown_count of each game

**Parameters:**
- `exclude_list` &mdash; A list of event_label strings for games we want to exclude from the number of games played defaults to an empty list


---#### def _total_games_played(exclude_list=[])

Returns the total number of games played by adding up the shown_count of each game

**Parameters:**
- `exclude_list` &mdash; A list of event_label strings for games we want to exclude from the number of games played defaults to an empty list


---