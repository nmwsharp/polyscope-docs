# Point Clouds

Point clouds are one of the core structures in Polyscope. In addition to simply displaying the points, Polyscope can show any number of scalar, vector, or color quantities associated with the points.

As always, try clicking on a point to see the data associated with that point.

![point_cloud_demo](../../media/point_cloud_demo.gif)

### Registering a point cloud

Example: a point cloud of random points
```cpp
#include "polyscope/point_cloud.h"

std::vector<glm::vec3> points;

// generate points
for (size_t i = 0; i < 3000; i++) {
  points.push_back(
      glm::vec3{polyscope::randomUnit() - .5, 
                polyscope::randomUnit() - .5, 
                polyscope::randomUnit() - .5});
}

// visualize!
polyscope::registerPointCloud("really great points", points);
```

??? func "`#!cpp polyscope::registerPointCloud(std::string name, const T& pointPositions)`"

    Add a new point cloud structure to Polyscope.

    - `pointPositions` is the array of 3D point locations. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 3-vectors. The length will be the number of points.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D point cloud, `registerPointCloud2D` exists with the same signature. See [2D data](/features/2D_data).


### Updating a point cloud

The locations of the points in a point cloud can be updated with the member function `updatePointPositions(newPositions)`. All quantities will be preserved. Changing the _number_ of points in the cloud is not supported, you will need to register a new cloud (perhaps with the same name to overwrite this one).


??? func "`#!cpp void PointCloud::updatePointPositions(const V& newPositions)`"

    Update the point positions in a point cloud structure.

    - `newPositions` is the vector array of 3D point locations. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 3-vectors.  The length must be equal to the current number of points.

    Note: `updatePointPositions2D` exists with the same signature. See [2D data](/features/2D_data).
