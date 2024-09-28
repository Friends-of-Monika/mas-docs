## Functions

### def isFilterSupported(flt)

Checks if the event supports a filter

**Parameters:**
- `flt` &mdash; the filter to check (perhaps one of the constants in mas_sprites)


**Returns:**<br>
boolean

### def IslandFilterWeatherDisplayable()

DynamicDisplayable for Island images.

**Returns:**<br>
DynamicDisplayable for Island images that respect filters and weather.

### def decode_data()

Attempts to decode the images

**Returns:**<br>
True upon success, False otherwise

### def advance_progression()

Increments the lvl of progression of the islands event, it will do nothing if the player hasn't unlocked the islands yet or if the current lvl is invalid

### def start_progression()

Starts islands progression

### def play_music()

Plays appropriate music based on the current weather

### def stop_music()

Stops islands music

### def get_islands_displayable(enable_interaction=True, check_progression=False)

Builds an image for islands and returns it

**Parameters:**
- `enable_interaction` &mdash; whether to enable events or not (including parallax effect) (Default: True)
- `check_progression` &mdash; whether to check for new unlocks or not, this might be a little slow (Default: False)


**Returns:**<br>
ParallaxBackground

### def is_winter_weather()

Checks if the weather on the islands is wintery

**Returns:**<br>
boolean: - True if we're using snow islands - False otherwise

### def is_cloudy_weather()

Checks if the weather on the islands is cloudy

**Returns:**<br>
boolean: - True if we're using overcast/rain islands - False otherwise

### def isFilterSupported(flt)

Checks if the event supports a filter

**Parameters:**
- `flt` &mdash; the filter to check (perhaps one of the constants in mas_sprites)


**Returns:**<br>
boolean

### def IslandFilterWeatherDisplayable()

DynamicDisplayable for Island images.

**Returns:**<br>
DynamicDisplayable for Island images that respect filters and weather.

### def decode_data()

Attempts to decode the images

**Returns:**<br>
True upon success, False otherwise

### def advance_progression()

Increments the lvl of progression of the islands event, it will do nothing if the player hasn't unlocked the islands yet or if the current lvl is invalid

### def start_progression()

Starts islands progression

### def play_music()

Plays appropriate music based on the current weather

### def stop_music()

Stops islands music

### def get_islands_displayable(enable_interaction=True, check_progression=False)

Builds an image for islands and returns it

**Parameters:**
- `enable_interaction` &mdash; whether to enable events or not (including parallax effect) (Default: True)
- `check_progression` &mdash; whether to check for new unlocks or not, this might be a little slow (Default: False)


**Returns:**<br>
ParallaxBackground

### def is_winter_weather()

Checks if the weather on the islands is wintery

**Returns:**<br>
boolean: - True if we're using snow islands - False otherwise

### def is_cloudy_weather()

Checks if the weather on the islands is cloudy

**Returns:**<br>
boolean: - True if we're using overcast/rain islands - False otherwise

### def register_room(id_)

Registers lr as a background object

**Parameters:**
- `id_` &mdash; the id to register under


**Returns:**<br>
MASFilterableBackground

### def register_room(id_)

Registers lr as a background object

**Parameters:**
- `id_` &mdash; the id to register under


**Returns:**<br>
MASFilterableBackground

### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _select_img(st, at, mfwm)

Selection function to use in Island-based images

**Parameters:**
- `st` &mdash; renpy related
- `at` &mdash; renpy related
- `mfwm` &mdash; MASFilterWeatherMap for this island


**Returns:**<br>
displayable data

### def _handle_raw_pkg_data(pkg_data, base_err_msg)

Handles raw data and returns clean, parsed data Logs errors

**Parameters:**
- `pkg_data` &mdash; memory buffer


**Returns:**<br>
memory buffer or None

### def _build_filter_pairs(img_map)

Builds filter pairs for IslandFilterWeatherDisplayable or MASFilterWeatherDisplayable

