Visualize color rgb-valued data at the elements of a surface mesh.

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
colors_vert = np.random.rand(N_vert, 3)
ps_mesh.add_color_quantity("rand colors", colors_vert, enabled=True)

# visualize some random data per-face
colors_face = np.random.rand(N_face, 3)
ps_mesh.add_color_quantity("rand colors2", colors_face, defined_on='faces')

# view the mesh with all of these quantities
ps.show() 
```

???+ func "`#!python SurfaceMesh.add_color_quantity(name, values, defined_on='vertices', enabled=None)`"

    Add a scalar quantity to the network.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, with rgb [0,1] colors at vertices/faces
    - `defined_on` string, one of `"vertices"` or `"faces"`, is this data a color per vertex or a color per face?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    
    
{!common/color_quantity.md!}
