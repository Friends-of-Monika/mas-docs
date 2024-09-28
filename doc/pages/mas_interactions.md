## Functions

### def get_vx(zone_enum)

Get vx list of a zone enum

**Parameters:**
- `zone_enum` &mdash; zone enum to get vertex list for


**Returns:**<br>
vertex list, or empty if not found

---

### def z_vx_list_zoom(zoom_level, zone_enum)

Generates a vertex list from the given zoom and zone enum

**Parameters:**
- `zoom_level` &mdash; zoom level to generate vertex list for
- `zone_enum` &mdash; zone enum to generate vertex list for


**Returns:**<br>
list of vertexes. May be empty if not valid zone enum

---

### def vx_list_zoom(zoom_level, vx_list)

Generates a vertex list from the given zoom

**Parameters:**
- `zoom_level` &mdash; zoom level to generate vertex list
- `vx_list` &mdash; list of vertexes to geneate new list for


**Returns:**<br>
list of vertexes

---

### def get_vx(zone_enum)

Get vx list of a zone enum

**Parameters:**
- `zone_enum` &mdash; zone enum to get vertex list for


**Returns:**<br>
vertex list, or empty if not found

---

### def z_vx_list_zoom(zoom_level, zone_enum)

Generates a vertex list from the given zoom and zone enum

**Parameters:**
- `zoom_level` &mdash; zoom level to generate vertex list for
- `zone_enum` &mdash; zone enum to generate vertex list for


**Returns:**<br>
list of vertexes. May be empty if not valid zone enum

---

### def vx_list_zoom(zoom_level, vx_list)

Generates a vertex list from the given zoom

**Parameters:**
- `zoom_level` &mdash; zoom level to generate vertex list
- `vx_list` &mdash; list of vertexes to geneate new list for


**Returns:**<br>
list of vertexes

---

### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

#### def _vx_list_zoom(zoom_level, vx_list, zoom_out)

Generates vertex list for zooming.

**Parameters:**
- `vx_list` &mdash; list of vetex points to adjust for zoom. NOTE: we generate a new list, so dont worry about this changing
- `zoom_out` &mdash; True if we are zooming out, False if zooming in


**Returns:**<br>
adjustd list of vertexes

---

#### def _vx_list_zoom(zoom_level, vx_list, zoom_out)

Generates vertex list for zooming.

**Parameters:**
- `vx_list` &mdash; list of vetex points to adjust for zoom. NOTE: we generate a new list, so dont worry about this changing
- `zoom_out` &mdash; True if we are zooming out, False if zooming in


**Returns:**<br>
adjustd list of vertexes

---

