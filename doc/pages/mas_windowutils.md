## Functions

### def getMousePosRelative()

Gets the mouse position relative to the MAS window. Returned as a set of coordinates (0, 0) being within the MAS window, (1, 0) being to the left, (0, 1) being above, etc.

**Returns:**<br>
Tuple representing the location of the mouse relative to the MAS window in terms of coordinates

### def isCursorInMASWindow()

Checks if the cursor is within the MAS window

**Returns:**<br>
True if cursor is within the mas window (within x/y), False otherwise Also returns True if we cannot get window position

### def isCursorLeftOfMASWindow()

Checks if the cursor is to the left of the MAS window (must be explicitly to the left of the left window bound)

**Returns:**<br>
True if cursor is to the left of the window, False otherwise Also returns False if we cannot get window position

### def isCursorRightOfMASWindow()

Checks if the cursor is to the right of the MAS window (must be explicitly to the right of the right window bound)

**Returns:**<br>
True if cursor is to the right of the window, False otherwise Also returns False if we cannot get window position

### def isCursorAboveMASWindow()

Checks if the cursor is above the MAS window (must be explicitly above the window bound)

**Returns:**<br>
True if cursor is above the window, False otherwise False as well if we're unable to get a window position

### def isCursorBelowMASWindow()

Checks if the cursor is above the MAS window (must be explicitly above the window bound)

**Returns:**<br>
True if cursor is above the window, False otherwise False as well if we're unable to get a window position

### def return_true()

Literally returns True

### def return_false()

Literally returns False

### def getMousePosRelative()

Gets the mouse position relative to the MAS window. Returned as a set of coordinates (0, 0) being within the MAS window, (1, 0) being to the left, (0, 1) being above, etc.

**Returns:**<br>
Tuple representing the location of the mouse relative to the MAS window in terms of coordinates

### def isCursorInMASWindow()

Checks if the cursor is within the MAS window

**Returns:**<br>
True if cursor is within the mas window (within x/y), False otherwise Also returns True if we cannot get window position

### def isCursorLeftOfMASWindow()

Checks if the cursor is to the left of the MAS window (must be explicitly to the left of the left window bound)

**Returns:**<br>
True if cursor is to the left of the window, False otherwise Also returns False if we cannot get window position

### def isCursorRightOfMASWindow()

Checks if the cursor is to the right of the MAS window (must be explicitly to the right of the right window bound)

**Returns:**<br>
True if cursor is to the right of the window, False otherwise Also returns False if we cannot get window position

### def isCursorAboveMASWindow()

Checks if the cursor is above the MAS window (must be explicitly above the window bound)

**Returns:**<br>
True if cursor is above the window, False otherwise False as well if we're unable to get a window position

### def isCursorBelowMASWindow()

Checks if the cursor is above the MAS window (must be explicitly above the window bound)

**Returns:**<br>
True if cursor is above the window, False otherwise False as well if we're unable to get a window position

### def return_true()

Literally returns True

### def return_false()

Literally returns False

### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

### def _m1_zz_windowutils__getActiveWindowObj_Linux()

Gets the active window object

**Returns:**<br>
Xlib.display.Window, or None if errors occur (or not possible to get window obj)

### def _m1_zz_windowutils__getMASWindowLinux()

Funtion to get the MAS window on Linux systems

**Returns:**<br>
Xlib.display.Window representing the MAS window

### def _m1_zz_windowutils__getMASWindowHWND()

Gets the hWnd of the MAS window

**Returns:**<br>
int - represents the hWnd of the MAS window

### def _m1_zz_windowutils__getAbsoluteGeometry(win)

Returns the (x, y, height, width) of a window relative to the top-left of the screen.

**Parameters:**
- `win` &mdash; Xlib.display.Window object representing the window we wish to get absolute geometry of


**Returns:**<br>
tuple, (x, y, width, height) if possible, otherwise None

### def _setMASWindow()

Sets the MAS_WINDOW global on Linux systems

**Returns:**<br>
the window object

### def _getActiveWindowHandle_Windows()

Funtion to get the active window on Windows systems

**Returns:**<br>
string representing the active window handle

### def _getActiveWindowHandle_Linux()

Funtion to get the active window on Linux systems

**Returns:**<br>
string representing the active window handle

### def _getActiveWindowHandle_OSX()

Gets the active window on macOS

### def _tryShowNotification_Windows(title, body)

