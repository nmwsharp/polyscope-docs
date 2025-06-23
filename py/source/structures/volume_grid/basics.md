# Volume Grids

Volume grid structures visualize data defined on an axis-aligned regularly-spaced 3D grid. 

As usual, first you register a volume grid, then add one or more quantities defined on that grid. Registering the grid itself just means specifying the locations of its extremal corners and the grid resolution. Then you can add data, such as scalar data as linearly-interpolated values per-node or as piecewise-constant values per-cell. Slice planes can also be used inspect the interior of the grid, isosurfaces can be extracted from scalar functions at nodes, and more. 

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/movies/volume_grid_demo_compress.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Example:** registering a volume grid and adding a scalar quantity
```python
import polyscope as ps
import numpy as np

ps.init()

# define the resolution and bounds of the grid
dims = (20, 20, 20)
bound_low = (-3., -3., -3.)
bound_high = (3., 3., 3.)

# register the grid
ps_grid = ps.register_volume_grid("sample grid", dims, bound_low, bound_high)

# your dimX*dimY*dimZ buffer of data
scalar_vals = np.zeros(dims[0], dims[1], dims[2]) 

# add a scalar function on the grid
ps_grid.add_scalar_quantity("node scalar1", scalar_vals, 
                            defined_on='nodes', vminmax=(-5., 5.), enabled=True)

ps.show()
```

### Registering a volume grid

!!! note "Specifying node vs. cells"

    Volume grid dimensions and locations are always defined in terms of _nodes_ (aka cell corners). The dimension is the number of _nodes_ along each axis, and the location is defined by the extremal _nodes_.

    For dimensions, if you are instead thinking in terms of the number of _cells_ (little cubical regions), add +1 to the number of cells along each dimension to get the equivalent number of nodes when registering the grid.

    For locations, the min/max bounds you specify when registering the grid are the locations up the minimum and maximum node (aka cell corner). If you are instead thinking in terms of cell center locations, shift them half-cell-width offset when registering the grid.


???+ func "`#!python register_volume_grid(name, node_dims, bound_low, bound_high, enabled=None, color=None, edge_color=None, edge_width=None, cube_size_factor=None, material=None, transparency=None)`"

    Add a new volume grid structure to Polyscope.

    - `name` the name of the structure
    - `node_dims` an integer 3-tuple giving the number of nodes in the grid along each dimension
    - `bound_low` a float 3-tuple giving the xyz coordinates for the minimal node corner of the grid
    - `bound_high` a float 3-tuple giving the xyz coordinates for the maximal node corner of the grid
    
    Additional optional keyword arguments:

    - `enabled` boolean, is the structure enabled initially
    - `color` float 3-tuple, color for the volume as rgb in [0,1]
    - `edge_color` float 3-tuple, color for grid edges as rgb in [0,1] (be sure to set `edge_width` too)
    - `edge_width` float, width of edges on the grid; default sets `0` to disable edges, `1` is a reasonable value to enable
    - `cube_size_factor` float, shrink factor from 0-1 to draw gaps between cells, 0 is no shrink (default)
    - `material` string, name of material to use for the grid

    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.


---

### Slice planes

[Slice planes]([[url.prefix]]/features/slice_planes) are particularly useful for inspecting the internal structure of a volume grid, as shown in the demo video at the top. Slice planes can be manipulated programmatically or manually in the GUI; see the slice plane documentation for more details.

### Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene. Picking volume grid elements works a little differently from other structures. For most structures, each click selects an element of the structure. However for volume grids, clicking on the structure once initiates picking, then the UI continuously displays data for the location under your mouse cursor. You can always deselect the volume grid elements by clicking somewhere off the grid.

By default, if you have only registered data defined on nodes, then only nodes can be picked (and vice-versa for cells). You can override this behavior by calling `volume_grid.mark_nodes_as_used()`, to act as if a node quantity had been added, and likewise for `volume_grid.mark_cells_as_used()`.

### Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
color | the color of the volume | `#!python get_color()` | `#!python set_color(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge color | the color of the grid edges | `#!python get_edge_color()` | `#!python set_edge_color(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!python double get_edge_width()` | `#!python set_edge_width(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
cube size factor | shrink factor from 0-1 to draw gaps between cells, 0 is no shrink (default) | `#!python get_cube_size_factor()` | `#!python set_cube_size_factor(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!python get_material()` | `#!python set_material(name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |

_(All setters return `this` to support chaining. Structure options return a generic structure pointer, so chain them last.)_
