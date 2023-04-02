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
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.


### Inspecting with slice planes

Slice planes have [special functionality]([[url.prefix]]/features/slice_planes/#inspecting-volume-meshes) for volume mesh vertex values---they can _inspect_ quantities on volume meshes and render them on the interior of the volume. See the slice plane documentation for details.

{!common/scalar_quantity.md!}
