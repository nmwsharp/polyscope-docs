Visualize vector-valued data at the elements of a volume mesh.

![volume mesh vector values]([[url.prefix]]/media/volume_vector.jpg)

**Example**: showing vectors on vertices (here random vectors)
```python
# ... initialization, create mesh ...

ps_vol = ps.register_volume_mesh("test volume mesh", verts, tets=tets)

n_vert = verts.shape[0]
n_cell = tets.shape[0]

# Add vectors on vertices (with some options set)
vecs = np.random.rand(n_vert, 3)
ps_vol.add_vector("my color", vecs, enabled=True, vectortype='ambient')

# Show the GUI
ps.show()
```

### Add vectors to elements

???+ func "`#!python VolumeMesh.add_vector_quantity(name, values, defined_on='vertices', enabled=None, vectortype="standard", length=None, radius=None, color=None)`"

    Add a vector quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, vectors at vertices/cells
    - `defined_on` string, one of `vertices` or `cells`, is this data a vector per-vertex or a vector per-cell?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
   

{!common/vector_quantity.md!}
