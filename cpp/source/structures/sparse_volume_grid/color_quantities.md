Visualize color data at the nodes or cells of a sparse volume grid.

![sparse volume grid color quantity]([[url.prefix]]/media/sparse_volume_color_quantity.jpg)


**Example:** adding color quantities to a sparse volume grid
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

// === Cell color: one RGB color per occupied cell ===
std::vector<glm::vec3> cellColors = {
    {1.f, 0.f, 0.f}, {0.f, 1.f, 0.f}, {0.f, 0.f, 1.f}, {1.f, 1.f, 0.f},
};
psGrid->addCellColorQuantity("cell color", cellColors);

// === Node color: colors at node indices ===
std::vector<glm::ivec3> nodeIndices = { /* all unique corner nodes */ };
std::vector<glm::vec3> nodeColors = { /* one RGB color per node index */ };
psGrid->addNodeColorQuantity("node color", nodeIndices, nodeColors);

polyscope::show();
```

### Add cell colors

???+ func "`#!cpp SparseVolumeGridCellColorQuantity* SparseVolumeGrid::addCellColorQuantity(std::string name, const T& colors)`"

    Add a color quantity defined at the cells of the grid.

    - `name` the name of the quantity
    - `colors` an array of RGB colors, one per occupied cell in the same order as the `occupiedCells` array used at registration. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `glm::vec3`. Colors are RGB floats in `[0, 1]`.


### Add node colors

???+ func "`#!cpp SparseVolumeGridNodeColorQuantity* SparseVolumeGrid::addNodeColorQuantity(std::string name, const TI& nodeIndices, const TC& nodeColors)`"

    Add a color quantity defined at the nodes of the grid.

    Node colors are passed as paired arrays of node indices and colors. For a cell with grid indices `(i, j, k)`, its corner nodes have indices `(i+dx, j+dy, k+dz)` for `dx, dy, dz` in `{0, 1}`. The node indices may be passed in any order, and extra entries (for nodes not required by any occupied cell) are ignored. However, all required node values must be present.

    - `name` the name of the quantity
    - `nodeIndices` an array of `glm::ivec3` node grid indices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `glm::ivec3`.
    - `nodeColors` an array of RGB colors, one per entry in `nodeIndices`. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `glm::vec3`. Colors are RGB floats in `[0, 1]`.
