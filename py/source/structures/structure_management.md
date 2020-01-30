## Intro

A **structure** is a geometric object visualized in Polyscope, like a mesh or a point cloud. The first step in seeing your data in Polyscope is to register one or more structures to add them to the visualization. Then, _quantities_ can be added to these structures, like scalar functions, colors, or vector fields.

Each structure should be given a name which is unique among structures of that type. You can then use this name as a handle to perform operations on the structure; For instance, you can register a mesh with:
```python
ps.register_surface_mesh("my mesh", vertices, faces)
```
Then, in a distant part of your code, add a scalar function to it with:
```python
ps.get_surface_mesh("my mesh").add_scalar_quantity("some values", values)
```
This avoids the need to pass a reference to the structure you created around your entire codebase. Alternately, one can directly use the handle returned by `register_surface_mesh()`, instead of keying on a name string.

The following structures available in Polyscope. Many more structures are in development!

- [Surface Mesh](../surface_mesh/basics)
- [Point Cloud](../point_cloud/basics)
- [Curve Network](../curve_network/basics)
- _in progress_: Camera View
- _in progress_: Tet Mesh


## Registering structures

Each structure offers a `register___(name, ...)` function (like `register_point_cloud()`) which accepts the name of the structure and the data necessary to construct it. These functions will return a structure object which may be used to add quantities to the structure. See the relevant sections for documentation on each of these register functions.

## Accessing structures

Polyscope offers two patterns for calling methods on a registered structure: you can either use the handle returned after structure creation, or refer to the structure by name.

```python
import polyscope as ps

# register a structure
ps_mesh = polyscope.register_surface_mesh("my mesh", vertices, faces)

# access with the handle
ps_mesh.add_scalar_quantity("some values", values)

# access by name
ps.get_surface_mesh("my mesh").add_scalar_quantity("some values", values)
```
The former is concise and programmatic, while the latter avoids the need to keep track of a variable.

As before, each structure offers a `get___(name)` method, like `get_surface_mesh(name)` which can be used to get a handle to the structure of that type by name.


## Removing structures

If no longer needed, structures can be removed by name or by handle. Removing a structure frees memory for the underlying objects, invalidating all references to the structure and its quantities.

```python
import polyscope as ps

# register a structure and some data
ps_mesh = polyscope.register_surface_mesh("my mesh", vertices, faces)
ps_mesh.add_scalar_quantity("some values", values)

# look at it
ps.show()
# (user exits ui)


# remove the structure
# (these two forms are equivalent, choose one) 
ps_mesh.remove()
ps.remove_surface_mesh("my_mesh")


# actually, just remove everything
ps.remove_all_structures()
```
