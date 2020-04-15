# Point Clouds

Point clouds are one of the core structures in Polyscope. In addition to simply displaying the points, Polyscope can show any number of scalar, vector, or color quantities associated with the points.

As always, try clicking on a point to see the data associated with that point.

![point_cloud_demo](../../media/point_cloud_demo.gif)

### Registering a point cloud

Example: a point cloud of random points
```python
import numpy as np
import polyscope as ps
ps.init()

# generate some points
points = np.random.rand(100, 3)

# visualize!
ps_cloud = ps.register_point_cloud("my points", points)
ps.show()
```

???+ func "`#!python register_point_cloud(name, points, enabled=None, radius=None, color=None, material=None)`"

    Add a new point cloud structure to Polyscope.

    - `name` is the name for the structure, as a string
    - `points` is an `N x 3` numpy array of point locations

    Additional optional keyword arguments:

    - `enabled` boolean, is the structure enabled initially
    - `radius` float, a size for the points relative to the scene length scale (use `set_radius(val, relative=False)` for absolute units)
    - `color` float 3-tuple, default color values for the points as rgb in [0,1]
    - `material` string, name of material to use for cloud

    if not specified, these optional parameters will assume a reasonable default value, or a [persistant value](/basics/parameters/#persistent-values) if previously set.
    
    2D point clouds are also supported, see [2D data](../../../features/2D_data).


### Updating a point cloud

The locations of the points in a point cloud can be updated with the member function `update_point_positions(newPositions)`. All quantities will be preserved. Changing the _number_ of points in the cloud is not supported, you will need to register a new cloud (perhaps with the same name to overwrite this one).


Example: update positions (continued from above)
```python
new_pos = np.random.rand(100, 3)
ps_cloud.update_point_positions(new_pos)
ps.show()
```

??? func "`#!python PointCloud.update_point_positions(newPos)`"

    Update the point positions in a point cloud structure. `newPos` must be valid input as to initially construct a point cloud, with the same number of points.


### Options

Options control the appearance of the cloud. Note that these options can also be passed as keyword arguments to the initial `register_point_cloud()`, as noted above.


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the structure enabled? |  `#!python is_enabled()` | `#!python set_enabled(newVal=True)` | [yes](../../../basics/parameters/#persistent-values)
point radius | size of rendered points | `#!python get_radius()` | `#!python set_radius(newVal, relative=True)` | [yes](../../../basics/parameters/#persistent-values) |
point color | default color for points | `#!python get_color()` | `#!python set_color(newVal)` | [yes](../../../basics/parameters/#persistent-values) |
material | material for point | `#!python get_material()` | `#!python set_material(newVal)` | [yes](../../../basics/parameters/#persistent-values) |


Example: set options which affect the appearance of the point cloud
```python
cloud = polyscope.register_point_cloud("my points", points)

cloud.set_enabled(False) # disable
cloud.set_enabled() # default is true

cloud.set_radius(0.02) # radius is relative to a scene length scale by default
cloud.set_radius(1.7, relative=False) # radius in absolute world units

cloud.set_color((0.3, 0.6, 0.8)) # rgb triple on [0,1]
cloud.set_material("candy")

# alternately:
ps.register_point_cloud("my points 2", points, enabled=False, material='candy',
                        radius=0.02, color=(1., 0., 0.))
```
