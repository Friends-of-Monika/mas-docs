# store songs

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def adjustVolume(channel='music', up=True)

---

### def getVolume(channel)

Gets the volume of the given audio channel.

**Parameters:**
- `channel` &mdash; audio channel to get volume for (string)


**Returns:**<br>
volume of the audio channel as double/float

---

### def getUserVolume(channel)

Gets user-defined slider volume of the given channel.

**Parameters:**
- `channel` &mdash; audio channel to get volume for (string)


**Returns:**<br>
value of the user slider for the audio channel (double/float)

---

### def hasMusicMuted()

Checks if the player has the music channel muted or the 'Mute All' option enabled.

**Returns:**<br>
True if the music channel is muted or the 'Mute All' option is enabled, False otherwise

---

### def getPlayingMusicName()

---

### def initMusicChoices(sayori=False)

---

### def setUserVolume(value, channel)

Sets user volume to the given value.

**Parameters:**
- `value` &mdash; value to set volume to. Should be between 0.0 and 1.0.
- `channel` &mdash; channel to set.


---

### def isValidExt(filename)

Checks if the given filename has an appropriate extension

**Parameters:**
- `filename` &mdash; filename to check


**Returns:**<br>
True if valid extension, false otherwise

---

### def cleanGUIText(unclean)

Cleans the given text so its applicable for gui usage

**Parameters:**
- `unclean` &mdash; unclean text


**Returns:**<br>
cleaned text

---

### def isInMusicList(filepath)

Checks if the a song with the given filepath is in the music choices list

**Parameters:**
- `filepath` &mdash; filepath of song to check


**Returns:**<br>
True if filepath is in the music_choices list, False otherwise

---

### def adjustVolume(channel='music', up=True)

---

### def getVolume(channel)

Gets the volume of the given audio channel.

**Parameters:**
- `channel` &mdash; audio channel to get volume for (string)


**Returns:**<br>
volume of the audio channel as double/float

---

### def getUserVolume(channel)

Gets user-defined slider volume of the given channel.

**Parameters:**
- `channel` &mdash; audio channel to get volume for (string)


**Returns:**<br>
value of the user slider for the audio channel (double/float)

---

### def hasMusicMuted()

Checks if the player has the music channel muted or the 'Mute All' option enabled.

**Returns:**<br>
True if the music channel is muted or the 'Mute All' option is enabled, False otherwise

---

### def getPlayingMusicName()

---

### def initMusicChoices(sayori=False)

---

### def setUserVolume(value, channel)

Sets user volume to the given value.

**Parameters:**
- `value` &mdash; value to set volume to. Should be between 0.0 and 1.0.
- `channel` &mdash; channel to set.


---

### def isValidExt(filename)

Checks if the given filename has an appropriate extension

**Parameters:**
- `filename` &mdash; filename to check


**Returns:**<br>
True if valid extension, false otherwise

---

### def cleanGUIText(unclean)

Cleans the given text so its applicable for gui usage

**Parameters:**
- `unclean` &mdash; unclean text


**Returns:**<br>
cleaned text

---

### def isInMusicList(filepath)

Checks if the a song with the given filepath is in the music choices list

**Parameters:**
- `filepath` &mdash; filepath of song to check


**Returns:**<br>
True if filepath is in the music_choices list, False otherwise

---

