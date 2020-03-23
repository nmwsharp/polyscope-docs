![Polyscope](../media/teaser.svg)
Polyscope is a C++/Python viewer and user interface for the rapid prototyping and debugging of geometric algorithms in 3D geometry processing, scientific computing, and computer graphics/vision. The lofty objective of Polyscope is to offer a useful visual interface to your data via a single line of code.

Polyscope uses a paradigm of *structures* and *quantities*. A **structure** is a geometric object in the scene, such as a surface mesh or point cloud. A **quantity** is data associated with a structure, such as a scalar function or a vector field.

When any of these structures and quantities are registered, Polyscope displays them in an interactive 3D scene, handling boilerplate concerns such as toggling the display of various data, colormapping data and editing maps, providing "picking" support to click in the scene and display numerical quantities, and generating histograms of scalar values.


!!! error "Python bindings are in beta"

    The python API for polyscope is new, and should considered experimental. It may be broken, and it may change without warning!

    Not all features of the C++ library are exposed in Python; they are being added incrementally.

A simple workflow for visualizing data in Polyscope looks like:
``` python
import polyscope as ps
ps.init()

### Register a point cloud
my_points = # your points, a Nx3 numpy array
ps_cloud = ps.register_point_cloud("my points", my_points)

# Also show a vector field defined at points
point_vecs = # vectors, a Nx3 numpy array with a vector per-point
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
