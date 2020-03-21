Visualize vector-valued data at the nodes or edges of a curve network.

Example:
```python
import numpy as np
import polyscope as ps

# register a curve network 
N_node = 100
N_edge = 250
nodes = np.random.rand(N_node, 3)
edges = np.random.randint(0, N_node, size=(N_edge,2))
ps_net = ps.register_curve_network("my network", nodes, edges)

# visualize some random vectors per-node
vecs_node = np.random.rand(N_node, 3)
ps_net.add_vector_quantity("rand vecs", vecs_node)

# visualize some random vectors per-edge
vecs_edge = np.random.rand(N_edge, 3)
ps_net.add_vector_quantity("rand vecs edge", vecs_edge, defined_on='edges')

# set radius/length/color of the vectors
ps_net.add_vector_quantity("rand vecs opt", vecs_node, radius=0.001, length=0.005, color=(0.2, 0.5, 0.5))

# ambient vectors don't get auto-scaled, useful e.g. when representing offsets in 3D space
ps_net.add_vector_quantity("vecs ambient", vecs_node, vectortype='ambient')

# view the network with all of these quantities
ps.show() 
```

???+ func "`#!python CurveNetwork.add_vector_quantity(name, values, defined_on=enabled=None, vectortype="standard", length=None, radius=None, color=None)`"

    Add a vector quantity to the network.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, vectors at nodes/edges (or `Nx2` for 2D data)
    - `defined_on` string, one of `nodes` or `edges`, is this data a vector per-node or a vector per-edge?
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled
    - `vectortype`, one of `standard` or `ambient`. Ambient vectors don't get auto-scaled, and thus are good for representing values in absolute 3D world coordinates
    - `length` float, a (relative) length for the vectors
    - `radius` float, a (relative) radius for the vectors
    - `color` 3-tuple, color for the vectors
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](/basics/parameters/#persistent-values) if previously set.
    
