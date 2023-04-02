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


### Inspecting with slice planes

Slice planes have [special functionality]([[url.prefix]]/features/slice_planes/#inspecting-volume-meshes) for volume mesh vertex values---they can _inspect_ quantities on volume meshes and render them on the interior of the volume. See the slice plane documentation for details.


{!common/scalar_quantity.md!}
