## Default ordering

Polyscope abstracts over data types by accepting generic ordered containers of data to visualize (see [input adaptors](../../../basics/array_adaptors)). Unfortunately, not everyone can agree on how to order the elements of their meshes---which edge is the i'th edge in a mesh?

For vertices and faces, Polyscope only supports one order: the order of the elements used when you registered the mesh. However, for edges, halfedges, and corners it is more complicated. For these data, you should generally explicitly tell Polyscope what ordering/indexing you will be using for the data.

The way it works is that Polyscope defines a _default ordering_ of mesh elements. If you happen to use the same ordering, everything will "just work", and you can simply call the relevant functions as you see in the tutorials and examples. However, if you happen to a different convention for ordering some mesh element, visualizations of data on that element will not work correctly out of the box---your data arrays will be associated with the wrong mesh elements.

This section describes the remedy: you can give the mesh a "permutation", which will be used to translate from the indexing conventions of your data to the indexing conventions of Polyscope. In general, this permutation `p` should be an array of integers, such that if `i` is the $i^\textrm{th}$ element in the default ordering, `p[i]` gives the index under your convention. Your data arrays will then be indexed as `#!cpp data[p[i]]` when passed as arguments to surface mesh visualization functions. In fact, your indexing convention need not even have the same number of elements as the Polyscope convention, so long as `#!cpp data[p[i]]` is always a valid access; if the size of your index space is different, a size can also be passed in (in this case we abuse terminology: it is not technically a permutation).

The sections below define the _default ordering_ of mesh elements, and show how to set an alternate permutation for each if the default ordering does not match your ordering.

### Vertices and Faces

For vertices and faces, Polyscope only supports one order: the order of the elements used when you registered the mesh. This order is always used automatically.

### Edges

The second argument when registering a surface mesh with Polyscope is a list of face indices. 
The edge ordering is defined from this list by the first time an edge appears in any face. More formally, the ordering is equivalent to the following C++ code:

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

For edge-valued data, a permutation _must_ be set. This is a sanity check to catch errors; for edges, it is highly unlikely that users happen to be storing their data in the same order.

??? func "`#!python SurfaceMesh.set_edge_permutation(perm, expected_size=None)`"

    Set a non-standard ordering for edge-valued data on a mesh.

    The argument `perm` should be an array of integers.

    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `perm`.

    Must be set _before_ any quantites are added.


### Halfedges

The second argument when registering a surface mesh with Polyscope is a list of face indices.  The halfedge ordering is defined from this list by first ordering by the faces, then ordering by the halfedges within each face.  More formally, the ordering is equivalent to the following C++ code:

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

Arrays of halfedge-valued data passed for visualization will be interpreted in that order, unless an alternate permutation is set as below.

??? func "`#!python SurfaceMesh.set_halfedge_permutation(perm, expected_size=None)`"

    Set a non-standard ordering for halfedge-valued data on a mesh.

    The argument `perm` should be an array of integers.

    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `perm`.

    Must be set _before_ any quantites are added.


### Corners

The second argument when registering a surface mesh with Polyscope is a list of face indices.  The corner ordering is defined from this list by first ordering by the faces, then ordering by the corners within each face.  More formally, the ordering is equivalent to the following C++ code:

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

Arrays of corner-valued data passed for visualization will be interpreted in that order, unless an alternate permutation is set as below.

??? func "`#!python SurfaceMesh.set_corner_permutation(perm, expected_size=None)`"

    Set a non-standard ordering for corner-valued data on a mesh.

    The argument `perm` should be an array of integers.
    
    If the size of your index space is different from size of the default index space, the optional second argument must give this new size. If not given, the size will be inferred from the largest entry in `perm`.

    Must be set _before_ any quantites are added.



### All at once

As a convenience, you can alternately use a single function which passes all permutations needed at the same time. This might ease writing a single helper function which defines any necessary permutations for the mesh convention in your codebase.

??? func "`#!cpp SurfaceMesh.set_all_permutations(edge_perm=None, edge_perm_size=None, corner_perm=None, corner_perm_size=None, halfedge_perm=None, halfedge_perm_size=None)`"

    Any non-`None` keyword arguments will simply be forwarded to the appropriate `set_XXX_permutation()` variant as above.

