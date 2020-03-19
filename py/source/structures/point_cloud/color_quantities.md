Visualize color rgb-valued data at the points of a point cloud.

Example:
```python
import numpy as np
import polyscope as ps

# register a point cloud
N = 100
points = np.random.rand(N, 3)
ps_cloud = ps.register_point_cloud("my points", points)

# generate some random color per-point
vals = np.random.rand(N,3)

# basic color visualization
ps_cloud.add_color_quantity("rand colors", vals)

ps.show() 
```

???+ func "`#!python PointCloud.add_color_quantity(name, values, enabled=None)`"

    Add a color quantity to the point cloud.

    - `name` string, a name for the quantity
    - `values` a length `N` numpy array, colors at points
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantitiy can be shown at a time; the most recent will be used)
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](/basics/parameters/#persistent-values) if previously set.
    
