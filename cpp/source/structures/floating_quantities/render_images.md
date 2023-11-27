Render images are special images which are renderings of scene through the Polyscope viewport. These are useful when using Polyscope to visualize renders from your own custom renderers, such as ray tracers, SDF-field implicit tracers, or neural field renderers.

Render images always show the image in fullscreen viewport. Additional, depth and transparency allow the image to be composited with other scene content, so that you can still see your usual Polyscope meshes and point clouds in the scene along with the outputs of your renderer.

**Sample:** A colored box and scalar torus, displayed as render images from a user's custom implicit surface renderer.

![sample render image](/media/render_image_implicit_example.jpg)


!!! info "Floating Quantities"

    Render images are _floating quantities_, which means they can be added to the scene at the root level, or added to any kind of structure.

    It is most common to add render image quantities at the root level. However, it might still be useful to add render images to structures, to associate the rendering with a particular structure, e.g. as a separate rendering of each point cloud in the scene.

    See the [floating quantity introduction](/structures/floating_quantities/basics/) for more info.


## Image Origin

When registering an image quantity, you also need to specify whether the image should be interpreted such that the first row is the "top" row of the image (`ImageOrigin::UpperLeft`), or the first row is the "bottom" row of the image (`ImageOrigin::LowerLeft`). This is a confusing issue, as there are many overlapping conventions of coordinate systems and buffer layouts for images.

Most of the time, `ImageOrigin::UpperLeft` is the right choice.

---
## Depth Render Image Quantity

A depth render image quantity takes a depth value per-pixel, and (optionally) a world-space normal per-pixel. The depth image will be rendered with surface shading using Polyscope's [materials](/features/materials/).

**Example:**
```cpp
size_t dimX = 1024; size_t dimY = 768;
std::vector<float> depthVals(dimX * dimY, 0.44); // placeholder data
std::vector<std::array<float, 3>> normalVals(dimX * dimY, std::array<float, 3>{0.44, 0.55, 0.66});
std::vector<std::array<float, 3>> normalValsEmpty;

polyscope::DepthRenderImageQuantity* im = polyscope::addDepthRenderImageQuantity(
    "render im depth", dimX, dimY, depthVals, normalVals, polyscope::ImageOrigin::UpperLeft);
im->setEnabled(true);

// with no normals
polyscope::DepthRenderImageQuantity* imNoNormal = polyscope::addDepthRenderImageQuantity(
    "render im depth no normal", dimX, dimY, depthVals, normalValsEmpty, polyscope::ImageOrigin::UpperLeft);
imNoNormal->setEnabled(true);
    
polyscope::show(3);
```

If normals are not given, they will be computed internally via screen-space derivatives.

This can be called at the root level, like `polyscope::addDepthRenderImageQuantity()`, or on a structure, like `cameraView->addDepthRenderImageQuantity()`.

??? func "`#!cpp DepthRenderImageQuantity* addDepthRenderImageQuantity(std::string name, size_t dimX, size_t dimY, const T1& depthData, const T2& normalData, ImageOrigin imageOrigin)`"

    Add a depth render image.

    - `width` and `height` are dimensions in pixels
    - `depthData` is a flattened array of depth scalars per pixel. Use `inf` for any pixels which missed the scene. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array . The length should be `width * height`.
    - `normalData` is an optional flattened array of world-space normals per pixel.  The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be `width * height`. If not given, pass an empty array.
    - `imageOrigin` is the row origin convention, see above

    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.


---
## Color Render Image Quantity

A color render image quantity takes a depth value per-pixel, (optionally) a world-space normal per-pixel, and a color value per-pixel. The depth image will be rendered with surface shading using Polyscope's [materials](/features/materials/), colored according to the given color.

!!! info "Color vs. Raw Color Render Images"

    A _color_ render image applies [materials](/features/materials/) shading and lighting to the image, just like Polyscope usually does for meshes and other objects. A _raw color_ render image does not do any additional shading, and simply displays the given colors directly onto the screen.

