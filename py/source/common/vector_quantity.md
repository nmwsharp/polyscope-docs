### Vector Quantity Options

When adding a vector quantity, the following keyword options can be set. These are available for all kinds of vector quantities on all structures.

Keyword arguments:

  - `enabled` boolean, whether the quantity is initially enabled (Default: `false`)
  - `vectortype`, one of `"standard"` or `"ambient"`. Ambient vectors don't get auto-scaled, and thus are good for representing values in absolute 3D world coordinates. (Default: `"standard"`)
  - `length` float, a (relative) length for the vectors
  - `radius` float, a (relative) radius for the vectors
  - `color` 3-tuple, color for the vectors
  - `material` string, shading material for the vectors

If not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
