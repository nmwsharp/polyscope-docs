These functions control the current viewing camera in for the Polyscope scene, as well as more-generally managing camera parameters across visualizations, such as for [Camera View structures]([[url.prefix]]/structures/camera_view/basics).

**Example of common camera operations:**
```cpp
#include "polyscope/polyscope.h"

// set the size of the window
polyscope::view::setWindowSize(600, 800);

// change the default up-direction or front-direction for the scene
polyscope::view::setUpDir(polyscope::UpDir::ZUp);
polyscope::view::setFrontDir(polyscope::FrontDir::NegYFront);

// change the navigation style (default is Turntable)
polyscope::view::setNavigateStyle(polyscope::NavigateStyle::Free);

// get the current camera matrix or position
glm::mat4 viewMat = polyscope::view::getCameraViewMatrix();
glm::vec3 pos = polyscope::view::getCameraWorldPosition();

// set the current camera matrix or position
polyscope::view::setCameraViewMatrix(viewMat);
polyscope::view::setCameraWorldPosition(pos);

// set the current camera pose to look-at something in the scene
polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.});

// manipulate the current camera with the CameraParameters object,
// which standardizes all camera information
polyscope::CameraParameters currParams = 
    polyscope::view::getCameraParametersForCurrentView();
polyscope::view::setCameraParametersForCurrentView(cam_params):

// you can even use the parameters to create a camera view structure,
// which visualize views of the scene as a frame and can hold image
// quantities
polyscope::CameraView* cam = polyscope::registerCameraView("cam1", params) 
```

## Window Controls

Get and set the size of the window which appears on the user's display.

??? func "`#!cpp void view::setWindowSize(int width, int height)`"

    Set the size of the window.

    Note that for some platforms, on high-DPI screens the pixel buffer resolution may be different from the logical size. This is the logical size.

??? func "`#!cpp std::tuple<int, int> getWindowSize()`"

    Get the current size of the window.

    Note that for some platforms, on high-DPI screens the pixel buffer resolution may be different from the logical size. This is the logical size.

??? func "`#!cpp std::tuple<int, int> getBufferSize()`"

    Get the current pixel buffer resolution of the window.

    Note that for some platforms, on high-DPI screens the pixel buffer resolution may be different from the logical size. This is the pixel buffer size.

??? func "`#!cpp void view::setWindowResizable(bool newVal)`"

    If `false`, the window will be locked to size and the OS will not allow it to be resized. (Default: `true`)

    There is also a corresponding `getWindowResizable()`.


## Manipulating the Current View

These settings affect the 3D camera view in polyscope. It is often convenient to set them just before calling `polyscope::init()`, but they may set be anywhere.

**View Getters:**
```cpp
CameraParameters view::getCameraParametersForCurrentView(); // contains all of this info

// (these friendly helpers get the same info as ^^^)
glm::mat4 view::getCameraViewMatrix();
void view::setCameraViewMatrix(glm::mat4 newMat);
glm::mat4 view::getCameraPerspectiveMatrix();
glm::vec3 view::getCameraWorldPosition();
void view::getCameraFrame(glm::vec3& lookDir, glm::vec3& upDir, glm::vec3& rightDir);
glm::vec3 view::getUpVec();
glm::vec3 view::getFrontVec();
float view::getVerticalFieldOfViewDegrees();
float view::getAspectRatioWidthOverHeight();
```

??? func "`#!cpp CameraParameters view::getCameraParametersForCurrentView()`"

    Get the camera parameters (intrinsic and extrinsics) that describe the current viewport view. 

    See the section below for additional methods to get values from the camera parameters.

    Example:
    ```cpp
    polyscope::CameraParameters currParams = 
        polyscope::view::getCameraParametersForCurrentView();

    // get some data from the parameters
    float fovVert = currParams.getFoVVerticalDegrees();
    float aspect = currParams.getAspectRatioWidthOverHeight();
    glm::mat4x4 view_mat = currParams.getViewMat();
    glm::vec3 pos = currParams.getPosition();
    ```


