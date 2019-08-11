Visualize scalar valued data at the nodes or edges of a curve network.

![curve network scalar demo](/media/curve_network_scalar.jpeg)

Example:
```cpp
#include "polyscope/curve_network.h"

std::vector<double> xC(nodes.size());
for (size_t i = 0; i < nodes.size(); i++) {
  xC[i] = nodes[i].x; // (use the x coordinate as sample data)
}

// visualize
polyscope::getCurveNetwork(curveNetworkName)->addNodeScalarQuantity("sample value", xC);
```

??? func "`#!cpp CurveNetwork::addNodeScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity to the nodes of the curve network.

    - `values` is the array of scalars at nodes. The type should be [adaptable](/data_adaptors) to a `float` scalar array. The length should be the number of nodes in the curve network.



??? func "`#!cpp CurveNetwork::addEdgeScalarQuantity(std::string name, const T& values, DataType type = DataType::STANDARD)`"

    Add a scalar quantity to the edges of the curve network.

    - `values` is the array of scalars at edges . The type should be [adaptable](/data_adaptors) to a `float` scalar array. The length should be the number of edges in the curve network.


