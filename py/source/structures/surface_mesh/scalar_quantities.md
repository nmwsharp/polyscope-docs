Visualize scalar (real or integer)-valued data at the elements of a surface mesh.


Example:
```python
import numpy as np
import polyscope as ps
ps.init()

N_vert = 100
N_face = 250
vertices = np.random.rand(N_vert, 3) # (V,3) vertex position array
faces = np.random.randint(0, N_vert, size=(N_face,3)) # (F,3) array of indices 
                                                      # for triangular faces

ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)

# visualize some random data per-vertex
vals_vert = np.random.rand(N_vert)
ps_mesh.add_scalar_quantity("rand vals", vals_vert, enabled=True)

# visualize some random data per-face
vals_face = np.random.rand(N_face)
ps_mesh.add_scalar_quantity("rand vals2", vals_face, defined_on='faces')

# visualize some random data per-edge (halfedges are also supported)
vals_edge = np.random.rand(ps_mesh.n_edges())
ps_mesh.add_scalar_quantity("rand vals3", vals_edge, defined_on='edges')

# as always, we can customize the initial appearance
ps_mesh.add_scalar_quantity("rand vals3 opt", vals_edge, defined_on='edges', 
                            enabled=True, vminmax=(-3., 3.), cmap='reds')

# view the mesh with all of these quantities
ps.show() 
```

???+ func "`#!python SurfaceMesh.add_scalar_quantity(name, values, defined_on='vertices', enabled=None, datatype="standard", vminmax=None, cmap=None)`"

    Add a scalar quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` a length `N` numpy array, scalars at vertices/faces/etc
    - `defined_on` one of `'vertices','faces','edges','halfedges'`, is this data a value per vertex or a value per face, etc?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    
{!common/scalar_quantity.md!}
