## Intro

A **structure** is a geometric object visualized in Polyscope, like a mesh or a point cloud. The first step in seeing your data in Polyscope is to register one or more structures to add them to the visualization. Then, _quantities_ can be added to these structures, like scalar functions, colors, or vector fields.

Each structure should be given a name which is unique among structures of that type. You can then use this name as a handle to perform operations on the structure; For instance, you can register a mesh with:
```cpp
polyscope::registerSurfaceMesh("my mesh", vertices, faces);
```
Then, in a distant part of your code, add a scalar function to it with:
```cpp
polyscope::getSurfaceMesh("my mesh")->addScalarQuantity("some values", values);
```
This avoids the need to pass a pointer to the structure you created around your entire codebase. 

!!! info "Memory management"

    As a general policy, Polyscope always manages its own memory, and will take care of deleting anything it allocated. Whenever a routine returns a pointer (like `getStructure()`), it is a _non-owning_ pointer. You **should never** `delete` one of these pointers. To delete a structure and free memory, see the `removeStructure()` methods below.


## Registering structures

Each structure offers a `register___(name, ...)` function (like `registerPointCloud()`) which accepts the name of the structure and the data necessary to construct it. These functions will return a `Structure*` pointer which may be used to add quantities to the structure. See the relevant sections for documentation on each of these register functions.

The general form for registering structures is below; it may be useful if you are implementing your own structures.

??? func "`#!cpp bool registerStructure(Structure* structure, bool replaceIfPresent = true)`"

    Register a new structure with Polyscope. The structure must have a `Structure::name` which is unique amongst all registered structures of that type.

    Polyscope takes ownership of the memory when the structure is registered, and will `delete` it when no longer needed.

    Note: most users will create structures via the individual `registerPointCloud()` (etc) functions, rather than this general form.

## Accessing structures

Polyscope offers two patterns for calling methods on a registered structure: you can either use the pointer returned after structure creation, or refer to the structure by name.

```cpp
#include "polyscope/surface_mesh.h"

// register a structure
polyscope::SurfaceMesh* psMesh = 
    polyscope::registerSurfaceMesh("my mesh", vertices, faces);

// access with the pointer
psMesh->addScalarQuantity("some values", values);

// access by name
polyscope::getSurfaceMesh("my mesh")->addScalarQuantity("some values", values);
```
The former is concise and programmatic, while the latter avoids the need to keep track of a variable.

As before, each structure offers a `get___(name)` method, like `getSurfaceMesh(name)` which can be used to get a pointer to the structure of that type by name. The general form below may be useful if you are implementing your own structures.


??? func "`#!cpp Structure* getStructure(std::string type, std::string name = "")`"

    Get a pointer to a registered structure. The `type` must be the unique string corresponding to the structure type.

    As a convenience, if the `name` may be argument omitted _only_ if there is exactly one structure of that type.

    If not such structure is available, `nullptr` will be returned.

    Note: most users will get structures via the individual `getPointCloud()` (etc) functions, rather than this general form.

## Removing structures

If no longer needed, structures can be removed by name or by pointer. Removing a structure frees memory for the underlying objects, invalidating all references to the structure and its quantities.


??? func "`#!cpp void removeStructure(Structure* structure, bool errorIfAbsent = true)`"

    Remove the specified structure and free objects associated with it.

    If `errorIfAbsent == true`, and error will be thrown if there is no such structure registered, otherwise the function will return silently.

??? func "`#!cpp void removeStructure(std::string type, std::string name, bool errorIfAbsent = true)`"

    Identical to `removeStructure(Struture*)`, but accepts a type name and name instead.


??? func "`#!cpp void removeStructure(std::string name, bool errorIfAbsent = true)`"
    
    Identical to `removeStructure(Struture*)`, but accepts a name instead. Will fail unless there is exactly one structure with the given name across all structure types.


??? func "`#!cpp void removeAllStructures()`"

    Remove all structures from the scene.

## Quantities

Quantities, like scalar functions, color fields, vector fields, and more, can be associated with structures. See the available options for each kind of structure.

Quantities can be removed from a structure by name.

??? func "`#!cpp void Structure::removeQuantity(std::string name, bool errorIfAbsent = false)`"

    Remove a quantity from the structure by name.


??? func "`#!cpp void Structure::removeAllQuantities()`"

    Remove all quantities which have been added to the structure.


## Structure options

