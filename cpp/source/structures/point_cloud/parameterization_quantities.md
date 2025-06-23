A _parameterization_ is a set of 2D coordinates associated with a surface, often referred to as "UV coordinates". 

Typically parameterizations are used on meshes (which is also supported in Polyscope!) but at times it may be useful to visualize a parameterization at the points of a point cloud.


## Adding

??? func "`#!cpp PointCloud::addParameterizationQuantity(std::string name, const T& coords, ParamCoordsType type=ParamCoordsType::UNIT)`"

    Add a new parameterization quantity to the structure, defined per-point of the point cloud.

    - `coords` is the array of 2D UV coordinates at points. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of points in the point cloud.

    - `type` the default interpretation of the coordinate scale, see below


??? func "`#!cpp PointCloud::addLocalParameterizationQuantity(std::string name, const T& coords, ParamCoordsType type=ParamCoordsType::WORLD)`"

    Add a new parameterization quantity to the structure, defined per-point of the point cloud.
    
    This is similar to `addParameterizationQuantity`, but has preset settings for `style` and `type` which are suitable for local parameterizations about a point.

    - `coords` is the array of 2D UV coordinates at points. The type should be [adaptable]([[url.prefix]]/data_adaptors) to an array of `float`-valued 2-vectors. The length should be the number of points in the point cloud.

    - `type` the default interpretation of the coordinate scale, see below


[[% include 'common/parameterization_quantity.md' %]]
