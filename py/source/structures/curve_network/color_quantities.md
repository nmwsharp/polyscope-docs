Visualize color rgb-valued data at the nodes or edges of a curve network.

![curve network color]([[url.prefix]]/media/curve_network_color.jpeg)

Example:
```python
import numpy as np
import polyscope as ps
ps.init()

# register a curve network 
N_node = 100
N_edge = 250
nodes = np.random.rand(N_node, 3)
edges = np.random.randint(0, N_node, size=(N_edge,2))
ps_net = ps.register_curve_network("my network", nodes, edges)

# visualize some random colors per-node
vals_node = np.random.rand(N_node, 3)
ps_net.add_color_quantity("rand vals", vals_node, enabled=True)

# visualize some random colors per-edge
vals_edge = np.random.rand(N_edge, 3)
ps_net.add_color_quantity("rand vals2", vals_edge, defined_on='edges')


# view the network with all of these quantities
ps.show() 
```

???+ func "`#!python CurveNetwork.add_color_quantity(name, values, defined_on='nodes', enabled=None)`"

    Add a scalar quantity to the network.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, with rgb [0,1] colors at nodes/edges
    - `defined_on` string, one of `nodes` or `edges`, is this data a color per-node or a value per-edge?
    
    Additional optional keyword arguments:

    - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantity can be shown at a time; the most recent will be used)
    
    if not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
    
