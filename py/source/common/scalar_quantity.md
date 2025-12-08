### Categorical Scalars

Scalar quantities can also be used to visualize integer-valued labels such as categories, classes, segmentations, flags, etc.

Add the labels as a scalar quantity where the values just happen to be integers (each integer represents a particular class or label), and set `datatype='categorical'`. This will change the visualization to a different set of defaults, adjust some shading rules, and use a distinct color from the colormap for each label.

### Color Bars

Each scalar quantity has an associated color map, which linearly maps scalar values to a spectrum of colors for visualization.
See [colormaps]([[url.prefix]]/features/color_maps) for a listing of the available maps, and use `add_scalar_quantity(..., cmap="cmap_name")` to choose the map.

The colormap is always displayed with an inline colorbar in the structures panel, which also gives a histogram of the scalar values in your quantity.
The limits (`vminmax`) of the colormap range are given by the two numeric fields below the colored display. You can click and drag horizontally on these fields to adjust the map range, or ctrl-click (cmd-click) to enter arbitrary custom values. 

![image inline and onscreen colorbar]([[url.prefix]]/media/colorbar_options.jpg)

!!! note "onscreen colorbar"

    Optionally an additional onscreen colorbar, which is more similar to the colorbars used in other plotting libraries, can be enabled with `add_scalar_quantity(..., onscreen_colorbar_enabled=True)`.

    By default it is positioned automatically inline with the other UI elements, or it can be manually positioned with `add_scalar_quantity(..., onscreen_colorbar_location=(400., 400.))`.

    You can even **export this color map to an `.svg` file** for creating figures via the options menu.

### Scalar Quantity Options

When adding a scalar quantity, the following keyword options can be set. These are available for all kinds of scalar quantities on all structures.
    
Keyword arguments:

  - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantitiy can be shown at a time; the most recent will be used)
  - `datatype`, one of `"standard"`, `"symmetric"`, `"magnitude"`, or `"categorical"`, affects default colormap and map range, and the categorical policies mentioned above
  - `vminmax`, a 2-tuple of floats, specifying the min and max range for colormap limits; the default is `None`, which computes the min and max of the data
  - colormap keywords:
      - `cmap`, which [colormap](../../../features/color_maps) to use
      - `onscreen_colorbar_enabled` set to `True` to enable an additional traditional colormap 
      - `onscreen_colorbar_location` set to screen coordinates like `(400., 400.)` to position the onscreen colorbar manually (default is automatic)
  - isoline keywords (darker-shaded stripes showing isocontours of the scalar field):
      - `isolines_enabled` are isolines enabled (default: `False`)
      - `isoline_style` one of `stripe`, `'contour` (default: `stripe`)
      - `isoline_period` how wide should the darkend stripes be, in data units (default: dynamically estimated)
      - `isoline_period_relative` if true, interpret the width value as relative to the world coordinate length scale (default: `False`)
      - `isoline_darkness` how much darker should the alternating stripes be (default: `0.7`)
      - `isoline_contour_thickness` how thick should the contour lines be (default: `0.3`)

If not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
