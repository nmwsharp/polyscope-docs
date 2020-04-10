![Polyscope](/media/teaser.svg)

![GitHub](https://img.shields.io/github/license/nmwsharp/polyscope?style=flat-square)
![Travis (.com)](https://img.shields.io/travis/com/nmwsharp/polyscope?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/nmwsharp/polyscope?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/polyscope?style=flat-square)

Polyscope is a C++ & Python viewer and user interface for 3D data like meshes and point clouds. Scientists, engineers, artists, and hackers can use Polyscope to prototype and debug algorithms---it is designed to easily integrate with existing codebases and popular libraries.  The lofty objective of Polyscope is to offer a useful visual interface to your data via a single line of code.

Polyscope uses a paradigm of *structures* and *quantities*. A **structure** is a geometric object in the scene, such as a surface mesh or point cloud. A **quantity** is data associated with a structure, such as a scalar function or a vector field.

When any of these structures and quantities are registered, Polyscope displays them in an interactive 3D scene, handling boilerplate concerns such as toggling visibility, color-mapping data and adjusting maps, "picking" to click in the scene and query numerical quantities, etc.

There are two variants of this documentation site, for C++ and Python. Use the buttons on the top bar to toggle between them.

A simple workflow for visualizing data in Polyscope looks like:

=== "C++"
    ``` C++
    #include "polyscope/polyscope.h"
    #include "polyscope/surface_mesh.h"

    // Initialize polyscope
    polyscope::init();

    // Register a surface mesh structure
    polyscope::registerSurfaceMesh("my mesh", mesh.vertices, mesh.faces);

    // Add a scalar and a vector function to the mesh
    polyscope::getSurfaceMesh("my mesh")->addVertexScalarQuantity("my_scalar", scalarQuantity);
    polyscope::getSurfaceMesh("my mesh")->addFaceVectorQuantity("my_vector", vectorQuantity);

    // Show the gui
    polyscope::show();
    ```

=== "Python"
    ``` python
    import polyscope as ps
    ps.init()

    ### Register a point cloud
    my_points = # your points, a Nx3 numpy array
    ps_cloud = ps.register_point_cloud("my points", my_points)

    # Also show a vector field defined at points
    point_vecs = # vectors, a Nx3 numpy array representing a vector per-point
    ps_cloud.add_vector_quantity("vecs", point_vecs, color=(0.2, 0.5, 0.5))


    ### Register a mesh
    verts = # a Nx3 numpy array of vertex positions
    faces = # a Fx3 array of indices, or a nested list
    ps.register_surface_mesh("my mesh", verts, faces, smooth_shade=True)

    # Also show a color mapped, scalar function
    face_vals = # a length n_faces numpy array, with a value per-face
    ps.get_surface_mesh("my mesh").add_scalar_quantity("some vals", 
            face_vals, defined_on='faces', cmap='blues')

    # View the point cloud and mesh we just registered in the 3D UI
    ps.show()
    ```

Polyscope is designed to make your life easier. It is simple to build, and fewer than 10 lines of code should be sufficient to start visualizing. In C++, some [template magic](../data_adaptors), means Polyscope can probably accept the data types you're already using!

---
Author: [Nicholas Sharp](http://www.nmwsharp.com)

If Polyscope contributes to an academic publication, cite it as:
```bib
@misc{polyscope,
  title = {Polyscope},
  author = {Nicholas Sharp and the Polyscope contributors},
  note = {www.polyscope.run},
  year = {2019}
}
```

Development of this software was funded in part by NSF Award 1717320, an NSF graduate research fellowship, and gifts from Adobe Research and Autodesk, Inc.
# 
<!--^^^ that pound is of immeasurable importance, it hides the top level title-->
