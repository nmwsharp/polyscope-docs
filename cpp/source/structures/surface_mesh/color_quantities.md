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


### Add Colors to Elements

??? func "`#!cpp SurfaceMesh::addVertexColorQuantity(std::string name, const T& values)`"

    Add a color quantity defined at the vertices of the mesh.

    - `values` is the array of colors at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of vertices in the mesh.

    RGB values are interpreted in the range `[0,1]`.

??? func "`#!cpp SurfaceMesh::addFaceColorQuantity(std::string name, const T& values)`"

    Add a color quantity defined at the faces of the mesh.

    - `values` is the array of colors at faces. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of faces in the mesh.

    RGB values are interpreted in the range `[0,1]`.


### Color Texture Maps

Texture images define data by storing it an image grid, and using coordinates defined on the face-corners or vertices of a mesh to sample values from the image for each point on the surface.

To visualize color data defined in texture maps, first add a [Parameterization Quantity]([[url.prefix]]/structures/surface_mesh/parameterization_quantities/) (aka UV map) defining the coordinates. Then, add a buffer of image data to be sampled from with the function below.

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
std::vector<glm::vec3> colorsTex(dimX * dimY, glm::vec3{.2, .3, .4});
polyscope::SurfaceTextureColorQuantity* qColor =
  psMesh->addTextureColorQuantity("tColor", *qParam, dimX, dimY, colorsTex, polyscope::ImageOrigin::UpperLeft);
qColor->setEnabled(true);

polyscope::show(3);
```

???+ func "`#!cpp SurfaceTextureColorQuantity* addTextureColorQuantity(std::string name, SurfaceParameterizationQuantity& param, size_t dimX, size_t dimY, const T& colors, ImageOrigin imageOrigin)`"

    Add a color quantity defined in a texture map.

    - `param` is a reference to a [`SurfaceParameterizationQuantity`]([[url.prefix]]/structures/surface_mesh/parameterization_quantities/), with coordinates on `[0,1]` which will be used to sample from the image.
    
    - the data, dimension, and origin arguments are the same as those used to define [images]([[url.prefix]]/structures/floating_quantities/images/). See there for details.


??? func "`#!cpp SurfaceTextureColorQuantity* addTextureColorQuantity(std::string name, std::string paramName, size_t dimX, size_t dimY, const T& colors, ImageOrigin imageOrigin)`"
    
    Like above, but takes the reference to the parameterization quantity by name.



{!common/color_quantity.md!}
