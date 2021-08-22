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

    - `values` is the array of scalars at points. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a `float` scalar array. The length should be the number of points in the point cloud.



### Options

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
color map | the [color map]({{url.prefix}}/features/color_maps) to use | `#!cpp std::string getColorMap()` | `#!cpp setColorMap(std::string newMap)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
map range | the lower and upper limits used when mapping the data in to the color map| `#!cpp std::pair<double,double> getMapRange()` | `#!cpp setMapRange(std::pair<double,double>)` and `#!cpp resetMapRange()`| no

_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

