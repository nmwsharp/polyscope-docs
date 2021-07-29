# Surface Meshes

Surface meshes are one of the core structures in Polyscope. In addition to simply displaying the mesh, Polyscope can show any number of scalar, vector,color, and other kinds of quantities associated with the vertices/faces/edges/etc of the mesh.

Polyscope does not impose any requirements on the meshes visualized. They may be polygonal or nonmanifold.  As always, try clicking on the vertices or faces of a mesh see the data associated with that mesh element.

![surface_mesh_demo](/media/mesh_demo.gif)

### Registering a surface mesh

Example: registering a surface mesh from libIGL
```cpp
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"
#include <igl/readOBJ.h>

// Initialize Polyscope
polyscope::init();

// Read the mesh
Eigen::MatrixXd meshV;
Eigen::MatrixXi meshF;
igl::readOBJ(filename, meshV, meshF);

// Register the mesh with Polyscope
polyscope::registerSurfaceMesh("input mesh", meshV, meshF);

// Show the GUI
polyscope::show();
```

Surface meshes are registered with Polyscope by passing the location of each vertex in the mesh, as well as the vertex indices for each face.

??? func "`#!cpp polyscope::registerSurfaceMesh(std::string name, const V& vertexPositions, const F& faceIndices)`"

    Add a new surface mesh structure to Polyscope.

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 3-vectors; this allows many common types to be used as input, including `Eigen::MatrixXd` and `std::vector<std::array<double, 3>>`. The length will be the number of vertices.

    - `faceIndices` is the nested array of vertex indices for each face. The type should be [adaptable](/data_adaptors) to a nested array of `size_t`; this allows many common types to be used as input, including `Eigen::MatrixXi` and `std::vector<std::array<size_t, 3>>`. The outer length will be the number of faces. All indices should be valid 0-based indices in to the vertex list.

    General nested lists can be used to create polygonal meshes of varying face degree, such as `std::vector<std::vector<size_t>>`. Also, passing a fixed-size 2D array of indices will work just fine, like `Eigen::MatrixXi` with `Fx3` dimensions for a triangle mesh, or `Fx4` for a quad mesh.
    
    Note: the inner vector type of the vertex positions _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D surface mesh, `registerSurfaceMesh2D` exists with the same signature. See [2D data](/features/2D_data).

---

!!! warning "Element ordering"

    Polyscope quantities are ordered arrays of data, but not everyone can agree on the ordering of elements in a mesh. See [indexing conventions](../indexing_convention/).

    The default ordering is probably the same as yours for data on **vertices, faces, and corners**. However, data on **edges and halfedges** is much more likely to require setting an ordering.


### Updating a mesh

The locations of the vertices in a mesh can be updated with the member function `updateVertexPositions(newPositions)`. All quantities will be preserved. Changing the connectivity or element counts in a mesh is not supported, you will need to register a new mesh (perhaps with the same name to overwrite).


??? func "`#!cpp void SurfaceMesh::updateVertexPositions(const V& newPositions)`"

    Update the vertex positions in a surface mesh structure.

    - `newPositions` is the vector array of 3D vertex locations. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 3-vectors.  The length must be equal to the current number of vertices.

    Note: `updateVertexPositions2D` exists with the same signature. See [2D data](/features/2D_data).


### Back face policies

The faces of a mesh are implicitly given an outward orientation by the order in which the vertices are listed. The standard convention, which Polyscope respects, is that a counter-clockwise ordering of vertices defines the "outward" direction. Faces which are viewed from behind are referred to as _back faces_; they can arise when a surface is viewed from the inside, or if a mesh is not properly oriented. Polyscope offers several options for how backfaces are displayed.

![backface policies diagram](../../media/backface_diagram.png)

- `BackFacePolicy::Identical` all faces are always rendered identically, whether viewed from the front or back
- `BackFacePolicy::Different` backfaces are shaded differently, so they can be distinguished (this is the default)
- `BackFacePolicy::Cull` backfaces are culled, and not rendered at all

The choice of these policies can be set as an option for each surface mesh structure, either in the GUI via `[Options] -> [Back Face Policy]` or programmatically with the function below.

??? func "`#!cpp SurfaceMesh* SurfaceMesh::setBackFacePolicy(BackFacePolicy newPolicy)`"

    Set the policy for rendering oppositely-oriented backfaces.

    - `newPolicy` is an enum giving the new policy, one of `BackFacePolicy::Identical`, `BackFacePolicy::Different`, or `BackFacePolicy::Cull` as described above

    There is also a corresponding `getBackFacePolicy()`.

### Options


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the structure enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes](/basics/parameters/#persistent-values)
transparency | [transparency](/features/transparency) alpha for this structure in `[0,1]` | `#!cpp double getTransparency()` | `#!cpp setTransparency(double val)` | [yes](/basics/parameters/#persistent-values)
shade smooth | use smooth shading along faces or simple flat faces | `#!cpp bool isSmoothShade()` | `#!cpp setSmoothShade(bool isSmooth)` | [yes](/basics/parameters/#persistent-values)
surface color | the color of the mesh | `#!cpp glm::vec3 getSurfaceColor()` | `#!cpp setSurfaceColor(glm::vec3 val)` | [yes](/basics/parameters/#persistent-values)
edge color | the color of the edges of the mesh | `#!cpp glm::vec3 getEdgeColor()` | `#!cpp setEdgeColor(glm::vec3 val)` | [yes](/basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!cpp double getEdgeWidth()` | `#!cpp setEdgeWidth(double val)` | [yes](/basics/parameters/#persistent-values)
material | what [material](/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes](/basics/parameters/#persistent-values) |
back face policy | what [back face policy](#back-face-policies) to use | `#!cpp BackFacePolicy getBackFacePolicy()` | `#! setBackFacePolicy(BackFacePolicy newPolicy)` | [yes](/basics/parameters/#persistent-values) |

_(all setters return `this` to support chaining. setEnabled()/setTransparency() return generic setter, so chain them last)_
