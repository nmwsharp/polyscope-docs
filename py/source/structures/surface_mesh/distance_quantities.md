Visualize distance-valued data at the elements of a surface mesh.

Distance quantities are basically scalars, but are visualized with alternating stripes to show distance contours.

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

dists = # your distances, a length N_vert array

# visualize the distance
ps_mesh.add_distance_quantity("distances", dists, enabled=True, stripe_size=0.01)

# use defaults for signed distances
ps_mesh.add_distance_quantity("signed distances", dists, signed=True)

# view the mesh with these quantities
ps.show() 
```

???+ func "`#!python SurfaceMesh.add_distance_quantity(name, values, defined_on='vertices', enabled=None, signed=False, vminmax=None, stripe_size=None, stripe_size_relative=True, cmap=None)`"

    Add a distance quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` a length `N` numpy array, distance scalars 
    - `defined_on` for now, only `'vertices'` is supported
    - `signed` boolean, if true the data is assumed to represent signed distances, and symmetric ranges/colormaps are used by default
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantity can be shown at a time; the most recent will be used)
    - `vminmax` a 2-tuple of floats, specifying the min and max range to colormap in to
    - `stripe_size` float, the width of stripes in the visualization
    - `stripe_size_relative` boolean, if true `stripe_size` is interpreted relative to the scene length scale, otherwise absolute
    - `cmap` string, which [colormap](../../../features/color_maps) to use
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
    
