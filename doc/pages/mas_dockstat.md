## Functions

### def decodeImages(dockstat, image_dict, selective=[])

Attempts to decode the iamges

**Parameters:**
- `dockstat` &mdash; docking station to use
- `image_dict` &mdash; image map to use
- `selective` &mdash; list of images keys to decode If not passed in, we decode EVERYTHINg (DEfault: [])


### def removeImages(dockstat, image_dict, selective=[], log=False)

Removes the decoded images at the end of their lifecycle

**Parameters:**
- `dockstat` &mdash; docking station
- `image_dict` &mdash; image map to use
- `selective` &mdash; list of image keys to delete If not passed in, we delete everything in the image dict (Default: [])
- `log` &mdash; should we log a delete failure? (Default: False)


### def decodeImages(dockstat, image_dict, selective=[])

Attempts to decode the iamges

**Parameters:**
- `dockstat` &mdash; docking station to use
- `image_dict` &mdash; image map to use
- `selective` &mdash; list of images keys to decode If not passed in, we decode EVERYTHINg (DEfault: [])


### def removeImages(dockstat, image_dict, selective=[], log=False)

Removes the decoded images at the end of their lifecycle

**Parameters:**
- `dockstat` &mdash; docking station
- `image_dict` &mdash; image map to use
- `selective` &mdash; list of image keys to delete If not passed in, we delete everything in the image dict (Default: [])
- `log` &mdash; should we log a delete failure? (Default: False)


### def setMoniSize(tdelta)

Sets the appropriate persistent size for monika

**Parameters:**
- `tdelta` &mdash; timedelta to use


### def setMoniSize(tdelta)

Sets the appropriate persistent size for monika

**Parameters:**
- `tdelta` &mdash; timedelta to use


### def checkMonika(status, moni_data)

Parses if a given set of monika data is a rogue monika, our monika, and so on, and does checkins and more for the appropriate case.

**Parameters:**
- `status` &mdash; findMonika's return status
- `moni_data` &mdash; findMonika's return data


**Returns:**<br>
TBD

### def checkinMonika()

Adds entry to checkin log that monika has returned to the spaceroom. Also clears the global checksum var.

### def checkoutMonika(chksum)

Adds entry to checkout log that monika has left the spaceroom. Also sets the chk to the global checksum var. Also removes monikas that had the same checksum

**Parameters:**
- `chksum` &mdash; monika's checksum when checking her out.


### def triageMonika(from_empty)

Jumps to an appropriate label based on retmoni_status and retmoni_data. If retmoni_status is None, we dont do anything.

**Parameters:**
- `from_empty` &mdash; True if we should assume from empty desk, False otherwise.


### def packageCheck(dockstat, pkg_name, pkg_slip, on_succ, on_fail, sign=True)

Checks for existence of a package that matches the pkg name and slip.  This acts as a wrapper around the signForPackage that can encapsulate return values with different values.  Success is when signForPackage returns 1. All other values are considered failures.

**Parameters:**
- `dockstat` &mdash; docking station to check packag ein
- `pkg_name` &mdash; name of the package to check
- `pkg_slip` &mdash; checksum of this package
- `on_succ` &mdash; value to return on successful package check
- `on_fail` &mdash; value to return on failed package check
- `sign` &mdash; True to use signForPackage (aka delete after checking), False uses getPackage + createPackageSlip (aka no delete after checking) (Default: True)


### def generateMonika(dockstat, logpath)

Generates / writes a monika blob file.

**Parameters:**
- `dockstat` &mdash; the docking station to generate Monika in
- `logpath` &mdash; path of log to write messagse to


**Returns:**<br>
checksum of monika -1 if checksums didnt match (and we cant verify data integrity of the generated moinika file) None otherwise

### def init_findMonika(dockstat)

findMonika variation that is meant to be run at init time.

**Parameters:**
- `dockstat` &mdash; MASDockingStation to use


### def findMonika(dockstat, logpath, at_init)

Attempts to find monika in the giving docking station

**Parameters:**
- `dockstat` &mdash; MASDockingStation to use
- `logpath` &mdash; path of log to write messages to
- `at_init` &mdash; True if we are in init, False if not


**Returns:**<br>
tuple of the following format: [0]: MAS_PKG_* constants depending on the state of monika [1]: either list of data or persistent object of data. Will be None if no data or errors occured

### def parseMoniData(data_line, log)

Parses monika data into its components

**Parameters:**
- `data_line` &mdash; PIPE delimeted data line
- `log` &mdash; log to write messages to, if needed


**Returns:**<br>
list of the following format: [0]: datetime of first sessin [1]: playername [2]: monika's nickname (could be Monika) [3]: affection, integer value (dont really rely on this for much) [4]: monika's hair setting [5]: monika's clothes setting  OR None if general (not item-specific) parse errors occurs)

### def parseMoniDataPer(data_line, log)

Parses persitent data into a persitent object.

**Parameters:**
- `data_line` &mdash; the data portion that may contain a persitent
- `log` &mdash; log to write messages to, if needed


**Returns:**<br>
a persistent object, or None if failure

### def selectReturnHomeGreeting(gre_type=None)

Selects the correct Return Home greeting.  If None was selected, we return the default returned home gre  We also default type to TYPE_GENERIC_RET if no type is given

**Parameters:**
- `gre_type` &mdash; greeting type to find If None, we use TYPE_GENERIC_RET (Default: None)


**Returns:**<br>
Event object representing the selected greeting

### def getCheckTimes(chksum=None)

Gets the corresponding checkin/out times for the given chksum.

