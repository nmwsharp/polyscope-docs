# Simple Triangle Mesh

`SimpleTriangleMesh` is an alternate minimal-and-efficient structure for displaying triangle meshes. It only supports pure triangle meshes and a limited set of quantities and other features, but it is higher-performance and supports more general updates (including changing the _number_ of vertices and faces without creating a new mesh).

The [Surface Mesh]([[url.prefix]]/structures/surface_mesh/basics/) structure is the primary way to display surface meshes in Polyscope for almost all use cases, and has a much larger feature set. Only use `SimpleTriangleMesh` if you particularly need fast performance, large meshes, or dynamic updates.


**Example:**
```python
import numpy as np
import polyscope as ps
ps.init()

vertices = np.random.rand(100, 3)          # (V,3) float array of vertex positions
faces = np.random.randint(0, 100, (200,3)) # (F,3) int array of triangle indices

# Register the mesh
ps_mesh = ps.register_simple_triangle_mesh("my mesh", vertices, faces)

# Add a scalar quantity at vertices
vals = np.random.rand(100)
ps_mesh.add_scalar_quantity("rand vals", vals, defined_on='vertices', enabled=True)

ps.show()
```


## Registering

???+ func "`#!python register_simple_triangle_mesh(name, vertices, faces)`"

    Add a new simple triangle mesh structure to Polyscope.

    - `name` string, a name for the structure
    - `vertices` an `(V, 3)` numpy float array of vertex positions
    - `faces` an `(F, 3)` numpy integer array of triangle face indices, as 0-based indices into the vertex array

    Only triangle faces are supported.

As with all structures, there are also `get_simple_triangle_mesh(name)`, `has_simple_triangle_mesh(name)`, and `remove_simple_triangle_mesh(name)`.


## Updating

`SimpleTriangleMesh` supports a wider range of updates than the standard `SurfaceMesh`. In particular, it is possible to change the number of vertices and faces on an existing structure without re-registering it.

??? func "`#!python SimpleTriangleMesh.update_vertex_positions(newPositions)`"

    Update the vertex positions. The vertex count and face connectivity must remain the same.

    - `newPositions` an `(V, 3)` numpy float array, with the same number of vertices as the current mesh.

??? func "`#!python SimpleTriangleMesh.update_mesh(vertices, faces)`"

    Update both vertices and faces. Vertex and face counts may change.

    - `vertices` an `(V, 3)` numpy float array of new vertex positions
    - `faces` an `(F, 3)` numpy integer array of new triangle face indices

    Internally the buffers use amortized doubling, so capacity is only reallocated when the new size exceeds the current capacity. Call `reserve_mesh_capacity()` beforehand to avoid reallocations entirely.

??? func "`#!python SimpleTriangleMesh.reserve_mesh_capacity(n_verts, n_faces)`"

    Pre-allocate buffer capacity for at least `n_verts` vertices and `n_faces` faces. Subsequent calls to `update_mesh()` that stay within this capacity will not trigger any memory reallocation.

    This is useful when the mesh size fluctuates but has a known upper bound, and you want to avoid the overhead of reallocating buffers on every update.


## Picking and Selection

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene. [See the section on picking for more info]([[url.prefix]]/basics/interactive_UIs_and_animation/#picking-selection-and-querying-the-scene).

Additional information about a pick which hits the mesh can be retrieved from the `PickResult.structure_data` dictionary, which will contain:

- `element_type` — `"vertex"` or `"face"`
- `index` — integer index of the clicked element

The selectable element types can be restricted with `set_selection_mode(mode)`, where `mode` is one of:

- `"auto"` — vertices and faces are both selectable (default)
- `"vertices_only"` — only vertices are selectable
- `"faces_only"` — only faces are selectable


## Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
color | surface color | `get_color()` | `set_color(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
back face policy | how back faces are rendered | `get_back_face_policy()` | `set_back_face_policy(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
back face color | color used when policy is `"custom"` | `get_back_face_color()` | `set_back_face_color(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
material | material used for shading | `get_material()` | `set_material(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
selection mode | which elements can be picked | `get_selection_mode()` | `set_selection_mode(val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |

The back face policy values are `"identical"`, `"different"` (default), `"custom"`, and `"cull"`. See the [Surface Mesh back face policies]([[url.prefix]]/structures/surface_mesh/basics/#back-face-policies) for details.


---

## Scalar Quantities

Visualize scalar (real-valued) data at the vertices or faces of the mesh.

**Example:**
```python
ps_mesh = ps.register_simple_triangle_mesh("my mesh", vertices, faces)

# vertex scalar (default)
vals_v = np.random.rand(ps_mesh.n_vertices())
q = ps_mesh.add_scalar_quantity("vert scalar", vals_v, defined_on='vertices', enabled=True)

# face scalar
vals_f = np.random.rand(ps_mesh.n_faces())
ps_mesh.add_scalar_quantity("face scalar", vals_f, defined_on='faces')
```

???+ func "`#!python SimpleTriangleMesh.add_scalar_quantity(name, values, defined_on='vertices', datatype='standard', enabled=None, vminmax=None, cmap=None)`"

    Add a scalar quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` a length `N` numpy float array of scalar values
    - `defined_on` one of `'vertices'` or `'faces'`
    - `datatype` one of `'standard'`, `'symmetric'`, `'magnitude'`; see [scalar quantities]([[url.prefix]]/features/scalar_quantities) for details

    This function also accepts optional keyword arguments to customize appearance and behavior.

    Returns the quantity object, which can be used to call `update_data()`.

### Updating Scalar Data

Scalar quantity values can be updated in-place without removing and re-adding the quantity. The new data must have the same count as the original.

??? func "`#!python SimpleTriangleMeshVertexScalarQuantity.update_data(values)`"

    Update the scalar values for a vertex scalar quantity. `values` must have the same length as the current vertex count.

??? func "`#!python SimpleTriangleMeshFaceScalarQuantity.update_data(values)`"

    Update the scalar values for a face scalar quantity. `values` must have the same length as the current face count.

[[% include 'common/scalar_quantity.md' %]]


---

## Color Quantities

Visualize RGB color data at the vertices or faces of the mesh. Colors are specified as `(N, 3)` float arrays with values in `[0, 1]`.

**Example:**
```python
ps_mesh = ps.register_simple_triangle_mesh("my mesh", vertices, faces)

# vertex color (default)
cols_v = np.random.rand(ps_mesh.n_vertices(), 3)
q = ps_mesh.add_color_quantity("vert color", cols_v, defined_on='vertices', enabled=True)

# face color
cols_f = np.random.rand(ps_mesh.n_faces(), 3)
ps_mesh.add_color_quantity("face color", cols_f, defined_on='faces')
```

???+ func "`#!python SimpleTriangleMesh.add_color_quantity(name, values, defined_on='vertices', enabled=None)`"

    Add an RGB color quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `(N, 3)` numpy float array of RGB colors in `[0, 1]`
    - `defined_on` one of `'vertices'` or `'faces'`

    Returns the quantity object, which can be used to call `update_data()`.

### Updating Color Data

Color quantity values can be updated in-place without removing and re-adding the quantity. The new data must have the same count as the original.

??? func "`#!python SimpleTriangleMeshVertexColorQuantity.update_data(values)`"

    Update the color values for a vertex color quantity. `values` must have shape `(V, 3)` matching the current vertex count.

??? func "`#!python SimpleTriangleMeshFaceColorQuantity.update_data(values)`"

    Update the color values for a face color quantity. `values` must have shape `(F, 3)` matching the current face count.

[[% include 'common/color_quantity.md' %]]
