These settings affect the 3D camera view in polyscope. It is often convenient to set them just before calling `polyscope::init`, but they may set be anywhere.

```cpp
#include "polyscope/polyscope.h"

// a few camera options
polyscope::view::upDir = UpDir::ZUp;
polyscope::view::style = NavigateStyle::Free;

// initialize
polyscope::init();
```

### Options

??? func "`#!cpp NavigateStyle view::style`"

    ##### navigation style
   
    The style of the camera navigation. Affects what happens when you drag to rotate around the 3D view with your mouse.

    This value can be manually set under the `view` menu of the ui. Programmatically, the enum `view::NavigateStyle` contains various settings:

    - `NavigateStyle::Turntable` The up direction (see below) is always fixed vertically, with rotation along the azumith and altitude directions.
    - `NavigateStyle::Free` The camera is free to take any orientation, rotation is always about relative to the current camera.
    - `NavigateStyle::Planar` The camera is locked in to a 2D view of the XY plane, with no rotation (see [2D data](/features/2D_data)).


    Example:
    ```cpp
    polyscope::view::style = NavigateStyle::Free;
    ```

??? func "`#!cpp UpDir view::upDir`"

    ##### up direction

    3D data is typically oriented with some natural "up" direction, but not everyone agrees as to which coordinate axis is "up".
    Computer graphics and vision often use a Y-up convention, where science and engineering more commonly use Z-up.

    This setting affects default orientation of the view, the behavior of some navigation styles (esp. `Turntable`), and the orientation of the ground plane.

    This value can be manually set under the `view` menu of the ui. Programmatically, the enum `view::UpDir` contains various settings:

    - `UpDir::XUp` The positive X-axis is up.
    - `UpDir::YUp` The positive Y-axis is up.
    - `UpDir::ZUp` The positive Z-axis is up.
   
    Default: `UpDir::Yup`.

    Example:
    ```cpp
    polyscope::view::upDir = UpDir::ZUp;
    ```
