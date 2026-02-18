# Sparse Volume Grids

Sparse volume grid structures visualize data defined on a sparse subset of cells in an axis-aligned 3D grid. Unlike the dense [Volume Grid]([[url.prefix]]/structures/volume_grid/basics), a sparse volume grid only stores and renders the cells you specify, making it well-suited for adaptive grids, occupancy maps, and other data that occupies only a portion of a regular grid.

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/sparse_volume_grid.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

As usual, first you register a sparse volume grid by specifying a grid origin, cell size, and list of occupied cells. Then you can add quantities such as scalar or color data defined per-cell or per-node.

**Example:** registering a sparse volume grid and adding a scalar quantity
```cpp
#include "polyscope/polyscope.h"
#include "polyscope/sparse_volume_grid.h"

polyscope::init();

// define the grid parameters
glm::vec3 origin{0., 0., 0.};
glm::vec3 cellWidth{0.1, 0.1, 0.1};

// list of occupied cells by their integer grid indices
std::vector<glm::ivec3> occupiedCells = {
    {0, 0, 0}, {1, 0, 0}, {0, 1, 0}, {0, 0, 1},
    {1, 1, 0}, {1, 0, 1}, {0, 1, 1}, {1, 1, 1},
};

// register the grid
polyscope::SparseVolumeGrid* psGrid = polyscope::registerSparseVolumeGrid(
        "sample sparse grid", origin, cellWidth, occupiedCells);

// add a scalar function on the grid (one value per cell)
std::vector<float> cellScalars(occupiedCells.size());
for (size_t i = 0; i < cellScalars.size(); i++) cellScalars[i] = static_cast<float>(i);

psGrid->addCellScalarQuantity("cell scalar", cellScalars);

polyscope::show();
```

### Registering a sparse volume grid

!!! note "Origin and cell width"

    The `origin` parameter specifies the position of the node/corner origin of the grid. Cell `(0,0,0)` has its lower-left corner at the origin. If you are thinking in terms of cell centers, shift the origin you pass in by half a cell width: `origin = cellCenter - 0.5 * cellWidth`.

    The `cellWidth` parameter gives the size of each grid cell along each axis. All cells have the same size.

???+ func "`#!cpp polyscope::registerSparseVolumeGrid(std::string name, glm::vec3 origin, glm::vec3 gridCellWidth, const T& occupiedCells)`"

    Add a new sparse volume grid structure to Polyscope.

    - `name` the name of the structure
    - `origin` a `glm::vec3` giving the xyz position of the node/corner origin
    - `gridCellWidth` a `glm::vec3` giving the width of each cell along each axis
    - `occupiedCells` an array of `glm::ivec3` giving the integer grid indices of all occupied cells. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `glm::ivec3`.


---

### Render modes

The sparse volume grid supports two render modes, controlled by `SparseVolumeGrid::setRenderMode()`:

- **`SparseVolumeGridRenderMode::Gridcube`** (default) renders each occupied cell as a filled cube. Quantities are visualized on the cube faces.
- **`SparseVolumeGridRenderMode::Wireframe`** renders only the grid outline as wireframe edges. This mode is useful for seeing through the grid to inspect its structure. Quantities are not drawn in wireframe mode.

![sparse volume grid render modes]([[url.prefix]]/media/sparse_volume_render_modes.jpg)

The wireframe appearance can be adjusted with `SparseVolumeGrid::setWireframeRadius()` and `SparseVolumeGrid::setWireframeColor()`.

```cpp
polyscope::SparseVolumeGrid* psGrid = polyscope::registerSparseVolumeGrid(
        "sample sparse grid", origin, cellWidth, occupiedCells);

psGrid->setRenderMode(SparseVolumeGridRenderMode::Wireframe);
psGrid->setWireframeRadius(0.5); 
psGrid->setWireframeColor(glm::vec3{1.f, 0.f, 0.f});
```

### Slice planes

As shown in the video above, [slice planes]([[url.prefix]]/features/slice_planes) are useful for inspecting the structure of a sparse volume grid. Slice planes can be manipulated programmatically or manually in the GUI; see the slice plane documentation for more details.

### Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene. Picking sparse volume grid elements works similarly to other structures, see [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#picking-selection-and-querying-the-scene) for general information.

By default, only cells can be selected, until you have added some data on nodes. You can override this behavior by calling `SparseVolumeGrid::markNodesAsUsed()`, to act as if a node quantity had been added.

As with other structures, you can call `interpretPickResult()` to get additional info about a click.

```cpp
struct SparseVolumeGridPickResult {
  SparseVolumeGridElement elementType; // which kind of element was clicked (enum values: {CELL, NODE})
  glm::ivec3 cellIndex;               // integer grid index of the clicked cell (only populated if cell)
  uint64_t cellFlatIndex;             // flat index into the occupied cells array (only populated if cell)
  glm::ivec3 nodeIndex;               // integer grid index of the clicked node (only populated if node)
};
```

??? func "`#!cpp SparseVolumeGridPickResult SparseVolumeGrid::interpretPickResult(PickResult result)`"

    Get additional information about a click, specific to this structure type (if it was the structure which was clicked on).


### Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
color | the color of the volume | `#!cpp glm::vec3 getColor()` | `#!cpp setColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!cpp double getEdgeWidth()` | `#!cpp setEdgeWidth(double val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge color | the color of the grid edges | `#!cpp glm::vec3 getEdgeColor()` | `#!cpp setEdgeColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
cube size factor | shrink factor from 0-1 to draw gaps between cells, 0 is no shrink (default) | `#!cpp double getCubeSizeFactor()` | `#!cpp setCubeSizeFactor(double val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#!cpp setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
render mode | how to render the voxels: `Gridcube` (default, filled cubes) or `Wireframe` (grid outline only) | `#!cpp SparseVolumeGridRenderMode getRenderMode()` | `#!cpp setRenderMode(SparseVolumeGridRenderMode mode)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
wireframe radius | relative radius for wireframe spheres/cylinders; `1` means radius is half the smallest cell width | `#!cpp double getWireframeRadius()` | `#!cpp setWireframeRadius(double val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
wireframe color | color used for wireframe rendering | `#!cpp glm::vec3 getWireframeColor()` | `#!cpp setWireframeColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
