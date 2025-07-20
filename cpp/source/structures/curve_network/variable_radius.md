By default, all nodes/edges in the curve network have the same radius. However, any node or edge scalar quantity can be additionally interpreted as the radius of the nodes or edges of the curve network. This can also be set manually in the GUI via the curve network `[Options]` --> `[Variable Node/Edge Radius]`.

![curve network radius demo]([[url.prefix]]/media/curve_network_variable_radius.jpg)

Any negative values in the scalar quantity will be clamped to `0`. By default, values will be rescaled such that the largest corresponds to the size from the radius option (thus, using any constant scalar quantity will make the radii identical to the default value with no radius set). This automatic scaling can be disabled by setting `autoScale=false` below.

!!! note "Reproducing radius in world units"

    Remember that curve networks always have a per-structure `radius` parameter which sets a radius for all of the nodes and edges in the curve network (and can be adjusted via a slider in the GUI, or via `setRadius()`). This per-structure parameter makes things a little more complicated when also setting length via a scalar quantity as described here.

    By default, the structure radius parameter is still respected. The variable radius from the quantity first scaled such that the largest value is `1.`, and then is multiplied by the structure parameter to get the actual radius used for the elements.

    This usually gives a reasonable visualization, but makes it difficult to set a precise radius in world units.  To properly reproduce a radius in world-coordinate units, you can circumvent autoscaling like `curveNetwork->setNodeRadiusQuantity(q, false)`. This will prevent the auto-scaling of the radii, and also ignore the structure's radius parameter.

!!! note "Node radius vs. edge radius"

    If you set _only_ a node radius, it will be used to set the radius of each node, and edges will be drawn as frustums with each end sized according to the incident node.

    If you set _only_ an edge radius, it will be used to set the radius of each edge, and nodes will be drawn with a radius which is the average of the radii of incident edges.
    
    If you set _both_ a node and an edge radius, then each will be used for the respective elements.

    In the edge-only case and the node-and-edge case, the edges may not perfectly line up the the nodes they are adjacent to, the only way to fix it is to manually set a proper node radius, or use node radius only.


To set values as the curve network radius, first [add them as a scalar quantity]([[url.prefix]]/structures/curve_network/scalar_quantities/), then assign the scalar quantity as the radius using the functions below.


??? func "`#!cpp void CurveNetwork::setNodeRadiusQuantity(CurveNetworkNodeScalarQuantity* quantity, bool autoScale = true)`"

    Set the node radius from the given quantity.

    When using a radius which is a physical length in world coordinates, set `autoScale` to `false` to skip rescaling and ignore the structure's radius parameter.

??? func "`#!cpp void CurveNetwork::setNodeRadiusQuantity(std::string name, bool autoScale = true)`"

    Set the node radius from a quantity by name. The quantity must be a node scalar quantity add to this curve network.
    
    When using a radius which is a physical length in world coordinates, set `autoScale` to `false` to skip rescaling and ignore the structure's radius parameter.

??? func "`#!cpp void CurveNetwork::clearNodeRadiusQuantity()`"

    Clear the node radius quantity and return to using the constant radius.

??? func "`#!cpp void CurveNetwork::setEdgeRadiusQuantity(CurveNetworkEdgeScalarQuantity* quantity, bool autoScale = true)`"

    Set the edge radius from the given quantity.

    When using a radius which is a physical length in world coordinates, set `autoScale` to `false` to skip rescaling and ignore the structure's radius parameter.

??? func "`#!cpp void CurveNetwork::setEdgeRadiusQuantity(std::string name, bool autoScale = true)`"

    Set the edge radius from a quantity by name. The quantity must be an edge scalar quantity add to this curve network.
    
    When using a radius which is a physical length in world coordinates, set `autoScale` to `false` to skip rescaling and ignore the structure's radius parameter.

??? func "`#!cpp void CurveNetwork::clearEdgeRadiusQuantity()`"

    Clear the edge radius quantity and return to using the constant radius.

