Visualize color rgb-valued data at the nodes or edges of a curve network.

![curve network color]([[url.prefix]]/media/curve_network_color.jpeg)

Example:
```cpp
#include "polyscope/curve_network.h"

std::vector<std::array<double, 3>> randColor(edges.size());
for (size_t i = 0; i < edges.size(); i++) {
  randColor[i] = {{polyscope::randomUnit(), polyscope::randomUnit(), polyscope::randomUnit()}};
}

// visualize
polyscope::getCurveNetwork(curveNetworkName)->addEdgeColorQuantity("random color", randColor);
```

??? func "`#!cpp CurveNetwork::addNodeColorQuantity(std::string name, const T& values)`"

    Add a color quantity to the nodes of the curve network

    - `values` is the array of colors at nodes. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of nodes in the curve network.

    RGB values are interpreted in the range `[0,1]`.

??? func "`#!cpp CurveNetwork::addEdgeColorQuantity(std::string name, const T& values)`"

    Add a color quantity to the edges of the curve network

    - `values` is the array of colors at edges. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of edges in the curve network.

    RGB values are interpreted in the range `[0,1]`.

[[% include 'common/color_quantity.md' %]]
