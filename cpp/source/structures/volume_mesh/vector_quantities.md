Visualize vector-valued data at the elements of a volume mesh.

![volume mesh vector values]({{url.prefix}}/media/volume_vector.jpg)

**Example**: showing vectors on vertices (here random vectors)
```cpp
/* ... initialization, create mesh ... */ 

// Register the volume mesh with Polyscope
polyscope::registerTetMesh("my mesh", verts, tets);

// Add a vector quantity
size_t nVerts = V.rows();
std::vector<std::array<double, 3>> randVec(nVerts);
for (size_t i = 0; i < nVerts; i++) {
  // use random vectors as test data
  randVec[i] = {{polyscope::randomUnit() - .5, 
                 polyscope::randomUnit() - .5, 
                 polyscope::randomUnit() - .5}};
}
auto vectorQ = polyscope::getVolumeMesh("my mesh")->addVertexVectorQuantity("random vec", randVec);

// Set some options
vectorQ->setEnabled(true);           // initially enabled
vectorQ->setVectorLengthScale(0.05); // make the vectors bigger

// Show the GUI
polyscope::show();
```

### Add vectors to elements

???+ func "`#!cpp VolumeMesh::addVertexVectorQuantity(std::string name, const T& vectors, VectorType vectorType = VectorType::STANDARD)`"

    Add a vector quantity defined at the vertices of the mesh.

    - `vectors` is the array of vectors at vertices. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a 3-vector array of `float`s. The length should be the number of vertices in the mesh.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.
    
    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse.

??? func "`#!cpp VolumeMesh::addCellVectorQuantity(std::string name, const T& vectors, VectorType vectorType = VectorType::STANDARD)`"

    Add a vector quantity defined at the cells of the mesh.

    - `vectors` is the array of vectors at cells. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a 3-vector array of `float`s. The length should be the number of cells in the mesh.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse.


### Options

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
vector radius | the radius vectors are drawn with | `#!cpp double getVectorRadius()` | `#!cpp setVectorRadius(double val, bool isRelative=true)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
vector length | vectors will be scaled so the longest is this long. ignored if `VectorType::Ambient` | `#!cpp double getVectorLengthScale()` | `#!cpp setVectorLengthScale(double val, bool isRelative=true)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
vector color | the color to draw the vectors with | `#!cpp glm::vec3 getVectorColor()` | `#!cpp setVectorColor(glm::vec3 val)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)
material | what [material]({{url.prefix}}/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values) |

_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

