### Scalar Quantity Options

When adding a scalar quantity, the following keyword options can be set. These are available for all kinds of scalar quantities on all structures.
    
Keyword arguments:

  - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantitiy can be shown at a time; the most recent will be used)
  - `datatype`, one of `"standard"`, `"symmetric"`, or `"magnitude"`, affects default colormap and map range
  - `vminmax`, a 2-tuple of floats, specifying the min and max range for colormap limits; the default is `None`, which computes the min and max of the data
  - `cmap`, which [colormap](../../../features/color_maps) to use
  - isoline keywords (darker-shaded stripes showing isocontours of the scalar field):
      - `isolines_enabled` are isolines enabled (default: `False`)
      - `isoline_width` how wide should the darkend stripes be, in data units (default: dynamically estimated)
      - `isoline_width_relative` if true, interpret the width value as relative to the world coordinate length scale (default: `False`)
      - `isoline_darkness` how much darker should the alternating stripes be (default: `0.7`)

If not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
