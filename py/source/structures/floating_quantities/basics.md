Most quantities in Polyscope are associated with a particular structure, such as a `PointCloudScalarQuantity` on a `PointCloud`. In contrast, _Floating Quantities_ are generic quantities which can be added to **any and all** kinds of structures. You can also add them to the root level of the scene, not associated with any structure. 

One example of a floating quantity is an Images Quantity. You might want to visualize a single image, not specific to any structure, by adding it to the scene at the root level. Or, you might have an image associated with a particular mesh, in which case you could add the image quantity to that `SurfaceMesh` structure.

!!! note "TL;DR What are floating quantities?"

    Floating quantities are quantities that are general and not specific to any kind of structure.

    You have two options for how to add them:

    - Add them as standalone quantities in the scene at the root level, like `polyscope.add_image_quantity(...)`.
    - Add them to _any_ structure of _any_ type, like `pointCloud.add_image_quantity(...)`. This can be useful to associate the quantity with a structure.


The sub-menus to the left give the various floating quantities available.

## Removing floating quantities

Floating quantities which were added at the root level of the scene can be removed by name.

```python
import polyscope as ps
import numpy as np

ps.init()

ps.add_scalar_image_quantity("my image", np.zeros((100, 200)))
ps.remove_floating_quantity("my image")
```

For a floating quantity which was added to a particular structure, use that structure's [`remove_quantity()`]([[url.prefix]]/structures/structure_management/#quantities), like `ps_mesh.remove_quantity("my image")`.

??? func "`#!python remove_floating_quantity(name, error_if_absent=False)`"

    Remove a floating quantity which was added at the root level of the scene.

    - `name` string, the name of the quantity
    - `error_if_absent` boolean, raise an error if there is no such quantity

