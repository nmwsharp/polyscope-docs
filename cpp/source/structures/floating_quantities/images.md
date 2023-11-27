Images are rectangular grids of pixel values.

**Sample:** An image quantity of a majestic cat, shown here in the ImGui window display mode.

![image example]([[url.prefix]]/media/image_example.jpg)

!!! info "Floating Quantities"

    Images are _floating quantities_, which means they can be added to the scene at the root level, or added to any kind of structure.

    See the [floating quantity introduction]([[url.prefix]]/structures/floating_quantities/basics/) for more info.


**Example:**

```cpp
#include "polyscope/image_quantity.h"
polyscope::init();

// Your image data, must be populated somehow
// Buffer layouts are assumed to be [rows, columns, components]
// As always, Polyscope's data adaptors allow it to directly read from many
// containers: std::vector<>, Eigen::MatrixXd, raw buffers, etc.
int width = 1024;
int height = 768;
std::vector<std::array<float, 3>> imageColor(width * height);
std::vector<std::array<float, 4>> imageColorAlpha(width * height);
std::vector<float> imageScalar(width * height);

// == Add images at the root level of the scene

polyscope::ColorImageQuanitity* colorImage =
polyscope::addColorImageQuantity("test color image", width, height, imageColor, 
                                  polyscope::ImageOrigin::UpperLeft);
polyscope::addColorAlphaImageQuantity("test color alpha image", width, height, imageColorAlpha,
                                      polyscope::ImageOrigin::UpperLeft);
polyscope::ColorImageQuanitity* scalarImage =
polyscope::addScalarImageQuantity("test scalar image", width, height, imageScalar,
                                  polyscope::ImageOrigin::UpperLeft);

// Set some options
colorImage->setEnabled(true);
colorImage->setShowFullscreen(false);
colorImage->setShowInImGuiWindow(true);
scalarImage->setColorMap("blues");
scalarImage->setMapRange({0.0, 10.0});

// == Add images associated with a structure
// Here, a camera view, you could also use a point cloud, or a mesh, etc
polyscope::CameraView* targetView = polyscope::getCameraView("my view"); // some structure you previously registered

polyscope::ColorImageQuanitity* colorImageView =
targetView->addColorImageQuantity("test color image", width, height, imageColor, 
                                  polyscope::ImageOrigin::UpperLeft);
targetView->addColorAlphaImageQuantity("test color alpha image", width, height, imageColorAlpha,
                                       polyscope::ImageOrigin::UpperLeft);
targetView->addScalarImageQuantity("test scalar image", width, height, imageScalar,
                                    polyscope::ImageOrigin::UpperLeft);

// When added to a camera view, images can be displayed in the camera frame
colorImageView->setShowInCameraBillboard(true);

polyscope::show();
```



!!! tip "Images vs. Render Images"

    If your image happens to represent a rendering of the scene from the user's viewport (for example, from custom renderer code), check out the [Render Image]([[url.prefix]]/structures/floating_quantities/render_images/) quantity, which offers additional functionality for view-rendered images such as depth-compositing them into the scene to layer and blend with other content.


!!! tip "Camera Views"

    Image quantities get special functionality when added to `CameraView` structures: they can additionally be displayed in the camera frame, aligned with the view of the scene.



## Image Origin

When registering an image quantity, you also need to specify whether the image should be interpreted such that the first row is the "top" row of the image (`ImageOrigin::UpperLeft`), or the first row is the "bottom" row of the image (`ImageOrigin::LowerLeft`). This is a confusing issue, as there are many overlapping conventions of coordinate systems and buffer layouts for images.

Most of the time, `ImageOrigin::UpperLeft` is the right choice.

---
## Scalar Image Quantity

These can be called at the root level, like `polyscope::addScalarImageQuantity()`, or on a structure, like `cameraView->addScalarImageQuantity()`.


??? func "`#!cpp ScalarImageQuantity* addScalarImageQuantity(std::string name, int width, int height, const T& values, ImageOrigin imageOrigin, DataType type = DataType::STANDARD)`"

    Add an image of scalar values

    - `width` and `height` are dimensions in pixels
    - `values` is a flattened array of scalars per pixel. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array . The length should be `width * height`.
    - `imageOrigin` is the row origin convention, see above
    - `type` is the scalar datatype as for other scalar quantities

{!common/scalar_quantity.md!}

---
## Color Image Quantity

These can be called at the root level, like `polyscope::addColorImageQuantity()`, or on a structure, like `cameraView->addColorImageQuantity()`.

??? func "`#!cpp ColorImageQuantity* addColorImageQuantity(std::string name, int width, int height, const T& values_rgb, ImageOrigin imageOrigin)`"

    Add an image of rgb color values

    - `width` and `height` are dimensions in pixels
    - `values_rgb` is a flattened array of rgb values per pixel. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be `width * height`.
    - `imageOrigin` is the row origin convention, see above
    
    RGB values are interpreted in the range `[0,1]`.

??? func "`#!cpp ColorImageQuantiy* addColorAlphaImageQuantity(std::string name, int width, int height, const T& values_rgba, ImageOrigin imageOrigin)`"

    Add an image of rgb color values

    - `width` and `height` are dimensions in pixels
    - `values_rgba` is a flattened array of rgba values per pixel. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 4-vector array of `float`s. The length should be `width * height`.
    - `imageOrigin` is the row origin convention, see above
    
    RGB values are interpreted in the range `[0,1]`.

By default, alpha values are interpreted to be non-premultiplied. Use  `colorAlphaImage->setIsPremultiplied(true);` to directly pass premultiplied alpha images.

{!common/color_quantity.md!}


---
## Image Options

These options are common to all images

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
transparency | the image transparency | `#!cpp float getTransparency()` | `#!cpp setTransparency(float val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
show fullscreen | show in the full window, if enabled | `#!cpp bool getShowFullscreen()` | `#!cpp setShowFullscreen(bool val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
show in ImGui | show in an ImGui UI window, if enabled | `#!cpp bool getShowInImGuiWindow()` | `#!cpp setShowInImGuiWindow(bool val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
show in camera billboard | for `CameraView` structure only, if enabled | `#!cpp bool getShowInCameraBillboard()` | `#!cpp setShowInCameraBillboard(bool val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
