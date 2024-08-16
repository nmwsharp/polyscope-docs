You can set the transparency individually for each point in a point cloud by specifing an existing scalar quantity to serve as the transparency.
This can also be set manually in the GUI via the point cloud `[Options] --> [Variable Transparency]` setting.

See the [transparency]([[url.prefix]]/features/transparency) section for more transparency-related options.

![point cloud transparency demo]([[url.prefix]]/media/point_cloud_scalar_transparency.jpg)

Example:
```python
import polyscope as ps
import numpy as np

# ... setup, register a point cloud, etc ...

# Get a reference to your point cloud
ps_cloud = ps.get_point_cloud("your point cloud name")

# Add a random scalar quantity
N = ps_cloud.n_points()
vals = np.random.rand(N)
ps_cloud.add_scalar_quantity("test_vals", vals)

# Set the quantity as the point transparency
ps_cloud.set_transparency_quantity("test_vals")
ps.show()

# Clear it out, go back to default constant size
ps_cloud.clear_transparency_quantity()
ps.show()
```

All values will be clamped into the `[0,1]` range. The transparency is multiplicative with any other transparency effects, such as setting the structure's global transparency value.


??? func "`#!python PointCloud.set_transparency_quantity(quantity_name)`"
    
    ##### set transparency quantity
    
    Set the transparency quantity by name. The quantity must be a point cloud scalar quantity added to this cloud.

    All values will be clamped into the `[0,1]` range.

    If transparency is not already enabled, updates the transparency mode to be `Pretty`.


??? func "`#!python PointCloud.clear_transparency_quantity()`"

    ##### clear transparency quantity

    Clear the transparency quantity.
