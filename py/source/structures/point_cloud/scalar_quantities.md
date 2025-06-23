Visualize scalar (real or integer)-valued data at the points of a point cloud.

Example:
```python
import numpy as np
import polyscope as ps
ps.init()

# register a point cloud
N = 100
points = np.random.rand(N, 3)
ps_cloud = ps.register_point_cloud("my points", points)

# generate some random data per-point
vals = np.random.rand(N)

# basic visualization
ps_cloud.add_scalar_quantity("rand vals", vals)

# manually specify a range for colormapping
ps_cloud.add_scalar_quantity("rand vals with range", vals, vminmax=(-5., 5.), enabled=True)

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

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    
[[% include 'common/scalar_quantity.md' %]]
