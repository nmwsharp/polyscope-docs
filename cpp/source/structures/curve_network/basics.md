# Curve Networks

Curve networks are collections of nodes sitting in space, connected by edges. In addition to displaying the nodes and edges of the network itself, Polyscope can show any number of scalar, vector, or color quantities associated with the nodes or edges of the network.

Try clicking on a node or edge to see the data associated with that point!

![curve_network_demo](../../media/curve_network_demo.gif)

### Registering a curve network

Curve network structures can be registered with Polyscope by passing the node position and edge indices. There are also two helpers for constructing lines and loops which only require the node locations and automatically build connectivity.

As usual in Polyscope, the [data adaptors]([[url.prefix]]/data_adaptors) allow these functions to accept a wide variety of data types as input-- any `nodes` which are essentially a list of vectors and any `edges` which are a list of index tuples will work. The `std::vector<>` types in the example below are just one possibility.

Example: add a curve network
```cpp
#include "polyscope/curve_network.h"

polyscope::init();

std::vector<glm::vec3> nodes = /* some nodes */;
std::vector<std::array<size_t, 2>> edges = /* edges between nodes */;

// Add the curve network
polyscope::registerCurveNetwork("my network", nodes, edges);

// visualize!
polyscope::show();
```

!!! Note  "Convenience adders for common cases"

    Rather than passing a vector of edge indices, there are also built-in helpers for common cases of connectivity, like a single continuous sequential line or loop, or a collection of line segments. To use them, call the alternate adders such as `registerCurveNetworkLine("name", nodes)`, which do not require a vector of edge indices.

    - `line` The nodes will be connected together sequentially, forming a single curve
    - `loop` The nodes will be connected together sequentially, including the last to the first, to form a closed loop
    - `segments` The `2N` nodes will be connected to form a set of `N` line segments, interleaved as in `[start_0 end_0 start_1 end_1 ...]`


??? func "`#!cpp CurveNetwork* polyscope::registerCurveNetwork(std::string name, const P& nodes, const E& edges)`"

    Add a new curve network to polyscope

    - `nodes` is the array of 3D point locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors. The length will be the number of nodes.

    - `edges` is the array of edges, each of which is a pair of 0-based node indices node. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `size_t`-valued 2-vectors. The length will be the number of edges.

    Note: the inner vector type of the `nodes` input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D curve network, `registerCurveNetwork2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

??? func "`#!cpp CurveNetwork* polyscope::registerCurveNetworkLine(std::string name, const P& nodes)`"

    Add a new curve network to Polyscope from a **polyline** of points. The connectivity will be automatically created to connect the points in order.

    - `nodes` is the array of 3D point locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors. The length will be the number of nodes.

    Note: the inner vector type of the `points` input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D curve network, `registerCurveNetworkLine2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).


??? func "`#!cpp CurveNetwork* polyscope::registerCurveNetworkLoop(std::string name, const P& nodes)`"

    Add a new curve network to Polyscope from a **closed loop** of points. The connectivity will be automatically created to connect the points in order.

    - `nodes` is the array of 3D point locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors. The length will be the number of nodes.

    Note: the inner vector type of the `points` input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D curve network, `registerCurveNetworkLoop2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

??? func "`#!cpp CurveNetwork* polyscope::registerCurveNetworkSegments(std::string name, const P& nodes)`"

    Add a new curve network to Polyscope from an interleaved set of lines. If `2N` nodes are passed, then `N` line segments will be created, connecting the points in an interleaved order like `[start_0 end_0 start_1 end_1 ...]`.

    - `nodes` is the array of 3D point locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors. The length will be the number of nodes.

    Note: the inner vector type of the `points` input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to register a 2D curve network, `registerCurveNetworkLoop2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

### Selection / Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene.  As with other structures, you can call `interpretPickResult()` to get additional info about a click. See [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#selection-picking) for general information.

```cpp
struct CurveNetworkPickResult {
  CurveNetworkElement elementType; // which kind of element did we click (enum values: {NODE, EDGE})
  int64_t index;                   // index of the clicked element
  float tEdge = -1;                // if the pick is an edge, the t-value in [0,1] along the edge
};
```

??? func "`#!cpp CurveNetworkPickResult CurveNetwork::interpretPickResult(PickResult result)`"

    Get additional information about a click.

### Updating a curve network

The locations of the nodes in a curve network can be updated with the member function `updateNodePositions(newPositions)`. All quantities will be preserved. Changing the connectivity or number of nodes/edges is not supported, you will need to register a new curve network (perhaps with the same name to overwrite).


??? func "`#!cpp void CurveNetwork::updateNodePositions(const V& newPositions)`"

    Update the node positions in a curve network structure.

    - `newPositions` is the vector array of 3D node locations. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 3-vectors.  The length must be equal to the current number of nodes.

    Note: `updatePointPositions2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

### Adjusting the node and edge radius

Set the radius of the nodes and edges in the curve network with `CurveNetwork::setRadius(newRad)`. By default, the radius is a [relative value]([[url.prefix]]/basics/parameters/#scaled-values) which gets scaled by the content in the scene, so for example a default of `0.02` will always be a reasonable size no matter what the scale of the content in your scene is. Or, set `isRelative=false` to set an absolute radius in world units.

??? func "`#!cpp void CurveNetwork::setRadius(double newVal, bool isRelative=true)`"

    Update the radius for the nodes and edges in the curve network.

    By default the radius is interpreted as a relative value, setting `isRelative=false` will treat is as an absolute length in world units.

To set a variable radius which is different for each node and/or edge in the curve network, see the [variable radius page]([[url.prefix]]/structures/curve_network/variable_radius/).


### Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
radius | size of rendered points and lines | `#!cpp double getRadius()` | `#!cpp setRadius(double newVal, bool isRelative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
color | default color the curve network | `#!cpp glm::vec3 getColor` | `#! setColor(glm::vec3 newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#! setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |


