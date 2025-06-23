Visualize scalar valued data at the nodes or edges of a curve network.

![curve network scalar demo]([[url.prefix]]/media/curve_network_scalar.jpeg)

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

# visualize some random data per-node
vals_node = np.random.rand(N_node)
ps_net.add_scalar_quantity("rand vals", vals_node, enabled=True)

# visualize some random data per-edge
vals_edge = np.random.rand(N_edge)
ps_net.add_scalar_quantity("rand vals2", vals_edge, defined_on='edges')

# as always, we can customize the initial appearance
ps_net.add_scalar_quantity("rand vals2 opt", vals_edge, defined_on='edges', 
                           enabled=True, vminmax=(-3., 3.), cmap='reds')


# view the network with all of these quantities
ps.show() 
```

???+ func "`#!python CurveNetwork.add_scalar_quantity(name, values, defined_on='nodes', enabled=None, datatype="standard", vminmax=None, cmap=None)`"

    Add a scalar quantity to the network.

    - `name` string, a name for the quantity
    - `values` a length `N` numpy array, scalars at nodes/edges
    - `defined_on` string, one of `"nodes"` or `"edges"`, is this data a value per-node or a value per-edge?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
    
[[% include 'common/scalar_quantity.md' %]]
