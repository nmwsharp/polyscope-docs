Visualize vector-valued data at the points of a point cloud.

Example:
```python
import numpy as np
import polyscope as ps
ps.init()

# register a point cloud
N = 100
points = np.random.rand(N, 3)
ps_cloud = ps.register_point_cloud("my points", points)

# generate some random vectors per-point
vecs = np.random.rand(N, 3)

# basic visualization
ps_cloud.add_vector_quantity("rand vecs", vecs, enabled=True)

# set radius/length/color of the vectors
ps_cloud.add_vector_quantity("rand vecs", vecs, radius=0.001, length=0.005, color=(0.2, 0.5, 0.5))

# ambient vectors don't get auto-scaled, useful e.g. when representing offsets in 3D space
ps_cloud.add_vector_quantity("vecs ambient", vecs, vectortype='ambient')

# view the point cloud with all of these quantities
ps.show() 
```

???+ func "`#!python PointCloud.add_vector_quantity(name, values, enabled=None, vectortype="standard", length=None, radius=None, color=None)`"


    Add a vector quantity to the point cloud.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, vectors at points (or `Nx2` for 2D data)
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
   

[[% include 'common/vector_quantity.md' %]]
