Visualize scalar-valued data at the nodes or cells of a volume grid.

![volume grid node cell values]([[url.prefix]]/media/volume_grid_cell_scalar.jpg)


**Example:** registering a volume grid and adding a scalar quantity
```python
import polyscope as ps
import numpy as np

ps.init()

# define the resolution and bounds of the grid
dims = (20, 20, 20)
bound_low = (-3., -3., -3.)
bound_high = (3., 3., 3.)

# register the grid
ps_grid = ps.register_volume_grid("sample grid", dims, bound_low, bound_high)

# your dimX*dimY*dimZ buffer of data
scalar_vals = np.zeros(dims[0], dims[1], dims[2]) 

# add a scalar function on the grid
ps_grid.add_scalar_quantity("node scalar", scalar_vals, defined_on='nodes')

# set some scalar options 
ps_grid.add_scalar_quantity("node scalar2", scalar_vals, defined_on='nodes', 
                            vminmax=(-5., 5.), cmap='blues', enabled=True)

ps.show()
```

### Add scalars

???+ func "`#!python VolumeGrid.add_scalar_quantity(name, values, defined_on='nodes', datatype="standard", **scalar_args)`"

    Add a scalar quantity defined at the nodes of the grid.
    
    - `name` string, a name for the quantity
    - `values` a numpy array of shape `(dimX, dimY, dimZ)` giving scalars at nodes/cells. 
    - `defined_on` one of `'nodes', 'cells'`, is this data a value per node or a value per cell?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.


### Add implicit scalars

!!! note "Implicit helpers"

    Implicit helpers offer an easier way to interface your data with Polyscope. You define a callback function which can be called at a batch of xyz coordinates to return a batch of values, and pass that function as input. Polyscope then automatically takes care of calling the function at the appropriate locations to sample the function onto the grid.
    
    See [Implicit Helpers]([[url.prefix]]/features/implicit_helpers) for more details about implicit helpers.


??? func "`#!python VolumeGrid.add_scalar_quantity_from_callable(name, func, defined_on='nodes', datatype="standard", **scalar_args)`"

    Add a scalar quantity defined at the nodes of the grid, sampling automatically via a callable function.
    
    - `func` is a function which performs a batch of evaluations of the implicit function. It should take a `(Q,3)` numpy array of world-space xyz locations at which to evaluate the function where `Q` is the number of queries, and return a `(Q,)` numpy array of results. 

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.

[[% include 'common/scalar_quantity.md' %]]

### Visualizing Isosurfaces

For a scalar values at nodes, we can additionally extract isosurfaces (aka levelsets) via the marching cubes algorithm, and visualize them as surface meshes.

![volume grid node scalar values]([[url.prefix]]/media/volume_grid_node_scalar.jpg)


**Example:** visualizing scalar isosurfaces
```python

# continued after the grid as been set up as in the example above

# draw the isosurfce, hiding the usual grid so it is visible
ps_grid.add_scalar_quantity("node scalar", scalar_vals, defined_on='nodes',
                            enable_isosurface_viz=True, isosurface_level=0.5,
                            isosurface_color=(0.2, 0.1, 0.8),
                            enable_gridcube_viz=False)
ps.show()

# draw the isosurface, using a slice plane to cut through it
ps_grid.add_scalar_quantity("node scalar", scalar_vals, defined_on='nodes',
                            enable_isosurface_viz=True, isosurface_level=0.5,
                            slice_planes_affect_isosurface=False)
ps.add_scene_slice_plane()
ps.show()


# extract the isosurface as its own mesh structure
scalarQ->registerIsosurfaceAsMesh("my isosurface mesh");
ps_grid.add_scalar_quantity("node scalar", scalar_vals, defined_on='nodes',
                            enable_isosurface_viz=True, isosurface_level=0.5,
                            register_isosurface_as_mesh_with_name='isosurface mesh')
```


The following optional arguments to the node scalar quantity adder affect the behavior of isosurfaces. 

!!! note 

    By default, the grid obscures the isosurface so it cannot be seen. You probably want to either:

    - use a slice plane, along with the `slice_planes_affect_isosurface=False` option, or
    - use `enable_gridcube_viz=False` to disable the default grid visualization



  - `enable_gridcube_viz` boolean, is the usual grid cube visualization drawn
  - `enable_isosurface_viz` boolean, should the isosurface be extracted and drawn
  - `isosurface_level` float, which isolevel should be extracted
  - `isosurface_color` 3-tuple of floats, color of the isosurface mesh
  - `slice_planes_affect_isosurface` boolean, do slice planes affect the isosurface
  - `register_isosurface_as_mesh_with_name` string, if given, register the isosurface as a new mesh with this name. Passing `""` generates a default name.

