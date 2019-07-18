This section demonstrates using Polyscope with [geometry-central](https://geometry-central.net)! Note that a few useful adaptor functions are included in `geometrycentral/surface/meshio.h`.

See [this repository](https://github.com/nmwsharp/gc-polyscope-project-template) for a sample project configuration and CMAKE build system.

!!! note
    This section is written against a soon-to-be released overhaul of geometry-central, which currently lives in the `v1` branch of that repository.

### Registering a surface mesh

```cpp
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"

#include "geometrycentral/surface/halfedge_mesh.h"
#include "geometrycentral/surface/vertex_position_geometry.h"
#include "geometrycentral/surface/meshio.h

using namespace geometrycentral::surface;

HalfedgeMesh& mesh = /* your mesh */;
EmbeddedGeometryInterface& geom = /* your geometry */;

// Be sure your mesh has vertex positions available
geom.requireVertexPositions();

// Register the mesh with polyscope
polyscope::registerSurfaceMesh("myMesh", geom.vertexPositions, 
                              mesh.getFaceVertexList());

// Note: for a VertexPositionGeometry, one could instead use:
VertexPositionGeometry& posGeom = /* your geometry */;
polyscope::registerSurfaceMesh("myMesh", posGeom.inputVertexPositions, 
                               mesh.getFaceVertexList());
```


### Meshdata containers

Geometry-central's `Meshdata<>` containers can be passed directly to Polyscope for visualization.

```cpp
/* (continuing up from the Registering example above) */

VertexData<double> myScalar = /* some scalar on vertices */;
polyscope::getMesh("myMesh")->addVertexScalarQuantity("myScalar", myScalar);

FaceData<double> otherScalar = /* another scalar on faces*/;
polyscope::getMesh("myMesh")->addFaceScalarQuantity("otherScalar", otherScalar);

FaceData<double> anotherScalar = /* another scalar on edges*/;
polyscope::getMesh("myMesh")->addEdgeScalarQuantity("super important edge scalar", 
                                                     anotherScalar);

// Containers holding `Vector3`s can be used for 3D vectors at faces and vertices
// Example: vertex normals as computed in geometry-central
posGeom->requireVertexNormals();
polyscope::getMesh("myMesh")->addVertexVectorQuantity("vertex normals", 
                                                       posGeom->vertexNormals);
```


#### Custom ordering

Geometry-central's ordering of mesh halfedges and corners is different from Polyscope's default ordering (see [indexing convention](../../../structures/surface_mesh/indexing_convention)). As such, you must tell Polyscope about this ordering for halfedge or corner-valued visualizations to work properly. The geometry-central function `polyscopePermutations(HalfedgeMesh& mesh)` from `meshio.h` generates the ordering data in an approriate form for Polyscope, and can be passed either at construction time or after.

```cpp
polyscope::SurfaceMesh* psMesh = 
    polyscope::registerSurfaceMesh("myMesh", 
                                   geom->vertexPositions, 
                                   mesh->getFaceVertexList());

psMesh->setAllPermutations(polyscopePermutations(*mesh));

// could alternately pass polyscopePermutations(*mesh) as additional 
// last parameter of constructor
polyscope::SurfaceMesh* psMesh = 
    polyscope::registerSurfaceMesh("myMesh", 
                                   geom->vertexPositions, 
                                   mesh->getFaceVertexList(),
                                   polyscopePermutations(*mesh));

```

#### Tangent vector data




#### 1-forms

To communicate the canonical edge orientation when passing a 1-form, use `polyscopeEdgeOrientations(mesh)` from `meshio.h`.

Example:
```cpp
#include "geometrycentral/surface/meshio.h"

HalfedgeMesh& mesh = /* your mesh */;
EdgeData<double> myForm = /* your 1-form */;

polyscope::getSurfaceMesh("myMesh")->
  addOneFormIntrinsicVectorQuantity("my form", myForm, 
                                    polyscopeEdgeOrientations(mesh));

```
