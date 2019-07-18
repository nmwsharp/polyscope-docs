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

    - `values` is the array of distances at vertices. The type should be [adaptable](/data_adaptors) to a `float` scalar array. The length should be the number of vertices in the mesh.

??? func "`#!cpp SurfaceMesh::addVertexDistanceQuantity(std::string name, const T& values)`"

    Add a signed distance quantity defined at the vertices of the mesh.

    - `values` is the array of distances at vertices. The type should be [adaptable](/data_adaptors) to a `float` scalar array. The length should be the number of vertices in the mesh.

    This quantity is very similar to `addVertexDistanceQuantity`, except the colormap is adjusted to scale symetrically for negative values.