### def _build_ifwd(img_map)

Builds a single IslandFilterWeatherDisplayable using the given image map

### def _build_fwd(img_map)

Builds a single MASFilterWeatherDisplayable using the given image map

### def _build_weather_overlay_transform(child, speed)

A wrapper around mas_islands_weather_overlay_transform It exists so we can properly pass the child argument to the transform

### def _build_displayables(island_imgs_maps, decal_imgs_maps, bg_imgs_maps, overlay_imgs_maps, interior_imgs_map, glitch_frames, tree_lights_imgs)

Takes multiple maps with images and builds displayables from them, sets global vars

**Parameters:**
- `island_imgs_maps` &mdash; the map from island names to raw images map
- `decal_imgs_maps` &mdash; the map from decal names to raw images map
- `bg_imgs_maps` &mdash; the map from bg ids to raw images map
- `overlay_imgs_maps` &mdash; the map from overlay ids to raw images map
- `interior_imgs_map` &mdash; the map from the interior stuff to the raw images map
- `glitch_frames` &mdash; tuple of glitch raw anim frames
- `tree_lights_imgs` &mdash; map of images for the tree lights, format: img_name: disp


### def _get_room_sprite(key, is_lit)

Returns the appropriate displayable for the room sprite based on the criteria

**Parameters:**
- `key` &mdash; str - the sprite key
- `is_lit` &mdash; bool - sprite for the lit or unlit version?


**Returns:**<br>
MASImageData or Null displayable if we failed to get the image

### def _apply_flt_on_room_sprite(room_img_tag, flt)

Returns the room image with the filter applied on it

**Parameters:**
- `room_img_tag` &mdash; str - the image tag
- `flt` &mdash; str - the filter id to use


**Returns:**<br>
image manipulator or Null displayable if we failed to decode the images

### def _is_unlocked(id_)

Checks if a sprite is unlocked

**Parameters:**
- `id_` &mdash; the unique id of the sprite


**Returns:**<br>
boolean

### def _unlock(id_)

Unlocks a sprite

**Parameters:**
- `id_` &mdash; the unique id of the sprite


**Returns:**<br>
boolean whether or not the sprite was unlocked

### def _lock(id_)

Locks a sprite

**Parameters:**
- `id_` &mdash; the unique id of the sprite


**Returns:**<br>
boolean whether or not the sprite was locked

### def _unlock_one()

Unlocks one of the sprites at random. Runs only once

**Returns:**<br>
boolean whether or not a sprite was unlocked

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_0()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_1()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_2()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_3()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_4()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_5()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_6()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_7()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_8()

### def _final_unlocks()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_9()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_10()

### def _m1_script0x2dislands0x2devent__handle_unlocks()

Method to unlock various islands features when the player progresses. For example: new decals, new islands, new extra events, set persistent vars, etc.

### def _calc_progress(curr_lvl, start_lvl)

Returns islands progress for the given current and start levels

**Parameters:**
- `curr_lvl` &mdash; int, current level
- `start_lvl` &mdash; int, start level


**Returns:**<br>
int, progress

### def _get_progression()

Returns current islands progress lvl

### def _reset_progression()

Resets island progress

### def _select_img(st, at, mfwm)

Selection function to use in Island-based images

**Parameters:**
- `st` &mdash; renpy related
- `at` &mdash; renpy related
- `mfwm` &mdash; MASFilterWeatherMap for this island


**Returns:**<br>
displayable data

### def _handle_raw_pkg_data(pkg_data, base_err_msg)

Handles raw data and returns clean, parsed data Logs errors

**Parameters:**
- `pkg_data` &mdash; memory buffer


**Returns:**<br>
memory buffer or None

### def _build_filter_pairs(img_map)

Builds filter pairs for IslandFilterWeatherDisplayable or MASFilterWeatherDisplayable

### def _build_ifwd(img_map)

Builds a single IslandFilterWeatherDisplayable using the given image map

### def _build_fwd(img_map)

Builds a single MASFilterWeatherDisplayable using the given image map

### def _build_weather_overlay_transform(child, speed)

A wrapper around mas_islands_weather_overlay_transform It exists so we can properly pass the child argument to the transform

### def _build_displayables(island_imgs_maps, decal_imgs_maps, bg_imgs_maps, overlay_imgs_maps, interior_imgs_map, glitch_frames, tree_lights_imgs)

Takes multiple maps with images and builds displayables from them, sets global vars

**Parameters:**
- `island_imgs_maps` &mdash; the map from island names to raw images map
- `decal_imgs_maps` &mdash; the map from decal names to raw images map
- `bg_imgs_maps` &mdash; the map from bg ids to raw images map
- `overlay_imgs_maps` &mdash; the map from overlay ids to raw images map
- `interior_imgs_map` &mdash; the map from the interior stuff to the raw images map
- `glitch_frames` &mdash; tuple of glitch raw anim frames
- `tree_lights_imgs` &mdash; map of images for the tree lights, format: img_name: disp


### def _get_room_sprite(key, is_lit)

Returns the appropriate displayable for the room sprite based on the criteria

**Parameters:**
- `key` &mdash; str - the sprite key
- `is_lit` &mdash; bool - sprite for the lit or unlit version?


**Returns:**<br>
MASImageData or Null displayable if we failed to get the image

### def _apply_flt_on_room_sprite(room_img_tag, flt)

Returns the room image with the filter applied on it

**Parameters:**
- `room_img_tag` &mdash; str - the image tag
- `flt` &mdash; str - the filter id to use


**Returns:**<br>
image manipulator or Null displayable if we failed to decode the images

### def _is_unlocked(id_)

Checks if a sprite is unlocked

**Parameters:**
- `id_` &mdash; the unique id of the sprite


**Returns:**<br>
boolean

### def _unlock(id_)

Unlocks a sprite

**Parameters:**
- `id_` &mdash; the unique id of the sprite


**Returns:**<br>
boolean whether or not the sprite was unlocked

### def _lock(id_)

Locks a sprite

**Parameters:**
- `id_` &mdash; the unique id of the sprite


**Returns:**<br>
boolean whether or not the sprite was locked

### def _unlock_one()

Unlocks one of the sprites at random. Runs only once

**Returns:**<br>
boolean whether or not a sprite was unlocked

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_0()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_1()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_2()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_3()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_4()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_5()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_6()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_7()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_8()

### def _final_unlocks()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_9()

### def _m1_script0x2dislands0x2devent__unlocks_for_lvl_10()

### def _m1_script0x2dislands0x2devent__handle_unlocks()

Method to unlock various islands features when the player progresses. For example: new decals, new islands, new extra events, set persistent vars, etc.

### def _calc_progress(curr_lvl, start_lvl)

Returns islands progress for the given current and start levels

**Parameters:**
- `curr_lvl` &mdash; int, current level
- `start_lvl` &mdash; int, start level


**Returns:**<br>
int, progress

### def _get_progression()

Returns current islands progress lvl

### def _reset_progression()

Resets island progress

### def _m1_script0x2dislands0x2devent__isld_1_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__isld_2_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__isld_3_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__isld_5_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__chibi_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _play_thunder(transform, st, at)

This is used in a transform to play the THUNDER sound effect

### def _m1_script0x2dislands0x2devent__isld_1_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__isld_2_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__isld_3_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__isld_5_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _m1_script0x2dislands0x2devent__chibi_transform_func(transform, st, at)

A function which we use as a transform, updates the child

### def _play_thunder(transform, st, at)

This is used in a transform to play the THUNDER sound effect

### def _living_room_entry(_old)

Entry pp for lr background

### def _living_room_exit(_new)

Exit pp for lr background

### def _living_room_entry(_old)

Entry pp for lr background

### def _living_room_exit(_new)

Exit pp for lr background

