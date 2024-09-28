## Functions

### def clr_cn()

SEE clear_console

### def ex_cn()

SEE exit_console

### def rst_cn()

SEE restart_console

### def w_cmd(cmd)

SEE write_command

### def x_cmd(context)

SEE exec_command

### def wx_cmd(cmd, context)

Does both write_command and exec_command

### def write_command(cmd)

Writes a command to the console

**Parameters:**
- `cmd` &mdash; the command to write to the console


### def clear_console()

Cleares console hisotry and current line  Also resets state to Single

### def restart_console()

Cleares console history and current line, also sets up version text

### def exit_console()

Disables the console

### def _m1_script0x2dpython__exec_cmd(line, context, block=False)

Tries to eval the line first, then executes. Returns the result of the command

**Parameters:**
- `line` &mdash; line to eval / exec
- `context` &mdash; dict that represnts the current context. should be locals
- `block` &mdash; True means we are executing a block command and should skip eval


**Returns:**<br>
the result of the command, as a string

### def _m1_script0x2dpython__exec_exec(line, context)

Runs exec on the given line Returns an empty string or a string with an error if it occured.

**Parameters:**
- `line` &mdash; line to exec
- `context` &mdash; dict that represents the current context


**Returns:**<br>
empty string or string with error message

### def _m1_script0x2dpython__exec_evalexec(line, context)

Tries to eval the line first, then executes. Returns the result of the command

**Parameters:**
- `line` &mdash; line to eval / exec
- `context` &mdash; dict that represents the current context.


**Returns:**<br>
the result of the command as a string

### def exec_command(context)

Executes the command that is currently in the console. This is basically pressing Enter

**Parameters:**
- `context` &mdash; dict that represnts the current context. You should pass locals here. If None, then we use the local_ctx.


### def get_last_line()

Retrieves the last line from the console history

**Returns:**<br>
last line from console history as a string

### def set_local_context(context)

Sets the local context to the given context.  Stuff in the old context are forgotten.

### def _m1_script0x2dpython__pushi(indent_level)

Pushes a indent level into the stack

**Parameters:**
- `indent_level` &mdash; indent to push into stack


### def _m1_script0x2dpython__popi()

Pops indent level from stack  REUTRNS: popped indent level

### def _m1_script0x2dpython__peeki()

Returns value that would be popped from stack

**Returns:**<br>
indent level that would be popped

### def _exp_toString(exp)

Converts the given exception into a string that looks like how python interpreter prints out exceptions

### def _indent_line(line)

Prepends the given line with an appropraite number of spaces, depending on the current stack level

**Parameters:**
- `line` &mdash; line to prepend


**Returns:**<br>
line prepended with spaces

### def _count_sp(line)

Counts number of spaces that prefix this line

**Parameters:**
- `line` &mdash; line to cound spaces


**Returns:**<br>
number of spaces at start of line

### def _update_console_history()

Updates the console history with the list of new lines to add

**Parameters:**
- `new_items` &mdash; the items to add to the console history


### def _update_console_history_list(new_items)

Updates console history with list of new lines to add

**Parameters:**
- `new_items` &mdash; list of new itme sto add to console history


### def _line_break(line)

Lines cant be too large. This will line break entries.

**Parameters:**
- `line` &mdash; the line to break


**Returns:**<br>
list of strings, each item is a line.

### def clr_cn()

SEE clear_console

### def ex_cn()

SEE exit_console

### def rst_cn()

SEE restart_console

### def w_cmd(cmd)

SEE write_command

### def x_cmd(context)

SEE exec_command

### def wx_cmd(cmd, context)

Does both write_command and exec_command

### def write_command(cmd)

Writes a command to the console

**Parameters:**
- `cmd` &mdash; the command to write to the console


### def clear_console()

Cleares console hisotry and current line  Also resets state to Single

### def restart_console()

Cleares console history and current line, also sets up version text

### def exit_console()

Disables the console

### def _m1_script0x2dpython__exec_cmd(line, context, block=False)

Tries to eval the line first, then executes. Returns the result of the command

**Parameters:**
- `line` &mdash; line to eval / exec
- `context` &mdash; dict that represnts the current context. should be locals
- `block` &mdash; True means we are executing a block command and should skip eval


**Returns:**<br>
the result of the command, as a string

### def _m1_script0x2dpython__exec_exec(line, context)

Runs exec on the given line Returns an empty string or a string with an error if it occured.

**Parameters:**
- `line` &mdash; line to exec
- `context` &mdash; dict that represents the current context


**Returns:**<br>
empty string or string with error message

### def _m1_script0x2dpython__exec_evalexec(line, context)

Tries to eval the line first, then executes. Returns the result of the command

**Parameters:**
- `line` &mdash; line to eval / exec
- `context` &mdash; dict that represents the current context.


**Returns:**<br>
the result of the command as a string

### def exec_command(context)

Executes the command that is currently in the console. This is basically pressing Enter

**Parameters:**
- `context` &mdash; dict that represnts the current context. You should pass locals here. If None, then we use the local_ctx.


### def get_last_line()

Retrieves the last line from the console history

**Returns:**<br>
last line from console history as a string

### def set_local_context(context)

Sets the local context to the given context.  Stuff in the old context are forgotten.

### def _m1_script0x2dpython__pushi(indent_level)

Pushes a indent level into the stack

**Parameters:**
- `indent_level` &mdash; indent to push into stack


### def _m1_script0x2dpython__popi()

Pops indent level from stack  REUTRNS: popped indent level

### def _m1_script0x2dpython__peeki()

Returns value that would be popped from stack

**Returns:**<br>
indent level that would be popped

### def _exp_toString(exp)

Converts the given exception into a string that looks like how python interpreter prints out exceptions

### def _indent_line(line)

Prepends the given line with an appropraite number of spaces, depending on the current stack level

**Parameters:**
- `line` &mdash; line to prepend


**Returns:**<br>
line prepended with spaces

### def _count_sp(line)

Counts number of spaces that prefix this line

**Parameters:**
- `line` &mdash; line to cound spaces


**Returns:**<br>
number of spaces at start of line

### def _update_console_history()

Updates the console history with the list of new lines to add

**Parameters:**
- `new_items` &mdash; the items to add to the console history


### def _update_console_history_list(new_items)

Updates console history with list of new lines to add

**Parameters:**
- `new_items` &mdash; list of new itme sto add to console history


### def _line_break(line)

Lines cant be too large. This will line break entries.

**Parameters:**
- `line` &mdash; the line to break


**Returns:**<br>
list of strings, each item is a line.

### def has_day_past_tip(tip_num)

Checks if the tip with the given number has already been seen and a day has past since it was unlocked.

**Parameters:**
- `tip_num` &mdash; number of the tip to check


**Returns:**<br>
true if the tip has been seen and a day has past since it was unlocked, False otherwise

### def has_day_past_tips()

Variant of has_day_past_tip that can check multiple numbers  SEE has_day_past_tip for more info

**Returns:**<br>
true if all the given tip nums have been see nand a day has past since the latest one was unlocked, False otherwise

### def has_day_past_tip(tip_num)

Checks if the tip with the given number has already been seen and a day has past since it was unlocked.

**Parameters:**
- `tip_num` &mdash; number of the tip to check


**Returns:**<br>
true if the tip has been seen and a day has past since it was unlocked, False otherwise

### def has_day_past_tips()

Variant of has_day_past_tip that can check multiple numbers  SEE has_day_past_tip for more info

**Returns:**<br>
true if all the given tip nums have been see nand a day has past since the latest one was unlocked, False otherwise

