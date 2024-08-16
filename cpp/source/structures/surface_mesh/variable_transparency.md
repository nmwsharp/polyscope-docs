You can set the transparency individually for each element in a surface mesh by specifing an existing scalar quantity to serve as the transparency.
This can also be set manually in the GUI via the point cloud `[Options] --> [Variable Transparency]` setting.

Per-vertex, per-face, and per-corner scalar quantities are supported for use as transparency values.

See the [transparency]([[url.prefix]]/features/transparency) section for more transparency-related options.

![surface mesh transparency demo]([[url.prefix]]/media/mesh_scalar_transparency.jpg)

All values will be clamped into the `[0,1]` range. The transparency is multiplicative with any other transparency effects, such as setting the structure's global transparency value.

??? func "`#!cpp void SurfaceMesh::setTransparencyQuantity(SurfaceScalarQuantity* quantity)`"

    ##### set transparency quantity

    Set the transparency quantity. All values will be clamped into the `[0,1]` range.

    If transparency is not already enabled, updates the transparency mode to be `Pretty`.

??? func "`#!cpp void SurfaceMesh::setTransparencyQuantity(std::string name)`"

    Set the transparency quantity by name. All values will be clamped into the `[0,1]` range.

    If transparency is not already enabled, updates the transparency mode to be `Pretty`.

??? func "`#!cpp void SurfaceMesh::clearTransparencyQuantity()`"
    
    ##### clear transparency quantity

    Clear the transparency quantity.
