These settings affect the 3D camera view in polyscope. It is often convenient to set them just before calling `polyscope::init`, but they may set be anywhere.

```cpp
#include "polyscope/polyscope.h"

// a few camera options
polyscope::view::upDir = UpDir::ZUp;
polyscope::view::style = NavigateStyle::Free;

// initialize
polyscope::init();

// set the camera pose explicitly
polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.});

// show the GUI
polyscope::show();
```

### Options

??? func "`#!cpp NavigateStyle view::style`"

    ##### navigation style
   
    The style of the camera navigation. Affects what happens when you drag to rotate around the 3D view with your mouse.

    This value can be manually set under the `view` menu of the ui. Programmatically, the enum `view::NavigateStyle` contains various settings:

    - `NavigateStyle::Turntable` The up direction (see below) is always fixed vertically, with rotation along the azumith and altitude directions.
    - `NavigateStyle::Free` The camera is free to take any orientation, rotation is always about relative to the current camera.
    - `NavigateStyle::Planar` The camera is locked in to a 2D view of the XY plane, with no rotation (see [2D data]({{url.prefix}}/features/2D_data)).


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
    - `UpDir::NegXUp` The negative X-axis is up.
    - `UpDir::YUp` The positive Y-axis is up.
    - `UpDir::NegYUp` The negative Y-axis is up.
    - `UpDir::ZUp` The positive Z-axis is up.
    - `UpDir::NegZUp` The negative Z-axis is up.
   
    Default: `UpDir::Yup`.

    Example:
    ```cpp
    polyscope::view::upDir = UpDir::ZUp;
    ```

??? func "`#!cpp void lookAt(glm::vec3 cameraLocation, glm::vec3 target, bool flyTo = false)`"
    
    ##### look at

    Set the camera to be located at the 3D position `cameraLocation` and looking at the 3D position `target`, both in world coordinates. The up direction for the camera is set to be the scene's up direction. If `flyTo=true`, the camera will smoothly animate to the new configuration.

    Example:
    ```cpp
    polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.});
    ```

??? func "`#!cpp void lookAt(glm::vec3 cameraLocation, glm::vec3 target, glm::vec3 upDir, bool flyTo = false)`"
    
    Set the camera to be located at the 3D position `cameraLocation` and looking at the 3D position `target`, oriented with the up direction `upDir`, all in world coordinates. If `flyTo=true`, the camera will smoothly animate to the new configuration.

    Note that setting the up direction for the camera view with this function is separate from the scene's `view::upDir` parameter, which affects things like ground plane placement, and manual view manipulation.

    Example:
    ```cpp
    polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.}, glm::vec3{0., 0., 1.});
    ```


??? func "`#!cpp void resetCameraToHomeView()`"

    ##### reset camera to home view

    Reset the camera view to the home view (a reasonable default view scaled to the scene).

    **Note:** The "home" view is dependent on the data in the scene; it is computed from the bounding boxes of all registered structures to ensure that everything is nicely scaled and in view. As such, one should generally call this function _after_ registering data.

    Example:
    ```cpp
    polyscope::view::resetCameraToHomeView();
    ```
