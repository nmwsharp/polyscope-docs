
## Parameterization Quantity Options

These options and behaviors are available for all types of parameterization quantities on any structure.

### Styles

Several styles are available for how a parameterization is displayed. 

The `enum class ParamVizStyle` has options for how parameterizations are visualized:

- `CHECKER`: a two-color checker pattern
- `GRID`: a grid with thin lines
- `LOCAL_CHECK`: a checkboard over a radial colormap, centered around `(0,0)`
- `LOCAL_RAD`: distance stripes over a radial colormap, centered around `(0,0)`
- `CHECKER_ISLANDS`: a checkerboard where islands are colored according to the island labels integer, which must be given explicitly (meshes only)

The function `SurfaceParameterizationQuantity::setStyle(ParamVizStyle newStyle)` can be used to programmatically change the style.

### Types

The `enum class ParamCoordsType` has options that control how parameter coordinates are interpreted:

 - `UNIT`: UV coords are assumed to lie on the `[0,1]` interval
 - `WORLD`: UV coords are assumed to be scaled like the world-space positions of the mesh

These enums can be passed as an optional third argument when a parameterization is registered.


### Options

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
style | the visualization style (see above) | `#!cpp ParamVizStyle getStyle` | `#!cpp setStyle(ParamVizStyle style)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
checker colors | two colors to use for checkerboards | `#!cpp std::pair<glm::vec3,glm::vec3>getCheckerColors()` | `#!cpp setCheckerColors(std::pair<glm::vec3, glm::vec3> colors) ` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
grid colors | two colors to use for line and background of grid | `#!cpp std::pair<glm::vec3,glm::vec3>getGridColors()` | `#!cpp setGridColors(std::pair<glm::vec3, glm::vec3> colors) ` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
checker size | the width of checkers / stripes, always used as a relative value, unless the coord tpe is `UNIT` | `#!cpp double getCheckerSize()` | `#!cpp setCheckerSize(double val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
color map | the [color map]([[url.prefix]]/features/color_maps) to use for radial displays | `#!cpp std::string getColorMap()` | `#!cpp setColorMap(std::string newMap)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)



