# Volume Meshes

Volumetric meshes, such as tetrahedral (*tet*) and hexahedral (*hex*, cube-like) meshes, represent a region of 3D space. Polyscope can display tet and hex meshes, including those which have a mix of hex and tet elements. We'll use the term *cell* to refer generically to a tet or hex in a volume mesh. As always, Polyscope can also handle scalar, color, or vector quantities associated with the vertices or cells of the mesh, and you can click on the mesh elements to inspect values.

<video width=100% autoplay muted loop>
  <source src="/media/movies/volume_demo_compress.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Registering a volume mesh

Example: registering a tetrahedral mesh from libIGL
```cpp
#include "polyscope/polyscope.h"
#include "polyscope/volume_mesh.h"
#include <igl/readMESH.h>

// Initialize Polyscope
polyscope::init();

// Read mesh from file
Eigen::MatrixXd V; // vertex positions
Eigen::MatrixXi T; // tetrahedra
Eigen::MatrixXi F; // faces (we don't use these here)
igl::readMESH("path/to/volume.mesh", V, T, F);

// Register the volume mesh with Polyscope
polyscope::registerTetMesh("my mesh", V, T);

// Add a scalar quantity
size_t nVerts = V.rows();
std::vector<double> scalarV(nVerts);
for (size_t i = 0; i < nVerts; i++) {
  // use the x-coordinate of vertex position as a test function
  scalarV[i] = V(i,0);
}
polyscope::getVolumeMesh("my mesh")->addVertexScalarQuantity("scalar Q", scalarV);

// Show the GUI
polyscope::show();
```

Volume meshes are registered with Polyscope by passing the location of each vertex in the mesh, as well as the vertex indices for each cell. There are a few different variants to register meshes with tets, hexes, or a mix of the two. All of these register helpers return a pointer to a `polyscope::VolumeMesh` object which you can then add quantities to.

![tet element ordering conventions]({{url.prefix}}/media/tet_element_orderings.jpg)

???+ func "`#!cpp polyscope::registerTetMesh(std::string name, const V& vertexPositions, const C& tetIndices)`"

    Add a new volume mesh structure to Polyscope, with all tetrahedral elements.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]({{url.prefix}}/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.

    - `tetIndices` is the 2D array of vertex indices for each tetrahedral cell, with dimension `(C,4)` where `C` is the number of tets. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 4>>`. All indices should be valid 0-based indices in to the vertex list.

??? func "`#!cpp polyscope::registerHexMesh(std::string name, const V& vertexPositions, const C& hexIndices)`"

    Add a new volume mesh structure to Polyscope, with all hexahedral (cube-like) elements.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]({{url.prefix}}/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.

    - `hexIndices` is the 2D array of vertex indices for each hexahedral cell, with dimension `(C,8)` where `C` is the number of hexes. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 8>>`. All indices should be valid 0-based indices in to the vertex list.

??? func "`#!cpp polyscope::registerVolumeMesh(std::string name, const V& vertexPositions, const C& hexIndices)`"

    Add a new volume mesh structure to Polyscope, which may have a mix of cell types. This variant takes a rectangular array as input, where all cell rows have 8 entries, but cells with less than 8 vertices are padded with negative values.
    
    For instance, a row of the 2D array `hexIndices` which refers to a tet cell might hold `[12, 9, 22, 51, -1, -1, -1, -1]`.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]({{url.prefix}}/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.

    - `hexIndices` is the 2D array of vertex indices for each hexahedral cell, with dimension `(C,8)` where `C` is the number of tet/hexes. For tet elements, the rows of the array should be padded with negative indices, which will be ignored. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a nested array of `unsigned int`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<int, 8>>`. All indices should be valid 0-based indices in to the vertex list. Signed types should be used to support the negative element convention as described above.

??? func "`#!cpp polyscope::registerTetHexMesh(std::string name, const V& vertexPositions, const Ct& tetIndices, const Ct& hexIndices)`"

    Add a new volume mesh structure to Polyscope. This variant takes a mix of tet and hex elements, where each are given in their own separate list.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]({{url.prefix}}/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.
    
    - `tetIndices` is the 2D array of vertex indices for each tetrahedral cell, with dimension `(C,4)` where `C` is the number of tets. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 4>>`. All indices should be valid 0-based indices in to the vertex list.

    - `hexIndices` is the 2D array of vertex indices for each hexahedral cell, with dimension `(C,8)` where `C` is the number of hexes. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 8>>`. All indices should be valid 0-based indices in to the vertex list.

    For the purposes of element ordering, the cells are presumed to be ordered with all tetrahedral cells coming first, then hexahedral cells.

---

!!! warning "No support for 2D"

    Unlike other structures, 2D volume meshes are not supported; they don't make much sense (see [2D data]({{url.prefix}}/features/2D_data)).


### Updating a mesh

The locations of the vertices in a mesh can be updated with the member function `updateVertexPositions(newPositions)`. All quantities will be preserved. Changing the connectivity or element counts in a mesh is not supported, you will need to register a new mesh (perhaps with the same name to overwrite).


??? func "`#!cpp void VolumeMesh::updateVertexPositions(const V& newPositions)`"

    Update the vertex positions in a volume mesh structure.

    - `newPositions` is the vector array of 3D vertex locations. The type should be [adaptable]({{url.prefix}}/data_adaptors) to an array of `float`-valued 3-vectors.  The length must be equal to the current number of vertices.


### Slice planes

[Slice planes]({{url.prefix}}/features/slice_planes) are particularly useful for inspecting the internal stucture of a volume mesh, as shown in the demo video at the top. Slice planes can be manipulated programmatically or manually in the GUI; see the slice plane documentation for more details.

### Options


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the structure enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
transparency | [transparency]({{url.prefix}}/features/transparency) alpha for this structure in `[0,1]` | `#!cpp double getTransparency()` | `#!cpp setTransparency(double val)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
color | the color of the outside of the volume | `#!cpp glm::vec3 getColor()` | `#!cpp setColor(glm::vec3 val)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
interior color | the color of the inside of the volume | `#!cpp glm::vec3 getInteriorColor()` | `#!cpp setInteriorColor(glm::vec3 val)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
edge color | the color of the edges of the mesh | `#!cpp glm::vec3 getEdgeColor()` | `#!cpp setEdgeColor(glm::vec3 val)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!cpp double getEdgeWidth()` | `#!cpp setEdgeWidth(double val)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
material | what [material]({{url.prefix}}/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values) |

_(all setters return `this` to support chaining. setEnabled()/setTransparency() return generic setter, so chain them last)_
