# store mas_randchat

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def reduceRandchatForAff(aff_level)

Reduces the randchat setting if we're too high for the current affection level

---

### def adjustRandFreq(slider_value)

Properly adjusts the random limits given the slider value

**Parameters:**
- `slider_value` &mdash; slider value given from the slider Should be between 0 - 6


---

### def getRandChatDisp(slider_value)

Retrieves the random chatter display string using the given slider value

**Parameters:**
- `slider_value` &mdash; slider value given from the slider


**Returns:**<br>
displayable string that reprsents the current random chatter setting

---

### def setWaitingTime()

Sets up the waiting time for the next random chat, depending on the current random chatter selection.

---

### def wait()

Pauses renpy for a small amount of seconds. This helps adapting fast to a new random chatter selection. All events before a random chat can also be handled rather than to keep waiting the whole time at once.

---

### def waitedLongEnough()

Checks whether the waiting time is up yet.

**Returns:**<br>
boolean to determine whether the wait is over

---

### def reduceRandchatForAff(aff_level)

Reduces the randchat setting if we're too high for the current affection level

---

### def adjustRandFreq(slider_value)

Properly adjusts the random limits given the slider value

**Parameters:**
- `slider_value` &mdash; slider value given from the slider Should be between 0 - 6


---

### def getRandChatDisp(slider_value)

Retrieves the random chatter display string using the given slider value

**Parameters:**
- `slider_value` &mdash; slider value given from the slider


**Returns:**<br>
displayable string that reprsents the current random chatter setting

---

### def setWaitingTime()

Sets up the waiting time for the next random chat, depending on the current random chatter selection.

---

### def wait()

Pauses renpy for a small amount of seconds. This helps adapting fast to a new random chatter selection. All events before a random chat can also be handled rather than to keep waiting the whole time at once.

---

### def waitedLongEnough()

Checks whether the waiting time is up yet.

**Returns:**<br>
boolean to determine whether the wait is over

---

