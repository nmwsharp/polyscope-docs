The Polyscope scene view includes a ground plane which optionally supports reflection and soft-shadow effects. This section outlines the various modes and options available for the ground plane.

![ground modes]([[url.prefix]]/media/ground_plane_options.jpg)

## Ground plane and shadow modes

- `none` no ground plane, nor reflection/shadows are shown
- `tile` a tiled ground plane 
- `tile_reflection` a tiled ground plane with a reflection of the scene (default)
- `shadow_only` a transparent ground plane with a soft vertical shadow of the scene

The ground plane and shadow settings can also be manually adjusted in the GUI under the `[Appearance] --> [Ground Plane]` menu.

**Example:** adjust the ground plane & shadow appearance

```python
import polyscope as ps

ps.init()

# set the ground height to a fixed location manually
ps.set_ground_height(0.) # in world coordinates

# set soft shadows on the ground
ps.set_ground_plane_mode("shadow_only")  # set +Z as up direction
ps.set_shadow_darkness(0.1)              # lighter shadows


# ... load your mesh, point cloud, etc ...

# take screenshot from the current camera view, which will have transparent shadows
ps.screenshot("test_image.png", True);

# open the GUI
ps.show(3)
```


??? func "`#!python set_ground_plane_mode(mode_str)`"
    
    Set the mode used for the ground plane, as described above. Should be one of `none`, `tile`, `tile_reflection`, or `shadow_only`.

    Default: `tile_reflection`.

Some more details: the ground plane is automatically faded away whenever the scene is viewed from underneath the ground, and also faded away in the distance far from the scene, as determined by the scene bounding box. Shadows are properly transparent, exporting a [screenshot]([[url.prefix]]/features/screenshots) with transparency will set `alpha = shadow_darkness` values for shadowed areas, and set `alpha=0` for unshadowed parts of the ground plane.


The `shadow_blur_iters` and `shadow_darkness` parameters below adjust the visual appearance of soft shadows for the ground plane mode `shadow_only`.

??? func "`#!python set_shadow_blur_iters(i)`"

    The number of blur iterations used to blur soft shadows. Increase to make the shadows more fuzzy.

    Default: `2`. 

??? func "`#!python set_shadow_darkness(val)`"

    How dark the shadows are. `0` is totally transparent (white), and `1` is fully black. When taking screenshots with transparency, these will become alpha transparency values for the shadowed regions.

    Default: `.25`. 

## Ground plane positioning

The orientation of the ground plane is determined by the [up direction for the scene]([[url.prefix]]/basics/camera_controls/#up-direction), which can be set along any of the coordinate directions such as `+X`, `-Z`, etc.

By default, the height of the ground plane is set automatically to the bottom of the bounding box for the scene content (and can optionally be relatively offset via `set_ground_plane_height_factor()`).

Alternately, the height can be specified to a fixed location in world coordinates like:
```python
ps.set_ground_height(0.) # in world coordinates along the up axis
```

??? func "`#!python set_ground_plane_height(x)`"

    Set the location of the ground plane, in world coordinates.

    Calling this function also implicitly sets `set_ground_plane_height_mode('manual')`
    
    Default: `0`. 


??? func "`#!python set_ground_plane_height_factor(x, is_relative=True)`"

    The offset of the ground plane from the bottom of the bounding box for the scene. Use postive/negative values to shift the ground plane up/down.
    
    Calling this function also implicitly sets `set_ground_plane_height_mode('automatic')`

    This parameter is a [scaled value]([[url.prefix]]/basics/parameters/#scaled-values). By default, values will be interpreted relative to the scene length scale, whereas calling `set_ground_plane_height_factor(0.1, is_relative=False)` will specify a value in absolute units.

    Default: `0`. 

??? func "`#!python set_ground_plane_height_mode(mode_str)`"

    Set which policy is used to determine the ground plane height.

    - `automatic` anchored to the bottom of the scene bounding box, optionally offset by `set_ground_plane_height_factor()`
    - `manual` in absolute world coordinates, at the location `set_ground_height()`


    Default: `automatic`.