**Example:**
```cpp
size_t dimX = 1024; size_t dimY = 768;
std::vector<float> depthVals(dimX * dimY, 0.44); // placeholder data
std::vector<std::array<float, 3>> normalVals(dimX * dimY, std::array<float, 3>{0.44, 0.55, 0.66});
std::vector<std::array<float, 3>> colorVals(dimX * dimY, std::array<float, 3>{0.44, 0.55, 0.66});

polyscope::ColorRenderImageQuantity* im = polyscope::addColorRenderImageQuantity(
    "render im color", dimX, dimY, depthVals, normalVals, colorVals, polyscope::ImageOrigin::UpperLeft);
im->setEnabled(true);

polyscope::show(3);
```

If normals are not given, they will be computed internally via screen-space derivatives.

This can be called at the root level, like `polyscope::addColorRenderImageQuantity()`, or on a structure, like `cameraView->addColorRenderImageQuantity()`.

??? func "`#!cpp ColorRenderImageQuantity* addColorRenderImageQuantity(std::string name, size_t dimX, size_t dimY, const T1& depthData, const T2& normalData, const T3& colorData, ImageOrigin imageOrigin)`"

    Add a depth render image, annotated with additional color values per-pixel.

    - `width` and `height` are dimensions in pixels
    - `depthData` is a flattened array of depth scalars per pixel. Use `inf` for any pixels which missed the scene. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array . The length should be `width * height`.
    - `normalData` is an optional flattened array of world-space normals per pixel.  The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be `width * height`. If not given, pass an empty array.
    - `colorData` is a flattened array of colors per pixel.  The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be `width * height`.
    - `imageOrigin` is the row origin convention, see above

    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.
    
    RGB values are interpreted in the range `[0,1]`.

{!common/color_quantity.md!}

---
## Scalar Render Image Quantity

A scalar render image quantity takes a depth value per-pixel, (optionally) a world-space normal per-pixel, and a scalar value per-pixel. The depth image will be rendered with surface shading using Polyscope's [materials](/features/materials/), with the scalar value shaded and colormapped as a scalar quantity.

**Example:**
```cpp
size_t dimX = 1024; size_t dimY = 768;
std::vector<float> depthVals(dimX * dimY, 0.44); // placeholder data
std::vector<std::array<float, 3>> normalVals(dimX * dimY, std::array<float, 3>{0.44, 0.55, 0.66});
std::vector<float> scalarVals(dimX * dimY, 0.44);

polyscope::ScalarRenderImageQuantity* im = polyscope::addScalarRenderImageQuantity(
    "render im scalar", dimX, dimY, depthVals, normalVals, scalarVals, polyscope::ImageOrigin::UpperLeft);
im->setEnabled(true);

polyscope::show(3);
```

If normals are not given, they will be computed internally via screen-space derivatives.

This can be called at the root level, like `polyscope::addScalarRenderImageQuantity()`, or on a structure, like `cameraView->addScalarRenderImageQuantity()`.

??? func "`#!cpp ScalarRenderImageQuantity* addScalarRenderImageQuantity(std::string name, size_t dimX, size_t dimY, const T1& depthData, const T2& normalData, const T3& scalarData, ImageOrigin imageOrigin, DataType type = DataType::STANDARD)`"

    Add a depth render image, annotated with additional scalar values per-pixel.

    - `width` and `height` are dimensions in pixels
    - `depthData` is a flattened array of depth scalars per pixel. Use `inf` for any pixels which missed the scene. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array . The length should be `width * height`.
    - `normalData` is an optional flattened array of world-space normals per pixel.  The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be `width * height`. If not given, pass an empty array.
    - `colorData` is a flattened array of colors per pixel.  The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be `width * height`.
    - `imageOrigin` is the row origin convention, see above
    - `type` is the scalar datatype as for other scalar quantities

    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.

{!common/scalar_quantity.md!}

---
## Raw Color Render Image Quantity

A raw color render image quantity takes a depth value per-pixel and a color value per-pixel. The colors will be directly displayed onscreen, with depth compositing into the scene.

**Example:**
```cpp
size_t dimX = 1024; size_t dimY = 768;
std::vector<float> depthVals(dimX * dimY, 0.44); // placeholder data
std::vector<std::array<float, 3>> colorVals(dimX * dimY, std::array<float, 3>{0.44, 0.55, 0.66});

polyscope::RawColorRenderImageQuantity* im = polyscope::addRawColorRenderImageQuantity(
    "render im raw color", dimX, dimY, depthVals, colorVals, polyscope::ImageOrigin::UpperLeft);
im->setEnabled(true);

polyscope::show(3);
```

!!! info "Color vs. Raw Color Render Images"

    A _color_ render image applies [materials](/features/materials/) shading and lighting to the image, just like Polyscope usually does for meshes and other objects. A _raw color_ render image does not do any additional shading, and simply displays the given colors directly onto the screen.

This can be called at the root level, like `polyscope::addRawColorRenderImageQuantity()`, or on a structure, like `cameraView->addRawColorRenderImageQuantity()`.

??? func "`#!cpp RawColorRenderImageQuantity* addRawColorRenderImageQuantity(std::string name, size_t dimX, size_t dimY, const T1& depthData, const T2& colorData, ImageOrigin imageOrigin)`"

    Add a raw color render image described by pixel color and depth.

    - `width` and `height` are dimensions in pixels
    - `depthData` is a flattened array of depth scalars per pixel. Use `inf` for any pixels which missed the scene. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array . The length should be `width * height`.
    - `colorData` is a flattened array of colors per pixel.  The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 3-vector array of `float`s. The length should be `width * height`.
    - `imageOrigin` is the row origin convention, see above

    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.
    
    RGB values are interpreted in the range `[0,1]`.


---
## Raw Color Alpha Render Image Quantity

Just like the above `ColorRenderImageQuantity`, but with an additional alpha channel which gets alpha-composited onto the scene.

**Example:**
```cpp
size_t dimX = 1024; size_t dimY = 768;
std::vector<float> depthVals(dimX * dimY, 0.44); // placeholder data
std::vector<std::array<float, 4>> colorAlphaVals(dimX * dimY, std::array<float, 4>{0.44, 0.55, 0.66, 0.77});

polyscope::RawColorAlphaRenderImageQuantity* im = polyscope::addRawColorAlphaRenderImageQuantity(
    "render im raw color alpha", dimX, dimY, depthVals, colorAlphaVals, polyscope::ImageOrigin::UpperLeft);
im->setEnabled(true);
im->setIsPremultiplied(true);
polyscope::show(3);
```

??? func "`#!cpp RawColorAlphaRenderImageQuantity* addRawColorAlphaRenderImageQuantity(std::string name, size_t dimX, size_t dimY, const T1& depthData, const T2& colorData, ImageOrigin imageOrigin)`"

    Add a raw color render image described by RGBA pixel color and depth.

    - `width` and `height` are dimensions in pixels
    - `depthData` is a flattened array of depth scalars per pixel. Use `inf` for any pixels which missed the scene. The type should be [adaptable]([[url.prefix]]/data_adaptors) to a `float` scalar array . The length should be `width * height`.
    - `colorData` is a flattened array of rgba colors per pixel.  The type should be [adaptable]([[url.prefix]]/data_adaptors) to a 4-vector array of `float`s. The length should be `width * height`.
    - `imageOrigin` is the row origin convention, see above

    Depth values should be radial ray distance from the camera origin, _not_ perpendicular distance from the image plane.
    
    RGBA values are interpreted in the range `[0,1]`.

By default, alpha values are interpreted to be non-premultiplied. Use  `rawColorAlphaRenderImage->setIsPremultiplied(true);` to directly pass premultiplied alpha images.

---
## Render Image Options

These options are common to all render images

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
transparency | the image transparency | `#!cpp float getTransparency()` | `#!cpp setTransparency(float val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
material | what [material]([[url.prefix]]/features/materials) to use | `#!cpp std::string getMaterial()` | `#!cpp setMaterial(std::string name)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values) |
allow compositing | if true, multiple renders can composite with each other | `#!cpp bool getAllowFullscreenCompositing()` | `#!cpp setAllowFullscreenCompositing(bool val)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)

Raw color render images ignore material-related settings.