These basic options are shared by all structures.  Structure options are managed as [persistent values]([[url.prefix]]/basics/parameters/#persistent-values), and thus will persist if a new structure is registered with the same name.

#### Enabled

If a structure is disabled, it will be hidden from view, along with any quantities associated with that structure.

??? func "`#!cpp bool Structure::isEnabled()`"

    Is the structure enabled?

??? func "`#!cpp void Structure::setEnabled(bool newVal)`"

    Set the structure to be enabled or disabled.


#### Transparency

Set the transparency parameter for the structure. `1` is fully opaque (the default), and `0` is fully transparent. When the first structure has transparency applied, transparent rendering will be automatically enabled.

Transparency can be controlled in the UI via the structure's `[Options] --> [Transparency]` menu.

??? func "`#!cpp float Structure::getTransparency()`"

    Get the transparency parameter for the structure.

??? func "`#!cpp void Structure::setTransparency(float alpha)`"

    Set the transparancy for the structure.

#### Transforms

Each structure has an associated spatial _transform_ applied to it for display in the scene. The transform encodes a translation, rotation, and scaling represented as a 4x4 homogeneous matrix. Initially this transformation is just the identity transform (it does nothing), but it can be adjusted to position the structures in your scene.

The transform can be controlled in the UI via the structure's `[Options] --> [Transform]` menu.
See [transformation gizmos]([[url.prefix]]/basics/interactive_UIs_and_animation/#transformation-gizmos) for more information on the interactive onscreen transformation gizmo.

??? func "`#!cpp glm::mat4x4 Structure::getTransform()`"

    Get the current transformation matrix. 

??? func "`#!cpp void Structure::setTransform(glm::mat4x4 transform)`"
    
    Set a particular transform matrix. 

??? func "`#!cpp glm::vec3 Structure::getPosition()`"

    Get the translation component of the transformation matrix, the position to which the structure's origin is translated.

??? func "`#!cpp void Structure::setPosition(glm::vec3 vec)`"

    Set the transformation matrix such that structure is transformed to the position `vec`.

??? func "`#!cpp void Structure::translate(glm::vec3 vec)`"
    
    Translate the transformation matrix by offset `vec`.

??? func "`#!cpp void Structure::centerBoundingBox()`"

    Set the transformation such that the structure's bounding box is centered at the world origin.

??? func "`#!cpp void Structure::rescaleToUnit()`"
    
    Set the transformation scaling such that the structure has length scale 1. This makes all structures roughly the same size.

??? func "`#!cpp void Structure::resetTransform()`"
    
    Reset the structure's transform to be the identity transform (i.e. to do nothing).

??? func "`#!cpp void Structure::setTransformGizmoEnabled(bool newVal)`"
    
    Enable/disable the interactive onscreen widget which lets the user adjust an object's transform.

??? func "`#!cpp bool Structure::getTransformGizmoEnabled()`"
    
    Get the enabled state of the interactive onscreen widget which lets the user adjust an object's transform.

??? func "`#!cpp TransformationGizmo& Structure::getTransformGizmo()`"
    
    Get a reference to the underlying `TransformationGizmo` object for the interactive transform widget.

    See [transformation gizmos]([[url.prefix]]/basics/interactive_UIs_and_animation/#transformation-gizmos) for options relate to the gizmo object.


    
#### Slice planes

Options relating to [slice planes]([[url.prefix]]/features/slice_planes/) which may be present in the scene.

Slice plane options can be controlled in the UI via the structure's `[Options] --> [Slice Planes]` menu.

??? func "`#!cpp Structure* Structure::setCullWholeElements(bool newVal)`"

    If `true`, slice planes will affect this structure by culling whole elements (tets, triangles, points, etc), rather than slicing through the middle of the elements.

    Note that not all structures may support culling whole elements. If not supported, this setting will do nothing.
    
    Default: false.

??? func "`#!cpp bool Structure::getCullWholeElements()`"

    Get whether the cull whole elements setting is applied.

??? func "`#!cpp Structure* Structure::setIgnoreSlicePlane(std::string name, bool newValue)`"
    
    Set a slice plane to be ignored by the structure. If `newValue` is `true` the slice plane will be ignored, and if `false` it will be respected.

??? func "`#!cpp bool Structure::getIgnoreSlicePlane(std::string name)`"

    Get if a slice plane is currently being ignored by the structure.
