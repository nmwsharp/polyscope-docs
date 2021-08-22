Visualize vector-valued data at the points of a point cloud.

??? func "`#!cpp PointCloud::addVectorQuantity(std::string name, const T& vectors, VectorType vectorType = VectorType::STANDARD)`"

    Add a vector quantity to the point cloud.

    - `vectors` is the array of vectors at points. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of points in the point cloud.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to add 2D vectors (usually to a 2D point cloud), `addVectorQuantity2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

### Options

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
vector radius | the radius vectors are drawn with | `#!cpp double getVectorRadius()` | `#!cpp setVectorRadius(double val, bool isRelative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
vector length | vectors will be scaled so the longest is this long. ignored if `VectorType::Ambient` | `#!cpp double getVectorLengthScale()` | `#!cpp setVectorLengthScale(double val, bool isRelative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
vector color | the color to draw the vectors with | `#!cpp glm::vec3 getVectorColor()` | `#!cpp setVectorColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |

_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

