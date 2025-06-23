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

_Tangent_ vectors lie flat against the surface of a mesh. They are defined as 2D vector in a local 2D coordinate system at each vertex or face. We need to specify the vector itself as well as the basis vectors for the local coordinate systems.

???+ func "`#!python SurfaceMesh.add_tangent_vector_quantity(name, values, basisX, basisY, defined_on='vertices', n_sym=1, enabled=None, vectortype="standard", length=None, radius=None, color=None, ribbon=None)`"

    Add a vector quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `Nx2` numpy array, of tangent vectors at vertices/faces
    - `basisX` an `Nx3` numpy array, giving the X component of the local basis at each vertex/face
    - `basisY` an `Nx3` numpy array, giving the Y component of the local basis at each vertex/face
    - `defined_on` string, one of `vertices` or `faces`, is this data a vector per-vertex or a vector per-face?
    - `n_sym` is a symmetry order for visualizing line fields (n = 2) and cross fields (n = 4), etc. If it is set to a non-`1` value, n distinct vectors will be displayed at each element, by rotating the input vector 2*PI/nSym radians.
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    

### One forms

_One forms_ are tangent vector-like quantities represented as integrated scalars along edges. They commonly arise, for example, as a gradient which is difference of scalar values at vertices.


???+ func "`#!python SurfaceMesh.add_one_form_vector_quantity(name, values, orientations, enabled=None, length=None, radius=None, color=None, ribbon=None)`"

    Add a one-form vector quantity to the mesh.  Remember, before passing edge-valued data, set the [indexing convention](../indexing_convention) Polyscope.

    - `name` string, a name for the quantity
    - `values` a length `n_edges` numpy float array, integrated 1-form values at edges
    - `orientations` a length `n_edges` numpy boolean array. 1-forms are defined with respect to an orientation of edges, so you need to tell Polyscope which direction your edges point in. These booleans should be `true` if the edge points from the lower indexed adjacent vertex to the higher-indexed vertex, and false otherwise.
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
   

[[% include 'common/vector_quantity.md' %]]
