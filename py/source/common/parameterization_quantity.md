### Styles

Several styles are available for how a parameterization is displayed. 

The `viz_style` option determines how parameterizations are visualized:

- `checker`: a two-color checker pattern
- `grid`: a two-color grid with thin lines
- `local_check`: a checkerboard over a radial colormap, centered around `(0,0)`
- `local_rad`: distance stripes over a radial colormap, centered around `(0,0)`

### Types

The `coords_type` options determines how parameter coordinates are interpreted for scaling:

 - `unit`: UV coords are assumed to lie on the `[0,1]` interval
 - `world`: UV coords are assumed to be scaled like the world-space positions of the mesh

### Parameterization Quantity Options

When adding a parameterization quantity, the following keyword options can be set. These are available for all kinds of parameterization quantities on all structures.

Keyword arguments:

  - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantity can be shown at a time; the most recent will be used)
  - `coords_type` string, one of `'unit'`, `'world'`  (see above)
  - `viz_style` string, one of `'checker'`, `'grid'`, `'local_check'`, `'local_rad'` (see above)
  - `grid_colors` 2-tuple of rgb colors, used to color the grid visualization
  - `checker_colors` 2-tuple of rgb colors, used to color the checkerboard visualization
  - `checker_size` float, the size of checkers/grid/stripes
  - `cmap` string, which [colormap](../../../features/color_maps) to use
    
If not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
