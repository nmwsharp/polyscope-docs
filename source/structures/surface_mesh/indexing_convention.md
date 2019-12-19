## Default ordering

Polyscope abstracts over data types by accepting generic ordered containers of data to visualize (see [input adaptors](../../../basics/array_adaptors)). Unfortunately, not everyone can agree on how to order the elements of their meshes---which edge is the $i^\textrm{th}$ edge in a mesh?

Polyscope defines a _default ordering_ of mesh elements. If you happen to use the same ordering, everything will "just work" (this is probably the case for quantities defined on vertices and faces), you can simply call the relevant functions as you see in the tutorials and examples.

However, if you happen to a different convention for ordering some mesh element (say, edges), visualizations of data on edges will not work correctly out of the box---your data arrays will be associated with the wrong mesh elements.

This section describes the remedy: you can give the mesh a permutation, which will be used to translate from the indexing conventions of your data to the indexing conventions of Polyscope. In general, this permutation `p` should be an array of integers, such that if `i` is the $i^\textrm{th}$ element in the default ordering, `p[i]` gives the index under your convention. Your data arrays will then be indexed as `#!cpp data[p[i]]` when passed as arguments to surface mesh visualization functions. In fact, your indexing convention need not even have the same number of elements as the Polyscope convention, so long as `#!cpp data[p[i]]` is always a valid access; if the size of your index space is different, a size can also be passed in.

The sections below define the _default ordering_ of mesh elements, and show how to set an alternate permutation for each if the default ordering does not match your ordering.


### Vertices

The first argument when registering a surface mesh with Polyscope is a list of vertex positions. The ordering of vertices in this list is the default ordering vertices. Arrays of vertex-valued data passed for visualization will be interpted in that order, unless an alternate permutation is set as below.

??? func "`#!cpp SurfaceMesh::setVertexPermutation(const T& permArr, size_t expectedSize = 0)`"

    Set a non-standard ordering for vertex-valued data on a mesh.

    The argument should be an array-like type which can be interpreted as an array integers, see [input adaptors](../../../basics/array_adaptors). One good choice is a `#!cpp std::vector<size_t>`.

    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `permArr`.

    Must be set _before_ any quantites are added.


### Faces

The second argument when registering a surface mesh with Polyscope is a list of face indices. The ordering of faces in this list is the default ordering faces. Arrays of face-valued data passed for visualization will be interpted in that order, unless an alternate permutation is set as below.

??? func "`#!cpp SurfaceMesh::setFacePermutation(const T& permArr, size_t expectedSize = 0)`"

    Set a non-standard ordering for face-valued data on a mesh.

    The argument should be an array-like type which can be interpreted as an array integers, see [input adaptors](../../../basics/array_adaptors). One good choice is a `#!cpp std::vector<size_t>`.

    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `permArr`.

    Must be set _before_ any quantites are added.

### Edges

The second argument when registering a surface mesh with Polyscope is a list of face indices. 
The edge ordering is defined from this list by the first time an edge appears in any face. More formally, the ordering is equivalent to the following code:

```cpp
std::vector<std::vector<size_t>> faceIndices;
for(std::vector<size_t> face : faceIndices) {

  size_t faceDegree = face.size();

  for(size_t i = 0; i < faceDegree; i++) {

    size_t vertex_A = face[ i ];
    size_t vertex_B = face[ (i+1) % faceDegree ];

    // emit edge (vertex_A, vertex_B), if neither it nor the 
    // equivalent edge (vertex_B, vertex_A) has been emitted already
  }
}
```
The default ordering of edges is the order in which they would be emitted by this loop.

Arrays of edge-valued data passed for visualization will be interpted in that order, unless an alternate permutation is set as below.

??? func "`#!cpp SurfaceMesh::setEdgePermutation(const T& permArr, size_t expectedSize = 0)`"

    Set a non-standard ordering for edge-valued data on a mesh.

    The argument should be an array-like type which can be interpreted as an array integers, see [input adaptors](../../../basics/array_adaptors). One good choice is a `#!cpp std::vector<size_t>`.

    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `permArr`.

    Must be set _before_ any quantites are added.


### Halfedges

The second argument when registering a surface mesh with Polyscope is a list of face indices.  The halfedge ordering is defined from this list by first ordering by the faces, then ordering by the halfedges within each face.  More formally, the ordering is equivalent to the following code:

