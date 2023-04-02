A _parameterization_ is a set of 2D coordinates associated with a mesh, often referred to as "UV coordinates". This sections details several functions for visualizing such parameterizations.

`#include "polyscope/surface_mesh.h"`

![param_demo](../../media/param_demo.gif)

**Example**: visualizing an LSCM parameterization via libIGL
```cpp
using namespace Eigen;
using namespace std;

// Fix two points on the boundary
VectorXi bnd, b(2, 1);
igl::boundary_loop(meshF, bnd);

if (bnd.size() == 0) {
  polyscope::warning("mesh has no boundary, cannot parameterize");
  return;
}

b(0) = bnd(0);
b(1) = bnd(round(bnd.size() / 2));
MatrixXd bc(2, 2);
bc << 0, 0, 1, 0;

// LSCM parametrization
Eigen::MatrixXd V_uv;
igl::lscm(meshV, meshF, b, bc, V_uv);

polyscope::getSurfaceMesh("input mesh")
    ->addVertexParameterizationQuantity("LSCM parameterization", V_uv);
```

## Adding

??? func "`#!cpp SurfaceMesh::addParameterizationQuantity(std::string name, const T& coords)`"

    Add a new parameterization quantity to the structure, defined at the corners of a mesh.

    - `coords` is the array of 2D UV coordinates at corners. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of corners in the mesh.


??? func "`#!cpp SurfaceMesh::addVertexParameterizationQuantity(std::string name, const T& coords)`"

    Add a new parameterization quantity to the structure, defined at the vertices of a mesh.

    - `coords` is the array of 2D UV coordinates at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of vertices in the mesh.


??? func "`#!cpp SurfaceMesh::addLocalParameterizationQuantity(std::string name, const T& coords)`"

    Add a new parameterization quantity to the structure, defined at the vertices of a mesh. this is similar to `addVertexParameterizationQuantity`, but has preset settings for `style` and `type` which are suitable for local parameterizations about a point.

    - `coords` is the array of 2D UV coordinates at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of vertices in the mesh.


{!common/parameterization_quantity.md!}
