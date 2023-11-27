# Camera Views

Use camera view structures to represent pinhole cameras in a 3D scene. Given camera locations, orientations, and field of view (intrinsics + extrinsics), Polyscope will draw a camera frame on the scene. Images quantities can be associated with the cameras and displayed on the camera frame. You can even align the interactive viewport with a selected camera.

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/camera_view_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

!!! info "Add an Image Quantity!"

    Camera views structures on their own are not so interesting; they are simplify displayed as a wireframe camera widget in the viewport.

    Try adding an [Image Quantitiy]([[url.prefix]]/structures/floating_quantities/images) to the camera view. When image quantities are added to camera view structures, they gain the additional ability to be displayed in the camera's frame.


**Example:**

```python
import polyscope as ps
import numpy as np

ps.init()

# Create a camera view from parameters
intrinsics = ps.CameraIntrinsics(fov_vertical_deg=60, aspect=2)
extrinsics = ps.CameraExtrinsics(root=(2., 2., 2.), look_dir=(-1., -1.,-1.), up_dir=(0.,1.,0.))
params = ps.CameraParameters(intrinsics, extrinsics)
cam = ps.register_camera_view("cam", params)

# Set some options for the camera view
# these can also be set as keyword args in register_camera_view()
cam.set_widget_focal_length(0.75)          # size of displayed widget (relative value)
cam.set_widget_thickness(0.25)             # thickness of widget lines
cam.set_widget_color((0.25, 0.25, 0.25))   # color of widget lines


# Add an image to be displayed in the camera frame
dimX = 600
dimY = 300
cam.add_scalar_image_quantity("scalar_img", np.zeros((dimX, dimY)),
                              enabled=True, show_in_camera_billboard=True)

ps.show(3)
```


## Registering a Camera View

Camera views are created from [Camera Parameters]([[url.prefix]]/basics/camera_controls/#camera-parameters).

Note that we **do not** specify an image resolution for the camera view. It can hold images of any resolution, as long as the aspect ratio is right.


??? func "`#!python register_camera_view(name, params, **kwargs)`"

    Add a new camera view structure to Polyscope.

    - `params` is a [Camera Parameters]([[url.prefix]]/basics/camera_controls/#camera-parameters).
    
    Additional optional keyword arguments:

    - `enabled` boolean, is the structure enabled initially
    - `widget_focal_length` float, size of displayed widget (relative value)
    - `widget_thickness` float, thickness of widget lines
    - `widget_color` float 3-tuple, color of widget lines


As with all structures, there is also `get_camera_view("name")`, `has_camera_view("name")`, and `remove_camera_view("name")`.


## Updating a Camera View

You can update the parameters associated with a camera view to move it within the scene after creation.

??? func "`#!python CameraView.update_camera_parameters(new_params)`"

    Update camera parameters.

    - `params` is a [Camera Parameters]([[url.prefix]]/basics/camera_controls/#camera-parameters).


## Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
focal length | size of rendered widget | `#!python get_widget_focal_length()` | `#!python set_widget_focal_length(newVal, relative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
thickness | rendered widget line thickness | `#!python get_widget_thickness()` | `#!python set_widget_thickness(newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
color | widget color | `#!python get_widget_color()` | `#!python set_widget_color(newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
