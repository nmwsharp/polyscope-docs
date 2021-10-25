Visualize scalar (real or integer)-valued data at the elements of a volume mesh.

![volume mesh scalar values]([[url.prefix]]/media/volume_scalar.jpg)

**Example**: showing a scalar on vertices (here just one of the spatial coordinate functions)
```cpp
/* ... initialization, create mesh ... */ 

// Register the volume mesh with Polyscope
polyscope::registerTetMesh("my mesh", verts, tets);

// Add a scalar quantity
size_t nVerts = verts.rows();
std::vector<double> scalarV(nVerts);
for (size_t i = 0; i < nVerts; i++) {
  // use the x-coordinate of vertex position as a test function
  scalarV[i] = V(i,0);
}
auto scalarQ = polyscope::getVolumeMesh("my mesh")->addVertexScalarQuantity("scalar Q", scalarV);

// Set some options
scalarQ->setEnabled(true);       // initially enabled
scalarQ->setMapRange({-1., 1.}); // colormap from [-1,1]
scalarQ->setColorMap("blues");   // use a blue colormap

// Show the GUI
polyscope::show();
```


### Add scalars to elements


???+ func "`#!cpp VolumeMesh::addVertexScalarQuantity(std::string name, const T& data, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the vertices of the mesh.

    - `data` is the array of scalars at vertices. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array; this includes may common types like `std::vector<float>` and `Eigen::VectorXd`. The length should be the number of vertices in the mesh.


??? func "`#!cpp VolumeMesh::addCellScalarQuantity(std::string name, const T& data, DataType type = DataType::STANDARD)`"

    Add a scalar quantity defined at the cells of the mesh.

    - `data` is the array of scalars, with one value per cell. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array; this includes may common types like `std::vector<float>` and `Eigen::VectorXd`. The length should be the number of cell in the mesh.


### Level sets

When a vertex scalar quantity is attached to a volume mesh, level sets of the vertex data can be rendered by enabling "Level Set" in the settings for the vertex scalar quantity. Show other scalar quantities on this generated geometry by selecting "Show Quantity".


![level set distance]([[url.prefix]]/media/level_set.png)
<b>Example</b>: showing a level set of a vertex scalar quantity which just represents the distance from the mesh's origin, resulting in a sphere with radius equal to the value at the level set.

```cpp
/* ... initialization, create mesh ... */ 
// Add a scalar quantity
size_t nVerts = verts.rows();
std::vector<double> scalarV(nVerts);
for (size_t i = 0; i < nVerts; i++) {
  // use the x-coordinate of vertex position as a test function
  scalarV[i] = abs(V(i,0));
}
auto scalarQ = polyscope::getVolumeMesh("my mesh")->addVertexScalarQuantity("scalar Q", scalarV);

// Add a second scalar quantity which is just distance from origin
std::vector<double> scalarV2(nVerts);
for (size_t i = 0; i < nVerts; i++) {
  // use the x-coordinate of vertex position as a test function
  scalarV2[i] = sqrt(pow(V(i,0), 2) + pow(V(i,1), 2) + pow(V(i,2), 2));
}
auto scalarQ2 = polyscope::getVolumeMesh("my mesh")->addVertexScalarQuantity("scalar Q2", scalarV2);

// Set level set options
scalarQ2->setEnabledLevelSet(true);  
// Sphere of radius 8
scalarQ2->setLevelSetValue(8.0f);  
// Show original scalar on this level set
scalarQ2->setLevelSetVisibleQuantity("scalar Q");  
// set the name of the other scalar quantity 
// to be rendered onto the level set

// Show the GUI
polyscope::show();
```

??? func "`#!cpp VolumeMeshVertexScalarQuantity::setEnabledLevelSet(bool enabled)`"

    Enable or disable level set rendering for a vertex scalar quantity. Enabling level set rendering will disable the normal surface rendering and all other quantities.

??? func "`#!cpp VolumeMeshVertexScalarQuantity::setLevelSetValue(float val)`"

    Set the value of the level set to show.

??? func "`#!cpp VolumeMeshVertexScalarQuantity::setLevelSetVisibleQuantity(std::string name)`"

    Set the secondary scalar quantity to render onto the level set geometry. Only names of vertex scalar quantities on the same volume mesh will work.

### Options

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
color map | the [color map]([[url.prefix]]/features/color_maps) to use | `#!cpp std::string getColorMap()` | `#!cpp setColorMap(std::string newMap)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
map range | the lower and upper limits used when mapping the data in to the color map| `#!cpp std::pair<double,double> getMapRange()` | `#!cpp setMapRange(std::pair<double,double>)` and `#!cpp resetMapRange()`| no

_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

