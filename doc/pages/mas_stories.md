# store mas_stories

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def check_can_unlock_new_story(story_type=TYPE_NORMAL, ignore_cooldown=False)

Checks if it has been at least one day since we've seen the last story or the initial story

**Parameters:**
- `story_type` &mdash; story type to check if we can unlock a new one (Default: TYPE_NORMAL)
- `ignore_cooldown` &mdash; Whether or not we ignore the cooldown or time between new stories (Default: False)


---

### def get_new_stories_for_type(story_type)

Gets all new (unseen) stories of the given ype

**Parameters:**
- `story_type` &mdash; story type to get


**Returns:**<br>
list of locked stories for the given story type

---

### def get_and_unlock_random_story(story_type=TYPE_NORMAL)

Unlocks and returns a random story of the provided type

**Parameters:**
- `story_type` &mdash; Type of story to unlock. (Default: TYPE_NORMAL)


---

### def check_can_unlock_new_story(story_type=TYPE_NORMAL, ignore_cooldown=False)

Checks if it has been at least one day since we've seen the last story or the initial story

**Parameters:**
- `story_type` &mdash; story type to check if we can unlock a new one (Default: TYPE_NORMAL)
- `ignore_cooldown` &mdash; Whether or not we ignore the cooldown or time between new stories (Default: False)


---

### def get_new_stories_for_type(story_type)

Gets all new (unseen) stories of the given ype

**Parameters:**
- `story_type` &mdash; story type to get


**Returns:**<br>
list of locked stories for the given story type

---

### def get_and_unlock_random_story(story_type=TYPE_NORMAL)

Unlocks and returns a random story of the provided type

**Parameters:**
- `story_type` &mdash; Type of story to unlock. (Default: TYPE_NORMAL)


---

### def dev_unlock_all_stories()

Dev function, unlocks all stories

---

