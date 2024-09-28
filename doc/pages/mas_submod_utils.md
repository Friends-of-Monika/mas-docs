## Functions

### def writeLog(msg)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `submod_log.debug, submod_log.info, submod_log.warning, submod_log.error, submod_log.exception`.

Writes to the submod log if it is open

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='submod_log.debug, submod_log.info, submod_log.warning, submod_log.error, submod_log.exception')`


**Parameters:**
- `msg` &mdash; message to write to log


### def isSubmodInstalled(name, version=None)

Checks if a submod with `name` is installed

**Parameters:**
- `name` &mdash; name of the submod to check for
- `version` &mdash; if a specific version (or greater) is installed


**Returns:**<br>
boolean: - True if submod with name is installed - False otherwise

### def writeLog(msg)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Instead, consider using `submod_log.debug, submod_log.info, submod_log.warning, submod_log.error, submod_log.exception`.

Writes to the submod log if it is open

**Decorators:**
- `@store.mas_utils.deprecated(use_instead='submod_log.debug, submod_log.info, submod_log.warning, submod_log.error, submod_log.exception')`


**Parameters:**
- `msg` &mdash; message to write to log


### def isSubmodInstalled(name, version=None)

Checks if a submod with `name` is installed

**Parameters:**
- `name` &mdash; name of the submod to check for
- `version` &mdash; if a specific version (or greater) is installed


**Returns:**<br>
boolean: - True if submod with name is installed - False otherwise

### def functionplugin(_label, _args=None, auto_error_handling=True, priority=0)

Decorator function to register a plugin  The same as registerFunction. See its doc for parameter details

### def getAndRunFunctions(key=None)

Gets and runs functions within the key provided

**Parameters:**
- `key` &mdash; Key to retrieve and run functions from


### def registerFunction(key, _function, args=None, auto_error_handling=True, priority=DEF_PRIORITY)

Registers a function to the function_plugins dict

**Parameters:**
- `key` &mdash; key to add the function to. NOTE: The key is either a label, or a function name NOTE: Function names only work if the function contains a getAndRunFunctions call. Without it, it does nothing.
- `_function` &mdash; function to register
- `auto_error_handling` &mdash; whether or function plugins should ignore errors in functions (Set this to False for functions which call or jump)
- `priority` &mdash; Order priority to run functions (Like init levels, the lower the number, the earlier it runs)


**Returns:**<br>
boolean: - True if the function was registered successfully - False otherwise

### def getArgs(key, _function)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Wrap your callable in 'functools.partial' to provide it args/kwargs.

Gets args for the given function at the given key

**Decorators:**
- `@mas_utils.deprecated(use_instead='functools.partial', use_instead_msg_fmt="Wrap your callable in '{use_instead}' to provide it args/kwargs.")`


**Parameters:**
- `key` &mdash; key to retrieve the function from
- `_function` &mdash; function to retrieve args from


**Returns:**<br>
list of args if the function is present If function is not present, None is returned

### def setArgs(key, _function, args=None)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Wrap your callable in 'functools.partial' to provide it args/kwargs.

Sets args for the given function at the key

**Decorators:**
- `@mas_utils.deprecated(use_instead='functools.partial', use_instead_msg_fmt="Wrap your callable in '{use_instead}' to provide it args/kwargs.")`


**Parameters:**
- `key` &mdash; key that the function's function dict is stored in
- `_function` &mdash; function to set the args


**Returns:**<br>
boolean: - True if args were set successfully - False if not

### def unregisterFunction(key, _function)

Unregisters a function from the function_plugins dict

**Parameters:**
- `key` &mdash; key the function we want to unregister is in
- `_function` &mdash; function we want to unregister


**Returns:**<br>
boolean: - True if function was unregistered successfully - False otherwise

### def functionplugin(_label, _args=None, auto_error_handling=True, priority=0)

Decorator function to register a plugin  The same as registerFunction. See its doc for parameter details

### def getAndRunFunctions(key=None)

Gets and runs functions within the key provided

**Parameters:**
- `key` &mdash; Key to retrieve and run functions from


### def registerFunction(key, _function, args=None, auto_error_handling=True, priority=DEF_PRIORITY)

Registers a function to the function_plugins dict

**Parameters:**
- `key` &mdash; key to add the function to. NOTE: The key is either a label, or a function name NOTE: Function names only work if the function contains a getAndRunFunctions call. Without it, it does nothing.
- `_function` &mdash; function to register
- `auto_error_handling` &mdash; whether or function plugins should ignore errors in functions (Set this to False for functions which call or jump)
- `priority` &mdash; Order priority to run functions (Like init levels, the lower the number, the earlier it runs)


**Returns:**<br>
boolean: - True if the function was registered successfully - False otherwise

### def getArgs(key, _function)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Wrap your callable in 'functools.partial' to provide it args/kwargs.

Gets args for the given function at the given key

**Decorators:**
- `@mas_utils.deprecated(use_instead='functools.partial', use_instead_msg_fmt="Wrap your callable in '{use_instead}' to provide it args/kwargs.")`


**Parameters:**
- `key` &mdash; key to retrieve the function from
- `_function` &mdash; function to retrieve args from


**Returns:**<br>
list of args if the function is present If function is not present, None is returned

### def setArgs(key, _function, args=None)

> [!WARNING]
> This function is flagged as **deprecated** and **is not recommended for use.**<br>
> Wrap your callable in 'functools.partial' to provide it args/kwargs.

Sets args for the given function at the key

**Decorators:**
- `@mas_utils.deprecated(use_instead='functools.partial', use_instead_msg_fmt="Wrap your callable in '{use_instead}' to provide it args/kwargs.")`


**Parameters:**
- `key` &mdash; key that the function's function dict is stored in
- `_function` &mdash; function to set the args


**Returns:**<br>
boolean: - True if args were set successfully - False if not

### def unregisterFunction(key, _function)

Unregisters a function from the function_plugins dict

**Parameters:**
- `key` &mdash; key the function we want to unregister is in
- `_function` &mdash; function we want to unregister


**Returns:**<br>
boolean: - True if function was unregistered successfully - False otherwise

