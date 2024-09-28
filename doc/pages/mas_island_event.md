# store mas_island_event

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def isFilterSupported(flt)

Checks if the event supports a filter

**Parameters:**
- `flt` &mdash; the filter to check (perhaps one of the constants in mas_sprites)


**Returns:**<br>
boolean

---

### def IslandFilterWeatherDisplayable()

DynamicDisplayable for Island images.

**Returns:**<br>
DynamicDisplayable for Island images that respect filters and weather.

---

### def decode_data()

Attempts to decode the images

**Returns:**<br>
True upon success, False otherwise

---

### def advance_progression()

Increments the lvl of progression of the islands event, it will do nothing if the player hasn't unlocked the islands yet or if the current lvl is invalid

---

### def start_progression()

Starts islands progression

---

### def play_music()

Plays appropriate music based on the current weather

---

### def stop_music()

Stops islands music

---

### def get_islands_displayable(enable_interaction=True, check_progression=False)

Builds an image for islands and returns it

**Parameters:**
- `enable_interaction` &mdash; whether to enable events or not (including parallax effect) (Default: True)
- `check_progression` &mdash; whether to check for new unlocks or not, this might be a little slow (Default: False)


**Returns:**<br>
ParallaxBackground

---

### def is_winter_weather()

Checks if the weather on the islands is wintery

**Returns:**<br>
boolean: - True if we're using snow islands - False otherwise

---

### def is_cloudy_weather()

Checks if the weather on the islands is cloudy

**Returns:**<br>
boolean: - True if we're using overcast/rain islands - False otherwise

---

### def isFilterSupported(flt)

Checks if the event supports a filter

**Parameters:**
- `flt` &mdash; the filter to check (perhaps one of the constants in mas_sprites)


**Returns:**<br>
boolean

---

### def IslandFilterWeatherDisplayable()

DynamicDisplayable for Island images.

**Returns:**<br>
DynamicDisplayable for Island images that respect filters and weather.

---

### def decode_data()

Attempts to decode the images

**Returns:**<br>
True upon success, False otherwise

---

### def advance_progression()

Increments the lvl of progression of the islands event, it will do nothing if the player hasn't unlocked the islands yet or if the current lvl is invalid

---

### def start_progression()

Starts islands progression

---

### def play_music()

Plays appropriate music based on the current weather

---

### def stop_music()

Stops islands music

---

### def get_islands_displayable(enable_interaction=True, check_progression=False)

Builds an image for islands and returns it

**Parameters:**
- `enable_interaction` &mdash; whether to enable events or not (including parallax effect) (Default: True)
- `check_progression` &mdash; whether to check for new unlocks or not, this might be a little slow (Default: False)


**Returns:**<br>
ParallaxBackground

---

### def is_winter_weather()

Checks if the weather on the islands is wintery

**Returns:**<br>
boolean: - True if we're using snow islands - False otherwise

---

### def is_cloudy_weather()

Checks if the weather on the islands is cloudy

**Returns:**<br>
boolean: - True if we're using overcast/rain islands - False otherwise

---

### def register_room(id_)

Registers lr as a background object

**Parameters:**
- `id_` &mdash; the id to register under


**Returns:**<br>
MASFilterableBackground

---

### def register_room(id_)

Registers lr as a background object

**Parameters:**
- `id_` &mdash; the id to register under


**Returns:**<br>
MASFilterableBackground

---