**Parameters:**
- `chksum` &mdash; chksum to retrieve checkin/checkout times. If None, then we simply get the latest checkin/checkout, regardless if they match or not. (Default: None)


**Returns:**<br>
tuple of the following format: [0] - checkout time [1] - checkin time If any param is None, then we couldn't find the matching chksum or there were no entries

### def diffCheckTimes(index=None)

Returns the difference between the latest checkout and check in times We do checkin - checkout.

**Parameters:**
- `index` &mdash; the index of checkout/checkin to use when diffing If None, we use the latest one (Default: None)


**Returns:**<br>
timedelta of the difference between checkin and checkout

### def timeOut(_date)

Given a date, return how long monika has been out  We assume that checkout logs are the source of truth

**Parameters:**
- `_date` &mdash; date to check


### def checkMonika(status, moni_data)

Parses if a given set of monika data is a rogue monika, our monika, and so on, and does checkins and more for the appropriate case.

**Parameters:**
- `status` &mdash; findMonika's return status
- `moni_data` &mdash; findMonika's return data


**Returns:**<br>
TBD

### def checkinMonika()

Adds entry to checkin log that monika has returned to the spaceroom. Also clears the global checksum var.

### def checkoutMonika(chksum)

Adds entry to checkout log that monika has left the spaceroom. Also sets the chk to the global checksum var. Also removes monikas that had the same checksum

**Parameters:**
- `chksum` &mdash; monika's checksum when checking her out.


### def triageMonika(from_empty)

Jumps to an appropriate label based on retmoni_status and retmoni_data. If retmoni_status is None, we dont do anything.

**Parameters:**
- `from_empty` &mdash; True if we should assume from empty desk, False otherwise.


### def packageCheck(dockstat, pkg_name, pkg_slip, on_succ, on_fail, sign=True)

Checks for existence of a package that matches the pkg name and slip.  This acts as a wrapper around the signForPackage that can encapsulate return values with different values.  Success is when signForPackage returns 1. All other values are considered failures.

**Parameters:**
- `dockstat` &mdash; docking station to check packag ein
- `pkg_name` &mdash; name of the package to check
- `pkg_slip` &mdash; checksum of this package
- `on_succ` &mdash; value to return on successful package check
- `on_fail` &mdash; value to return on failed package check
- `sign` &mdash; True to use signForPackage (aka delete after checking), False uses getPackage + createPackageSlip (aka no delete after checking) (Default: True)


### def generateMonika(dockstat, logpath)

Generates / writes a monika blob file.

**Parameters:**
- `dockstat` &mdash; the docking station to generate Monika in
- `logpath` &mdash; path of log to write messagse to


**Returns:**<br>
checksum of monika -1 if checksums didnt match (and we cant verify data integrity of the generated moinika file) None otherwise

### def init_findMonika(dockstat)

findMonika variation that is meant to be run at init time.

**Parameters:**
- `dockstat` &mdash; MASDockingStation to use


### def findMonika(dockstat, logpath, at_init)

Attempts to find monika in the giving docking station

**Parameters:**
- `dockstat` &mdash; MASDockingStation to use
- `logpath` &mdash; path of log to write messages to
- `at_init` &mdash; True if we are in init, False if not


**Returns:**<br>
tuple of the following format: [0]: MAS_PKG_* constants depending on the state of monika [1]: either list of data or persistent object of data. Will be None if no data or errors occured

### def parseMoniData(data_line, log)

Parses monika data into its components

**Parameters:**
- `data_line` &mdash; PIPE delimeted data line
- `log` &mdash; log to write messages to, if needed


**Returns:**<br>
list of the following format: [0]: datetime of first sessin [1]: playername [2]: monika's nickname (could be Monika) [3]: affection, integer value (dont really rely on this for much) [4]: monika's hair setting [5]: monika's clothes setting  OR None if general (not item-specific) parse errors occurs)

### def parseMoniDataPer(data_line, log)

Parses persitent data into a persitent object.

**Parameters:**
- `data_line` &mdash; the data portion that may contain a persitent
- `log` &mdash; log to write messages to, if needed


**Returns:**<br>
a persistent object, or None if failure

### def selectReturnHomeGreeting(gre_type=None)

Selects the correct Return Home greeting.  If None was selected, we return the default returned home gre  We also default type to TYPE_GENERIC_RET if no type is given

**Parameters:**
- `gre_type` &mdash; greeting type to find If None, we use TYPE_GENERIC_RET (Default: None)


**Returns:**<br>
Event object representing the selected greeting

### def getCheckTimes(chksum=None)

Gets the corresponding checkin/out times for the given chksum.

**Parameters:**
- `chksum` &mdash; chksum to retrieve checkin/checkout times. If None, then we simply get the latest checkin/checkout, regardless if they match or not. (Default: None)


**Returns:**<br>
tuple of the following format: [0] - checkout time [1] - checkin time If any param is None, then we couldn't find the matching chksum or there were no entries

### def diffCheckTimes(index=None)

Returns the difference between the latest checkout and check in times We do checkin - checkout.

**Parameters:**
- `index` &mdash; the index of checkout/checkin to use when diffing If None, we use the latest one (Default: None)


**Returns:**<br>
timedelta of the difference between checkin and checkout

### def timeOut(_date)

Given a date, return how long monika has been out  We assume that checkout logs are the source of truth

**Parameters:**
- `_date` &mdash; date to check


### def abortGenPromise()

Attempts to about the monikagen promise and properly delete the monika package.

### def abortGenPromise()

Attempts to about the monikagen promise and properly delete the monika package.

