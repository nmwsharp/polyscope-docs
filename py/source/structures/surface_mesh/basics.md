# Surface Meshes

Surface meshes are one of the core structures in Polyscope. In addition to simply displaying the mesh, Polyscope can show any number of scalar, vector,color, and other kinds of quantities associated with the vertices/faces/etc of the mesh.

Polyscope does not impose any requirements on the meshes visualized. They may be polygonal or nonmanifold, and all faces need not have the same degree.  As always, try clicking on the vertices or faces of a mesh see the data associated with that mesh element.

![surface_mesh_demo](../../media/mesh_demo.gif)

### Registering a surface mesh

Example: registering a mesh
```python
import numpy as np
import polyscope as ps
ps.init()

vertices = np.random.rand(100, 3) # (V,3) vertex position array
faces = np.random.randint(0, 100, size=(250,3)) # (F,3) array of indices 
                                                # for triangular faces

# visualize!
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)
ps.show()
```

Surface meshes are registered with Polyscope by passing the location of each vertex in the mesh, as well as the vertex indices for each face.


???+ func "`#!python register_surface_mesh(name, vertices, faces, enabled=None, color=None, edge_color=None, smooth_shade=None, edge_width=None, material=None)`"

    Add a new surface mesh structure to Polyscope.

    - `name` string, a name for the structure
    - `vertices`, an `Nx3` numpy float array of vertex locations (or `Nx2` for 2D)
    - `faces`, an `FxD` numpy integer array of faces, as 0-based indices in to the vertices array, OR a plain python list-of-lists of indices (or really, anything twice-iterable which yields integers). The latter option enables meshes where not all faces have the same degree.

    Additional optional keyword arguments:

    - `enabled` boolean, is the structure enabled initially
    - `color` float 3-tuple, default color values for the mesh as rgb in [0,1]
    - `edge_color` float 3-tuple, default color values for edges of the mesh as rgb in [0,1] (be sure to set `edge_width` too)
    - `edge_width` float, width of edges in rendered mesh; default sets `0` to disable edges, `1` is a reasonable value to enable
    - `smooth_shade` boolean, if `True` use smooth shading (default: `False` for flat shading)
    - `material` string, name of material to use for the mesh

    if not specified, these optional parameters will assume a reasonable default value, or a [persistant value](../../../basics/parameters/#persistent-values) if previously set.
    
    2D vertex positions are also supported, see [2D data](../../../features/2D_data).

---

!!! warning "Element ordering"

    Polyscope quantities are ordered arrays of data, but not everyone can agree on the ordering of elements in a mesh. See [indexing conventions](../indexing_convention/).

    The default ordering is probably the same as yours for data on **vertices, faces, and corners**. However, data on **edges and halfedges** is much more likely to require setting an ordering.


### Updating a mesh

The locations of the vertices in a mesh can be updated with the member function `update_vertex_positions(newPositions)`. All quantities will be preserved. Changing the connectivity or element counts in a mesh is not supported, you will need to register a new mesh (perhaps with the same name to overwrite).

??? func "`#!python SurfaceMesh.update_vertex_positions(newPos)`"

    Update the vertex positions in a surface mesh structure. `newPos` must be valid input as to initially construct the vertex positions, with the same number of vertices.

### Back face policies

The faces of a mesh are implicitly given an outward orientation by the order in which the vertices are listed. The standard convention, which Polyscope respects, is that a counter-clockwise ordering of vertices defines the "outward" direction. Faces which are viewed from behind are referred to as _back faces_; they can arise when a surface is viewed from the inside, or if a mesh is not properly oriented. Polyscope offers several options for how backfaces are displayed.

![backface policies diagram](../../media/backface_diagram.png)

- `identical` all faces are always rendered identically, whether viewed from the front or back
- `different` backfaces are shaded differently, so they can be distinguished (this is the default)
- `cull` backfaces are culled, and not rendered at all

The choice of these policies can be set as an option for each surface mesh structure, either in the GUI via `[Options] -> [Back Face Policy]` or programmatically with the function below or when a mesh is registered.

??? func "`#!python SurfaceMesh.set_back_face_policy(val)`"

    Set the policy for rendering oppositely-oriented backfaces.

    - `newPolicy` is string giving the new policy, one of `identical`, `different`, or `cull` as described above

    You can also set `back_face_policy='cull'` when registering a mesh.

    There is also a corresponding `SurfaceMesh.get_back_face_policy()`.


### Options


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the structure enabled? | `#!python bool is_enabled()` | `#!python set_enabled(newVal)` | [yes](../../../basics/parameters/#persistent-values)
surface color | the color of the mesh | `#!python get_color()` | `#!python set_color(val)` | [yes](../../../basics/parameters/#persistent-values)
edge color | the color of the edges of the mesh | `#!python get_edge_color()` | `#!python set_edge_color(val)` | [yes](../../../basics/parameters/#persistent-values)
edge width | how thick to draw mesh edges, use `0.` to disable and `1.` for reasonable edges | `#!python get_edge_width()` | `#!python set_edge_width(val)` | [yes](../../../basics/parameters/#persistent-values)
shade smooth | use smooth shading along faces or simple flat faces | `#!python get_smoooth_shade()` | `#!python set_smooth_shade(isSmooth)` | [yes](../../../basics/parameters/#persistent-values)
material | material for structure | `#!python get_material()` | `#!python set_material(newVal)` | [yes](../../../basics/parameters/#persistent-values) |
back face policy | what [back face policy](#back-face-policies) to use | `#!python get_back_face_policy()` | `#!python set_back_face_policy(val)` | [yes](/basics/parameters/#persistent-values) |

Example: set options which affect the appearance of the mesh
```python
import numpy as np
import polyscope as ps

vertices = np.random.rand(100, 3) # (V,3) vertex position array
faces = np.random.randint(0, 100, size=(250,3)) # (F,3) array of indices 
                                                # for triangular faces
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)

ps_mesh.set_enabled(False) # disable
ps_mesh.set_enabled() # default is true

ps_mesh.set_color((0.3, 0.6, 0.8)) # rgb triple on [0,1]
ps_mesh.set_edge_color((0.8, 0.8, 0.8)) 
ps_mesh.set_edge_width(1.0)
ps_mesh.set_smooth_shade(True)
ps_mesh.set_material("candy")

# alternately:
ps.register_surface_mesh("my mesh2", vertices, faces, enabled=False, 
                         color=(1., 0., 0.), edge_color=((0.8, 0.8, 0.8)),
                         edge_width=1.0, smooth_shade=True,
                         material='candy')
```
