# Simple Triangle Mesh

`SimpleTriangleMesh` is an alternate minimal-and-efficient structure for displaying triangle meshes. It only supports pure triangle meshes and a limited set of quantities and other features, but it is higher-performance and supports more general updates (including changing the _number_ of vertex and faces without creating a new mesh).

The [Surface Mesh]([[url.prefix]]/structures/surface_mesh/basics/) structure is the primary way to display surface meshes in Polyscope for almost all use cases, and has a much larger feature set. Only use `SimpleTriangleMesh` if you particularly need for fast performance, large meshes, or dynamic updates.


**Example:**
```cpp
#include "polyscope/polyscope.h"
#include "polyscope/simple_triangle_mesh.h"

polyscope::init();

// Some mesh data
std::vector<glm::vec3> vertices = { {0,0,0}, {1,0,0}, {0,1,0}, {0,0,1} };
std::vector<glm::uvec3> faces   = { {0,1,2}, {0,1,3}, {0,2,3}, {1,2,3} };

// Register the mesh
polyscope::SimpleTriangleMesh* mesh =
    polyscope::registerSimpleTriangleMesh("my mesh", vertices, faces);

// Add a scalar quantity at vertices
std::vector<float> vertScalar = {0.f, 1.f, 0.5f, 0.25f};
mesh->addVertexScalarQuantity("height", vertScalar);

polyscope::show();
```


## Registering

??? func "`#!cpp SimpleTriangleMesh* registerSimpleTriangleMesh(std::string name, const V& vertexPositions, const F& faceIndices)`"

    Add a new simple triangle mesh structure to Polyscope.

    - `vertexPositions` is the array of 3D vertex positions. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors. The length gives the vertex count.

    - `faceIndices` is the array of triangular faces, each given as a triple of vertex indices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of 3-vectors of integers (e.g. `Eigen::MatrixXi` with `Fx3` dimensions, or `std::vector<std::array<size_t,3>>`). All indices must be valid 0-based indices into the vertex list.

    Only triangle faces are supported; quad or polygonal input is not accepted.


As with all structures, there are also `getSimpleTriangleMesh("name")`, `hasSimpleTriangleMesh("name")`, and `removeSimpleTriangleMesh("name")`.


## Updating

The `SimpleTriangleMesh` structure supports a wider range of updates than the standard `SurfaceMesh`, and all updates are faster.  In particular, it is possible to change the number of vertices and faces on an existing `SimpleTriangleMesh`, and update any quantities accordingly.

??? func "`#!cpp void SimpleTriangleMesh::updateVertexPositions(const V& newPositions)`"

    Update the vertex positions. The vertex count and face connectivity must remain the same.

    - `newPositions` is the new array of vertex positions. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors. Length must equal the current vertex count.

??? func "`#!cpp void SimpleTriangleMesh::updateMesh(const V& newVertices, const F& newFaces)`"

    Update both vertices and faces. Vertex and face counts may change.

    - `newVertices` is the new array of vertex positions.
    - `newFaces` is the new array of face index triples.

    Internally the buffers use amortized doubling, so capacity is only reallocated when the new size exceeds the current capacity. Call `reserveMeshCapacity()` beforehand to avoid reallocations entirely.

??? func "`#!cpp void SimpleTriangleMesh::reserveMeshCapacity(size_t nVerts, size_t nFaces)`"

    Pre-allocate buffer capacity for at least `nVerts` vertices and `nFaces` faces. Subsequent calls to `updateMesh()` that stay within this capacity will not trigger any memory reallocation.

    Even naively calling `updateMesh()` each time will not _always_ trigger a reallocation, since the internal buffers use amortized doubling. However, if you know the maximum size of your mesh in advance, calling `reserveMeshCapacity()` can guarantee that no reallocations will occur during updates, which can improve performance and avoid stutters.


<!-- TODO document on-device GPU updates here -->

## Selection / Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene. As with other structures, call `interpretPickResult()` to get element-level information about a click. See [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#selection-picking) for general information.

```cpp
struct SimpleTriangleMeshPickResult {
  MeshElement elementType;  // which kind of element was clicked (VERTEX or FACE)
  int64_t index;            // index of the clicked element
};
```

??? func "`#!cpp SimpleTriangleMeshPickResult SimpleTriangleMesh::interpretPickResult(const PickResult& result)`"

    Get additional mesh-specific info about a pick result. This function is only valid to call on the structure that was clicked.

The selectable element types can be restricted:

??? func "`#!cpp SimpleTriangleMesh* SimpleTriangleMesh::setSelectionMode(MeshSelectionMode newMode)`"

    Set which element types can be selected by clicking. Options:

    - `MeshSelectionMode::Auto` — vertices and faces are both selectable (default)
    - `MeshSelectionMode::VerticesOnly` — only vertices are selectable
    - `MeshSelectionMode::FacesOnly` — only faces are selectable

??? func "`#!cpp MeshSelectionMode SimpleTriangleMesh::getSelectionMode()`"


## Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
color | surface color | `#!cpp glm::vec3 getSurfaceColor()` | `#!cpp setSurfaceColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
back face policy | how back faces are rendered | `#!cpp BackFacePolicy getBackFacePolicy()` | `#!cpp setBackFacePolicy(BackFacePolicy newPolicy)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
back face color | color used when policy is `Custom` | `#!cpp glm::vec3 getBackFaceColor()` | `#!cpp setBackFaceColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
material | material used for shading | `#!cpp std::string getMaterial()` | `#!cpp setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
selection mode | which elements can be picked | `#!cpp MeshSelectionMode getSelectionMode()` | `#!cpp setSelectionMode(MeshSelectionMode mode)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |

The back face policy values mirror those of [Surface Mesh]([[url.prefix]]/structures/surface_mesh/basics/#back-face-policies): `BackFacePolicy::Identical`, `BackFacePolicy::Different` (default), `BackFacePolicy::Custom`, and `BackFacePolicy::Cull`.


---

## Scalar Quantities

Visualize scalar (real-valued) data at the vertices or faces of the mesh.

**Example:**
```cpp
polyscope::SimpleTriangleMesh* mesh =
    polyscope::registerSimpleTriangleMesh("my mesh", vertices, faces);

// Vertex scalars
std::vector<float> vScalar(nVerts);
/* fill vScalar ... */
auto* q = mesh->addVertexScalarQuantity("my vertex scalar", vScalar);
q->setEnabled(true);

// Face scalars
std::vector<float> fScalar(nFaces);
/* fill fScalar ... */
mesh->addFaceScalarQuantity("my face scalar", fScalar);
```

??? func "`#!cpp SimpleTriangleMeshVertexScalarQuantity* SimpleTriangleMesh::addVertexScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the vertices of the mesh.

    - `values` is the array of scalars at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length must equal the current vertex count.
    - `type` is the [data type]([[url.prefix]]/features/scalar_quantities/#data-type) hint used for color mapping. Default is `DataType::STANDARD`.

??? func "`#!cpp SimpleTriangleMeshFaceScalarQuantity* SimpleTriangleMesh::addFaceScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the faces of the mesh.

    - `values` is the array of scalars at faces. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array. The length must equal the current face count.
    - `type` is the [data type]([[url.prefix]]/features/scalar_quantities/#data-type) hint used for color mapping. Default is `DataType::STANDARD`.

### Updating Scalar Data

Scalar quantity values can be updated in-place without removing and re-adding the quantity. The new data must have the same count as the original.

??? func "`#!cpp void SimpleTriangleMeshVertexScalarQuantity::updateData(const T& newValues)`"

    Update the scalar values for a vertex scalar quantity. Length must match the current vertex count.

??? func "`#!cpp void SimpleTriangleMeshFaceScalarQuantity::updateData(const T& newValues)`"

    Update the scalar values for a face scalar quantity. Length must match the current face count.

[[% include 'common/scalar_quantity.md' %]]


---

## Color Quantities

Visualize RGB color data at the vertices or faces of the mesh. Colors are specified as 3-vectors of floats in the range `[0,1]`.

**Example:**
```cpp
polyscope::SimpleTriangleMesh* mesh =
    polyscope::registerSimpleTriangleMesh("my mesh", vertices, faces);

// Vertex colors
std::vector<glm::vec3> vColor(nVerts, {0.5f, 0.2f, 0.8f});
auto* qv = mesh->addVertexColorQuantity("my vertex color", vColor);
qv->setEnabled(true);

// Face colors
std::vector<glm::vec3> fColor(nFaces, {0.1f, 0.9f, 0.3f});
mesh->addFaceColorQuantity("my face color", fColor);
```

??? func "`#!cpp SimpleTriangleMeshVertexColorQuantity* SimpleTriangleMesh::addVertexColorQuantity(std::string name, const T& values)`"

    Add an RGB color quantity defined at the vertices of the mesh.

    - `values` is the array of colors at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length must equal the current vertex count.

    RGB values are interpreted in the range `[0,1]`.

??? func "`#!cpp SimpleTriangleMeshFaceColorQuantity* SimpleTriangleMesh::addFaceColorQuantity(std::string name, const T& values)`"

    Add an RGB color quantity defined at the faces of the mesh.

    - `values` is the array of colors at faces. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length must equal the current face count.

    RGB values are interpreted in the range `[0,1]`.

### Updating Color Data

Color quantity values can be updated in-place without removing and re-adding the quantity. The new data must have the same count as the original.

??? func "`#!cpp void SimpleTriangleMeshVertexColorQuantity::updateData(const T& newValues)`"

    Update the color values for a vertex color quantity. Length must match the current vertex count.

??? func "`#!cpp void SimpleTriangleMeshFaceColorQuantity::updateData(const T& newValues)`"

    Update the color values for a face color quantity. Length must match the current face count.

[[% include 'common/color_quantity.md' %]]
