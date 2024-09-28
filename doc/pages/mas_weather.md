## Functions

### def weatherProgress()

Runs a roll on mas_shouldRain() to pick a new weather to change to after a time between half an hour - one and a half hour

**Returns:**<br>
- True or false on whether or not to call spaceroom

### def loadMWData()

Loads persistent MASWeather data into the weather map

### def saveMWData()

Saves MASWeather data from weather map into persistent

### def unlockedWeathers()

Returns number of unlocked weather items

### def weatherProgress()

Runs a roll on mas_shouldRain() to pick a new weather to change to after a time between half an hour - one and a half hour

**Returns:**<br>
- True or false on whether or not to call spaceroom

### def loadMWData()

Loads persistent MASWeather data into the weather map

### def saveMWData()

Saves MASWeather data from weather map into persistent

### def unlockedWeathers()

Returns number of unlocked weather items

### def shouldRainToday()

### def shouldRainToday()

### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _generate_old_image(disp)

Generates an image for the old-style weather.

**Parameters:**
- `disp` &mdash; displayable to pass to renpy.image


**Returns:**<br>
the created image tag

### def _generate_old_image(disp)

Generates an image for the old-style weather.

**Parameters:**
- `disp` &mdash; displayable to pass to renpy.image


**Returns:**<br>
the created image tag

### def _weather_rain_entry(_old)

Rain start programming point

### def _weather_rain_exit(_new)

RAIN stop programming point

### def _weather_snow_entry(_old)

Snow entry programming point

### def _weather_snow_exit(_new)

Snow exit programming point

### def _weather_thunder_entry(_old)

Thunder entry programming point

### def _weather_thunder_exit(_new)

Thunder exit programming point

### def _weather_overcast_entry(_old)

Overcast entry programming point

### def _weather_overcast_exit(_new)

Overcast exit programming point

### def _weather_rain_entry(_old)

Rain start programming point

### def _weather_rain_exit(_new)

RAIN stop programming point

### def _weather_snow_entry(_old)

Snow entry programming point

### def _weather_snow_exit(_new)

Snow exit programming point

### def _weather_thunder_entry(_old)

Thunder entry programming point

### def _weather_thunder_exit(_new)

Thunder exit programming point

### def _weather_overcast_entry(_old)

Overcast entry programming point

### def _weather_overcast_exit(_new)

Overcast exit programming point

### def _determineCloudyWeather(rain_chance, thunder_chance, overcast_chance, rolled_chance=None)

Determines if weather should be rainiy/thunder/overcase, or none of those.

**Parameters:**
- `rain_chance` &mdash; chance of rain out of 100
- `thunder_chance` &mdash; chance of thunder out of 100 NOTE: this should be percentage based on rain chance, i.e.: thunder_chance * (rain_chance as %)
- `overcast_chance` &mdash; chance of overcast out of 100
- `rolled_chance` &mdash; if passed, then we use that chance instead of generating a random chance. None means we generate our own chance. (Default: None)


**Returns:**<br>
appropriate weather type, or None if neither of these weathers.

### def _determineCloudyWeather(rain_chance, thunder_chance, overcast_chance, rolled_chance=None)

Determines if weather should be rainiy/thunder/overcase, or none of those.

**Parameters:**
- `rain_chance` &mdash; chance of rain out of 100
- `thunder_chance` &mdash; chance of thunder out of 100 NOTE: this should be percentage based on rain chance, i.e.: thunder_chance * (rain_chance as %)
- `overcast_chance` &mdash; chance of overcast out of 100
- `rolled_chance` &mdash; if passed, then we use that chance instead of generating a random chance. None means we generate our own chance. (Default: None)


**Returns:**<br>
appropriate weather type, or None if neither of these weathers.

