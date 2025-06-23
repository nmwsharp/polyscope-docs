Visualize scalar (real or integer)-valued data at the points of a point cloud.

Example:
```cpp
#include "polyscope/point_cloud.h"

std::vector<double> xC(points.size());
for (size_t i = 0; i < points.size(); i++) {
  xC[i] = points[i].x;
}

// visualize
polyscope::getPointCloud(pointCloudName)->addScalarQuantity("xC", xC);
```

??? func "`#!cpp PointCloud::addScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity to the point cloud.

    - `values` is the array of scalars at points. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length should be the number of points in the point cloud.


[[% include 'common/scalar_quantity.md' %]]