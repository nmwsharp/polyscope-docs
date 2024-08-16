The Polyscope scene view includes a ground plane which optionally supports reflection and soft-shadow effects. This section outlines the various modes and options available for the ground plane.

![ground modes]([[url.prefix]]/media/ground_plane_options.jpg)


## Ground plane and shadow modes

- `GroundPlaneMode::None` no ground plane, nor reflection/shadows are shown
- `GroundPlaneMode::Tile` a tiled ground plane 
- `GroundPlaneMode::TileReflection` a tiled ground plane with a reflection of the scene (default)
- `GroundPlaneMode::ShadowOnly` a transparent ground plane with a soft vertical shadow of the scene

The ground plane and shadow settings can also be manually adjusted in the GUI under the `[Appearance] --> [Ground Plane]` menu.

**Example:** adjust the ground plane & shadow appearance

```cpp

#include "polyscope/polyscope.h"

polyscope::init();

// set the ground location manually
polyscope::options::groundPlaneHeightMode = polyscope::GroundPlaneHeightMode::Manual;
polyscope::options::groundPlaneHeight = 0.; // in world coordinates along the up axis

// set soft shadows on the ground
polyscope::options::groundPlaneMode = polyscope::GroundPlaneMode::ShadowOnly;
polyscope::view::upDir = UpDir::ZUp;                 // set +Z as up direction
polyscope::options::groundPlaneHeightFactor = -0.25; // adjust the plane height
polyscope::options::shadowDarkness = 0.1;            // lighter shadows

/* load your mesh, point cloud, etc */

// take screenshot from the current camera view, which will have transparent shadows
polyscope::screenshot("test_image.png", true);

// open the GUI
polyscope::show();
```

??? func "`#!cpp GroundPlaneMode options::groundPlaneMode`"
    
    Set the mode used for the ground plane, as described above. Should be one of `GroundPlaneMode::None`, `GroundPlaneMode::Tile`, `GroundPlaneMode::TileReflection`, or `GroundPlaneMode::ShadowOnly`.

    Default: `GroundPlaneMode::TileReflection`.

Some more details: the ground plane is automatically faded away whenever the scene is viewed from underneath the ground, and also faded away in the distance far from the scene, as determined by the scene bounding box. Shadows are properly transparent, exporting a [screenshot]([[url.prefix]]/features/screenshots) with transparency will set `alpha = options::shadowDarkness` values for shadowed areas, and set `alpha=0` for unshadowed parts of the ground plane.

The `options::shadowBlurIters` and `options::shadowDarkness` parameters below adjust the visual appearance of soft shadows for `GroundPlaneMode::ShadowOnly`.

??? func "`#!cpp int options::shadowBlurIters`"

    The number of blur iterations used to blur soft shadows. Increase to make the shadows more fuzzy.

    Default: `2`. 

??? func "`#!cpp float options::shadowDarkness`"

    How dark the shadows are. `0` is totally transparent (white), and `1` is fully black. When taking screenshots with transparency, these will become alpha transparency values for the shadowed regions.

    Default: `.25`. 

## Ground plane positioning

The orientation of the ground plane is determined by the [up direction for the scene]([[url.prefix]]/basics/camera_controls/#up-direction), which can be set along any of the coordinate directions such as `+X`, `-Z`, etc.

By default, the height of the ground plane is set automatically to the bottom of the bounding box for the scene content (and can optionally be relatively offset via `groundPlaneHeightFactor`).

Alternately, the height can be specified to a fixed location in world coordinates like:
```cpp
polyscope::options::groundPlaneHeightMode = polyscope::GroundPlaneHeightMode::Manual;
polyscope::options::groundPlaneHeight = 0.; // in world coordinates along the up axis
```

??? func "`#!cpp GroundPlaneMode options::groundPlaneHeightMode`"
    
    Set how the height of the ground plane is computed, one of:

    - `GroundPlaneHeightMode::Automatic` anchored to the bottom of the scene bounding box, optionally offset by `groundPlaneHeightFactor`
    - `GroundPlaneHeightMode::Manual` in absolute world coordinates, at the location `groundPlaneHeight`


    Default: `GroundPlaneHeightMode::Automatic`.


??? func "`#!cpp ScaledValue<float> options::groundPlaneHeight`"

    The location of the ground plane, in world coordinates.
    
    This parameter only has an effect if `options::groundPlaneHeightMode == GroundPlaneHeightMode::Manual`.
    
    Default: `0`. 


??? func "`#!cpp ScaledValue<float> options::groundPlaneHeightFactor`"

    The offset of the ground plane from the bottom of the bounding box for the scene. Use postive/negative values to shift the ground plane up/down.

    This parameter only has an effect if `options::groundPlaneHeightMode == GroundPlaneHeightMode::Automatic`.

    This parameter is a [scaled value]([[url.prefix]]/basics/parameters/#scaled-values). You can assign to it like a normal float, `options::groundPlaneHeightFactor = 0.5`, and the resulting value will be _relative_ to the scene length scale. Alternately, absolute values can also be used, as described on the linked page.

    Default: `0`. 




