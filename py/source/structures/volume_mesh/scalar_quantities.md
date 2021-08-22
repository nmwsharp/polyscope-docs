Visualize scalar (real or integer)-valued data at the elements of a volume mesh.

![volume mesh scalar values]([[url.prefix]]/media/volume_scalar.jpg)

**Example**: showing a scalar on vertices (here, random values)
```python
# ... initialization, create mesh ...

ps_vol = ps.register_volume_mesh("test volume mesh", verts, tets=tets)

n_vert = verts.shape[0]
n_cell = tets.shape[0]

# Add a scalar function on vertices
data_vert = np.random.rand(n_vert)
ps_vol.add_scalar_quantity("my vertex val", data_vert)

# Add a scalar function on cells (with some options set)
data_cell = np.random.rand(n_cell)
ps_vol.add_scalar_quantity("my cell val", data_cell, defined_on='cells',
                           vminmax=(-3., 3.), cmap='blues', enabled=True)

// Show the GUI
ps.show()
```


### Add scalars to elements

???+ func "`#!python VolumeMesh.add_scalar_quantity(self, name, values, defined_on='vertices', enabled=None, datatype="standard", vminmax=None, cmap=None)`"

    Add a scalar quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` a length `N` numpy array, scalars at vertices/cells
    - `defined_on` one of `'vertices','cells'`, is this data a value per vertex or a value per cell?
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantity can be shown at a time; the most recent will be used)
    - `datatype` one of `standard`, `symmetric`, or `magnitude`, affects default colormap and map range
    - `vminmax` a 2-tuple of floats, specifying the min and max range to colormap in to
    - `cmap` string, which [colormap](../../../features/color_maps) to use
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
