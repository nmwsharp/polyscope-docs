# Volume Grids

Volume grid structures visualize data defined on an axis-aligned regularly-spaced 3D grid. 

As usual, first you register a volume grid, then add one or more quantities defined on that grid. Registering the grid itself just means specifying the locations of its extremal corners and the grid resolution. Then you can add data, such as scalar data as linearly-interpolated values per-node or as piecewise-constant values per-cell. Slice planes can also be used inspect the interior of the grid, isosurfaces can be extracted from scalar functions at nodes, and more. 

<video width=100% autoplay muted loop>
  <source src="/media/movies/volume_grid_demo_compress.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Example:** registering a volume grid and adding a scalar quantity
```cpp
#include "polyscope/polyscope.h"
#include "polyscope/volume_grid.h"

polyscope::init();

// define the resolution and bounds of the grid
uint32_t dimX = 20;
uint32_t dimY = 20;
uint32_t dimZ = 20;
glm::vec3 bound_low{-3., -3., -3.};
glm::vec3 bound_high{3., 3., 3.};

// register the grid
polyscope::VolumeGrid* psGrid = polyscope::registerVolumeGrid(
        "sample grid", {dimX, dimY, dimZ}, bound_low, bound_high);

// add a scalar function on the grid
uint32_t nData = dimX*dimY*dimZ;
float* scalarVals = /* your dimX*dimY*dimZ buffer of data*/;

polyscope::VolumeGridNodeScalarQuantity* scalarQ = 
    psGrid->addNodeScalarQuantity("node scalar1", 
                                  std::make_tuple(scalarVals, nData));
scalarQ->setEnabled(true);

polyscope::show();
```

### Registering a volume grid

!!! note "Specifying node vs. cells"

    Volume grid dimensions and locations are always defined in terms of _nodes_ (aka cell corners). The dimension is the number of _nodes_ along each axis, and the location is defined by the extremal _nodes_.

    For dimensions, if you are instead thinking in terms of the number of _cells_ (little cubical regions), add +1 to the number of cells along each dimension to get the equivalent number of nodes when registering the grid.

    For locations, the min/max bounds you specify when registering the grid are the locations up the minimum and maximum node (aka cell corner). If you are instead thinking in terms of cell center locations, shift them half-cell-width offset when registering the grid.


???+ func "`#!cpp polyscope::registerVolumeGrid(std::string name, glm::uvec3 gridNodeDim, glm::vec3 boundMin, glm::vec3 boundMax)`"

    Add a new volume grid structure to Polyscope.

    - `name` the name of the structure
    - `gridNodeDim` a `glm::uvec3` integer 3-vector giving the number of nodes in the grid along each dimension
    - `boundMin` a `glm::vec3` float 3-vector giving the xyz coordinates for the minimal node corner of the grid
    - `boundMax` a `glm::vec3` float 3-vector giving the xyz coordinates for the maximal node corner of the grid


??? func "`#!cpp polyscope::registerVolumeGrid(std::string name, uint64_t gridNodeAxesDim, glm::vec3 boundMin, glm::vec3 boundMax)`"

    Same as above, but takes a single axis dimension which is used for all 3 axes.


---

### Slice planes

[Slice planes]([[url.prefix]]/features/slice_planes) are particularly useful for inspecting the internal structure of a volume grid, as shown in the demo video at the top. Slice planes can be manipulated programmatically or manually in the GUI; see the slice plane documentation for more details.

### Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene.  See [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#selection-picking) for general information. 

By default, if you have only registered data defined on nodes, then only nodes can be picked (and vice-versa for cells). You can override this behavior by calling `VolumeGrid::markNodesAsUsed()`, to act as if a node quantity had been added, and likewise for `VolumeGrid::markCellsAsUsed()`.

As with other structures, you can call `interpretPickResult()` to get additional info about a click. 

```cpp
struct VolumeGridPickResult {
  VolumeGridElement elementType; // which kind of element did we click (enum values: {NODE, CELL})
  int64_t index;                 // index of the clicked element
};
```

??? func "`#!cpp CurveNetworkPickResult CurveNetwork::interpretPickResult(PickResult result)`"

    Get additional information about a click.


### Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
color | the color of the volume | `#!cpp glm::vec3 getColor()` | `#!cpp setColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge color | the color of the grid edges | `#!cpp glm::vec3 getEdgeColor()` | `#!cpp setEdgeColor(glm::vec3 val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!cpp double getEdgeWidth()` | `#!cpp setEdgeWidth(double val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
cube size factor | shrink factor from 0-1 to draw gaps between cells, 0 is no shrink (default) | `#!cpp double getCubeSizeFactor()` | `#!cpp setCubeSizeFactor(double val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |


