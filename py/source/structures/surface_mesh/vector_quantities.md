Visualize vector-valued data at the elements of a surface mesh.

![face_vector_demo](../../media/face_vectors_demo.png)

Example:
```python
import numpy as np
import polyscope as ps
ps.init()

# register a surface mesh
N_vert = 100
N_face = 250
vertices = np.random.rand(N_vert, 3) # (V,3) vertex position array
faces = np.random.randint(0, N_vert, size=(N_face,3)) # (F,3) array of indices 
                                                      # for triangular faces

ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)

# visualize some random vectors per vertex
vecs_vert = np.random.rand(N_vert, 3)
ps_mesh.add_vector_quantity("rand vecs", vecs_vert, enabled=True)

# set radius/length/color of the vectors
ps_mesh.add_vector_quantity("rand vecs opt", vecs_vert, radius=0.001, 
                            length=0.005, color=(0.2, 0.5, 0.5))

# ambient vectors don't get auto-scaled, useful e.g. when representing offsets in 3D space
ps_mesh.add_vector_quantity("vecs ambient", vecs_vert, vectortype='ambient')

# view the mesh with all of these quantities
ps.show() 
```

???+ func "`#!python SurfaceMesh.add_vector_quantity(name, values, defined_on='vertices', enabled=None, vectortype="standard", length=None, radius=None, color=None)`"

    Add a vector quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, vectors at vertices/faces (or `Nx2` for 2D data)
    - `defined_on` string, one of `vertices` or `faces`, is this data a vector per-vertex or a vector per-face?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.


### Tangent vectors

_Tangent_ vectors lie flat against the surface of the mesh. They are expressed as 2D vectors with X-Y coordinates in some basis frame at each mesh element.


#### Specifying the tangent basis

Tangent vectors are defined with respect to a coordinate frame at each vertex (resp., face). Before adding any tangent vector quantities, you probably need to tell Polyscope what this coordinate frame looks like. To do so, pass an array of the x-axis vectors (in 3D) for each mesh element.

??? func "`#!python SurfaceMesh.set_vertex_tangent_basisX(vectors)`"

    Specify the tangent coordinate system at vertices, by giving the direction of the x-axis of the basis.

    - `vectors` is an `Vx3` (or `Vx2` for 2D) array of one 3D vector at each vertex, giving the direction of the x-axis of the basis. The rest of the basis will be computed from the normal.

??? func "`#!python SurfaceMesh.set_face_tangent_basisX(vectors)`"

    Specify the tangent coordinate system at faces, by giving the direction of the x-axis of the basis.

    - `vectors` is an `Fx3` (or `Fx2` for 2D) array of one 3D vector at each face, giving the direction of the x-axis of the basis. The rest of the basis will be computed from the normal.


#### Adding intrinsic tangent vectors

In these function names, _intrinsic vector_ is a fancy synonym for tangent vector, which indicates that the vectors lie in the surface itself, not the containing 3D space.

???+ func "`#!python SurfaceMesh.add_intrinsic_vector_quantity(name, values, n_sym=1, defined_on='vertices', enabled=None, vectortype="standard", length=None, radius=None, color=None, ribbon=None)`"

    Add a vector quantity to the mesh. Remember to specify your tangent basis first!

    - `name` string, a name for the quantity
    - `values` an `Nx2` numpy array, of tangent vectors at vertices/faces
    - `n_sym` is a symmetry order for visualizing line fields (n = 2) and cross fields (n = 4), etc. If it is set to a non-`1` value, n distinct vectors will be displayed at each element. This function presumes a "power"-representation for symmetric fields, which the inputs result from raising symmetric vectors to the n'th power.
    - `defined_on` string, one of `vertices` or `faces`, is this data a vector per-vertex or a vector per-face?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    

### One forms

_One forms_ are tangent vector-like quantities represented as integrated scalars along edges. They commonly arise, for example, as a gradient which is difference of scalar values at vertices.


???+ func "`#!python SurfaceMesh.add_one_form_vector_quantity(name, values, orientations, enabled=None, length=None, radius=None, color=None, ribbon=None)`"

    Add a one-form vector quantity to the mesh.  Remember, before passing edge-valued data, be sure your [indexing convention](../indexing_convention) matches what Polyscope expects.

    - `name` string, a name for the quantity
    - `values` a length `n_edges` numpy float array, integrated 1-form values at edges
    - `orientations` a length `n_edges` numpy boolean array. 1-forms are defined with respect to an orientation of edges, so you need to tell Polyscope which direction your edges point in. These booleans should be `true` if the edge points from the lower indexed adjacent vertex to the higher-indexed vertex, and false otherwise.
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
   

{!common/vector_quantity.md!}
