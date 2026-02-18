Visualize scalar-valued data at the nodes or cells of a sparse volume grid.

![sparse volume grid scalar quantity]([[url.prefix]]/media/sparse_volume_scalar_quantity.jpg)


**Example:** adding scalar quantities to a sparse volume grid
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

# === Cell scalar: one value per occupied cell ===
cell_scalars = np.array([0.1, 0.5, 0.9, 0.3])
ps_grid.add_scalar_quantity("cell scalar", cell_scalars, defined_on='cells', enabled=True)

# === Node scalar: values at node indices ===
# For each cell (i,j,k), its corner nodes are (i+dx, j+dy, k+dz) for dx,dy,dz in {0,1}.
# Collect all unique nodes and provide a value for each.
node_set = set()
for cell in occupied_cells:
    for dx in range(2):
        for dy in range(2):
            for dz in range(2):
                node_set.add((cell[0]+dx, cell[1]+dy, cell[2]+dz))
node_indices = np.array(list(node_set), dtype=np.int32)
node_values = np.random.rand(len(node_indices)).astype(np.float32)

ps_grid.add_scalar_quantity("node scalar", node_values, defined_on='nodes',
                            node_indices=node_indices, enabled=True)

ps.show()
```

### Add cell scalars

???+ func "`#!python SparseVolumeGrid.add_scalar_quantity(name, values, defined_on='cells', datatype='standard', **scalar_args)`"

    Add a scalar quantity defined at the cells of the grid.

    - `name` string, a name for the quantity
    - `values` a numpy array of length `n_cells`, one value per occupied cell in the same order as the `occupied_cells` array used at registration
    - `defined_on` string, must be `'cells'`
    - `datatype` one of `'standard'`, `'symmetric'`, `'magnitude'`, `'categorical'`

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.


### Add node scalars

???+ func "`#!python SparseVolumeGrid.add_scalar_quantity(name, values, defined_on='nodes', node_indices=..., datatype='standard', **scalar_args)`"

    Add a scalar quantity defined at the nodes of the grid.

    Node values are passed as paired arrays of node indices and values. For a cell with grid indices `(i, j, k)`, its corner nodes have indices `(i+dx, j+dy, k+dz)` for `dx, dy, dz` in `{0, 1}`. The node indices may be passed in any order, and extra entries (for nodes not required by any occupied cell) are ignored. However, all required node values must be present.

    - `name` string, a name for the quantity
    - `values` a numpy array of length `N`, one scalar per node
    - `defined_on` string, must be `'nodes'`
    - `node_indices` an `(N, 3)` integer numpy array of node grid indices, required when `defined_on='nodes'`
    - `datatype` one of `'standard'`, `'symmetric'`, `'magnitude'`, `'categorical'`

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.

[[% include 'common/scalar_quantity.md' %]]
