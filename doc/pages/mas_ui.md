# store mas_ui

> [!NOTE]
> These docs are auto-generated. Please [open an issue](https://github.com/Friends-of-Monika/mas-docs/issues/new)
> in case you found inconsistencies, errors or other things we should correct.

## Public functions

### def check_scr_menu_return_values(buttons_data, return_all)

A method to return buttons keys and values

**Parameters:**
- `buttons_data` &mdash; the screen buttons data
- `return_all` &mdash; whether or not we return all items


**Returns:**<br>
dict of key-value pairs

---

### def check_scr_menu_choose_prompt(buttons_data, selected_prompt, default_prompt)

A method to choose a prompt for the return button.

**Parameters:**
- `buttons_data` &mdash; the screen buttons data
- `selected_prompt` &mdash; the prompt for the return button when at least one item was selected
- `default_prompt` &mdash; the prompt to use when no items are selected


**Returns:**<br>
string with prompt

---

### def twopane_menu_delegate_callback(ev_label)

A method to handle delegate logic for some of our events when the user skips a delegate label using search

**Parameters:**
- `ev_label` &mdash; the ev_label of the event the user's selected


---

### def twopane_menu_adj_ranged_callback(adj)

This is called by an adjustment of the twopane menu when its range is being changed (set)

**Parameters:**
- `adj` &mdash; the adj object


---

### def twopane_menu_search_callback(search_query)

The callback the input calls when the user enters anything. Updates flt_evs of the twopane menu and causes RenPy to update the screen.

**Parameters:**
- `search_query` &mdash; search query to filter and sort by


---

### def check_scr_menu_return_values(buttons_data, return_all)

A method to return buttons keys and values

**Parameters:**
- `buttons_data` &mdash; the screen buttons data
- `return_all` &mdash; whether or not we return all items


**Returns:**<br>
dict of key-value pairs

---

### def check_scr_menu_choose_prompt(buttons_data, selected_prompt, default_prompt)

A method to choose a prompt for the return button.

**Parameters:**
- `buttons_data` &mdash; the screen buttons data
- `selected_prompt` &mdash; the prompt for the return button when at least one item was selected
- `default_prompt` &mdash; the prompt to use when no items are selected


**Returns:**<br>
string with prompt

---

### def twopane_menu_delegate_callback(ev_label)

A method to handle delegate logic for some of our events when the user skips a delegate label using search

**Parameters:**
- `ev_label` &mdash; the ev_label of the event the user's selected


---

### def twopane_menu_adj_ranged_callback(adj)

This is called by an adjustment of the twopane menu when its range is being changed (set)

**Parameters:**
- `adj` &mdash; the adj object


---

### def twopane_menu_search_callback(search_query)

The callback the input calls when the user enters anything. Updates flt_evs of the twopane menu and causes RenPy to update the screen.

**Parameters:**
- `search_query` &mdash; search query to filter and sort by


---

