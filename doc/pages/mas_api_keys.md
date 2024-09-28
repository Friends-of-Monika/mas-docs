## Functions

### def feature_registered(feature)

Checks if a feature is registered for API keys

**Parameters:**
- `feature` &mdash; feature to check (string)


**Returns:**<br>
True if the feature is registered for API keys

### def register_feature(feature, data)

Registers a feature for API key usage

**Parameters:**
- `feature` &mdash; name of the feature
- `data` &mdash; data to associate with the feature


### def features_for_display()

Returns list of the features for display

**Returns:**<br>
list of the features as tuples, sorted for display: [0] - the display name of the feature [1] - the on_change function to run

### def has_features()

Do we have API-key based features?

**Returns:**<br>
True if we have api key based features

### def clean_key(dirty_key)

Cleans an aPI key

**Parameters:**
- `dirty_key` &mdash; key to clean


**Returns:**<br>
cleaned key

### def _run_on_change(feature, api_key)

Runs on change for a feature with api key

**Parameters:**
- `feature` &mdash; feature to run on change for
- `api_key` &mdash; api key to run on change with


**Returns:**<br>
tuple of the following format: [0] - True if valid key, False if not [1] - error message to show

### def screen_clear(feature)

Called when the clear button is used on the api key screen

**Parameters:**
- `feature` &mdash; the feature whose key is being cleared


### def screen_paste(feature)

Called when the paste button is used on the api key screen.

**Parameters:**
- `feature` &mdash; the feature whose key is being pasted


### def screen_update_cert()

Called when the update cert button is used on the api key screen

### def load_keys()

Loads API keys from config file

### def save_keys()

Saves API keys to disk

### def feature_registered(feature)

Checks if a feature is registered for API keys

**Parameters:**
- `feature` &mdash; feature to check (string)


**Returns:**<br>
True if the feature is registered for API keys

### def register_feature(feature, data)

Registers a feature for API key usage

**Parameters:**
- `feature` &mdash; name of the feature
- `data` &mdash; data to associate with the feature


### def features_for_display()

Returns list of the features for display

**Returns:**<br>
list of the features as tuples, sorted for display: [0] - the display name of the feature [1] - the on_change function to run

### def has_features()

Do we have API-key based features?

**Returns:**<br>
True if we have api key based features

### def clean_key(dirty_key)

Cleans an aPI key

**Parameters:**
- `dirty_key` &mdash; key to clean


**Returns:**<br>
cleaned key

### def _run_on_change(feature, api_key)

Runs on change for a feature with api key

**Parameters:**
- `feature` &mdash; feature to run on change for
- `api_key` &mdash; api key to run on change with


**Returns:**<br>
tuple of the following format: [0] - True if valid key, False if not [1] - error message to show

### def screen_clear(feature)

Called when the clear button is used on the api key screen

**Parameters:**
- `feature` &mdash; the feature whose key is being cleared


### def screen_paste(feature)

Called when the paste button is used on the api key screen.

**Parameters:**
- `feature` &mdash; the feature whose key is being pasted


### def screen_update_cert()

Called when the update cert button is used on the api key screen

### def load_keys()

Loads API keys from config file

### def save_keys()

Saves API keys to disk

