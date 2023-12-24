_Implicit_ functions take an xyz position as input, and return a value. Polyscope contains several helper features to directly visualize implicit functions by taking a callable as input and automatically invoking it as needed. This can be a much easier way to interface with volumetric and inherently implicit data. In particular, Polyscope contains a built-in renderer to render images of levelsets of implicit functions.

`#include "polyscope/implicit_helpers.h"`

!!! info "Individual vs. Batch Evaluation"

    Each implicit helper function comes in two versions:
   
    - A simple individual version, which invokes the implicit function just once to produce a single value. It expects a function with a signature like `float my_func(glm::vec3 pos)`. 
    - A batch evaluation version, which invokes the implicit function many times on a batch of inputs in buffers. It expects a function with a signature like `void my_func(float* inPos, float* outResult, size_t N)`, where the first argument is a length-`3*N` array of query locations, the second argument is an already-allocated buffer of length N to store the results, and `N` is the number of queries. For color functions, the outResult with be of length `3*N` instead.

    The first individual version is simplest, and fits the usual definition of an implicit function. However, Polyscope might need to invoke the callback function millions of times, which can introduce excessive performance overhead, especially if the underlying function is being evaluated on a GPU, or via bindings to another language. For this reason, the batch version is also available, to perform many evaluations with each invocation and amortize the overhead.

## Directly Rendering Implicit Isosurfaces

Polyscope can directly render images of an isosurface of an implicit function in space, from the current viewport or from a defined camera view. The resulting renders are added as [Render Images]([[url.prefix]]/structures/floating_quantities/render_images), which support material shading, colormapping, transparency, and depth-compositing with other content in the scene.

![sample render image]([[url.prefix]]/media/render_image_implicit_example.jpg)

!!! warning "Not a Fast Renderer"

    There is a long history of highly efficient real-time implicit shaders and ray marchers in computer graphics. **Polyscope's built-in implicit ray marching renderer is not _fast_, and it never will be!** It should be viewed as a debugging tool, not a real-time renderer. Its design fundamentally prioritizes ease-of-use over speed; for instance even if your function is defined on the GPU, Polyscope will perform many expensive CPU round-trips to render it, doing multiple evaluations of the given implicit function.

    If you want real-time implicit rendering, you will need to perform that rendering outside of Polyscope. However, the resulting renders can still be added to Polyscope as a [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) to take advantage of Polyscope's functionality. You can even use direct GPU interop (beta feature!) to do so with minimal realtime overhead.


**Example:**
```cpp
#include "polyscope/implicit_helpers.h"

polyscope::init();

// define some implicit functions
auto torusSDF = [](glm::vec3 p) { /* evaluates the SDF of a torus, returns a float */ };
auto boxFrameSDF = [](glm::vec3 p) { /* evaluates the SDF of a box, returns a float */ };
auto colorFunc = [](glm::vec3 p) { /* gives a color in space, returns a glm::vec3 */ };
auto scalarFunc = [](glm::vec3 p) {/* gives a scalar in space, returns a float */  };

// setup options
polyscope::ImplicitRenderOpts opts;
polyscope::ImplicitRenderMode mode = polyscope::ImplicitRenderMode::SphereMarch;
// polyscope::ImplicitRenderMode mode = polyscope::ImplicitRenderMode::FixedStep; // (alternately, if not an SDF)
opts.subsampleFactor = 2; // downsample the rendering

// render the implicit isosurfaces from the current viewport
polyscope::DepthRenderImageQuantity* img = polyscope::renderImplicitSurface("torus sdf", torusSDF, mode, opts);
polyscope::DepthRenderImageQuantity* img2 = polyscope::renderImplicitSurface("box sdf", boxFrameSDF, mode, opts);
polyscope::ColorRenderImageQuantity* img2Color =
  polyscope::renderImplicitSurfaceColor("box sdf color", boxFrameSDF, colorFunc, mode, opts);
polyscope::RawColorRenderImageQuantity* img2rawColor =
  polyscope::renderImplicitSurfaceRawColor("box sdf raw color", boxFrameSDF, colorFunc, mode, opts);
polyscope::ScalarRenderImageQuantity* imgScalar =
  polyscope::renderImplicitSurfaceScalar("torus sdf scalar", torusSDF, scalarFunc, mode, opts);

polyscope::show();
```
There is also an alternate version of every render function that takes an additional first argument which is a pointer to any structure. The resulting render images will be added to that structure, following the same semantics as [floating quantities]([[url.prefix]]/structures/floating_quantities/basics/).

#### Implicit Render Options

The most important option to set the `mode` for the renderer. There are two choices:

- `ImplicitRenderMode::SphereMarch` should be used if your implicit function is a Signed Distance Function (SDF). That is, its magnitude gives the distance to the surface, or at least a conservative bound on the distance. This allows the renderer to take large steps based on the SDF value.
- `ImplicitRenderMode::FixedStep` must be used if your implicit function is not necessarily an SDF. This forces to renderer to take many small steps, which is inefficient but always works for sufficiently small step size.

The `ImplicitRenderOpts` struct controls the remaining settings for the renderer.

