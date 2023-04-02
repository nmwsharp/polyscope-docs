Visualize color rgb-valued data at the points of a point cloud.

Example:
```cpp
#include "polyscope/point_cloud.h"

std::vector<std::array<double, 3>> randColor(points.size());
for (size_t i = 0; i < points.size(); i++) {
  randColor[i] = {{polyscope::randomUnit(), polyscope::randomUnit(), polyscope::randomUnit()}};
}

// visualize
polyscope::getPointCloud(pointCloudName)->addColorQuantity("random color", randColor);
```

??? func "`#!cpp PointCloud::addColorQuantity(std::string name, const T& values)`"

    Add a color quantity to the point cloud.

    - `values` is the array of colors at points. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of points in the point cloud.

    RGB values are interpreted in the range `[0,1]`.


{!common/color_quantity.md!}
