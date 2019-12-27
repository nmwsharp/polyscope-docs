This section demonstrates using Polyscope with [DGtal](https://dgtal.org/) for digital geometry processing. See [this repository](https://github.com/dcoeurjo/polyscope-dgtal) for a sample project configuration, CMAKE build system, and a quick demo!

### Adding a surface

These snippets are from the example [here](https://github.com/dcoeurjo/polyscope-dgtal/blob/master/simpleTest.cpp). See that code for full setup and template definitions!
```cpp
// Initialize polyscope
polyscope::init();

// ... surface setup here, see full example...
// create the surface
auto primalSurface = SH3::makePrimalPolygonalSurface(c2i, surface);

// Convert faces to appropriate indexed format
std::vector<std::vector<unsigned long>> faces;
for(auto &face: primalSurface->allFaces())
  faces.push_back(primalSurface->verticesAroundFace( face ));

// Register pointels as a point cloud
polyscope::registerPointCloud("Pointels", primalSurface->positions());

// Register surface with quadrilateral faces
auto digsurf = polyscope::registerSurfaceMesh("Primal surface", 
                 primalSurface->positions(), faces);

// Set appearance parameters
digsurf->edgeWidth=1.0;
digsurf->edgeColor={1.,1.,1.};

// Show the gui
polyscope::show();
```

The resulting surface:

![DGtal surface](/media/dgtal_surface.jpg)

### Computing surface quantities

```cpp
// Compute some differential quantities
params("r-radius", 5.0);
auto normals   = SHG3::getCTrivialNormalVectors(surface, surfels, params);
auto normalsTrivial   = SHG3::getTrivialNormalVectors(K,surfels);
auto normalsII = SHG3::getIINormalVectors(binary_image, surfels, params);
auto Mcurv     = SHG3::getIIMeanCurvatures(binary_image, surfels, params);
auto Gcurv     = SHG3::getIIGaussianCurvatures(binary_image, surfels, params);

// Surfel area measure
std::vector<double> areaMeasure(surfels.size());
for(auto i=0; i < areaMeasure.size(); ++i)
  areaMeasure[i] = normalsTrivial[i].dot(normalsII[i]);
 

// Add quantities for visualization 
digsurf->addFaceVectorQuantity("Trivial normal vectors", normalsTrivial);
digsurf->addFaceVectorQuantity("CTrivial normal vectors", normals);
digsurf->addFaceVectorQuantity("II normal vectors", normalsII);
digsurf->addFaceScalarQuantity("II mean curvature", Mcurv);
digsurf->addFaceScalarQuantity("II Gaussian curvature", Gcurv);
digsurf->addFaceScalarQuantity("Surfel area measure", areaMeasure);

// Show the gui
polyscope::show();
```

The resulting curvatures:

![DGtal curvature](/media/dgtal_curvature.jpg)

The resulting normal vectors:

![DGtal vectors](/media/dgtal_vectors.jpg)
