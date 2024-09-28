## Public functions

### def get_default_house_rules()

Returns default house rules

**Returns:**<br>
dict

---

### def update_house_rules(force=False)

Adds keys from the def values dict to the persistent dict Useful after updates

**Parameters:**
- `force` &mdash; bool, do we want to rewrite existing keys?


---

### def are_default_house_rules()

Checks if the current settings are default

**Returns:**<br>
bool

---

### def get_house_rule(name)

Returns a house rule for the given name  This WILL raise KeyError if you enter invalid name  But this WILL try to fall back to a sane value if the key isn't in the persistent for some reason

**Parameters:**
- `name` &mdash; the string with the rule key


**Returns:**<br>
rule value or None in the worst case

---

### def set_house_rule(name, value)

Sets a new value for a house rule  This WILL raise KeyError if you enter invalid name

**Parameters:**
- `name` &mdash; the string with the rule key
- `value` &mdash; the new value for the rule


---

### def reverse_house_rule(name)

Reversed a value of a house rule Only useful for bools

---

### def visit_game_ev()

Updates game ev props like if it was seen by the player now Increments show count Sets last seen

---

### def does_want_suggest_play()

A func to check if Monika wants to suggest play nou Yes if: NEVER played nou before played in the last 15 mins NOT played in the past 3 days otherwise 30% to say yes

**Returns:**<br>
bool

---

### def give_points()

Gives points to the winner

---

### def reset_points()

Resets the persistent var to 0 for both Monika and the player

---

### def get_player_points_percentage(player_persist_key)

Returns proportion of the corrent points of a player to the maximum possible score

**Parameters:**
- `player_persist_key` &mdash; persistent key for the player ('Monika' or 'Player')


**Returns:**<br>
float as proportion (0.0 - 1.0)

---

### def get_wins_for(player)

Returns wins in nou

**Parameters:**
- `player` &mdash; the player key to return the stats for


**Returns:**<br>
int

---

### def get_total_games()

Returns total nou games

**Returns:**<br>
int

---

### def get_default_house_rules()

Returns default house rules

**Returns:**<br>
dict

---

### def update_house_rules(force=False)

Adds keys from the def values dict to the persistent dict Useful after updates

**Parameters:**
- `force` &mdash; bool, do we want to rewrite existing keys?


---

### def are_default_house_rules()

Checks if the current settings are default

**Returns:**<br>
bool

---

### def get_house_rule(name)

Returns a house rule for the given name  This WILL raise KeyError if you enter invalid name  But this WILL try to fall back to a sane value if the key isn't in the persistent for some reason

**Parameters:**
- `name` &mdash; the string with the rule key


**Returns:**<br>
rule value or None in the worst case

---

### def set_house_rule(name, value)

Sets a new value for a house rule  This WILL raise KeyError if you enter invalid name

**Parameters:**
- `name` &mdash; the string with the rule key
- `value` &mdash; the new value for the rule


---

### def reverse_house_rule(name)

Reversed a value of a house rule Only useful for bools

---

### def visit_game_ev()

Updates game ev props like if it was seen by the player now Increments show count Sets last seen

---

### def does_want_suggest_play()

A func to check if Monika wants to suggest play nou Yes if: NEVER played nou before played in the last 15 mins NOT played in the past 3 days otherwise 30% to say yes

**Returns:**<br>
bool

---

### def give_points()

Gives points to the winner

---

### def reset_points()

Resets the persistent var to 0 for both Monika and the player

---

### def get_player_points_percentage(player_persist_key)

Returns proportion of the corrent points of a player to the maximum possible score

**Parameters:**
- `player_persist_key` &mdash; persistent key for the player ('Monika' or 'Player')


**Returns:**<br>
float as proportion (0.0 - 1.0)

---

### def get_wins_for(player)

Returns wins in nou

**Parameters:**
- `player` &mdash; the player key to return the stats for


**Returns:**<br>
int

---

### def get_total_games()

Returns total nou games

**Returns:**<br>
int

---

