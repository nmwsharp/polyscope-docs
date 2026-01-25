Visualize distance-valued data at the elements of a surface mesh.

Distance quantities are basicly scalars, but are visualized with alternating stripes to show distance contours.

**Example**: visualizing exact geodesic distance computed via libIGL's wrappers around Kirsanov's MMP implementation.
```cpp
// Compute distance from vertex iVertexSource
Eigen::VectorXi VS, FS, VT, FT;
VS.resize(1);
VS << iVertexSource;
VT.setLinSpaced(meshV.rows(), 0, meshV.rows() - 1);
Eigen::VectorXd d;
igl::exact_geodesic(meshV, meshF, VS, FS, VT, FT, d);

// Add the distance quantity to the surface mesh
polyscope::getSurfaceMesh("input mesh")
    ->addVertexDistanceQuantity(
        "distance from vertex " + std::to_string(iVertexSource), d);
```


### Add distance to vertices

??? func "`#!cpp SurfaceMesh::addVertexDistanceQuantity(std::string name, const T& values)`"

    Add a distance quantity defined at the vertices of the mesh.

    - `values` is the array of distances at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length should be the number of vertices in the mesh.

??? func "`#!cpp SurfaceMesh::addVertexDistanceQuantity(std::string name, const T& values)`"

    Add a signed distance quantity defined at the vertices of the mesh.

    - `values` is the array of distances at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length should be the number of vertices in the mesh.

    This quantity is very similar to `addVertexDistanceQuantity`, except the colormap is adjusted to scale symetrically for negative values.

### Options

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
color map | the [color map]([[url.prefix]]/features/color_maps) to use | `#!cpp std::string getColorMap()` | `#!cpp setColorMap(std::string newMap)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
map range | the lower and upper limits used when mapping the data in to the color map| `#!cpp std::pair<double,double> getMapRange()` | `#!cpp setMapRange(std::pair<double,double>)` and `#!cpp resetMapRange()`| no
stripe size | the size of the stripes showing distance isolines | `#!cpp setStripeSize(double size, bool isRelative=true)` | `#!cpp double getStripeSize()` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)



