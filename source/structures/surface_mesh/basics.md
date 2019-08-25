# Surface Meshes

Surface meshes are one of the core structures in Polyscope. In addition to simply displaying the mesh, Polyscope can show any number of scalar, vector,color, and other kinds of quantities associated with the vertices/faces/edges/etc of the mesh.

Polyscope does not impose any requirements on the meshes visualized. They may be polygonal or nonmanifold.  As always, try clicking on the vertices or faces of a mesh see the data associated with that mesh element.

![surface_mesh_demo](../../media/mesh_demo.gif)

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

    - `vertexPositions` is the vector array of 3D vertex locations. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 3-vectors. The length will be the number of vertices.

    - `faceIndices` is the nested array of vertex indices for each face. The type should be [adaptable](/data_adaptors) to a nested array of `size_t`. The outer length will be the number of faces. All indices should be valid 0-based indices in to the vertex list.

    Fortunately, although Polyscope accepts a general nested list of face vertex indices to support Polygonal meshes, passing a fixed-size `Nx3` array for a triangle will work just fine, like `Eigen::MatrixXi`.
    
    Note: the inner vector type of the vertex positions _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D surface mesh, `registerSurfaceMesh2D` exists with the same signature. See [2D data](/features/2D_data).

---

!!! warning "Element ordering"

    Polyscope quantities are ordered arrays of data, but not everone can agree on the ordering of elements in a mesh. See [indexing conventions](../indexing_convention/).

    The default ordering is probably the same as yours for data on **vertices, faces, and corners**. However, data on **edges and halfedges** is much more likely to require setting an ordering.


### Updating a mesh

The locations of the vertices in a mesh can be updated with the member function `updateVertexPositions(newPositions)`. All quantities will be preserved. Changing the connectivity or element counts in a mesh is not supported, you will need to register a new mesh (perhaps with the same name to overwrite).


??? func "`#!cpp void SurfaceMesh::updateVertexPositions(const V& newPositions)`"

    Update the vertex positions in a surface mesh structure.

    - `newPositions` is the vector array of 3D vertex locations. The type should be [adaptable](/data_adaptors) to an array of `float`-valued 3-vectors.  The length must be equal to the current number of vertices.

    Note: `updateVertexPositions2D` exists with the same signature. See [2D data](/features/2D_data).
