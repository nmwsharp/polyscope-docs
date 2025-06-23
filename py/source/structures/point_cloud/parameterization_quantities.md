A _parameterization_ is a set of 2D coordinates associated with a surface, often referred to as "UV coordinates". 

Typically parameterizations are used on meshes (which is also supported in Polyscope!) but at times it may be useful to visualize a parameterization at the points of a point cloud.


## Adding


???+ func "`#!python PointCloud.add_parameterization_quantity(name, values, coords_type='unit', enabled=None, viz_style=None, grid_colors=None, checker_colors=None, checker_size=None, cmap=None)`"

    Add a parameterization quantity to the mesh.

    - `name` string, a name for the quantity
    - `values` an `Nx2` numpy array, coordinates at vertices/corners
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    


[[% include 'common/parameterization_quantity.md' %]]

