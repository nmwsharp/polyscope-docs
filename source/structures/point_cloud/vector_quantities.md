Visualize vector-valued data at the points of a point cloud.

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

??? func "`#!cpp PointCloud::addVectorQuantity(std::string name, const T& vectors, VectorType vectorType = VectorType::STANDARD)`"

    Add a vector quantity to the point cloud.

    - `vectors` is the array of vectors at points. The type should be [adaptable](/data_adaptors) to a 3-vector array of `float`s. The length should be the number of points in the point cloud.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, but passing `VectorType::AMBIENT` ensures they have the proper world-space length.

