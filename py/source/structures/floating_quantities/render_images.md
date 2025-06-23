Render images are special images which are renderings of scene through the Polyscope viewport. These are useful when using Polyscope to visualize renders from your own custom renderers, such as ray tracers, SDF-field implicit tracers, or neural field renderers.

Render images always show the image in fullscreen viewport. Additional, depth and transparency allow the image to be composited with other scene content, so that you can still see your usual Polyscope meshes and point clouds in the scene along with the outputs of your renderer.

**Sample:** A colored box and scalar torus, displayed as render images from a user's custom implicit surface renderer.

![sample render image]([[url.prefix]]/media/render_image_implicit_example.jpg)


!!! info "Floating Quantities"

    Render images are _floating quantities_, which means they can be added to the scene at the root level, or added to any kind of structure.

    It is most common to add render image quantities at the root level. However, it might still be useful to add render images to structures, to associate the rendering with a particular structure, e.g. as a separate rendering of each point cloud in the scene.

    See the [floating quantity introduction]([[url.prefix]]/structures/floating_quantities/basics/) for more info.


## Image Origin

When registering an image quantity, you can also specify whether the image should be interpreted such that the first row is the "top" row of the image (`'upper_left'`), or the first row is the "bottom" row of the image (`'lower_left'`). This is a confusing issue, as there are many overlapping conventions of coordinate systems and buffer layouts for images.

Most of the time, `'upper_left'` (the default) is the right choice.

---
## Depth Render Image Quantity

A depth render image quantity takes a depth value per-pixel, and (optionally) a world-space normal per-pixel. The depth image will be rendered with surface shading using Polyscope's [materials]([[url.prefix]]/features/materials/).

**Example:**
```python
import polyscope as ps
import numpy as np

w = 1024
h = 768
depths = np.zeros((h, w))
normals = np.ones((h, w, 3))
        
ps.add_depth_render_image_quantity("render_img", depths, normals, 
                                   enabled=True, image_origin='upper_left', 
                                   color=(0., 1., 0.), material='wax', transparency=0.7,
                                   allow_fullscreen_compositing=True)
    
polyscope::show(3);
```

If normals are not given, they will be computed internally via screen-space derivatives.

??? func "`#!python add_depth_render_image_quantity(name, depths, normals, **kwargs)`"

    Add a depth render image.

    - `name` string, a name for the quantity
    - `depths` an `HxW` numpy array, with scalar depth values
    - `normals` an `HxWx3` numpy array, with world-space normals values, or `None` to automatically compute normals
    
    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.


---
## Color Render Image Quantity

A color render image quantity takes a depth value per-pixel, (optionally) a world-space normal per-pixel, and a color value per-pixel. The depth image will be rendered with surface shading using Polyscope's [materials]([[url.prefix]]/features/materials/), colored according to the given color.

!!! info "Color vs. Raw Color Render Images"

    A _color_ render image applies [materials](/features/materials/) shading and lighting to the image, just like Polyscope usually does for meshes and other objects. A _raw color_ render image does not do any additional shading, and simply displays the given colors directly onto the screen.

**Example:**
```python
import polyscope as ps
import numpy as np

w = 1024
h = 768
depths = np.zeros((h, w))
normals = np.ones((h, w, 3))
colors = np.ones((h, w, 3))

ps.add_color_render_image_quantity("render_img", depths, normals, colors, 
                                   enabled=True, image_origin='upper_left', 
                                   material='wax', transparency=0.7, )
```

If normals are not given, they will be computed internally via screen-space derivatives.

??? func "`#!python add_color_render_image_quantity(name, depths, normals, colors, **kwargs)`"

    Add a depth render image, annotated with additional color values per-pixel.

    - `name` string, a name for the quantity
    - `depths` an `HxW` numpy array, with scalar depth values
    - `normals` an `HxWx3` numpy array, with world-space normals values, or `None` to automatically compute normals
    - `colors` an `HxWx3` numpy array, with colors
    
    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.

    RGB values are interpreted in the range `[0,1]`.
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.

[[% include 'common/color_quantity.md' %]]

---
## Scalar Render Image Quantity

A scalar render image quantity takes a depth value per-pixel, (optionally) a world-space normal per-pixel, and a scalar value per-pixel. The depth image will be rendered with surface shading using Polyscope's [materials]([[url.prefix]]/features/materials/), with the scalar value shaded and colormapped as a scalar quantity.

**Example:**
```python
import polyscope as ps
import numpy as np

w = 1024
h = 768
depths = np.zeros((h, w))
normals = np.ones((h, w, 3))
scalars = np.ones((h, w))

ps.add_scalar_render_image_quantity("render_img3", depths, normals, scalars, 
                                     enabled=True, image_origin='upper_left', 
                                     vminmax=(-3.,.3), cmap='reds')

```

If normals are not given, they will be computed internally via screen-space derivatives.

??? func "`#!python ps.add_scalar_render_image_quantity(name, depths, normals, scalars, **kwargs)`"

    Add a depth render image, annotated with additional scalar values per-pixel.

    - `name` string, a name for the quantity
    - `depths` an `HxW` numpy array, with scalar depth values
    - `normals` an `HxWx3` numpy array, with world-space normals values, or `None` to automatically compute normals
    - `scalars` an `HxW` numpy array, with scalar values
    
    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.

    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.

[[% include 'common/scalar_quantity.md' %]]

---
## Raw Color Render Image Quantity

A raw color render image quantity takes a depth value per-pixel and a color value per-pixel. The colors will be directly displayed onscreen, with depth compositing into the scene.

**Example:**
```python
import polyscope as ps
import numpy as np

w = 1024
h = 768
depths = np.zeros((h, w))
colors = np.ones((h, w, 3))

ps.add_raw_color_render_image_quantity("render_img3", depths, colors, 
                                       enabled=True, allow_fullscreen_compositing=True)

```

!!! info "Color vs. Raw Color Render Images"

    A _color_ render image applies [materials]([[url.prefix]]/features/materials/) shading and lighting to the image, just like Polyscope usually does for meshes and other objects. A _raw color_ render image does not do any additional shading, and simply displays the given colors directly onto the screen.

??? func "`#!python add_raw_color_render_image_quantity(name, depths, colors, **kwargs)`"

    Add a raw color render image described by pixel color and depth.

    - `name` string, a name for the quantity
    - `depths` an `HxW` numpy array, with scalar depth values
    - `colors` an `HxWx3` numpy array, with colors
    
    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.

    RGB values are interpreted in the range `[0,1]`.
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.


---
## Raw Color Alpha Render Image Quantity

Just like the above `ColorRenderImageQuantity`, but with an additional alpha channel which gets alpha-composited onto the scene.

**Example:**
```python
import polyscope as ps
import numpy as np

w = 1024
h = 768
depths = np.zeros((h, w))
color_alphas = np.ones((h, w, 4))

ps.add_raw_color_alpha_render_image_quantity("render_img3", depths, color_alphas, 
                                             enabled=True, image_origin='upper_left', 
                                             is_premultiplied=True)
```

??? func "`#!python add_raw_color_alpha_render_image_quantity(name, depths, color_alphas, **kwargs)`"

    Add a raw color render image described by RGBA pixel color and depth.

    - `name` string, a name for the quantity
    - `depths` an `HxW` numpy array, with scalar depth values
    - `colors_alphas` an `HxWx4` numpy array, with colors
    
    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.

    RGB values are interpreted in the range `[0,1]`.
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.

By default, alpha values are interpreted to be non-premultiplied. Use `is_premultiplied=True` to directly pass premultiplied alpha images.

---
## Render Image Options

These options are common to all render images

Keyword arguments:

  - `enabled` boolean, whether the quantity is initially enabled 
  - `transparency` float, an opacity to apply to the image
  - `image_origin` string, either `upper_left` (default) or `lower_left` to give the row layout convention
  - `material` string, material name for the surface rendering
  - `allow_fullscreen_compositing`, boolean, if `False` only one render image is displayed at a time (default), if `True`, multiple can be displayed and will layer on top of each other, although the render order is arbitrary

If not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.

Raw color render images ignore material-related settings.
