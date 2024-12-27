Visualize color rgb-valued data at the elements of a surface mesh.

Example:
```python
import numpy as np
import polyscope as ps
ps.init()

N_vert = 100
N_face = 250
vertices = np.random.rand(N_vert, 3) # (V,3) vertex position array
faces = np.random.randint(0, N_vert, size=(N_face,3)) # (F,3) array of indices 
                                                      # for triangular faces

ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)

# visualize some random data per-vertex
colors_vert = np.random.rand(N_vert, 3)
ps_mesh.add_color_quantity("rand colors", colors_vert, enabled=True)

# visualize some random data per-face
colors_face = np.random.rand(N_face, 3)
ps_mesh.add_color_quantity("rand colors2", colors_face, defined_on='faces')

# view the mesh with all of these quantities
ps.show() 
```

### Add Colors to Elements

???+ func "`#!python SurfaceMesh.add_color_quantity(name, values, defined_on='vertices', enabled=None, param_name=None, image_origin="upper_left")`"

    Add a color quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, with rgb [0,1] colors at vertices/faces
    - `defined_on` string, one of `'vertices','faces','texture'`, is this data a color per vertex, per face, or texture image?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    
    The `param_name` and `image_origin` arguments are used only if `defined_on='texture'`. See below for details.


### Color Texture Maps

Texture images define data by storing it an image grid, and using coordinates defined on the face-corners or vertices of a mesh to sample values from the image for each point on the surface.

To visualize color data defined in texture maps, first add a [Parameterization Quantity]([[url.prefix]]/structures/surface_mesh/parameterization_quantities/) (aka UV map) defining the coordinates. Then, add a buffer of image data to be sampled from.

**Example**
```python
import numpy as np
import polyscope as ps

ps.init()

# add a mesh
N_vert = 100
N_face = 250
vertices = np.random.rand(N_vert, 3)
faces = np.random.randint(0, N_vert, size=(N_face,3))
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)

# add a parameterization (aka UV map)
param_vals = np.random.rand(ps_mesh.n_vertices(), 2)
ps_mesh.add_parameterization_quantity("test_param", param_vals, 
                                      defined_on='vertices', enabled=True)
           
# add the texture quantity
dims = (200,300,3)
color_vals = np.random.rand(*dims) # dummy placeholder image data
ps_mesh.add_color_quantity("test_vals", color_vals, 
                           defined_on='texture', param_name="test_param", filter_mode='nearest', enabled=True)

ps.show()
```

Texture image data is added via `add_color_quantity()`, with `defined_on='texture'` and `param_name=...` specifying the name of the [parameterization UV map]([[url.prefix]]/structures/surface_mesh/parameterization_quantities/) with coordinates on `[0,1]` which will be used to sample from the image.
    
The texture image data, dimension, and origin conventions are the same as those used to define [images]([[url.prefix]]/structures/floating_quantities/images/). See there for details.

The filter mode can be set as an additional argument to adjust how values are sampled from the texture. `filter_mode='linear'` (default) will smoothly linearly interpolate values, while `filter_mode='nearest'` will use nearest-neighbor sampling, which can be useful for sharp edges and crisp boundaries.

    
    
{!common/color_quantity.md!}
