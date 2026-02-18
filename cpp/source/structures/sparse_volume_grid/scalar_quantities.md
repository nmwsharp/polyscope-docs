Visualize scalar-valued data at the nodes or cells of a sparse volume grid.

![sparse volume grid scalar quantity]([[url.prefix]]/media/sparse_volume_scalar_quantity.jpg)


**Example:** adding scalar quantities to a sparse volume grid
```cpp
#include "polyscope/polyscope.h"
#include "polyscope/sparse_volume_grid.h"

polyscope::init();

glm::vec3 origin{0., 0., 0.};
glm::vec3 cellWidth{0.1, 0.1, 0.1};

std::vector<glm::ivec3> occupiedCells = {
    {0, 0, 0}, {1, 0, 0}, {0, 1, 0}, {1, 1, 0},
};

polyscope::SparseVolumeGrid* psGrid = polyscope::registerSparseVolumeGrid(
        "sample sparse grid", origin, cellWidth, occupiedCells);

// === Cell scalar: one value per occupied cell ===
std::vector<float> cellScalars = {0.1f, 0.5f, 0.9f, 0.3f};
psGrid->addCellScalarQuantity("cell scalar", cellScalars);

// === Node scalar: values at node indices ===
// For each cell (i,j,k), its corner nodes are (i+dx, j+dy, k+dz) for dx,dy,dz in {0,1}.
// Collect all unique nodes and provide a value for each.
std::vector<glm::ivec3> nodeIndices = { /* all unique corner nodes */ };
std::vector<float> nodeValues = { /* one value per node index */ };
psGrid->addNodeScalarQuantity("node scalar", nodeIndices, nodeValues);

polyscope::show();
```

### Add cell scalars

???+ func "`#!cpp SparseVolumeGridCellScalarQuantity* SparseVolumeGrid::addCellScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the cells of the grid.

    - `name` the name of the quantity
    - `values` a flat array of scalars, one per occupied cell in the same order as the `occupiedCells` array used at registration. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array.
    - `type` the [data type]([[url.prefix]]/features/data_types) of the scalar (standard, symmetric, magnitude, etc.)


### Add node scalars

???+ func "`#!cpp SparseVolumeGridNodeScalarQuantity* SparseVolumeGrid::addNodeScalarQuantity(std::string name, const TI& nodeIndices, const TV& nodeValues, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the nodes of the grid.

    Node values are passed as paired arrays of node indices and values. For a cell with grid indices `(i, j, k)`, its corner nodes have indices `(i+dx, j+dy, k+dz)` for `dx, dy, dz` in `{0, 1}`. The node indices may be passed in any order, and extra entries (for nodes not required by any occupied cell) are ignored. However, all required node values must be present.

    - `name` the name of the quantity
    - `nodeIndices` an array of `glm::ivec3` node grid indices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `glm::ivec3`.
    - `nodeValues` a flat array of scalar values, one per entry in `nodeIndices`. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array.
    - `type` the [data type]([[url.prefix]]/features/data_types) of the scalar (standard, symmetric, magnitude, etc.)


[[% include 'common/scalar_quantity.md' %]]
