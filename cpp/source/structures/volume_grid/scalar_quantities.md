Visualize scalar-valued data at the nodes or cells of a volume grid.

![volume grid node cell values]([[url.prefix]]/media/volume_grid_cell_scalar.jpg)


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

### Add scalars

???+ func "`#!cpp VolumeGridNodeScalarQuantity* VolumeGrid::addNodeScalarQuantity(std::string name, const T& data, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the nodes of the grid.
    
    The data is passed as a flattened vector of length `nodeDimX*nodeDimY*nodeDimZ`, with data layout such that the X values are changing fastest. For example with 3D xyz indexing, the values would be laid out as `[data[0,0,0], data[1,0,0], data[2,0,0], ...]`, etc.

    - `data` is the (flattened) array of scalars at nodes. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array; this includes may common types like `std::vector<float>` and `Eigen::VectorXd`. The length should be the number of nodes in the grid.


??? func "`#!cpp VolumeGridCellScalarQuantity* VolumeMesh::addCellScalarQuantity(std::string name, const T& data, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the cells of the grid.
    
    The data is passed as a flattened vector of length `cellDimX*cellDimY*cellDimZ`, with data layout such that the X values are changing fastest. For example with 3D xyz indexing, the values would be laid out as `[data[0,0,0], data[1,0,0], data[2,0,0], ...]`, etc.

    - `data` is the (flattened) array of scalars at cells. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array; this includes may common types like `std::vector<float>` and `Eigen::VectorXd`. The length should be the number of cells in the grid.


### Add implicit scalars

!!! note "Implicit helpers"

    Implicit helpers offer an easier way to interface your data with Polyscope. You define a callback function which can be called at an xyz coordinate to return a value, and pass that function as input. Polyscope then automatically takes care of calling the function at the appropriate locations to sample the function onto the grid.
    
    See [Implicit Helpers]([[url.prefix]]/features/implicit_helpers) for more details about implicit helpers, and the meaning of _batch_ helpers.


??? func "`#!cpp VolumeGridNodeScalarQuantity* VolumeGrid::addNodeScalarQuantityFromCallable(std::string name, Func&& func, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the nodes of the grid, sampling automatically via a callable function.
    
    - `func` is a function which takes a single `glm::vec3` world-space position as input, and returns the scalar value at that point

??? func "`#!cpp VolumeGridCellScalarQuantity* VolumeGrid::addCellScalarQuantityFromCallable(std::string name, Func&& func, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the cells of the grid, sampling automatically via a callable function.
    
    - `func` is a function which takes a single `glm::vec3` world-space position as input, and returns the scalar value at that point

??? func "`#!cpp VolumeGridNodeScalarQuantity* VolumeGrid::addNodeScalarQuantityFromBatchCallable(std::string name, Func&& func, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the nodes of the grid, sampling automatically via a callable function.
    
    - `func` is a function which performs a batch of evaluations of the implicit function. It should have a signature like `void(float* in_pos_ptr, float* out_val_ptr, size_t N)`. The first arg is a length-3N array of positions for queries, and the second is an (already-allocated) length-N output array of floats to write the result to. The last arg is the numbrer of queries `N`.

??? func "`#!cpp VolumeGridCellScalarQuantity* VolumeGrid::addCellScalarQuantityFromBatchCallable(std::string name, Func&& func, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the cells of the grid, sampling automatically via a callable function.
    
    - `func` is a function which performs a batch of evaluations of the implicit function. It should have a signature like `void(float* in_pos_ptr, float* out_val_ptr, size_t N)`. The first arg is a length-3N array of positions for queries, and the second is an (already-allocated) length-N output array of floats to write the result to. The last arg is the numbrer of queries `N`.

{!common/scalar_quantity.md!}

### Visualizing Isosurfaces

For a scalar values at nodes, we can additionally extract isosurfaces (aka levelsets) via the marching cubes algorithm, and visualize them as surface meshes.

![volume grid node scalar values]([[url.prefix]]/media/volume_grid_node_scalar.jpg)

**Example:** visualizing scalar isosurfaces
```cpp

/* continued after `scalarQ` has been added as in the first example above */

scalarQ->setGridcubeVizEnabled(false); // hide the default grid viz
scalarQ->setIsosurfaceLevel(0.5); // set which isosurface we will visualize
scalarQ->setIsosurfaceVizEnabled(true); // extracts the isosurface
polyscope::show();

// add a slice plane to cut through the grid while leaving the isosurface
// untouched, as in the screenshot above
scalarQ->setGridcubeVizEnabled(true);
polyscope::SlicePlane* p = polyscope::addSceneSlicePlane();
scalarQ->setSlicePlanesAffectIsosurface(false); 
polyscope::show();

// extract the isosurface as its own mesh structure
scalarQ->registerIsosurfaceAsMesh("my isosurface mesh");
```


The following settings on the `VolumeGridNodeScalarQuantity` class affect the behavior of isosurfaces. 

!!! note 

    By default, the grid obscures the isosurface so it cannot be seen. You probably want to either:

    - use a slice plane, along with the `setSlicePlanesAffectIsosurface(false)` option, or
    - use `setGridcubeVizEnabled(false)` to disable the default grid visualization

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the isosurface enabled | `#!cpp bool getIsosurfaceVizEnabled()` | `#!cpp setIsosurfaceVizEnabled(bool)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
level | at what value to extract the isosurface (default: 0) | `#!cpp float getIsosurfaceLevel()` | `#!cpp setIsosurfaceLevel(float)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
color | the color of the isosurface mesh | `#!cpp glm::vec3 getIsosurfaceColor()` | `#!cpp setIsosurfaceColor(glm::vec3)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
slice planes affect | do slice planes affect the isosurface | `#!cpp bool getSlicePlanesAffectIsosurface()` | `#!cpp setSlicePlanesAffectIsosurface(bool)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
gridcube viz enabled | are the usual gridcubes rendered | `#!cpp bool getGridcubeVizEnabled()` | `#!cpp setGridcubeVizEnabled(bool)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)

You can also register the isosurface as its own Polyscope surface mesh structure for further visualization.

??? func "`#!cpp SurfaceMesh* VolumeGridNodeScalarQuantity::registerIsosurfaceAsMesh(std::string structureName = "")`"

    Extract the scalar function isosurface as described above, and register it as its own new `SurfaceMesh` structure.

    ` `structureName` is the name of the newly created structure. If not given, a default name will be automatically generated.