**View Setters:**
```cpp
void view::setViewToCamera(const CameraParameters& p); // contains all of this info

// (these friendly helpers set the same info as ^^^)
void view::setCameraViewMatrix(glm::mat4 newMat);
void view::lookAt(glm::vec3 cameraLocation, glm::vec3 target, bool flyTo = false);
void view::lookAt(glm::vec3 cameraLocation, glm::vec3 target, glm::vec3 upDir, bool flyTo = false);
void view::setVerticalFieldOfViewDegrees(float newVal);
// there is no aspect ratio setter: it is determined by the window size
```

??? func "`#!cpp void view::setCameraParametersForCurrentView(const CameraParameters& params)`"

    Set the camera parameters (intrinsic and extrinsics) that describe the current viewport view. 

    See the section below for additional methods to construct these camera parameters.

    Example:
    ```cpp
    polyscope::CameraParameters newParams(
            polyscope::CameraIntrinsics::fromFoVDegVerticalAndAspect(60, 2.),
            polyscope::CameraExtrinsics::fromVectors(
                glm::vec3{2., 2., 2.},      // world-space position
                glm::vec3{-1., 0., 0.},     // world-space look direction
                glm::vec3{0., 1., 0.}       // world-space up direction
            )
        );

    polyscope::view::setCameraParametersForCurrentView(newParams);
    ```

### Look-At

The look-at functions are particularly easy to use to position the camera towards content of interest.

??? func "`#!cpp void view::lookAt(glm::vec3 cameraLocation, glm::vec3 target, bool flyTo = false)`"

    Set the camera to be located at the 3D position `cameraLocation` and looking at the 3D position `target`, both in world coordinates. The up direction for the camera is set to be the scene's up direction. If `flyTo=true`, the camera will smoothly animate to the new configuration.

    Example:
    ```cpp
    polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.});
    ```

??? func "`#!cpp void view::lookAt(glm::vec3 cameraLocation, glm::vec3 target, glm::vec3 upDir, bool flyTo = false)`"
    
    Set the camera to be located at the 3D position `cameraLocation` and looking at the 3D position `target`, oriented with the up direction `upDir`, all in world coordinates. If `flyTo=true`, the camera will smoothly animate to the new configuration.

    Note that setting the up direction for the camera view with this function is separate from the scene's `view::upDir` parameter, which affects things like ground plane placement, and manual view manipulation.

    Example:
    ```cpp
    polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.}, glm::vec3{0., 0., 1.});
    ```

### Home View

The home view is a reasonable default camera view, computed based on the up- and front- direction, as well as the scene extents which may be computed automatically from data you have registered.

By default, the camera is located at the home view when the scene is first opened. You can also return it to that view at any time with `view::resetCameraToHomeView()`.

??? func "`#!cpp void view::resetCameraToHomeView()`"

    Reset the camera view to the home view (a reasonable default view scaled to the scene).

    **Note:** The "home" view is dependent on the data in the scene; it is computed from the bounding boxes of all registered structures to ensure that everything is nicely scaled and in view. As such, one should generally call this function _after_ registering data.

    Example:
    ```cpp
    polyscope::view::resetCameraToHomeView();
    ```


## Navigation Style

The navigation style affects how the user's mouse interactions navigate the scene. The default is a Turntable rotating around the current canonical `Up` direction.

**Navigation Styles Enum**:

- `NavigateStyle::Turntable` The up direction (see below) is always fixed vertically, with rotation along the azumith and altitude directions.
- `NavigateStyle::Free` The camera is free to take any orientation, rotation is always about relative to the current camera.
- `NavigateStyle::Planar` The camera is locked in to a 2D view of the XY plane, with no rotation (see [2D data]([[url.prefix]]/features/2D_data)).


??? func "`#!cpp void view::setNavigateStyle(NavigateStyle newStyle)`"
   
    The style of the camera navigation. Affects what happens when you drag to rotate around the 3D view with your mouse.

    This value can be manually set under the `view` menu of the ui. 

    Example:
    ```cpp
    polyscope::view::setNavigateStyle(NavigateStyle::Free);
    ```

??? func "`#!cpp NavigateStyle view::getNavigateStyle()`"

    Get the current navigation style (see explanation in the setter above)

## Canonical Up and Front

Unfortunately, no one can agree which cartesian direction is "up" in a 3D scene. Polyscope does not assume any particular up direction, it can be configured (default is `Y-up`).

This effects many defaults of the scene, such as how the camera is oriented and where the ground plane is placed. 

??? func "`#!cpp void view::setUpDir(UpDir newDir)`"

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

A default front direction can also be configured, which effects the placement of the home camera location.

??? func "`#!cpp void view::setFrontDir(FrontDir newDir)`"

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



## Perspective and Orthographic Views

By default, Polyscope's view uses [perspective projection](https://en.wikipedia.org/wiki/3D_projection#Perspective_projection). Perspective projections roughly correspond to how images are usually perceived by our eyes and cameras.

Alternately [orthographic projection](https://en.wikipedia.org/wiki/3D_projection#Orthographic_projection) is also supported. Orthographic projections are common in engineering and architecture, because they have the property that distances are preserved in the projected image, regardless of whether the object is near or far from the camera.

![image of perspective and orthographic projection]([[url.prefix]]/media/projection_diagram.jpg)

In perspective mode, zooming (for instance, by manually scrolling the mouse) translates the camera forward in space. In orthographic mode, it instead adjusts the field of view without moving the camera. This is because counter-intuitively, translating the camera forward does not actually change the view in an orthographic projection!


??? func "`#!cpp ProjectionMode view::projectionMode`"

    Set the camera view projection to be either orthographic or perspective (default).

    Example:
    ```cpp
    // Enable the orthographic view
    polyscope::view::projectionMode = polyscope::ProjectionMode::Orthographic;

    // Go back to default perspective projection
    polyscope::view::projectionMode = polyscope::ProjectionMode::Perspective;
    ```

## Centering the View on Scene Content

To focus on particular areas of interest, hold ctrl+shift (cmd+shift on macOS) and click in the scene. This will re-center the view in the clicked location. You can also hold ctrl+shift (cmd+shift on macOS) and scroll to zoom relative to selected center location, which makes it easer to zoom in on small details. Use the Reset View button to reset the center of interest.

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/rotation_center.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

??? func "`#!cpp void view::setViewCenter(glm::vec3 newCenter, bool flyTo = false)`"

    Programmatically set the view center to a location in world-space. For example, with the Turntable view, this changes the center of rotation.

    For some view types, the view must immediately be projected to conform to the new center. If `flyTo=true` this projection will be a smooth flight, otherwise it will be instantaneous.


## Saving/Restoring views

The current camera view (location, direction, camera parameters, and window size) can be saved or loaded from a json string. This is useful for quickly setting up repeatable visualizations.

Also, in the Polyscope GUI, this string can be copied to the clipboard at any time via the "copy" hotkey (ctrl-C or cmd-C), or loaded from your current clipboard using the "paste" hotkey (ctrl-V or cmd-V).

??? func "`#!cpp std::string view::getViewAsJson()`"

    Get the current view parameters specified as a json string.

    Example:
    ```cpp
    std::string myString = polyscope::view::getViewAsJson();
    ```
    

??? func "`#!cpp void view::setViewFromJson(std::string jsonString, bool animateFlight=false)`"

    Set the current view to match the parameters specified in the json string.

    Example:
    ```cpp
    polyscope::view::setViewFromJson(myString);
    ```

## Camera Parameters Objects

`CameraParameters` objects describe a camera view in Polyscope, including its _intrinsics_ (the field of view and aspect ratio), and _extrinsics_ (the location and orientation). These parameters are used both for manipulations of the interactive viewport, as well as creating [Camera View structures]([[url.prefix]]/structures/camera_view/basics) which are visualized as part of the content in your scene.

**Example:**
```cpp
// construct camera parameters 
polyscope::CameraParameters params(
            polyscope::CameraIntrinsics::fromFoVDegVerticalAndAspect(60, 2.),
            polyscope::CameraExtrinsics::fromVectors(
                glm::vec3{2., 2., 2.},      // world-space position
                glm::vec3{-1., 0., 0.},     // world-space look direction
                glm::vec3{0., 1., 0.}       // world-space up direction
            )
        );

// set the viewport view to those parameters
polyscope::view::setViewToCamera(params);

// get the current viewport view
polyscope::CameraParameters currParams = 
    polyscope::view::getCameraParametersForCurrentView();

// or, use the parameters to create a camera view
polyscope::CameraView* cam = polyscope::registerCameraView("cam1", params);
```

### Intrinsics

A `CameraIntrinsics` object describes the field of view and aspect ratio of a camera. It **does not** describe a "pixel resolution" for a camera---you could have many images of different resolutions all associated with the same camera, as long as the aspect ratios are right.

Camera intrinsics can be created by specifying any pair of vertical field of view, horizontal field of view, and aspect ratio.

??? func "`#!cpp static CameraIntrinsics CameraIntrinsics::fromFoVDegVerticalAndAspect(const float& fovVertDeg, const float& aspectRatioWidthOverHeight)`"

    Construct camera intrinsics.

    - `fovVertDeg` vertical field of view in degrees
    - `aspectRatioWidthOverHeight` aspect ratio, as `width / height`

    This is a **static named constructor**. Call it like
    ```cpp
    CameraIntrinsics camInt = CameraIntrinsics::fromFoVDegVerticalAndAspect(20., 2.);
    ```

??? func "`#!cpp static CameraIntrinsics CameraIntrinsics::fromFoVDegHorizontalAndAspect(const float& fovHorzDeg, const float& aspectRatioWidthOverHeight)`"

    Construct camera intrinsics.

    - `fovHorzDeg` horizontal field of view in degrees
    - `aspectRatioWidthOverHeight` aspect ratio, as `width / height`

    This is a **static named constructor**. Call it like
    ```cpp
    CameraIntrinsics camInt = CameraIntrinsics::fromFoVDegHorizontalAndAspect(20., 2.);
    ```

??? func "`#!cpp static CameraIntrinsics CameraIntrinsics::fromFoVDegHorizontalAndVertical(const float& fovHorzDeg, const float& fovVertDeg)`"

    Construct camera intrinsics.

    - `fovHorzDeg` horizontal field of view in degrees
    - `fovVertDeg` vertical field of view in degrees

    This is a **static named constructor**. Call it like
    ```cpp
    CameraIntrinsics camInt = CameraIntrinsics::fromFoVDegHorizontalAndVertical(20., 30.);
    ```

Various getters access the properties of an intrinsics object:
```cpp
float CameraIntrinsics::getFoVVerticalDegrees()             // vertical FoV
float CameraIntrinsics::getAspectRatioWidthOverHeight()     // horizontal FoV
```

### Extrinsics

A `CameraExtrinsics` object describes the location and orientation of a camera. It can be defined by the forward/up/right axes of the camera in world coordinates, or via an extrinsic matrix, typically denoted `E`, which maps points in world coordinates to points in the camera's local coordinate system. Polyscope uses openGL conventions for camera space, such that the camera points toward the -Z axis, with +Y pointing up and +X pointing right.

Camera extrinsics can be created by specifying frame axes or an extrinsic matrix.

??? func "`#!cpp static CameraExtrinsics CameraExtrinsics::fromVectors(const T1& root, const T2& lookDir, const T3& upDir)`"

    Construct camera extrinsics.

    - `root` the world-space position of the camera
    - `lookDir` a world-space unit vector along which the camera looks
    - `upDir` a world-space unit vector defining the up axis for the camera

    These are all 3D vectors, and can be any type which is accessible via Polyscope's [data adaptors](/data_adaptors/).

    This is a **static named constructor**. Call it like
    ```cpp
    CameraExtrinsics camExt = CameraExtrinsics::fromVectors(rootVec, lookDir, upDir);
    ```

??? func "`#!cpp static CameraExtrinsics CameraExtrinsics::fromMatrix(const glm::mat4& E)`"

    Construct camera extrinsics.

    - `E` is a 4x4 matrix mapping points in world-space to local camera space. Polyscope's camera space uses openGL convention.

    This is a **static named constructor**. Call it like
    ```cpp
    CameraExtrinsics camExt = CameraExtrinsics::fromMatrix(E_mat);
    ```

Various getters access the properties of an extrinsics object:
```cpp
glm::vec3       CameraExtrinsics::getT()
glm::mat3x3     CameraExtrinsics::getR()
glm::mat4x4     CameraExtrinsics::getViewMat() // synonym for getE()
glm::mat4x4     CameraExtrinsics::getE()
glm::vec3       CameraExtrinsics::getPosition()
glm::vec3       CameraExtrinsics::getLookDir()
glm::vec3       CameraExtrinsics::getUpDir()
glm::vec3       CameraExtrinsics::getRightDir()
std::tuple<glm::vec3, glm::vec3, glm::vec3> CameraExtrinsics::getCameraFrame() // <look, up, right> world-space vectors
```
### Camera Parameters

The `CameraParameters` object combines a set of intrinsics and extrinsics to fully define a camera.


??? func "`#!cpp CameraParameters(const CameraIntrinsics& intrinsics, const CameraExtrinsics& extrinsics)`"

    Construct camera parameters from intrinsics and extrinsics.

    This is a plain old constructor. Call it like
    ```cpp
    CameraExtrinsics camExt = CameraExtrinsics::fromMatrix(E_mat);
    CameraIntrinsics camInt = CameraIntrinsics::fromFoVDegHorizontalAndVertical(20., 30.);
    CameraParameters camParam(camInt, camExt);
    ```


Various getters access the properties of the parameters object. All getters for the intrinsics and extrinsics are also forwarded to the combined parameters class.
```cpp
// intrinsics
float CameraParameters::getFoVVerticalDegrees()             // vertical FoV
float CameraParameters::getAspectRatioWidthOverHeight()     // horizontal FoV

// extrinsics
glm::vec3       CameraParameters::getT()
glm::mat3x3     CameraParameters::getR()
glm::mat4x4     CameraParameters::getViewMat() // synonym for getE()
glm::mat4x4     CameraParameters::getE()
glm::vec3       CameraParameters::getPosition()
glm::vec3       CameraParameters::getLookDir()
glm::vec3       CameraParameters::getUpDir()
glm::vec3       CameraParameters::getRightDir()
std::tuple<glm::vec3, glm::vec3, glm::vec3> CameraParameters::getCameraFrame() // <look, up, right> world-space vectors
```


#### Generating pixel rays

It is often necessary to generate the world-space ray corresponding to each pixel of an image in a camera view. The base point for these rays is easy, it is just `params.getPosition()`. However the ray directions vary-per pixel; the `CameraParameters` object has two helpers to automatically construct these rays.

??? func "`#!cpp std::vector<glm::vec3> CameraParameters::generateCameraRays(size_t w, size_t h, ImageOrigin origin = ImageOrigin::UpperLeft)`"

    Fill a buffer with rays corresponding to an image with the given resolution. The result is a `w*h`-length buffer, flattened such that each row is stored contiguously. Ray origins are all implicitly given by `this->getPosition()`.


??? func "`#!cpp std::array<glm::vec3, 4> CameraParameters::generateCameraRayCorners()`"

    Generate the rays corresponding to the [upperleft, upperright, lowerleft, lowerright] corners of the camera's view. 

    This method is useful because the caller can easily linearly interpolate the normalize get ray directions for all pixels in an image, but this method just needs to return a small amount of data. This makes it easy to e.g. generate rays for a real-time renderer on a GPU, without transferring a whole buffer of ray directions for each frame.
