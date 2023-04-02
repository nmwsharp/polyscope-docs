Visualize vector-valued data at the nodes or edges of a curve network.

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

# visualize some random vectors per-node
vecs_node = np.random.rand(N_node, 3)
ps_net.add_vector_quantity("rand vecs", vecs_node, enabled=True)

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

???+ func "`#!python CurveNetwork.add_vector_quantity(name, values, defined_on='nodes', enabled=None, vectortype="standard", length=None, radius=None, color=None)`"

    Add a vector quantity to the network.

    - `name` string, a name for the quantity
    - `values` an `Nx3` numpy array, vectors at nodes/edges (or `Nx2` for 2D data)
    - `defined_on` string, one of `nodes` or `edges`, is this data a vector per-node or a vector per-edge?
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.
   

{!common/vector_quantity.md!}
