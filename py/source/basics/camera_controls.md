These settings affect the 3D camera view in polyscope. It is often convenient to set them just before calling `polyscope.init()`, but they may generally be set anywhere.

```python
import polyscope as ps

ps.set_navigation_style("free")
ps.set_up_dir("z_up")

# initialize
ps.init()
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
    - `'y_up'` The positive Y-axis is up.
    - `'z_up'` The positive Z-axis is up.
   
    Default: `'y_up'`.

    Example:
    ```python
    import polyscope as ps
    ps.set_up_dir("z_up")
    ```
