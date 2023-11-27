Images are rectangular grids of pixel values.

**Sample:** An image quantity of a majestic cat, shown here in the ImGui window display mode.

![image example](/media/image_example.jpg)

!!! info "Floating Quantities"

    Images are _floating quantities_, which means they can be added to the scene at the root level, or added to any kind of structure.

    See the [floating quantity introduction](/structures/floating_quantities/basics/) for more info.


**Example:**

```python
import polyscope as ps
ps.init()

# Your image data, must be populated somehow
dimX = 1024
dimY = 768

# == Add images at the root level of the scene
# try out a few of the options while we're at it

ps.add_color_image_quantity("color_img", np.zeros((dimX, dimY, 3)), enabled=True, 
                            show_fullscreen=True, show_in_camera_billboard=False, transparency=0.5)
        
ps.add_color_alpha_image_quantity("color_alpha_img", np.zeros((dimX, dimY, 4)), enabled=True, 
                                  show_in_imgui_window=True, show_in_camera_billboard=False,
                                  is_premultiplied=True, image_origin='lower_left')

ps.add_scalar_image_quantity("scalar_img", np.zeros((dimX, dimY)), enabled=True, 
                             image_origin='lower_left', 
                             datatype='symmetric', vminmax=(-3.,.3), cmap='reds')


# == Add images associated with a structure
# Here, a camera view, you could also use a point cloud, or a mesh, etc
cam = ps.get_camera_view("my view"); # some structure you previously registered

cam.add_color_image_quantity("color_img", np.zeros((dimX, dimY, 3)), enabled=True,
                             show_in_camera_billboard=True)
                             # when adding an image to a camera view, we can display it
                             # in the camera billboard

ps.show()
```



!!! tip "Images vs. Render Images"

    If your image happens to represent a rendering of the scene from the user's viewport (for example, from custom renderer code), check out the [Render Image](/structures/floating_quantities/render_images/) quantity, which offers additional functionality for view-rendered images such as depth-compositing them into the scene to layer and blend with other content.


!!! tip "Camera Views"

    Image quantities get special functionality when added to `CameraView` structures: they can additionally be displayed in the camera frame, aligned with the view of the scene.



## Image Origin

When registering an image quantity, you can also specify whether the image should be interpreted such that the first row is the "top" row of the image (`'upper_left'`), or the first row is the "bottom" row of the image (`'lower_left'`). This is a confusing issue, as there are many overlapping conventions of coordinate systems and buffer layouts for images.

Most of the time, `'upper_left'` (the default) is the right choice.

---
## Scalar Image Quantity

These can be called at the root level, like `ps.add_scalar_image_quantity()`, or on a structure, like `cam_view.add_scalar_image_quantity()`.


??? func "`#!python add_scalar_image_quantity(name, values, **kwargs)`"

    Add an image of scalar values

    - `name` string, a name for the quantity
    - `values` an `WxH` numpy array, with scalar values
    
    This function also accepts optional keyword arguments listed below, which customize the appearance and behavior of the quantity.

{!common/scalar_quantity.md!}

---
## Color Image Quantity

These can be called at the root level, like `ps.add_color_image_quantity()`, or on a structure, like `cam_view.add_color_image_quantity()`.

??? func "`#!python add_color_image_quantity(name, values_rgb, **kwargs)`"

    Add an image of rgb color values

    - `name` string, a name for the quantity
    - `values_rgb` an `WxHx3` numpy array, with color values
    
    RGB values are interpreted in the range `[0,1]`.

??? func "`#!python add_color_alpha_image_quantity(name, values_rgba, **kwargs)`"

    Add an image of rgb color values

    - `name` string, a name for the quantity
    - `values_rgba` an `WxHx4` numpy array, with color values
    
    RGB values are interpreted in the range `[0,1]`.


By default, alpha values are interpreted to be non-premultiplied. Use the keyword argument `is_premultiplied=True` to directly pass premultiplied alpha images.

{!common/color_quantity.md!}


---
## Image Options

These options are common to all images

Keyword arguments:

  - `enabled` boolean, whether the quantity is initially enabled (note that generally only one quantitiy can be shown at a time; the most recent will be used)
  - `transparency` float, an opacity to apply to the image
  - `image_origin` string, either `upper_left` (default) or `lower_left` to give the row layout convention
  - `show_fullscreen` boolean, if enabled the image will be shown fullscreen in the Polyscope window
  - `show_in_imgui_window` boolean, if enabled the image will be shown in an ImGui window
  - `show_in_camera_billboard` boolean, if this image was added to a camera view structure, show it in the camera frame

If not specified, these optional parameters will assume a reasonable default value, or a [persistent value](../../../basics/parameters/#persistent-values) if previously set.
