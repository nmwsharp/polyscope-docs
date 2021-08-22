Visualize color rgb-valued data at the elements of a volume mesh.

![volume mesh color values]({{url.prefix}}/media/volume_color.jpg)

**Example**: showing a color value at cells (here randomly generated data)
```cpp
/* ... initialization, create mesh ... */ 

// Register the volume mesh with Polyscope
polyscope::registerTetMesh("my mesh", verts, tets);

// Add a color quantity
size_t nCells = tets.rows();
std::vector<std::array<double, 3>> randColor(nCells);
for (size_t i = 0; i < nCells; i++) {
  // generate random colors 
  randColor[i] = {{polyscope::randomUnit(), polyscope::randomUnit(), polyscope::randomUnit()}};
}
polyscope::getVolumeMesh("my mesh")->addCellColorQuantity("random color", randColor);

// Show the GUI
polyscope::show();
```

### Add colors to elements

???+ func "`#!cpp VolumeMesh::addVertexColorQuantity(std::string name, const T& data)`"

    Add a color quantity defined at the vertices of the mesh.

    - `data` is the array of colors at vertices. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a 3-vector array of `float`s. The length should be the number of vertices in the mesh.

    RGB values are interpreted in the range `[0,1]`.

??? func "`#!cpp VolumeMesh::addCellColorQuantity(std::string name, const T& data)`"

    Add a color quantity defined at the faces of the mesh.

    - `data` is the array of colors at faces. The type should be [adaptable]({{url.prefix}}/data_adaptors) to a 3-vector array of `float`s. The length should be the number of cells (tets, hexes, etc) in the mesh.

    RGB values are interpreted in the range `[0,1]`.


### Options

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]({{url.prefix}}/basics/parameters/#persistent-values)

_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

