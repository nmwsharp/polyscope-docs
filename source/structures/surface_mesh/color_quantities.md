Visualize color rgb-valued data at the elements of a surface mesh.

**Example**: visualizing random colors at faces
```cpp
#include "polyscope/surface_mesh.h"

// Make some random colors
std::vector<std::array<double, 3>> fColor(nFaces);
for (size_t iF = 0; iF < nFaces; iF++) {
  std::vector<size_t>& face = faceIndices[iF];
  fColor[iF] = {{polyscope::randomUnit(), polyscope::randomUnit(), polyscope::randomUnit()}};
}

// Visualize
polyscope::getSurfaceMesh("name")->addFaceColorQuantity("fColor", fColor);
```


### Add colors to elements

??? func "`#!cpp SurfaceMesh::addVertexColorQuantity(std::string name, const T& values)`"

    Add a color quantity defined at the vertices of the mesh.

    - `values` is the array of colors at vertices. The type should be [adaptable](/data_adaptors) to a 3-vector array of `float`s. The length should be the number of vertices in the mesh.

    RGB values are interpreted in the range `[0,1]`.

??? func "`#!cpp SurfaceMesh::addFaceColorQuantity(std::string name, const T& values)`"

    Add a color quantity defined at the faces of the mesh.

    - `values` is the array of colors at faces. The type should be [adaptable](/data_adaptors) to a 3-vector array of `float`s. The length should be the number of faces in the mesh.

    RGB values are interpreted in the range `[0,1]`.

