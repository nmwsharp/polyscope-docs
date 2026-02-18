# Sparse Volume Grids

Sparse volume grid structures visualize data defined on a sparse subset of cells in an axis-aligned 3D grid. Unlike the dense [Volume Grid]([[url.prefix]]/structures/volume_grid/basics), a sparse volume grid only stores and renders the cells you specify, making it well-suited for adaptive grids, occupancy maps, and other data that occupies only a portion of a regular grid.

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/sparse_volume_grid.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

As usual, first you register a sparse volume grid by specifying a grid origin, cell size, and list of occupied cells. Then you can add quantities such as scalar or color data defined per-cell or per-node.

**Example:** registering a sparse volume grid and adding a scalar quantity
```python
import polyscope as ps
import numpy as np

ps.init()

# define the grid parameters
origin = (0., 0., 0.)
cell_width = (0.1, 0.1, 0.1)

# list of occupied cells by their integer grid indices
occupied_cells = np.array([
    [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1],
    [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1],
])

# register the grid
ps_grid = ps.register_sparse_volume_grid("sample sparse grid", origin, cell_width, occupied_cells)

# add a scalar function on the grid (one value per cell)
cell_scalars = np.random.rand(len(occupied_cells))
ps_grid.add_scalar_quantity("cell scalar", cell_scalars, defined_on='cells', enabled=True)

ps.show()
```

### Registering a sparse volume grid

!!! note "Origin and cell width"

    The `origin` parameter specifies the position of the node/corner origin of the grid. Cell `(0,0,0)` has its lower-left corner at the origin. If you are thinking in terms of cell centers, shift the origin you pass in by half a cell width: `origin = cell_center - 0.5 * cell_width`.

    The `cell_width` parameter gives the size of each grid cell along each axis. All cells have the same size.


???+ func "`#!python register_sparse_volume_grid(name, origin, grid_cell_width, occupied_cells, enabled=None, color=None, edge_color=None, edge_width=None, cube_size_factor=None, material=None, transparency=None, render_mode=None, wireframe_radius=None, wireframe_color=None)`"

    Add a new sparse volume grid structure to Polyscope.

    - `name` the name of the structure
    - `origin` a float 3-tuple giving the xyz position of the node/corner origin
    - `grid_cell_width` a float 3-tuple giving the width of each cell along each axis
    - `occupied_cells` an `(N, 3)` integer numpy array giving the grid indices of all occupied cells

    Additional optional keyword arguments:

    - `enabled` boolean, is the structure enabled initially
    - `color` float 3-tuple, color for the volume as rgb in [0,1]
    - `edge_color` float 3-tuple, color for grid edges as rgb in [0,1] (be sure to set `edge_width` too)
    - `edge_width` float, width of edges on the grid; default is `0` to disable edges, `1` is a reasonable value to enable
    - `cube_size_factor` float, shrink factor from 0-1 to draw gaps between cells, 0 is no shrink (default)
    - `material` string, name of material to use for the grid
    - `transparency` float, transparency value in [0,1]
    - `render_mode` string, `'gridcube'` (default) or `'wireframe'`
    - `wireframe_radius` float, relative radius for wireframe spheres/cylinders; `1` means radius is half the smallest cell width
    - `wireframe_color` float 3-tuple, color for wireframe rendering as rgb in [0,1]

    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.

---

### Render modes

The sparse volume grid supports two render modes, controlled by `set_render_mode()`:

- **`'gridcube'`** (default) renders each occupied cell as a filled cube. Scalar and color quantities are visualized on the cube faces.
- **`'wireframe'`** renders only the grid outline as wireframe edges. This mode is useful for seeing through the grid to inspect its structure. Quantities are not drawn in wireframe mode.

![sparse volume grid render modes]([[url.prefix]]/media/sparse_volume_render_modes.jpg)

The wireframe appearance can be adjusted with `set_wireframe_radius()` and `set_wireframe_color()`.

```python
ps_grid = polyscope.register_sparse_volume_grid("sample sparse grid", origin, cellWidth, occupiedCells);

ps_grid.set_render_mode("wireframe")
ps_grid.set_wireframe_radius(0.5)
ps_grid.set_wireframe_color([1., 0., 0.])
```

### Slice planes

As shown in the video above, [slice planes]([[url.prefix]]/features/slice_planes) are useful for inspecting the structure of a sparse volume grid. Slice planes can be manipulated programmatically or manually in the GUI; see the slice plane documentation for more details.

### Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene. Picking sparse volume grid elements works similarly to other structures, see [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#picking-selection-and-querying-the-scene) for general information.

Picking a sparse volume grid returns a dictionary with the following additional keys:
```python
io = polyscope.imgui.GetIO()
screen_coords = io.MousePos
pick_result = polyscope.pick(screen_coords=screen_coords)

if pick_result.structure_type_name == "Sparse Volume Grid":
    # always:
    pick_result.structure_data["element_type"]    # either "cell" or "node", depending on what was picked

    # if a cell was picked:
    pick_result.structure_data["cell_index"]      # the integer grid index of the picked cell, as a tuple (i,j,k)
    pick_result.structure_data["cell_flat_index"] # the ID of the picked cell, i.e. its index in the occupied_cells list

    # if a node was picked:
    pick_result.structure_data["node_index"]      # the integer grid index of the picked node, as a tuple (i,j,k)
```

By default, only cells can be selected, until you have added some data on nodes. You can override this behavior by calling `sparse_volume_grid.mark_nodes_as_used()`, to act as if a node quantity had been added.


### Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
color | the color of the volume | `#!python get_color()` | `#!python set_color(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!python get_edge_width()` | `#!python set_edge_width(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge color | the color of the grid edges | `#!python get_edge_color()` | `#!python set_edge_color(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
cube size factor | shrink factor from 0-1 to draw gaps between cells, 0 is no shrink (default) | `#!python get_cube_size_factor()` | `#!python set_cube_size_factor(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!python get_material()` | `#!python set_material(name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
render mode | how to render the voxels: `'gridcube'` (default, filled cubes) or `'wireframe'` (grid outline only) | `#!python get_render_mode()` | `#!python set_render_mode(mode)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
wireframe radius | relative radius for wireframe spheres/cylinders; `1` means radius is half the smallest cell width | `#!python get_wireframe_radius()` | `#!python set_wireframe_radius(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
wireframe color | color used for wireframe rendering | `#!python get_wireframe_color()` | `#!python set_wireframe_color(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
