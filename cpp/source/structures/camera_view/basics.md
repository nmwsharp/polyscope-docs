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

```cpp
#include "polyscope/camera_view.h"
polyscope::init();

// Create a camera view from parameters
polyscope::CameraParameters params(
                polyscope::CameraIntrinsics::fromFoVDegVerticalAndAspect(60, 2.),
                polyscope::CameraExtrinsics::fromVectors(
                        glm::vec3{2., 2., 2.},      // root position
                        glm::vec3{-1., 0., 0.},   // look direction 
                        glm::vec3{0., 1., 0.})      // up direction
                );

polyscope::CameraView* cam1 = polyscope::registerCameraView("cam1", params);

// Set some options for the camera view
cam1->setWidgetFocalLength(0.75);           // size of displayed widget (relative value)
cam1->setWidgetThickness(0.25);             // thickness of widget lines
glm::vec3 c = glm::vec3{0.25, 0.25, 0.25}; 
cam1->setWidgetColor(c);                    // color of widget lines


// Add an image to be displayed in the camera frame
int width = 600;
int height = 300;
std::vector<std::array<float, 3>> imageColor(width * height); // fill with your data
polyscope::ColorImageQuantity* im = 
    cam1->addColorImageQuantity("color image", width, height, imageColor, 
                                polyscope::ImageOrigin::UpperLeft);
im->setEnabled(true);
im->setShowInCameraBillboard(true);

polyscope::show(3);
```


## Registering a Camera View

Camera views are created from [Camera Parameters]([[url.prefix]]/basics/camera_controls/#camera-parameters).

Note that we **do not** specify an image resolution for the camera view. It can hold images of any resolution, as long as the aspect ratio is right.


??? func "`#!cpp CameraView* registerCameraView(std::string name, const CameraParameters& params)`"

    Add a new camera view structure to Polyscope.

    - `params` is a [Camera Parameters](/basics/camera_controls/#camera-parameters).


As with all structures, there is also `getCameraView("name")`, `hasCameraView("name")`, and `removeCameraView("name")`.


## Updating a Camera View

You can update the parameters associated with a camera view to move it within the scene after creation.

??? func "`#!cpp void CameraView::updateCameraParameters(const CameraParameters& newParams)`"

    Update camera parameters.

    - `params` is a [Camera Parameters]([[url.prefix]]/basics/camera_controls/#camera-parameters).


## Selection / Picking

"Picking" refers to selecting and inspecting elements by clicking on the object in the scene.  As with other structures, you can call `interpretPickResult()` to get additional info about a click. See [the overview of Selection / Picking]([[url.prefix]]/basics/interactive_UIs_and_animation/#selection-picking) for general information.

```cpp
struct CameraViewPickResult {
  // currently nothing, just following the same pattern as other structures
};
```

??? func "`#!cpp CameraViewPickResult CameraView::interpretPickResult(PickResult result)`"

    Get additional information about a click.

## Options

See [structure management]([[url.prefix]]/structures/structure_management/#structure-options) for options common to all structures such as enabling/disabling, transforms, and transparency.


**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
focal length | size of rendered widget | `#!cpp double getWidgetFocalLength()` | `#!cpp setWidgetFocalLength(double newVal, bool isRelative=true)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
thickness | rendered widget line thickness | `#!cpp double getWidgetThickness()` | `#!cpp setWidgetThickness(double newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
color | widget color | `#!cpp glm::vec3 getWidgetColor()` | `#!cpp setWidgetColor(glm::vec3 newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |

_(All setters return `this` to support chaining. Structure options return a generic structure pointer, so chain them last.)_
