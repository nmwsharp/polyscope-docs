A _parameterization_ is a set of 2D coordinates associated with a mesh, often referred to as "UV coordinates". This sections details several functions for visualizing such parameterizations.

![param_demo](../../media/param_demo.gif)

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

# parameterization per vertex
param_vert = np.random.rand(N_vert,2)
ps_mesh.add_parameterization_quantity("rand param", param_vert, enabled=True)

# parameterization per corner
param_corner = np.random.rand(ps_mesh.n_corners(),2)
ps_mesh.add_parameterization_quantity("rand param corner", param_corner, defined_on='corners')

# use options to customize visualization
ps_mesh.add_parameterization_quantity("rand param corner2", param_corner, defined_on='corners',
                                       coords_type='world', viz_style='local_rad')

                                 
# with custom checker/grid color
cA = (0.1, 0.2, 0.3)
cB = (0.4, 0.5, 0.6)
ps_mesh.add_parameterization_quantity("rand param corner3", param_corner, defined_on='corners',
                                       coords_type='unit', viz_style='grid', grid_colors=(cA, cB))

# view the mesh with all of these quantities
ps.show() 
```


???+ func "`#!python SurfaceMesh.add_parameterization_quantity(name, values, defined_on='vertices', coords_type='unit', enabled=None, viz_style=None, grid_colors=None, checker_colors=None, checker_size=None, cmap=None)`"

    Add a parameterization quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `Nx2` numpy array, coordinates at vertices/corners
    - `defined_on` one of `'vertices','corners'`, is this a coordinate per vertex or per corner?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    

{!common/parameterization_quantity.md!}
