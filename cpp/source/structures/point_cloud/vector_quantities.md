Visualize vector-valued data at the points of a point cloud.

??? func "`#!cpp PointCloud::addVectorQuantity(std::string name, const T& vectors, VectorType vectorType = VectorType::STANDARD)`"

    Add a vector quantity to the point cloud.

    - `vectors` is the array of vectors at points. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be the number of points in the point cloud.
    - `vectorType` indicates how to interpret vector data. The default setting is as a freely-scaled value, which will be automatically scaled to be visible. Passing `VectorType::AMBIENT` ensures vectors have the proper world-space length.

    Note: the inner vector type of the input _must_ be 3D dimensional, or you risk compiler errors, segfaults, or worse. If you want to add 2D vectors (usually to a 2D point cloud), `addVectorQuantity2D` exists with the same signature. See [2D data]([[url.prefix]]/features/2D_data).

[[% include 'common/vector_quantity.md' %]]
