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

## Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _sanitizeVolume(value)

Santizes the given value as if it were a volume.

**Parameters:**
- `value` &mdash; value to sanitize


**Returns:**<br>
valid volume value

---

### def _m1_zz_music_selector__paginate(music_list)

Paginates the music list and returns a dict of the pages.

**Parameters:**
- `music_list` &mdash; list of music choice tuples (see initMusicChoices)


**Returns:**<br>
dict of music choices, paginated nicely: [0]: first page of music [1]: next page of music ... [n]: last page of music

---

### def _m1_zz_music_selector__genPage(music_list)

Generates the a page of music choices

**Parameters:**
- `music_list` &mdash; list of music choice tuples (see initMusicChoices)


**Returns:**<br>
tuple of the following format: [0] - page of the music choices [1] - reamining items in the music_list

---

### def _m1_zz_music_selector__scanCustomBGM(music_list)

Scans the custom music directory for custom musics and adds them to the given music_list.  IN/OUT: music_list - list of music tuples to append to

---

### def _getAudioFile(filepath)

Atteempts to retrive the correct audio object based on file extension

**Parameters:**
- `filepath` &mdash; full filepath to the audio file we want


**Returns:**<br>
tuple of the following format: [0]: audio object we want (May be None if this failed to load) [1]: extension of this audio object

---

### def _getDispName(_audio_file, _ext, _filename)

Attempts to retreive the display name for an audio file If that fails, then it will use the _filename as song name, minus extension.

**Parameters:**
- `_audio_file` &mdash; audio object
- `_ext` &mdash; extension of the audio file
- `_filename` &mdash; filename of the audio file


**Returns:**<br>
The name of this Song (probably)

---

### def _getLoopData(_audio_file, _ext)

Attempts to retrieve loop data from the given audio file and generates the appropraite string to put in front of the file name

**Parameters:**
- `_audio_file` &mdash; audio object
- `_ext` &mdash; extension of hte audio file


**Returns:**<br>
loop string, or and empty string if no loop string available

---

### def _getMP3(filepath)

Attempts to retrieve the MP3 object from the given audio file

**Parameters:**
- `filepath` &mdash; full filepath to the mp3 file want tags from


**Returns:**<br>
mutagen.mp3.EasyMP3 object, or None if we coudlnt do it

---

### def _getMP3Name(_audio_file)

Attempts to retrieve song name from mp3 id3 tag

**Parameters:**
- `_audio_file` &mdash; audio object


**Returns:**<br>
The display name for this song, or None if not possible

---

### def _getOgg(filepath)

Attempts to retreive the Ogg object from the given audio file

**Parameters:**
- `filepath` &mdash; full filepath to the ogg file


**Returns:**<br>
mutagen.ogg.OggVorbis or None if we coudlnt get the info

---

### def _getOggName(_audio_file)

Attempts to retreive song name from Ogg tag

**Parameters:**
- `_audio_file` &mdash; audio object


**Returns:**<br>
The display name for this song, or None if not possible

---

### def _getOggLoop(_audio_file, _ext)

Attempts to retreive loop data from Ogg tags

**Parameters:**
- `_audio_file` &mdash; audio object
- `_ext` &mdash; extension of the audio file


**Returns:**<br>
the loop string we should use, or "" if no loop

---

### def _getOggLoopMAS(loopstart, loopend, _audio_file)

Attempts to retrieve MAS-based loop data from Ogg tags

**Parameters:**
- `loopstart` &mdash; list of loopstart tags
- `loopend` &mdash; list of loopend tags
- `_audio_file` &mdash; audio object


**Returns:**<br>
the loop string we should use or "" if no loop

---

### def _getOggLoopRPG(loopstart, looplen, _audio_file)

Attempts to retrieve RPGMaker-based loop data form Ogg tags

**Parameters:**
- `loopstart` &mdash; list of loopstart tags
- `looplen` &mdash; list of loop length tags
- `_audio_file` &mdash; audio object


**Returns:**<br>
the loop string we should use or "" if no loop

---

### def _getOpus(filepath)

Attempts to retrieve the Opus object from the given audio file

**Parameters:**
- `filepath` &mdash; full filepath to the opus file


**Returns:**<br>
mutagen.ogg.OggOpus or None if we couldnt get the info

