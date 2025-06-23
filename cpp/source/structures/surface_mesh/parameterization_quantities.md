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

??? func "`#!cpp SurfaceMesh::addParameterizationQuantity(std::string name, const T& coords, ParamCoordsType type=ParamCoordsType::UNIT)`"

    Add a new parameterization quantity to the structure, defined at the corners of a mesh.

    - `coords` is the array of 2D UV coordinates at corners. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of corners in the mesh.

    - `type` the default interpretation of the coordinate scale, see below

??? func "`#!cpp SurfaceMesh::addVertexParameterizationQuantity(std::string name, const T& coords, ParamCoordsType type=ParamCoordsType::UNIT)`"

    Add a new parameterization quantity to the structure, defined at the vertices of a mesh.

    - `coords` is the array of 2D UV coordinates at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of vertices in the mesh.

    - `type` the default interpretation of the coordinate scale, see below

??? func "`#!cpp SurfaceMesh::addLocalParameterizationQuantity(std::string name, const T& coords, ParamCoordsType type=ParamCoordsType::WORLD)`"

    Add a new parameterization quantity to the structure, defined at the vertices of a mesh. this is similar to `addVertexParameterizationQuantity`, but has preset settings for `style` and `type` which are suitable for local parameterizations about a point.

    - `coords` is the array of 2D UV coordinates at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of vertices in the mesh.

    - `type` the default interpretation of the coordinate scale, see below

## Visualizing islands and seams

<!-- TODO add an image -->

For parameterizations on surface meshes, additional features are available to visualize UV island and seams. The term _islands_ refers to connected components of faces in the 2D parameterization, and the term _seams_ refers to the subset of edges separating adjacent faces which are not connected.
    
UV islands can be colored per-island with the `ParamVizStyle::CHECKER_ISLANDS` style. Each face should have a distinct integer indicating which island it is a part of, which the caller must compute and pass via the function below (Polyscope does not compute it automatically). 

??? func "`#!cpp void SurfaceParameterizationQuantity::setIslandLabels(const T& labels)`"

    #### setIslandLabels

    Set an integer value per-face of the mesh, which can be used to color islands distinctly in the `ParamVizStyle::CHECKER_ISLANDS` style. Each face should have a distinct integer indicating which island it is a part of, which V
    
    Technically this can be any integer per-face, although it is generally useful for visualizing islands.

    - `labels` is the array of face labels. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of integers.  The length must be equal to the number of faces in the mesh.
    
    This will have no effect unless you also set `ParamVizStyle::CHECKER_ISLANDS`.


Additionally, the seams of a parameterization can be visualized as a [curve network]([[url.prefix]]/structures/curve_network/basics). These seams are computed automatically by Polyscope, the curve network is created by calling the function below, and is otherwise an ordinary curve network.

??? func "`#!cpp CurveNetwork* SurfaceParameterizationQuantity::createCurveNetworkFromSeams(std::string structureName="")`"
    
    #### createCurveNetworkFromSeams

    Create a [curve network]([[url.prefix]]/structures/curve_network/basics) from the seams of a UV map.
    
    - `structureName` the name of the new curve network structure. If left as the empty string (default) a name will be generated.


{!common/parameterization_quantity.md!}
