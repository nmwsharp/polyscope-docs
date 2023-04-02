Visualize vector-valued data at the nodes or edges of a curve network.

Example: add vectors at nodes
```cpp
#include "polyscope/curve_network.h"

// Generate random vectors as example vector data
std::vector<glm::vec3> randVec(nNodes);
for (size_t iN = 0; iN < nNodes; iN++) {
  randVec[iN] = glm::vec3{polyscope::randomUnit() - .5, polyscope::randomUnit() - .5, polyscope::randomUnit() - .5};
}

// Add the vector data to the curve network
polyscope::getCurveNetwork("my curve")->addNodeVectorQuantity("sample vectors", randVec);

// Visualize
polyscope::show();
```


??? func "`#!cpp CurveNetwork::addNodeVectorQuantity(std::string name, const T& vectors, VectorType vectorType = VectorType::STANDARD)`"

    Add a vector quantity to the nodes of a curve network. Vectors will be drawn with their roots at each edge.

    - `vectors` is the array of vectors at nodes. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of nodes in the curve network.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to add 2D vectors (usually to a 2D curve network), `addNodeVectorQuantity2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

??? func "`#!cpp CurveNetwork::addEdgeVectorQuantity(std::string name, const T& vectors, VectorType vectorType = VectorType::STANDARD)`"

    Add a vector quantity to the edges of a curve network. Vectors will be drawn with their roots at the center of each each.

    - `vectors` is the array of vectors at edges. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of edges in the curve network.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to add 2D vectors (usually to a 2D curve network), `addEdgeVectorQuantity2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).


{!common/vector_quantity.md!}
