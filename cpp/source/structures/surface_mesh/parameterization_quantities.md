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

    - `coords` is the array of 2D UV coordinates at corners. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of corners in the mesh.


??? func "`#!cpp SurfaceMesh::addVertexParameterizationQuantity(std::string name, const T& coords)`"

    Add a new parameterization quantity to the structure, defined at the vertices of a mesh.

    - `coords` is the array of 2D UV coordinates at vertices. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of vertices in the mesh.


??? func "`#!cpp SurfaceMesh::addLocalParameterizationQuantity(std::string name, const T& coords)`"

    Add a new parameterization quantity to the structure, defined at the vertices of a mesh. this is similar to `addVertexParameterizationQuantity`, but has preset settings for `style` and `type` which are suitable for local parameterizations about a point.

    - `coords` is the array of 2D UV coordinates at vertices. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of vertices in the mesh.


## Options

### Styles

Several styles are available for how a parameterization is displayed. 

The `enum class ParamVizStyle` has options for how parameterizations are visualized:

- `CHECKER`: a two-color checker pattern
- `GRID`: a grid with thin lines
- `LOCAL_CHECK`: a checkboard over a radial colormap, centered around `(0,0)`
- `LOCAL_RAD`: distance stripes over a radial colormap, centered around `(0,0)`

The function `SurfaceParameterizationQuantity::setStyle(ParamVizStyle newStyle)` can be used to programmatically change the style.

### Types

The `enum class ParamCoordsType` has options that control how parameter coordinates are interpreted:

 - `UNIT`: UV coords are assumed to lie on the `[0,1]` interval
 - `WORLD`: UV coords are assumed to be scaled like the world-space positions of the mesh

These enums can be passed as an optional third argument when a parameterization is registered.


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes](/basics/parameters/#persistent-values)
style | the visualization style (see above) | `#!cpp ParamVizStyle getStyle` | `#!cpp setStyle(ParamVizStyle style)` | [yes](/basics/parameters/#persistent-values)
checker colors | two colors to use for checkerboards | `#!cpp std::pair<glm::vec3,glm::vec3>getCheckerColors()` | `#!cpp setCheckerColors(std::pair<glm::vec3, glm::vec3> colors) ` | [yes](/basics/parameters/#persistent-values)
grid colors | two colors to use for line and background of grid | `#!cpp std::pair<glm::vec3,glm::vec3>getGridColors()` | `#!cpp setGridColors(std::pair<glm::vec3, glm::vec3> colors) ` | [yes](/basics/parameters/#persistent-values)
checker size | the width of checkers / stripes, always used as a relative value, unless the coord tpe is `UNIT` | `#!cpp double getCheckerSize()` | `#!cpp setCheckerSize(double val)` | [yes](/basics/parameters/#persistent-values)
color map | the [color map](/features/color_maps) to use for radial displays | `#!cpp std::string getColorMap()` | `#!cpp setColorMap(std::string newMap)` | [yes](/basics/parameters/#persistent-values)

_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

