Visualize scalar (real or integer)-valued data at the points of a point cloud.

Example:
```python
import numpy as np
import polyscope as ps

# register a point cloud
N = 100
points = np.random.rand(N, 3)
ps_cloud = ps.register_point_cloud("my points", points)

# generate some random data per-point
vals = np.random.rand(N)

# basic visualization
ps_cloud.add_scalar_quantity("rand vals", vals)

# manually specify a range for colormapping
ps_cloud.add_scalar_quantity("rand vals with range", vals, vminmax=(-5., 5.))

# use a different colormap
ps_cloud.add_scalar_quantity("rand vals with range", vals, cmap='blues')

# use the 'datatype' to specify default visualization semantics
vals_gaussian = np.random.normal(size=N)
ps_cloud.add_scalar_quantity("gaussian vals symmetric", vals_gaussian, datatype='symmetric')

# view the point cloud with all of these quantities
ps.show() 
```

???+ func "`#!python PointCloud.add_scalar_quantity(name, values, enabled=None, datatype="standard", vminmax=None, cmap=None)`"

    Add a scalar quantity to the point cloud.

    - `name` string, a name for the quantity
    - `values` a length `N` numpy array, scalars at points
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantitiy can be shown at a time; the most recent will be used)
    - `datatype`, one of `standard`, `symmetric`, or `magnitude`, affects default colormap and map range
    - `vminmax`, a 2-tuple of floats, specifying the min and max range to colormap in to
    - `cmap`, which [colormap](/features/color_maps) to use
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](/basics/parameters/#persistent-values) if previously set.
    
