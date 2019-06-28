This section outlines using Polyscope with [geometry-central](https://github.com/nmwsharp/geometry-central)!


### Registering a surface mesh

```cpp
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"

#include "geometrycentral/surface/halfedge_mesh.h"
#include "geometrycentral/surface/vertex_position_geometry.h"

using namespace geometrycentral::surface;

HalfedgeMesh& mesh = /* your mesh */;
EmbeddedGeometryInterface& geom = /* your geometry */;

// Be sure your mesh has vertex positions available
geom.requireVertexPositions();

// Register the mesh with polyscope
polyscope::registerSurfaceMesh(mesh.getFaceVertexList(), geom.vertexPositions);

// Note: for a VertexPositionGeometry, one could instead use
VertexPositionGeometry& posGeom = /* your geometry */;
polyscope::registerSurfaceMesh(mesh.getFaceVertexList(), 
                               posGeom.inputVertexPositions);
```


### Meshdata containers

Geometry-central's `Meshdata<>` containers can be passed directly to Polyscope for visualization.

```cpp


```


#### Custom ordering

Geometry-central's ordering of mesh halfedges and corners is different from Polyscope's ordering (see [indexing convention](../../../structures/surface_mesh/indexing_convention)). As such, you must tell Polyscope about this ordering for halfedge or corner-valued visualizations to work properly.

You can do this at mesh construction time...
