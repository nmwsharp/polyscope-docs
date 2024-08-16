You can set the transparency individually for each point in a point cloud by specifing an existing scalar quantity to serve as the transparency.
This can also be set manually in the GUI via the point cloud `[Options] --> [Variable Transparency]` setting.

See the [transparency]([[url.prefix]]/features/transparency) section for more transparency-related options.

![point cloud transparency demo]([[url.prefix]]/media/point_cloud_scalar_transparency.jpg)

Example:
```cpp
#include "polyscope/point_cloud.h"

// Populate a random scalar quantity
std::vector<double> xC(points.size());
for (size_t i = 0; i < points.size(); i++) {
  xC[i] = points[i].x;
}

// Get a reference to some point cloud
auto psCloud = polyscope::getPointCloud(/* your point cloud name */);

auto q = psCloud->addScalarQuantity("xC", xC); // add the quantity
psCloud->setTransparencyQuantity(q); // set the quantity as the radius
// psCloud->setTransparencyQuantity("xC"); // equivalently, the name can be used
```

All values will be clamped into the `[0,1]` range. The transparency is multiplicative with any other transparency effects, such as setting the structure's global transparency value.

??? func "`#!cpp void PointCloud::setTransparencyQuantity(PointCloudScalarQuantity* quantity)`"
    
    ##### set transparency quantity

    Set the transparency quantity. All values will be clamped into the `[0,1]` range.

    If transparency is not already enabled, updates the transparency mode to be `Pretty`.

??? func "`#!cpp void PointCloud::setTransparencyQuantity(std::string name)`"

    Set the transparency quantity by name. All values will be clamped into the `[0,1]` range.

    If transparency is not already enabled, updates the transparency mode to be `Pretty`.

??? func "`#!cpp void PointCloud::clearTransparencyQuantity()`"
    
    ##### clear transparency quantity

    Clear the transparency quantity.
