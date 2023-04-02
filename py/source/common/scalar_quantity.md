### Scalar Quantity Options

When adding a scalar quantity, the following keyword options can be set. These are available for all kinds of scalar quantities on all structures.
    
Keyword arguments:

  - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantitiy can be shown at a time; the most recent will be used)
  - `datatype`, one of `"standard"`, `"symmetric"`, or `"magnitude"`, affects default colormap and map range
  - `vminmax`, a 2-tuple of floats, specifying the min and max range for colormap limits; the default is `None`, which computes the min and max of the data
  - `cmap`, which [colormap](../../../features/color_maps) to use

If not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
