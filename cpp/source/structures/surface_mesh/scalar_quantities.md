Visualize scalar (real or integer)-valued data at the elements of a surface mesh.

**Example**: visualizing cotangent weights at edges with geometry-central
```cpp
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"

// (external library, used as an example)
#include "geometrycentral/surface/vertex_position_geometry.h"
using namespace geometrycentral::surface;

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


### Add Scalars to Elements

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


### Scalar Texture Maps

Texture images define data by storing it an image grid, and using coordinates defined on the face-corners or vertices of a mesh to sample values from the image for each point on the surface.

To visualize scalar data defined in texture maps, first add a [Parameterization Quantity]([[url.prefix]]/structures/surface_mesh/parameterization_quantities/) (aka UV map) defining the coordinates. Then, add a buffer of image data to be sampled from with the function below.

The resulting scalar texture supports color mapping and all of the other usual scalar data features.

**Example**
```cpp

polyscope::SurfaceMesh* psMesh = /* register a surface mesh */;

// a UV map to use (here, dummy data)
std::vector<glm::vec2> vals(psMesh->nCorners(), {0.5, 0.6});
auto qParam = psMesh->addParameterizationQuantity("param", vals);

// an image texture to use
// (here, dummy data)
size_t dimX = 100;
size_t dimY = 150;
std::vector<float> valuesTex(dimX * dimY, 0.77);
polyscope::SurfaceTextureScalarQuantity* qScalar =
  psMesh->addTextureScalarQuantity("tScalar", *qParam, dimX, dimY, valuesTex, polyscope::ImageOrigin::UpperLeft);
qScalar->setEnabled(true);

polyscope::show(3);
```

???+ func "`#!cpp SurfaceMesh::addTextureScalarQuantity(std::string name, SurfaceParameterizationQuantity& param, size_t dimX, size_t dimY, const T& data, ImageOrigin imageOrigin, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined in a texture map.

    - `param` is a reference to a [`SurfaceParameterizationQuantity`]([[url.prefix]]/structures/surface_mesh/parameterization_quantities/), with coordinates on `[0,1]` which will be used to sample from the image.
    
    - the data, dimension, and origin arguments are the same as those used to define [images]([[url.prefix]]/structures/floating_quantities/images/). See there for details.


??? func "`#!cpp SurfaceMesh::addTextureScalarQuantity(std::string name, std::string paramName, size_t dimX, size_t dimY, const T& data, ImageOrigin imageOrigin, DataType type = DataType::STANDARD)`"
    
    Like above, but takes the reference to the parameterization quantity by name.


{!common/scalar_quantity.md!}