---

### def _sanitizeVolume(value)

Santizes the given value as if it were a volume.

**Parameters:**
- `value` &mdash; value to sanitize


**Returns:**<br>
valid volume value

---

### def _m1_zz_music_selector__paginate(music_list)

Paginates the music list and returns a dict of the pages.

**Parameters:**
- `music_list` &mdash; list of music choice tuples (see initMusicChoices)


**Returns:**<br>
dict of music choices, paginated nicely: [0]: first page of music [1]: next page of music ... [n]: last page of music

---

### def _m1_zz_music_selector__genPage(music_list)

Generates the a page of music choices

**Parameters:**
- `music_list` &mdash; list of music choice tuples (see initMusicChoices)


**Returns:**<br>
tuple of the following format: [0] - page of the music choices [1] - reamining items in the music_list

---

### def _m1_zz_music_selector__scanCustomBGM(music_list)

Scans the custom music directory for custom musics and adds them to the given music_list.  IN/OUT: music_list - list of music tuples to append to

---

### def _getAudioFile(filepath)

Atteempts to retrive the correct audio object based on file extension

**Parameters:**
- `filepath` &mdash; full filepath to the audio file we want


**Returns:**<br>
tuple of the following format: [0]: audio object we want (May be None if this failed to load) [1]: extension of this audio object

---

### def _getDispName(_audio_file, _ext, _filename)

Attempts to retreive the display name for an audio file If that fails, then it will use the _filename as song name, minus extension.

**Parameters:**
- `_audio_file` &mdash; audio object
- `_ext` &mdash; extension of the audio file
- `_filename` &mdash; filename of the audio file


**Returns:**<br>
The name of this Song (probably)

---

### def _getLoopData(_audio_file, _ext)

Attempts to retrieve loop data from the given audio file and generates the appropraite string to put in front of the file name

**Parameters:**
- `_audio_file` &mdash; audio object
- `_ext` &mdash; extension of hte audio file


**Returns:**<br>
loop string, or and empty string if no loop string available

---

### def _getMP3(filepath)

Attempts to retrieve the MP3 object from the given audio file

**Parameters:**
- `filepath` &mdash; full filepath to the mp3 file want tags from


**Returns:**<br>
mutagen.mp3.EasyMP3 object, or None if we coudlnt do it

---

### def _getMP3Name(_audio_file)

Attempts to retrieve song name from mp3 id3 tag

**Parameters:**
- `_audio_file` &mdash; audio object


**Returns:**<br>
The display name for this song, or None if not possible

---

### def _getOgg(filepath)

Attempts to retreive the Ogg object from the given audio file

**Parameters:**
- `filepath` &mdash; full filepath to the ogg file


**Returns:**<br>
mutagen.ogg.OggVorbis or None if we coudlnt get the info

---

### def _getOggName(_audio_file)

Attempts to retreive song name from Ogg tag

**Parameters:**
- `_audio_file` &mdash; audio object


**Returns:**<br>
The display name for this song, or None if not possible

---

### def _getOggLoop(_audio_file, _ext)

Attempts to retreive loop data from Ogg tags

**Parameters:**
- `_audio_file` &mdash; audio object
- `_ext` &mdash; extension of the audio file


**Returns:**<br>
the loop string we should use, or "" if no loop

---

### def _getOggLoopMAS(loopstart, loopend, _audio_file)

Attempts to retrieve MAS-based loop data from Ogg tags

**Parameters:**
- `loopstart` &mdash; list of loopstart tags
- `loopend` &mdash; list of loopend tags
- `_audio_file` &mdash; audio object


**Returns:**<br>
the loop string we should use or "" if no loop

---

### def _getOggLoopRPG(loopstart, looplen, _audio_file)

Attempts to retrieve RPGMaker-based loop data form Ogg tags

**Parameters:**
- `loopstart` &mdash; list of loopstart tags
- `looplen` &mdash; list of loop length tags
- `_audio_file` &mdash; audio object


**Returns:**<br>
the loop string we should use or "" if no loop

---

### def _getOpus(filepath)

Attempts to retrieve the Opus object from the given audio file

**Parameters:**
- `filepath` &mdash; full filepath to the opus file


**Returns:**<br>
mutagen.ogg.OggOpus or None if we couldnt get the info

---