Tries to push a notification to the notification center on Windows. If it can't it should fail silently to the user.

**Parameters:**
- `title` &mdash; notification title
- `body` &mdash; notification body


**Returns:**<br>
bool. True if the notification was successfully sent, False otherwise

### def _tryShowNotification_Linux(title, body)

Tries to push a notification to the notification center on Linux. If it can't it should fail silently to the user.

**Parameters:**
- `title` &mdash; notification title
- `body` &mdash; notification body


**Returns:**<br>
bool - True, representing the notification's success

### def _tryShowNotification_OSX(title, body)

Tries to push a notification to the notification center on macOS. If it can't it should fail silently to the user.

**Parameters:**
- `title` &mdash; notification title
- `body` &mdash; notification body


**Returns:**<br>
bool - True, representing the notification's success

### def _getAbsoluteMousePos_Windows()

Returns an (x, y) co-ord tuple for the mouse position

**Returns:**<br>
tuple representing the absolute position of the mouse

### def _getAbsoluteMousePos_Linux()

Returns an (x, y) co-ord tuple represening the absolute mouse position

### def _getMASWindowPos_Windows()

Gets the window position for MAS as a tuple of (left, top, right, bottom)

**Returns:**<br>
tuple representing window geometry or None if the window's hWnd could not be found

### def _getMASWindowPos_Linux()

Returns (x1, y1, x2, y2) relative to the top-left of the screen.

**Returns:**<br>
tuple representing (left, top, right, bottom) of the window bounds, or None if not possible to get

### def _m1_zz_windowutils__getActiveWindowObj_Linux()

Gets the active window object

**Returns:**<br>
Xlib.display.Window, or None if errors occur (or not possible to get window obj)

### def _m1_zz_windowutils__getMASWindowLinux()

Funtion to get the MAS window on Linux systems

**Returns:**<br>
Xlib.display.Window representing the MAS window

### def _m1_zz_windowutils__getMASWindowHWND()

Gets the hWnd of the MAS window

**Returns:**<br>
int - represents the hWnd of the MAS window

### def _m1_zz_windowutils__getAbsoluteGeometry(win)

Returns the (x, y, height, width) of a window relative to the top-left of the screen.

**Parameters:**
- `win` &mdash; Xlib.display.Window object representing the window we wish to get absolute geometry of


**Returns:**<br>
tuple, (x, y, width, height) if possible, otherwise None

### def _setMASWindow()

Sets the MAS_WINDOW global on Linux systems

**Returns:**<br>
the window object

### def _getActiveWindowHandle_Windows()

Funtion to get the active window on Windows systems

**Returns:**<br>
string representing the active window handle

### def _getActiveWindowHandle_Linux()

Funtion to get the active window on Linux systems

**Returns:**<br>
string representing the active window handle

### def _getActiveWindowHandle_OSX()

Gets the active window on macOS

### def _tryShowNotification_Windows(title, body)

Tries to push a notification to the notification center on Windows. If it can't it should fail silently to the user.

**Parameters:**
- `title` &mdash; notification title
- `body` &mdash; notification body


**Returns:**<br>
bool. True if the notification was successfully sent, False otherwise

### def _tryShowNotification_Linux(title, body)

Tries to push a notification to the notification center on Linux. If it can't it should fail silently to the user.

**Parameters:**
- `title` &mdash; notification title
- `body` &mdash; notification body


**Returns:**<br>
bool - True, representing the notification's success

### def _tryShowNotification_OSX(title, body)

Tries to push a notification to the notification center on macOS. If it can't it should fail silently to the user.

**Parameters:**
- `title` &mdash; notification title
- `body` &mdash; notification body


**Returns:**<br>
bool - True, representing the notification's success

### def _getAbsoluteMousePos_Windows()

Returns an (x, y) co-ord tuple for the mouse position

**Returns:**<br>
tuple representing the absolute position of the mouse

### def _getAbsoluteMousePos_Linux()

Returns an (x, y) co-ord tuple represening the absolute mouse position

### def _getMASWindowPos_Windows()

Gets the window position for MAS as a tuple of (left, top, right, bottom)

**Returns:**<br>
tuple representing window geometry or None if the window's hWnd could not be found

### def _getMASWindowPos_Linux()

Returns (x1, y1, x2, y2) relative to the top-left of the screen.

**Returns:**<br>
tuple representing (left, top, right, bottom) of the window bounds, or None if not possible to get