```cpp
struct ImplicitRenderOpts {

  // = Options for how the image is defined

  // (1) If camera parameters & resolution are passed, in these options, they will always be respected.
  //
  // (2) Otherwise, if the parent structure is null (or the global floating struct), we will render from the current
  // polyscope camera view, and take the resolution etc from that.
  //
  // (3) Otherwise, if the parent structure is a camera view, we will take the camera parameters from that, but the
  // dimensions must be specified.
  //
  // (4) Otherwise, if the parent structure is a structure other than the camera view, the parameters should have been
  // explicitly specified as in (1), and an error will be thrown.

  // The camera parameters to use.
  // If left as the default uninitialized camera, it will be overwritten according to the policies above.
  CameraParameters cameraParameters = CameraParameters::createInvalid();

  // The dimensions at which to render the image.
  // These normally must be set explicitly, unless we are rendering from the current view as specified above.
  int32_t dimX = -1;
  int32_t dimY = -1;

  // If dimX and dimY are being set automatically, downscale them by this factor (e.g. subsampleFactor=2 means use
  // dimX/2 and dimY/2)
  int subsampleFactor = 1;

  // = Options for the rendering computation itself

  // How far the ray must go before it is abandoned as a miss
  ScaledValue<float> missDist = ScaledValue<float>::relative(20.);

  // How small the the value of the implicit function must be to be considered a hit
  ScaledValue<float> hitDist = ScaledValue<float>::relative(1e-4);

  // For mode == SphereMarch, a small tolerance factor applied to step sizes
  float stepFactor = 0.99;

  // Used to estimate normals via finite differences, also used relative value times the hit distance.
  float normalSampleEps = 1e-3;

  // The size of the steps used for mode == FixedStep
  ScaledValue<float> stepSize = ScaledValue<float>::relative(1e-2);

  // The maximum number of steps to take
  size_t nMaxSteps = 1024;
};
```

#### Render Depth Images
    
Render a depth [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. The resulting surface will be shaded with materials and lighting.

??? func "`#!cpp DepthRenderImageQuantity* renderImplicitSurface(std::string name, Func&& func, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts())`"
    
    - `func` a callable defining the function whose 0-levelset we will render

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.


??? func "`#!cpp DepthRenderImageQuantity* renderImplicitSurfaceBatch(std::string name, Func&& func, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts())`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.


#### Render Scalar Images

Render a scalar [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. The resulting surface will be shaded with materials and lighting. An additional implicit function defines a scalar value which will be shaded with colormapping on the isosurface.

??? func "`#!cpp ScalarRenderImageQuantity* renderImplicitSurfaceScalar(std::string name, Func&& func, FuncScalar&& funcScalar, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts(), DataType dataType = DataType::STANDARD)`"
    
    - `func` a callable defining the function whose 0-levelset we will render
    - `funcScalar` another callable defining a scalar function which will be evaluated on the isosurface and displayed with color mapping

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.


??? func "`#!cpp ScalarRenderImageQuantity* renderImplicitSurfaceScalarBatch(std::string name, Func&& func, FuncScalar&& funcScalar, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts(), DataType dataType = DataType::STANDARD)`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render
    - `funcScalar` another batch callable defining a scalar function which will be evaluated on the isosurface and displayed with color mapping

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.



#### Render Color Images

Render a color [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. The resulting surface will be shaded with materials and lighting. An additional implicit function defines a color value which will be shaded with colormapping on the isosurface.

??? func "`#!cpp ColorRenderImageQuantity* renderImplicitSurfaceColor(std::string name, Func&& func, FuncColor&& funcColor, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts())`"
    
    - `func` a callable defining the function whose 0-levelset we will render
    - `funcColor` another callable defining a color function which will be evaluated on the isosurface and displayed with color mapping

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.


??? func "`#!cpp ColorRenderImageQuantity* renderImplicitSurfaceColorBatch(std::string name, Func&& func, FuncColor&& funcColor, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts())`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render
    - `funcColor` another batch callable defining a color function which will be evaluated on the isosurface and displayed with color mapping

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.



#### Render Raw Color Images

Render a raw color [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. An additional implicit function defines a color value which will be used on the isosurface. The difference between _color_ and _raw color_ images is that plain `Color` rendered images apply lighting and material shading to the colors (like a `SurfaceMesh` would), whereas `RawColor` images really just directly display the given color as the pixel values.


??? func "`#!cpp RawColorRenderImageQuantity* renderImplicitSurfaceRawColor(std::string name, Func&& func, FuncColor&& funcColor, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts())`"
    
    - `func` a callable defining the function whose 0-levelset we will render
    - `funcColor` another callable defining a color function which will be evaluated on the isosurface

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.


??? func "`#!cpp RawColorRenderImageQuantity* renderImplicitSurfaceRawColorBatch(std::string name, Func&& func, FuncColor&& funcColor, ImplicitRenderMode mode, ImplicitRenderOpts opts = ImplicitRenderOpts())`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render
    - `funcColor` another batch callable defining a color function which will be evaluated on the isosurface

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Individual vs. Batch" popout at the top for a description of the expected signatures for function arguments.



## Implicit Volumes

In addition rendering isosurfaces, Polyscope can automatically register the implicit function as a volumetric grid of values. See the [volume grid scalar quantity]([[url.prefix]]/structures/volume_grid/scalar_quantities/#add-implicit-scalars) for details.
