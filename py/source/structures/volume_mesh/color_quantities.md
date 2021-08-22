Visualize color rgb-valued data at the elements of a volume mesh.

![volume mesh color values]({{url.prefix}}/media/volume_color.jpg)

**Example**: showing a color value at cells (here, random values)
```python
# ... initialization, create mesh ...

ps_vol = ps.register_volume_mesh("test volume mesh", verts, tets=tets)

n_vert = verts.shape[0]
n_cell = tets.shape[0]

# Add a color function on cells (with some options set)
colors = np.random.rand(n_cell, 3)
ps_vol.add_color_quantity("my color", colors, defined_on='cells', enabled=True)

# Show the GUI
ps.show()
```

### Add colors to elements

???+ func "`#!python VolumeMesh.add_color_quantity(name, values, defined_on='vertices', enabled=None)`"

    Add a scalar quantity to the network.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, with rgb [0,1] colors at vertices/cells
    - `defined_on` string, one of `vertices` or `cells`, is this data a color per vertex or a color per cell?
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantity can be shown at a time; the most recent will be used)
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.