```cpp
std::vector<std::vector<size_t>> faceIndices;
for(std::vector<size_t> face : faceIndices) {

  size_t faceDegree = face.size();

  for(size_t i = 0; i < faceDegree; i++) {

    size_t vertex_A = face[ i ];
    size_t vertex_B = face[ (i+1) % faceDegree ];

    // emit halfedge (vertex_A, vertex_B)
  }
}
```
The default ordering of halfedges is the order in which they would be emitted by this loop.

Arrays of halfedge-valued data passed for visualization will be interpted in that order, unless an alternate permutation is set as below.

??? func "`#!cpp SurfaceMesh::setHalfedgePermutation(const T& permArr, size_t expectedSize = 0)`"

    Set a non-standard ordering for halfedge-valued data on a mesh.

    The argument should be an array-like type which can be interpreted as an array integers, see [input adaptors](../../../basics/array_adaptors). One good choice is a `#!cpp std::vector<size_t>`.

    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `permArr`.

    Must be set _before_ any quantites are added.


### Corners

The second argument when registering a surface mesh with Polyscope is a list of face indices.  The corner ordering is defined from this list by first ordering by the faces, then ordering by the corners within each face.  More formally, the ordering is equivalent to the following code:

```cpp
std::vector<std::vector<size_t>> faceIndices;
for(std::vector<size_t> face : faceIndices) {

  size_t faceDegree = face.size();

  for(size_t i = 0; i < faceDegree; i++) {

    size_t vertex_A = face[ i ];

    // emit corner in this face incident on vertex_A
  }
}
```
The default ordering of corners is the order in which they would be emitted by this loop.

Arrays of corner-valued data passed for visualization will be interpted in that order, unless an alternate permutation is set as below.

??? func "`#!cpp SurfaceMesh::setCornerPermutation(const T& permArr, size_t expectedSize = 0)`"

    Set a non-standard ordering for corner-valued data on a mesh.

    The argument should be an array-like type which can be interpreted as an array integers, see [input adaptors](../../../basics/array_adaptors). One good choice is a `#!cpp std::vector<size_t>`.
    
    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `permArr`.

    Must be set _before_ any quantites are added.



### All at once

As a convenience, you can alternately define a single function which passes all permutations needed at the same time. This is useful because you can write a single helper function which defines any necessary permutations for the mesh convention in your codebase; see the [geometry-central integration](../../../integrations/geometry_central) for an example.

The permutations should be passed as a `#!cpp std::array<std::pair<T,size_t>,5>`, where `T` is any type that could be used in the `set___Permutation()` functions above---one good choice is a `#!cpp std::array<std::pair<std::vector<size_t>, size_t>, 5>`.  Each entry of this array is one of the permutations listed above: [vertices, faces, edges, halfedges, corners].  Any permutations which have `size() == 0` will be untouched. The second entry of the pair is the optional size of the target index space, as in `expectedSize` above.

These permutations can either be set with `SurfaceMesh::setAllPermutations()`, or at construction time via a third argument to `registerSurfaceMesh()`.
    
??? func "`#!cpp SurfaceMesh::setAllPermutations(const std::array<std::pair<T,size_t>,5>& perms)`"

    Set all of the ordering permutations at once, as described above.
    
    The argument should be a `std::array<>` of an array-like type which can be interpreted as an array integers, see [input adaptors](../../../basics/array_adaptors). One good choice is a `#!cpp std::array<std::pair<std::vector<size_t>, size_t>, 5>`.
    
    If the size of your index space is different from size of the default index space, the second component of each pair must give this new size. Otherwise, the second component of the pair may be set to zero, to infer the size of the index space from the maximum index given.
    
    Must be set _before_ any quantites are added.


??? func "`#!cpp SurfaceMesh* polyscope::registerSurfaceMesh(std::string name, const V& vertexPositions, const F& faceIndices, const std::array<std::pair<P,size_t>,5>& perms, bool replaceIfPresent = true)`"

    Register a mesh and immediately set all custom permutations, as described above.

    Equivalent to
    ```cpp
    SurfaceMesh* s = registerSurfaceMesh(name, vertexPositions, faceIndices, replaceIfPresent);
    s->setAllPermutations(perms);
    ```

    Other wise behave like the standard `registerSurfaceMesh()`.
    
    The argument should be a `std::array<>` of an array-like type which can be interpreted as an array integers, see [input adaptors](../../../basics/array_adaptors). One good choice is a `#!cpp std::array<std::pair<std::vector<size_t>, size_t>, 5>`.
    
    Must be set _before_ any quantites are added.
