# Volume Meshes

Visualize volumetric 3D meshes, with tetrahedral and hexahedral (cube-like) elements, or even more general prism or pyramidal elements. Meshes may be pure tet/hex/etc, or a mixture of different element types---we'll use the term *cell* to refer generically to either a tet, hex, prism or pyramid element in a volume mesh.

As always, Polyscope can visualize the mesh itself, as well as any combination of scalar, color, or vector quantities associated with the vertices or cells of the mesh. Try clicking on the mesh to inspect the value of any quantity at that location, or using *slice planes* to inspect the internal structure and quantities defined within.

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/movies/volume_demo_compress.mp4" type="video/mp4">
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

Volume meshes are registered with Polyscope by passing the location of each vertex in the mesh, as well as the vertex indices for each cell. There are a few different variants to register meshes with pure tets and hexes, or a more general mixture of tets, hexes, prisms and pyramids. All of these register helpers return a pointer to a `polyscope::VolumeMesh` object which you can then add quantities to.

![element ordering conventions]([[url.prefix]]/media/volume_mesh_element_orderings.jpg)

???+ func "`#!cpp polyscope::registerTetMesh(std::string name, const V& vertexPositions, const C& tetIndices)`"

    Add a new volume mesh structure to Polyscope, with all tetrahedral elements.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.

    - `tetIndices` is the 2D array of vertex indices for each tetrahedral cell, with dimension `(C,4)` where `C` is the number of tets. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 4>>`. All indices should be valid 0-based indices in to the vertex list.

??? func "`#!cpp polyscope::registerHexMesh(std::string name, const V& vertexPositions, const C& hexIndices)`"

    Add a new volume mesh structure to Polyscope, with all hexahedral (cube-like) elements.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.

    - `hexIndices` is the 2D array of vertex indices for each hexahedral cell, with dimension `(C,8)` where `C` is the number of hexes. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 8>>`. All indices should be valid 0-based indices in to the vertex list.

??? func "`#!cpp polyscope::registerVolumeMesh(std::string name, const V& vertexPositions, const C& cellIndices)`"

    Add a new volume mesh structure to Polyscope, with a general mix of cell types.
    
    This variant takes a rectangular array as input, where all cell rows have 8 entries, but cells which are specified by less than 8 vertices are padded with `-1`.
    
    For instance, a row of the 2D array `cellIndices` which refers to a tet cell might hold `[12, 9, 22, 51, -1, -1, -1, -1]`.  A row in the 2D array `cellIndices` which refers to a prism cell might hold `[18, 32, 51, 17, 85, 23, -1, -1]`, etc.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.

    - `cellIndices` is the 2D array of vertex indices for each cell, with dimension `(C,8)` where `C` is the number of cells. For tet, prism and pyramid elements, the rows of the array should be right-padded with `-1` as appropriate for the cell topology. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a nested array of `unsigned int`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<int, 8>>`. All indices should be valid 0-based indices in to the vertex list, except padding entries which must be `-1`. Signed types should be used to support the `-1` padding convention. (NOTE: internally cell indices use `UINT32_MAX` for invalid entries, but you should pass padding as `-1` via a signed type to the input adaptor.)

??? func "`#!cpp polyscope::registerTetHexMesh(std::string name, const V& vertexPositions, const Ct& tetIndices, const Ct& hexIndices)`"

    Add a new volume mesh structure to Polyscope. This variant takes a mix of tet and hex elements, where each are given in their own separate list. Note that prisms and pyramids are also supported by the class, but not this constructor; use the general variant.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.
    
    - `tetIndices` is the 2D array of vertex indices for each tetrahedral cell, with dimension `(C,4)` where `C` is the number of tets. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 4>>`. All indices should be valid 0-based indices in to the vertex list.

    - `hexIndices` is the 2D array of vertex indices for each hexahedral cell, with dimension `(C,8)` where `C` is the number of hexes. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 8>>`. All indices should be valid 0-based indices in to the vertex list.

    For the purposes of element ordering, the cells are presumed to be ordered with all tetrahedral cells coming first, then hexahedral cells.

---

!!! warning "No support for 2D"

    Unlike other structures, 2D volume meshes are not supported; they don't make much sense (see [2D data]([[url.prefix]]/features/2D_data)).


### Updating a mesh

The locations of the vertices in a mesh can be updated with the member function `updateVertexPositions(newPositions)`. All quantities will be preserved. Changing the connectivity or element counts in a mesh is not supported, you will need to register a new mesh (perhaps with the same name to overwrite).


??? func "`#!cpp void VolumeMesh::updateVertexPositions(const V& newPositions)`"

    Update the vertex positions in a volume mesh structure.

    - `newPositions` is the vector array of 3D vertex locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors.  The length must be equal to the current number of vertices.


### Slice planes

[Slice planes]([[url.prefix]]/features/slice_planes) are particularly useful for inspecting the internal structure of a volume mesh, as shown in the demo video at the top. Slice planes can be manipulated programmatically or manually in the GUI; see the slice plane documentation for more details.

Slice planes have [special functionality]([[url.prefix]]/features/slice_planes/#inspecting-volume-meshes) for volume mesh vertex values---they can _inspect_ quantities on volume meshes and render them on the interior of the volume. See the slice plane documentation for details.

### Selection / Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene.  As with other structures, you can call `interpretPickResult()` to get additional info about a click. See [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#selection-picking) for general information.

```cpp
struct VolumeMeshPickResult {
  VolumeMeshElement elementType; // which kind of element did we click (enum values: {VERTEX, EDGE, FACE, CELL})
  int64_t index;                 // index of the clicked element
};
```

??? func "`#!cpp VolumeMeshPickResult VolumeMesh::interpretPickResult(PickResult result)`"

    Get additional information about a click.

### Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
color | the color of the outside of the volume | `#!cpp glm::vec3 getColor()` | `#!cpp setColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
interior color | the color of the inside of the volume | `#!cpp glm::vec3 getInteriorColor()` | `#!cpp setInteriorColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge color | the color of the edges of the mesh | `#!cpp glm::vec3 getEdgeColor()` | `#!cpp setEdgeColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!cpp double getEdgeWidth()` | `#!cpp setEdgeWidth(double val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |


