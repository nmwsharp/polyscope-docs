
### Vector Quantity Options

These options and behaviors are available for all types of vector quantities on any structure.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
vector radius | the radius vectors are drawn with | `#!cpp double getVectorRadius()` | `#!cpp setVectorRadius(double val, bool isRelative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
vector length | vectors will be scaled so the longest is this long. ignored if `VectorType::Ambient` | `#!cpp double getVectorLengthScale()` | `#!cpp setVectorLengthScale(double val, bool isRelative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
vector color | the color to draw the vectors with | `#!cpp glm::vec3 getVectorColor()` | `#!cpp setVectorColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |



