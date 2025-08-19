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


## Registering structures

Each structure offers a `register___(name, ...)` function (like `register_point_cloud()`) which accepts the name of the structure and the data necessary to construct it. These functions will return a structure object which may be used to add quantities to the structure. See the relevant sections for documentation on each of these register functions.

## Accessing structures

Polyscope offers two patterns for calling methods on a registered structure: you can either use the handle returned after structure creation, or refer to the structure by name.

```python
import polyscope as ps

# register a structure
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)

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
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)
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

??? func "`#!python remove_all_structures()`"

    Remove all structures from the scene.


## Quantities

Quantities, like scalar functions, color fields, vector fields, and more, can be associated with structures. See the available options for each kind of structure.

Quantities can be removed from a structure by name.


??? func "`#!python Structure.remove_quantity(name, error_if_absent=False)`"

    Remove a quantity from the structure by name.


??? func "`#!python Structure.remove_all_quantities()`"

    Remove all quantities which have been added to the structure.


## Structure options

These basic options are shared by all structures.  Structure options are managed as [persistent values]([[url.prefix]]/basics/parameters/#persistent-values), and thus will persist if a new structure is registered with the same name.


#### Enabled

If a structure is disabled, it will be hidden from view, along with any quantities associated with that structure.

??? func "`#!python Structure.is_enabled()`"

    Is the structure enabled? Returns a boolean.

??? func "`#!python Structure.set_enabled(newVal=True)`"

    Set the structure to be enabled or disabled. Takes a boolean.

    Can also be set when registering, like `register_point_cloud(..., enabled=True)`.


#### Transparency

Set the transparency parameter for the structure. `1` is fully opaque (the default), and `0` is fully transparent. When the first structure has transparency applied, transparent rendering will be automatically enabled.

Transparency can be controlled in the UI via the structure's `[Options] --> [Transparency]` menu.

??? func "`#!python Structure.get_transparency()`"

    Get the transparency parameter for the structure. Returns a float

??? func "`#!python Structure.set_transparency(alpha)`"

    Set the transparency for the structure. Takes a float.
    
    Can also be set when registering, like `register_point_cloud(..., transparency=0.5)`.

#### Transforms

Each structure has an associated spatial _transform_ applied to it for display in the scene. The transform encodes a translation, rotation, and scaling represented as a 4x4 homogeneous matrix. Initially this transformation is just the identity transform (it does nothing), but it can be adjusted to position the structures in your scene.

The transform can be controlled in the UI via the structure's `[Options] --> [Transform]` menu.

??? func "`#!python Structure.get_transform()`"

    Get the current transformation matrix. Returns a 4x4 numpy matrix.

??? func "`#!python Structure.set_transform(transform)`"
    
    Set a particular transform matrix. Takes a 4x4 numpy array.

??? func "`#!python Structure.get_position()`"

    Get the translation component of the transformation matrix, the position to which the structure's origin is translated. Returns a length-3 numpy vector.

??? func "`#!python Structure.set_position(vec)`"

    Set the transformation matrix such that structure is transformed to the position `vec`. Takes a length-3 numpy vector.

??? func "`#!python Structure.translate(vec)`"
    
    Translate the transformation matrix by offset `vec`. Takes a length-3 numpy vector.

??? func "`#!python Structure.center_bounding_box()`"

    Set the transformation such that the structure's bounding box is centered at the world origin.

??? func "`#!python Structure.rescale_to_unit()`"
    
    Set the transformation scaling such that the structure has length scale 1. This makes all structures roughly the same size.

??? func "`#!python Structure.reset_transform()`"
    
    Reset the structure's transform to be the identity transform (i.e. to do nothing).

??? func "`#!python void Structure.set_transform_gizmo_enabled(b)`"
    
    Enable/disable the interactive onscreen widget which lets the user adjust an object's transform. Takes a boolean as input.

??? func "`#!python Structure.get_transform_gizmo_enabled()`"
    
    Get the enabled state of the interactive onscreen widget which lets the user adjust an object's transform.  Returns a boolean.


    
#### Slice planes

Options relating to [slice planes]([[url.prefix]]/features/slice_planes/) which may be present in the scene.

Slice plane options can be controlled in the UI via the structure's `[Options] --> [Slice Planes]` menu.

??? func "`#!python Structure.set_cull_whole_elements(newVal)`"

    If `true`, slice planes will affect this structure by culling whole elements (tets, triangles, points, etc), rather than slicing through the middle of the elements. Takes a boolean.

    Note that not all structures may support culling whole elements. If not supported, this setting will do nothing.
    
    Default: false.

??? func "`#!python Structure.get_cull_whole_elements()`"

    Get whether the cull whole elements setting is applied. Returns a boolean.

??? func "`#!python Structure.set_ignore_slice_plane(name, newValue)`"
    
    Set a slice plane to be ignored by the structure. If `newValue` is `true` the slice plane will be ignored, and if `false` it will be respected. Takes a string and a boolean.

??? func "`#!python Structure.get_ignore_slice_plane(name)`"

    Get if a slice plane is currently being ignored by the structure. Takes a string, returns a boolean.
