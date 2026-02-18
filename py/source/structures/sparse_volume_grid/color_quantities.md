Visualize color data at the nodes or cells of a sparse volume grid.

![sparse volume grid color quantity]([[url.prefix]]/media/sparse_volume_color_quantity.jpg)


**Example:** adding color quantities to a sparse volume grid
```python
import polyscope as ps
import numpy as np

ps.init()

origin = (0., 0., 0.)
cell_width = (0.1, 0.1, 0.1)

occupied_cells = np.array([
    [0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0],
])

ps_grid = ps.register_sparse_volume_grid("sample sparse grid", origin, cell_width, occupied_cells)

# === Cell color: one RGB color per occupied cell ===
cell_colors = np.array([
    [1., 0., 0.], [0., 1., 0.], [0., 0., 1.], [1., 1., 0.],
])
ps_grid.add_color_quantity("cell color", cell_colors, defined_on='cells', enabled=True)

# === Node color: colors at node indices ===
node_set = set()
for cell in occupied_cells:
    for dx in range(2):
        for dy in range(2):
            for dz in range(2):
                node_set.add((cell[0]+dx, cell[1]+dy, cell[2]+dz))
node_indices = np.array(list(node_set), dtype=np.int32)
node_colors = np.random.rand(len(node_indices), 3).astype(np.float32)

ps_grid.add_color_quantity("node color", node_colors, defined_on='nodes',
                           node_indices=node_indices, enabled=True)

ps.show()
```

### Add cell colors

???+ func "`#!python SparseVolumeGrid.add_color_quantity(name, colors, defined_on='cells', **color_args)`"

    Add a color quantity defined at the cells of the grid.

    - `name` string, a name for the quantity
    - `colors` an `(N, 3)` numpy array of RGB colors in `[0, 1]`, one per occupied cell in the same order as the `occupied_cells` array used at registration
    - `defined_on` string, must be `'cells'`

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.


### Add node colors

???+ func "`#!python SparseVolumeGrid.add_color_quantity(name, colors, defined_on='nodes', node_indices=..., **color_args)`"

    Add a color quantity defined at the nodes of the grid.

    Node colors are passed as paired arrays of node indices and colors. For a cell with grid indices `(i, j, k)`, its corner nodes have indices `(i+dx, j+dy, k+dz)` for `dx, dy, dz` in `{0, 1}`. The node indices may be passed in any order, and extra entries (for nodes not required by any occupied cell) are ignored. However, all required node values must be present.

    - `name` string, a name for the quantity
    - `colors` an `(N, 3)` numpy array of RGB colors in `[0, 1]`, one per node
    - `defined_on` string, must be `'nodes'`
    - `node_indices` an `(N, 3)` integer numpy array of node grid indices, required when `defined_on='nodes'`

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
