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
polyscope::PointCloud* psCloud = polyscope::registerPointCloud("really great points", points);

// set some options
psCloud->setPointRadius(0.02);
psCloud->setPointRenderMode(polyscope::PointRenderMode::Quad);

// show
polyscope::show()
```

??? func "`#!cpp PointCloud* registerPointCloud(std::string name, const T& pointPositions)`"

    Add a new point cloud structure to Polyscope.

    - `pointPositions` is the array of 3D point locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors. The length will be the number of points.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D point cloud, `registerPointCloud2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).


As with all structures, there is also `getPointCloud("name")`, `hasPointCloud("name")`, and `removePointCloud("name")`.

### Updating a point cloud

The locations of the points in a point cloud can be updated with the member function `updatePointPositions(newPositions)`. All quantities will be preserved. Changing the _number_ of points in the cloud is not supported, you will need to register a new cloud (perhaps with the same name to overwrite this one).


??? func "`#!cpp void PointCloud::updatePointPositions(const V& newPositions)`"

    Update the point positions in a point cloud structure.

    - `newPositions` is the vector array of 3D point locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors.  The length must be equal to the current number of points.

    Note: `updatePointPositions2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).


### Adjusting the point radius

Set the radius of the points with `PointCloud::setPointRadius(newRad)`. By default, the radius is a [relative value]([[url.prefix]]/basics/parameters/#scaled-values) which gets scaled by the content in the scene, so for example a default of `0.02` will always be a reasonable size no matter what the scale of the content in your scene is. Or, set `isRelative=false` to set an absolute radius in world units.

??? func "`#!cpp void PointCloud::setPointRadius(double newVal, bool isRelative=true)`"

    Update the radius for points in the point cloud.

    By default the radius is interpreted as a relative value, setting `isRelative=false` will treat is as an absolute length in world units.

To set a variable radius which is different for each point in the point cloud, see the [variable radius page]([[url.prefix]]/structures/point_cloud/variable_radius/).


### Selection / Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene.  As with other structures, you can call `interpretPickResult()` to get additional info about a click. See [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#selection-picking) for general information.

```cpp
struct PointCloudPickResult {
  int64_t index; // index of the clicked point
};
```

??? func "`#!cpp PointCloudPickResult PointCloud::interpretPickResult(PickResult result)`"

    Get additional information about a click.

### Point render mode

By default, Polyscope renders point clouds with a sphere for each point. However, for large point clouds (for instance, > 500,000 points, or on low-end hardware), this sphere rendering may become prohibitively expensive and lead to a laggy interface. As an alternative, points can be rendered as a small quad per-point, which is more efficient (for instance, it renders in real-time with 20,000,000+ points on my mid-range GPU).

![point render mode diagram](../../media/point_render_mode_diagram.jpg)

The `PointRenderMode` specifies which style is used:

- `PointRenderMode::Sphere` a small sphere is drawn for each point (default)
- `PointRenderMode::Quad` a small quad is drawn for each point

??? func "`#!cpp PointCloud* PointCloud::setPointRenderMode(PointRenderMode newVal)`"

    Set the the rendering method used to draw each point. One of `PointRenderMode::Sphere` (default) or `PointRenderMode::Quad`.

    There is also a corresponding `getPointRenderMode()`.


### Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
point radius | size of rendered points | `#!cpp double getPointRadius()` | `#!cpp setPointRadius(double newVal, bool isRelative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
point color | default color for point | `#!cpp glm::vec3 getPointColor()` | `#!cpp setPointColor(glm::vec3 newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
point render mode | how to draw points | `#!cpp PointRenderMode getPointRenderMode()` | `#!cpp setPointRenderMode(PointRenderMode newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#!cpp setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |


