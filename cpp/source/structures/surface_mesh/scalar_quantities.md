Visualize scalar (real or integer)-valued data at the elements of a surface mesh.

**Example**: visualizing cotangent weights at edges with geometry-central
```cpp
#include "geometrycentral/surface/vertex_position_geometry.h"
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"

polyscope::init();

// Load mesh
std::unique_ptr<HalfedgeMesh> mesh;
std::unique_ptr<VertexPositionGeometry> geom;

std::tie(mesh, geom) = loadMesh(args::get(inputFilename));
geom->requireVertexPositions();


// Register the geometry-central mesh
auto psMesh = polyscope::registerSurfaceMesh("input mesh", 
                                             geom->vertexPositions, 
                                             mesh->getFaceVertexList());
psMesh->setAllPermutations(polyscopePermutations(*mesh)); // set permutations, 
                                                          // so edge data is meaningful

// Build cotan weights for the mesh
geom->requireEdgeCotanWeights();

// Visualize cotan weights
psMesh->addEdgeScalarQuantity("edge cotan weights", geom->edgeCotanWeights);
polyscope::show();
```


### Add scalars to elements

??? func "`#!cpp SurfaceMesh::addVertexScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the vertices of the mesh.

    - `values` is the array of scalars at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length should be the number of vertices in the mesh.


??? func "`#!cpp SurfaceMesh::addFaceScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the faces of the mesh.

    - `values` is the array of scalars at faces. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length should be the number of faces in the mesh.


??? func "`#!cpp SurfaceMesh::addEdgeScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the edges of the mesh.

    - `values` is the array of scalars at edges. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length should be the number of edges in the mesh.
    
    Remember, before passing edge-valued data, be sure your [indexing convention](../indexing_convention) matches what Polyscope expects.


??? func "`#!cpp SurfaceMesh::addHalfedgeScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the halfedges of the mesh.

    - `values` is the array of scalars at halfedges. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length should be the number of halfedges in the mesh.

    Remember, before passing halfedge-valued data, be sure your [indexing convention](../indexing_convention) matches what Polyscope expects.


{!common/scalar_quantity.md!}
