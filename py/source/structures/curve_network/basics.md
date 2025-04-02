# Curve Networks

Curve networks are collections of nodes sitting in space, connected by edges. In addition to displaying the nodes and edges of the network itself, Polyscope can show any number of scalar, vector, or color quantities associated with the nodes or edges of the network.

Try clicking on a node or edge to see the data associated with that point!

![curve_network_demo](../../media/curve_network_demo.gif)

### Registering a curve network

Curve network structures can be registered with Polyscope by passing the node position and edge indices. 

**Example:** a network of random curves 
```python
import numpy as np
import polyscope as ps
ps.init()

# generate some random nodes and edges between them
nodes = np.random.rand(100, 3)
edges = np.random.randint(0, 100, size=(250,2))

# visualize!
ps_net = ps.register_curve_network("my network", nodes, edges)
ps.show()
```

!!! Note  "Convenience adders for common cases"

    Rather than passing a vector of edge indices, there are also built-in helpers for common cases of connectivity, like a single continuous sequential line or loop, or a collection of line segments. To use them, pass the string `line`, `loop`, or `segments` in places of edge indices, like `register_curve_network("name", nodes, edges='segments')`.

    - `edges='line'` The nodes will be connected together sequentially, forming a single curve
    - `edges='loop'` The nodes will be connected together sequentially, including the last to the first, to form a closed loop
    - `edges='segments'` The `2N` nodes will be connected to form a set of `N` line segments, interleaved as in `[start_0 end_0 start_1 end_1 ...]`


???+ func "`#!python register_curve_network(name, nodes, edges, enabled=None, radius=None, color=None, material=None)`"

    Add a new curve network structure to Polyscope.

    - `name` string, a name for the structure
    - `nodes`, an `Nx3` numpy float array of node locations (or `Nx2` for 2D)
    - `edges`, an `Ex2` numpy integer array of edge connections, as 0-based indices in to the nodes array, OR the string `line`/`loop`/'segments',  to generate node connectivity as a line or loop, respectively.

    Additional optional keyword arguments:

    - `enabled` boolean, is the structure enabled initially
    - `radius` float, a size for the nodes and edges relative to the scene length scale (use `set_radius(val, relative=False)` for absolute units)
    - `color` float 3-tuple, default color values for the network as rgb in [0,1]
    - `material` string, name of material to use for network 

    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
    
    2D node positions are also supported, see [2D data](../../../features/2D_data).



### Updating a curve network

The locations of the nodes in a curve network can be updated with the member function `update_node_positions(newPositions)`. All quantities will be preserved. Changing the connectivity or number of nodes/edges is not supported, you will need to register a new curve network (perhaps with the same name to overwrite).


??? func "`#!python CurveNetwork.update_node_positions(newPos)`"

    Update the node positions in a curve network structure. `newPos` must be valid input as to initially construct the nodes of the network, with the same number of nodes as the network curently has.


### Options

Options control the appearance of the curve network. These options can also be passed as keyword arguments to the initial `register_curve_network()`, as noted above.  See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
radius | size of rendered nodes/edges | `#!python get_radius()` | `#!python set_radius(newVal, relative=True)` | [yes](../../../basics/parameters/#persistent-values) |
color | default color for the network | `#!python get_color()` | `#!python set_color(newVal)` | [yes](../../../basics/parameters/#persistent-values) |
material | material for structure | `#!python get_material()` | `#!python set_material(newVal)` | [yes](../../../basics/parameters/#persistent-values) |


Example: set options which affect the appearance of the curve network
```python
network = polyscope.register_curve_network("my net", nodes, edges)

network.set_enabled(False) # disable
network.set_enabled() # default is true

network.set_radius(0.02) # radius is relative to a scene length scale by default
network.set_radius(1.7, relative=False) # radius in absolute world units

network.set_color((0.3, 0.6, 0.8)) # rgb triple on [0,1]
network.set_material("candy")
network.set_transparency(0.5)

# alternately:
ps.register_curve_network("my net 2", nodes, edges, enabled=False, 
                           material='candy', radius=0.02, color=(1., 0., 0.),
                           transparency=0.5)
```
