# store mas_ptod

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def clr_cn()

SEE clear_console

---

### def ex_cn()

SEE exit_console

---

### def rst_cn()

SEE restart_console

---

### def w_cmd(cmd)

SEE write_command

---

### def x_cmd(context)

SEE exec_command

---

### def wx_cmd(cmd, context)

Does both write_command and exec_command

---

### def write_command(cmd)

Writes a command to the console

**Parameters:**
- `cmd` &mdash; the command to write to the console


---

### def clear_console()

Cleares console hisotry and current line  Also resets state to Single

---

### def restart_console()

Cleares console history and current line, also sets up version text

---

### def exit_console()

Disables the console

---

### def exec_command(context)

Executes the command that is currently in the console. This is basically pressing Enter

**Parameters:**
- `context` &mdash; dict that represnts the current context. You should pass locals here. If None, then we use the local_ctx.


---

### def get_last_line()

Retrieves the last line from the console history

**Returns:**<br>
last line from console history as a string

---

### def set_local_context(context)

Sets the local context to the given context.  Stuff in the old context are forgotten.

---

### def clr_cn()

SEE clear_console

---

### def ex_cn()

SEE exit_console

---

### def rst_cn()

SEE restart_console

---

### def w_cmd(cmd)

SEE write_command

---

### def x_cmd(context)

SEE exec_command

---

### def wx_cmd(cmd, context)

Does both write_command and exec_command

---

### def write_command(cmd)

Writes a command to the console

**Parameters:**
- `cmd` &mdash; the command to write to the console


---

### def clear_console()

Cleares console hisotry and current line  Also resets state to Single

---

### def restart_console()

Cleares console history and current line, also sets up version text

---

### def exit_console()

Disables the console

---

### def exec_command(context)

Executes the command that is currently in the console. This is basically pressing Enter

**Parameters:**
- `context` &mdash; dict that represnts the current context. You should pass locals here. If None, then we use the local_ctx.


---

### def get_last_line()

Retrieves the last line from the console history

**Returns:**<br>
last line from console history as a string

---

### def set_local_context(context)

Sets the local context to the given context.  Stuff in the old context are forgotten.

---

### def has_day_past_tip(tip_num)

Checks if the tip with the given number has already been seen and a day has past since it was unlocked.

**Parameters:**
- `tip_num` &mdash; number of the tip to check


**Returns:**<br>
true if the tip has been seen and a day has past since it was unlocked, False otherwise

---

### def has_day_past_tips()

Variant of has_day_past_tip that can check multiple numbers  SEE has_day_past_tip for more info

**Returns:**<br>
true if all the given tip nums have been see nand a day has past since the latest one was unlocked, False otherwise

---

### def has_day_past_tip(tip_num)

Checks if the tip with the given number has already been seen and a day has past since it was unlocked.

**Parameters:**
- `tip_num` &mdash; number of the tip to check


**Returns:**<br>
true if the tip has been seen and a day has past since it was unlocked, False otherwise

---

### def has_day_past_tips()

Variant of has_day_past_tip that can check multiple numbers  SEE has_day_past_tip for more info

**Returns:**<br>
true if all the given tip nums have been see nand a day has past since the latest one was unlocked, False otherwise

---

