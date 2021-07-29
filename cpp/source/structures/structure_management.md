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

The following structures available in Polyscope. Many more structures are in development!

- [Surface Mesh](../surface_mesh/basics)
- [Point Cloud](../point_cloud/basics)
- [Curve Network](../curve_network/basics)
- [Volume Mesh](../volume_mesh/basics)
- _in progress_: Camera View


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
