These settings affect the 3D camera view in polyscope. It is often convenient to set them just before calling `polyscope::init`, but they may set be anywhere.

```cpp
#include "polyscope/polyscope.h"

// a few camera options
polyscope::view::setUpDir(polyscope::UpDir::ZUp);
polyscope::view::setFrontDir(polyscope::FrontDir::NegYFront);
polyscope::view::setNavigateStyle(polyscope::NavigateStyle::Free);

// initialize
polyscope::init();

// set the camera pose explicitly
polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.});

// show the GUI
polyscope::show();
```

### Options

??? func "`#!cpp void view::setNavigateStyle(NavigateStyle newStyle)`"

    ##### navigation style
   
    The style of the camera navigation. Affects what happens when you drag to rotate around the 3D view with your mouse.

    This value can be manually set under the `view` menu of the ui. Programmatically, the enum `view::NavigateStyle` contains various settings:

    - `NavigateStyle::Turntable` The up direction (see below) is always fixed vertically, with rotation along the azumith and altitude directions.
    - `NavigateStyle::Free` The camera is free to take any orientation, rotation is always about relative to the current camera.
    - `NavigateStyle::Planar` The camera is locked in to a 2D view of the XY plane, with no rotation (see [2D data]([[url.prefix]]/features/2D_data)).


    Example:
    ```cpp
    polyscope::view::setNavigateStyle(NavigateStyle::Free);
    ```

??? func "`#!cpp NavigateStyle view::getNavigateStyle()`"

    Get the current navigation style (see explanation in the setter above)


??? func "`#!cpp void view::setUpDir(UpDir newDir)`"

    ##### up direction

    Set the default "up" direction for the scene. This setting affects default orientation of the view, the behavior of some navigation styles (esp. `Turntable`), and the orientation of the ground plane.

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
    polyscope::view::setUpDir(UpDir::ZUp);
    ```

??? func "`#!cpp UpDir view::getUpDir()`"

    Get the current up direction (see explanation in the setter above).

??? func "`#!cpp void view::setFrontDir(FrontDir newDir)`"

    ##### front direction

    Set the default "front" direction for the scene. This setting affects default orientation of the view; the starting camera looks at the front of the data.

    This value is interpeted as if the scene were a cube, and you are specifying which face of the cube is the 'front'. So `ZFront` means the +Z face of the cube is the front face, and thus our camera initially points down the -Z axis to look at it.

    This value can be manually set under the `view` menu of the ui. Programmatically, the enum `view::FrontDir` contains various settings:

    - `FrontDir::XFront` The positive X-axis is the front.
    - `FrontDir::NegXFront` The negative X-axis is the front.
    - `FrontDir::YFront` The positive Y-axis is the front.
    - `FrontDir::NegYFront` The negative Y-axis is the front.
    - `FrontDir::ZFront` The positive Z-axis is the front.
    - `FrontDir::NegZFront` The negative Z-axis is the front.
   
    Default: `FrontDir::ZFront`.

    Example:
    ```cpp
    polyscope::view::setFrontDir(FrontDir::NegYFront);
    ```

??? func "`#!cpp FrontDir view::getFrontDir()`"

    Get the current front direction (see explanation in the setter above).

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

#### Orthographic view

By default, Polyscope's view uses [perspective projection](https://en.wikipedia.org/wiki/3D_projection#Perspective_projection). Perspective projections roughly correspond to how images are usually perceived by our eyes and cameras.

Alternately [orthographic projection](https://en.wikipedia.org/wiki/3D_projection#Orthographic_projection) is also supported. Orthographic projections are common in engineering and architecture, because they have the property that distances are preserved in the projected image, regardless of whether the object is near or far from the camera.

![image of perspective and orthographic projection]([[url.prefix]]/media/projection_diagram.jpg)

In perspective mode, zooming (for instance, by manually scrolling the mouse) translates the camera forward in space. In orthographic mode, it instead adjusts the field of view without moving the camera. This is because counter-intuitively, translating the camera forward does not actually change the view in an orthographic projection!


??? func "`#!cpp ProjectionMode view::projectionMode`"

    ##### set projection mode

    Set the camera view projection to be either orthographic or perspective (default).

    Example:
    ```cpp
    // Enable the orthographic view
    polyscope::view::projectionMode = polyscope::ProjectionMode::Orthographic;

    // Go back to default perspective projection
    polyscope::view::projectionMode = polyscope::ProjectionMode::Perspective;
    ```

#### Saving/restoring views

The current camera view (location, direction, camera parameters, and window size) can be saved or loaded from a json string. This is useful for quickly setting up repeatable visualizations.

Also, in the Polyscope GUI, this string can be copied to the clipboard at any time via the "copy" hotkey (ctrl-C or cmd-C), or loaded from your current clipboard using the "paste" hotkey (ctrl-V or cmd-V).

??? func "`#!cpp std::string getViewAsJson()`"

    Get the current view parameters specified as a json string.

    Example:
    ```cpp
    std::string myString = polyscope::view::getViewAsJson();
    ```
    

??? func "`#!cpp void setViewFromJson(std::string jsonString, bool animateFlight=false)`"

    Set the current view to match the parameters specified in the json string.

    Example:
    ```cpp
    polyscope::view::setViewFromJson(myString);
    ```
