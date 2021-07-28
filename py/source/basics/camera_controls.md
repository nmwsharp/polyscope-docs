These settings affect the 3D camera view in polyscope. It is often convenient to set them just before calling `polyscope.init()`, but they may generally be set anywhere.

```python
import polyscope as ps
import numpy as np

ps.set_navigation_style("free")
ps.set_up_dir("z_up")

# initialize
ps.init()
   
# set the camera pose explicitly
ps.look_at((0., 0., 5.), (1., 1., 1.))

# (alternately, use numpy vectors)
ps.look_at(np.array((0., 0., 5.)), np.array((1., 1., 1.)))

# show the GUI
ps.show()
```

### Options

??? func "`#!python set_navigation_style(s)`"

    ##### navigation style
   
    The style of the camera navigation. Affects what happens when you drag to rotate around the 3D view with your mouse.

    This value can be manually set under the `view` menu of the ui. Programmatically, pass a string for the following settings:

    - `'turntable'` The up direction (see below) is always fixed vertically, with rotation along the azumith and altitude directions.
    - `'free'` The camera is free to take any orientation, rotation is always about relative to the current camera.
    - `'planar'` The camera is locked in to a 2D view of the XY plane, with no rotation (see [2D data](/features/2D_data)).

    Default: `'turntable'`.

    Example:
    ```python
    import polyscope as ps
    ps.set_navigation_style("free")
    ```

??? func "`#!python set_up_dir(s)`"

    ##### up direction

    3D data is typically oriented with some natural "up" direction, but not everyone agrees as to which coordinate axis is "up".
    Computer graphics and vision often use a Y-up convention, where science and engineering more commonly use Z-up.

    This setting affects default orientation of the view, the behavior of some navigation styles (esp. `turntable`), and the orientation of the ground plane.

    This value can be manually set under the `view` menu of the ui. Programmatically, the setting strings are:

    - `'x_up'` The positive X-axis is up.
    - `'neg_x_up'` The negative X-axis is up.
    - `'y_up'` The positive Y-axis is up.
    - `'neg_y_up'` The negative Y-axis is up.
    - `'z_up'` The positive Z-axis is up.
    - `'neg_z_up'` The negative Z-axis is up.
   
    Default: `'y_up'`.

    Example:
    ```python
    import polyscope as ps
    ps.set_up_dir("z_up")
    ```


??? func "`#!python look_at(camera_location, target, fly_to=False)`"

    ##### look at

    Set the camera to be located at the 3D position `camera_location` and looking at the 3D position `target`, both in world coordinates. The up direction for the camera is set to be the scene's up direction. If `fly_to=True`, the camera will smoothly animate to the new configuration.

    The input 3D vectors can be tuples, length-3 numpy arrays, or really anything that can be indexed for three components.

    Example:
    ```python
    polyscope.look_at((0., 0., 5.), (1., 1., 1.))
    ```

??? func "`#!python look_at_dir(camera_location, target, up_dir, fly_to=False)`"
    
    Set the camera to be located at the 3D position `camera_location` and looking at the 3D position `target`, oriented with the up direction `up_dir`, all in world coordinates. If `fly_to=True`, the camera will smoothly animate to the new configuration.

    Note that setting the up direction for the camera view with this function is separate from the scene's up direction with `set_up_dir()`, which affects things like ground plane placement, and manual view manipulation.

    The input 3D vectors can be tuples, length-3 numpy arrays, or really anything that can be indexed for three components.

    Example:
    ```python
    polyscope.look_at_dir((0., 0., 5.), (1., 1., 1.), (-1., -1., 0.))
    ```

??? func "`#!python reset_camera_to_home_view()`"

    ##### reset camera to home view

    Reset the camera view to the home view (a reasonable default view scaled to the scene).

    **Note:** The "home" view is dependent on the data in the scene; it is computed from the bounding boxes of all registered structures to ensure that everything is nicely scaled and in view. As such, one should generally call this function _after_ registering data.

    Example:
    ```python
    ps.reset_camera_to_home_view()
    ```
