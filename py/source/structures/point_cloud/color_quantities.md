Visualize color rgb-valued data at the points of a point cloud.

Example:
```python
import numpy as np
import polyscope as ps
ps.init()

# register a point cloud
N = 100
points = np.random.rand(N, 3)
ps_cloud = ps.register_point_cloud("my points", points, enabled=True)

# generate some random color per-point
vals = np.random.rand(N,3)

# basic color visualization
ps_cloud.add_color_quantity("rand colors", vals)

ps.show() 
```

???+ func "`#!python PointCloud.add_color_quantity(name, values, enabled=None)`"

    Add a color quantity to the point cloud.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, with rgb [0,1] colors at points
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.

    
{!common/color_quantity.md!}
