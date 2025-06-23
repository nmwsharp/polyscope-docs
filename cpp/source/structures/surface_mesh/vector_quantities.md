Visualize vector-valued data at the elements of a surface mesh.

### Ambient vectors

_Ambient_ vectors are "standard" vectors, which have X-Y-Z vector coordinates in world space.

![face_vector_demo](../../media/face_vectors_demo.png)

??? func "`#!cpp SurfaceMesh::addVertexVectorQuantity(std::string name, const T& vectors, VectorType vectorType=VectorType::STANDARD)`"

    Add a vector quantity defined at the vertices of the mesh.

    - `vectors` is the array of vectors at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of vertices in the mesh.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.
    
    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to add 2D vectors (usually to a 2D mesh), `addVertexVectorQuantity2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

??? func "`#!cpp SurfaceMesh::addFaceVectorQuantity(std::string name, const T& vectors)`"

    Add a vector quantity defined at the faces of the mesh.

    - `vectors` is the array of vectors at faces. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of faces in the mesh.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to add 2D vectors (usually to a 2D mesh), `addFaceVectorQuantity2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).


### Tangent vectors

_Tangent_ vectors lie flat against the surface of a mesh. They are defined as 2D vector in a local 2D coordinate system at each vertex or face. We need to specify the vector itself as well as the basis vectors for the local coordinate systems.

Example: visualizing tangent vectors with geometry-central
```cpp 
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"

polyscope::init();

// Load mesh
std::unique_ptr<HalfedgeMesh> mesh;
std::unique_ptr<VertexPositionGeometry> geometry;
std::tie(mesh, geometry) = loadMesh(filename);

// Register the mesh with polyscope
psMesh = polyscope::registerSurfaceMesh("mesh",
              geometry->inputVertexPositions, mesh->getFaceVertexList(),
              polyscopePermutations(*mesh));


// Gather vertex tangent spaces
geometry->requireVertexTangentBasis();
VertexData<Vector3> vBasisX(*mesh);
VertexData<Vector3> vBasisY(*mesh);
for(Vertex v : mesh->vertices()) {
  vBasisX[v] = geometry->vertexTangentBasis[v][0];
  vBasisY[v] = geometry->vertexTangentBasis[v][1];
}

// Make a vector field
VertexData<Vector2> vecField = /* some field */

// Register the field
polyscope::getSurfaceMesh("mesh")->
  addVertexIntrinsicVectorQuantity("great vectors", 
                                   vecField, vBasisX, vBasisY);

polyscope::show();
```


??? func "`#!cpp SurfaceMesh::addVertexTangentVectorQuantity(std::string name, const T& vectors, const B1& basisX, const B2& basisY, int nSym=1, VectorType vectorType=VectorType::STANDARD)`"

    Add a tangent vector quantity defined at the vertices of the mesh.

    - `vectors` is the array of 2D vectors at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 2-vector array of `float`s. The length should be the number of vertices in the mesh.
    - `basisX` is the array of 3D vectors at vertices defining the X vector of the tangent basis. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of vertices in the mesh.
    - `basisY` is the array of 3D vectors at vertices defining the Y vector of the tangent basis. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of vertices in the mesh.
    - `nSym` is a symmetry order, for visualizing line fields (n = 2) and cross fields (n = 4), etc. If it is set to a non-`1` value, nSym distinct vectors will be displayed at each element, by rotating the input vector 2*PI/nSym radians.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

??? func "`#!cpp SurfaceMesh::addFaceTangentVectorQuantity(std::string name, const T& vectors, const B1& basisX, const B2& basisY, int nSym=1, VectorType vectorType=VectorType::STANDARD)`"

    Add a tangent vector quantity defined at the faces of the mesh.

    - `vectors` is the array of vectors at faces. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 2-vector array of `float`s. The length should be the number of faces in the mesh.
    - `basisX` is the array of 3D vectors at faces defining the X vector of the tangent basis. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of faces in the mesh.
    - `basisY` is the array of 3D vectors at faces defining the Y vector of the tangent basis. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of faces in the mesh.
    - `nSym` is a symmetry order, for visualizing line fields (n = 2) and cross fields (n = 4), etc. If it is set to a non-`1` value, nSym distinct vectors will be displayed at each element, by rotating the input vector 2*PI/nSym radians.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

### One forms

_One forms_ are tangent vector-like quantities represented as integrated scalars along edges. They commonly arise, for example, as a gradient which is difference of scalar values at vertices.


??? func "`#!cpp SurfaceMesh::addOneFormTangentVectorQuantity(std::string name, const T& data, const O& orientations)`"

    Add a one-form quantity via a scalar at edges, which will be shown like a vector field.

    - `data` is the array of scalars at edges. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`s. The length should be the number of edges in the mesh.
    - `orientations` 1-forms are defined with respect to an orientation of edges, so you need to tell Polyscope which direction your edges point in. This input is an array of booleans at edges. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `char`s (because `std::vector<bool>` is broken). The length should be the number of edges in the mesh. These booleans should be `true` if the edge points from the lower indexed adjacent vertex to the higher-indexed vertex, and false otherwise.

    Remember, before passing edge-valued data, be sure your [indexing convention](../indexing_convention) matches what Polyscope expects.

[[% include 'common/vector_quantity.md' %]]
