The Polyscope rendering framework supports transparent rendering to visualize complicated data with nested internal structures.

![transparency modes](/media/transparency_modes.jpg)

**Example:** register a surface mesh and render it with transparency

```cpp

#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"

polyscope::init();

/* load a mesh */

// Register the mesh with Polyscope
auto* psMesh = polyscope::registerSurfaceMesh("input mesh", /* vertices */, /* faces */);

// Set transparency
psMesh->setTransparency(0.5);

// Optional: change transparency rendering settings
// polyscope::options::transparencyMode = polyscope::TransparencyMode::Simple;
// polyscope::options::transparencyRenderPasses = 16;

polyscope::show();
```

## Transparency modes

In computer graphics, rendering scenes with transparent content is surprisingly difficult and often computationally expensive. Polyscope supports three different modes for transparent rendering:

- `TransparencyMode::None` is the default, which does not use any transparency and ignores any related settings.
- `TransparencyMode::Simple` uses an approximation which takes a weighted average of objections in view. The benefit is that this method is efficient, only slightly more expensive than normal rendering. However, it ignores the relative depth of different objects, and thus can yield noticeable and confusing artifacts on complex scenes. Generally, this method should only be used when rendering performance is a concern (i.e., if the view is otherwise too laggy to use).
- `TransparencyMode::Pretty` implements expensive-but-accurate "true" transparency, which properly accounts for objects at different depths. This mode is implemented using [depth peeling](https://en.wikipedia.org/wiki/Depth_peeling), which internally renders the scene many times to generate each frame. Because many internal render passes are needed, this mode may be dramatically more expensive than normal rendering, leading to a laggy interface. The parameter `polyscope::options::transparencyRenderPasses` controls the number passes performed (default: `8`); smaller values will reduce the performance hit, whereas larger values may be necessary to resolve complex scenes.

The modes are set in `options::transparencyMode`. Initially, the transparency mode is set to `TransparencyMode::None`. However, if the transparency of any object is modified while the mode is `None`, the mode will be automatically updated to `Pretty` so that the effect is visible.

The transparency mode can be changed in the GUI in the [Appearance] --> [Transparency] menu.

??? func "`#!cpp TransparencyMode options::transparencyMode`"
    
    Set the mode used for transparent rendering. One of `TransparencyMode::None`, `TransparencyMode::Simple`, or `TransparencyMode::Pretty` (see above for explanation).

    Default: `None`. Automatically updated when a transparency value is set for some structure.

??? func "`#!cpp int options::transparencyRenderPasses`"

    The number of passes used for `Transparency::Pretty`. Lower values will reduce the performance impact, but larger values may be necessary to resolve transparency in complex scenes.

    Default: `8`. 


## Setting transparency

Transparency is controlled via a real-valued parameter from `0` to `1`, commonly called "alpha". Setting transparency to `1` means completely opaque (the default), whereas `0` means completely transparent.

This parameter is specified on a per-structure basis via `Structure::setTransparency(float)`. In the future, Polyscope could also support setting transparency more granularly on individual quantities or textures, but for now it is managed at the structure level.

Transparency for each structure can also be modified in the GUI by selecting [Options] --> [Transparency] for the structure.
