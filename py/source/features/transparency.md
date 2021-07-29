The Polyscope rendering framework supports transparency to visualize complicated data with nested internal structures.

![transparency modes](/media/transparency_modes.jpg)

**Example:** register a surface mesh and render it with transparency

```python
import polyscope as ps

ps.init()
  
# Add a mesh with transparency
# ... load verts and faces ...
ps_mesh = ps.register_surface_mesh("mesh", verts, faces, 
                                    transparency=0.7)

# As soon as any structure has transparency set, the transparency mode
# is automatically changed to 'pretty' (depth peeling). It can be further
# changed like:
ps.set_transparency_mode('simple')

# take screenshot from the current camera view, 
# which will have transparency according to the structure
ps.screenshot("test_image.png", True);

# open the GUI
ps.show(3)
```

## Transparency modes

In computer graphics, rendering scenes with transparent content is surprisingly difficult and often computationally expensive. Polyscope supports three different modes for transparent rendering:

- `'none'` is the default, which does not use any transparency and ignores any related settings.
- `'simple'` uses an approximation which takes a weighted average of objects in view. The benefit is that this method is efficient, only slightly more expensive than normal rendering. However, it ignores the relative depth of different objects, and thus can yield noticeable and confusing artifacts on complex scenes. Generally, this method should only be used when rendering performance is a concern (i.e., if the view is otherwise too laggy to use).
- `'pretty'` implements expensive-but-accurate "true" transparency, which properly accounts for objects at different depths. This mode is implemented using [depth peeling](https://en.wikipedia.org/wiki/Depth_peeling), which internally renders the scene many times to generate each frame. Because many internal render passes are needed, this mode may be dramatically more expensive than normal rendering, leading to a laggy interface. The parameter configured with `set_transparency_render_passes()` controls the number passes performed (default: `8`); smaller values will reduce the performance hit, whereas larger values may be necessary to resolve complex scenes.

The modes are set via `set_transparency_mode`. Initially, the transparency mode is set to `'none'`. However, if the transparency of any object is modified while the mode is `'none'`, the mode will be automatically updated to `'pretty'` so that the effect is visible.

Any ground plane reflections are disabled when using transparency.

The transparency mode can also be changed in the GUI in the `[Appearance] --> [Transparency]` menu.

??? func "`#!python set_transparency_mode(mode_str)`"
    
    Set the mode used for transparent rendering. One of `'none'`, `'simple'`, or `'pretty'` (see above for explanation).

    Default: `'none'`. Automatically updated when a transparency value is set for some structure.

??? func "`#!python set_transparency_render_passes(n)`"

    The number of passes used for `'pretty'` mode. Lower values will reduce the performance impact, but larger values may be necessary to resolve transparency in complex scenes.

    Default: `8`. 


## Setting structure transparency

Transparency is controlled via a real-valued parameter from `0` to `1`, commonly called "alpha". Setting transparency to `1` means completely opaque (the default), whereas `0` means completely transparent.  This parameter is specified on a per-structure basis via `Structure.set_transparency(val)`, or by using a `transparency` keyword argument when registering the structure.  Transparency for each structure can also be modified in the GUI by selecting `[Options] --> [Transparency]` for the structure.

??? func "`#!python Structure.set_transparency(val)`"

    Set the transparency for a structure, `1` means completely opaque (the default), whereas `0` means completely transparent.

    Example:
    ```python
    ps_mesh = polyscope.register_surface_mesh("mesh", verts, faces)
    ps_mesh.set_transparency(0.5)
    ```
