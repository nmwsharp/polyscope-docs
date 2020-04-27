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


## Adding

???+ func "`#!python SurfaceMesh.add_parameterization_quantity(name, values, defined_on='vertices', coords_type='unit', enabled=None, viz_style=None, grid_colors=None, checker_colors=None, checker_size=None, cmap=None)`"

    Add a parameterization quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `Nx2` numpy array, coordinates at vertices/corners
    - `defined_on` one of `'vertices','corners'`, is this a coordinate per vertex or per corner?
    - `coords_type` string, one of `'unit'`, `'world'`  (see below)
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantity can be shown at a time; the most recent will be used)
    - `viz_style` string, one of `'checker'`, `'grid'`, `'local_check'`, `'local_rad'` (see below)
    - `grid_colors` 2-tuple of rgb colors, used to color the grid visualization
    - `checker_colors` 2-tuple of rgb colors, used to color the checkerboard visualization
    - `checker_size` float, the size of checkers/grid/stripes
    - `cmap` string, which [colormap](../../../features/color_maps) to use
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
    

## Options

### Styles

Several styles are available for how a parameterization is displayed. 

The `viz_style` option determines how parameterizations are visualized:

- `checker`: a two-color checker pattern
- `grid`: a two-color grid with thin lines
- `local_check`: a checkerboard over a radial colormap, centered around `(0,0)`
- `local_rad`: distance stripes over a radial colormap, centered around `(0,0)`

### Types

The `coords_type` options determines how parameter coordinates are interpreted for scaling:

 - `unit`: UV coords are assumed to lie on the `[0,1]` interval
 - `world`: UV coords are assumed to be scaled like the world-space positions of the mesh
