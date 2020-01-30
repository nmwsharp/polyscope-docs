This section demonstrates using Polyscope with [libIGL](https://libigl.github.io/).

See [this repository](https://github.com/nmwsharp/libigl-polyscope-project-template) for a sample project configuration, CMAKE build system, and a quick demo.

Generally, Polyscope's data adaptors work as expected with libIGL! You can simply call Polyscope functions and pass your IGL Eigen matrix types.

### Adding a mesh

Example:
```cpp
// Initialize polyscope
polyscope::init();

// Read a mesh
igl::readOBJ(filename, meshV, meshF);

// Register the mesh with Polyscope
polyscope::registerSurfaceMesh("input mesh", meshV, meshF);

// Show the gui
polyscope::show();
```

#### Adding mesh quantities

Adding a scalar quantity:
```cpp
using namespace Eigen;

// Compute pointwise Gaussian curvature
VectorXd K;
igl::gaussian_curvature(meshV, meshF, K);
SparseMatrix<double> M, Minv;
igl::massmatrix(meshV, meshF, igl::MASSMATRIX_TYPE_DEFAULT, M);
igl::invert_diag(M, Minv);
K = (Minv * K).eval();

// Add for visualization in Polyscope
polyscope::getSurfaceMesh("input mesh")->addVertexScalarQuantity("gaussian curvature", K);
```

Adding a vector quantity:
```cpp

// Compute vertex normals
Eigen::MatrixXd N_vertices;
igl::per_vertex_normals(meshV, meshF, N_vertices);

// Add them for visualization in Polyscope
polyscope::getSurfaceMesh("input mesh")
  ->addVertexVectorQuantity("libIGL vertex normals", N_vertices);
```
