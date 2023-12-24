_Implicit_ functions take an xyz position as input, and return a value. Polyscope contains several helper features to directly visualize implicit functions by taking a callable as input and automatically invoking it as needed. This can be a much easier way to interface with volumetric and inherently implicit data. In particular, Polyscope contains a built-in renderer to render images of levelsets of implicit functions.

!!! info "Batch Evaluation"

    In principle, an implicit function takes a single xyz position as input, and returns a single value. However, Polyscope might need to invoke the callback function millions of times, which can introduce excessive performance overhead, especially if the underlying function is being evaluated on a GPU, or due to cross-language binding overhead. For this reason, we use _batch evaluation_, to perform many evaluations with each invocation and amortize the overhead.

    Implict helpers expect you to pass a callback function which takes as input an `(N,3)` numpy array of query positions, and returns an `(N,)` array of evaluated values (or returns `(N,3)` array of colors for color functions). `N` is the number of queries, which will be determined as-needed internally by Polyscope.


## Directly Rendering Implicit Isosurfaces

Polyscope can directly render images of an isosurface of an implicit function in space, from the current viewport or from a defined camera view. The resulting renders are added as [Render Images]([[url.prefix]]/structures/floating_quantities/render_images), which support material shading, colormapping, transparency, and depth-compositing with other content in the scene.

![sample render image]([[url.prefix]]/media/render_image_implicit_example.jpg)

!!! warning "Not a Fast Renderer"

    There is a long history of highly efficient real-time implicit shaders and ray marchers in computer graphics. **Polyscope's built-in implicit ray marching renderer is not _fast_, and it never will be!** It should be viewed as a debugging tool, not a real-time renderer. Its design fundamentally prioritizes ease-of-use over speed; for instance even if your function is defined on the GPU, Polyscope will perform many expensive CPU round-trips to render it, doing multiple evaluations of the given implicit function.

    If you want real-time implicit rendering, you will need to perform that rendering outside of Polyscope. However, the resulting renders can still be added to Polyscope as a [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) to take advantage of Polyscope's functionality. You can even use direct GPU interop (beta feature!) to do so with minimal realtime overhead.


**Example:**
```python
import polyscope as ps
import numpy as np

ps.init()

# define some implicit functions
def sphere_sdf(pts): # takes [N,3] query pos array, returns [N,] SDF values
    res = np.linalg.norm(pts, axis=-1) - 1.
    return res
def color_func(pts): # takes [N,3] query pos array, returns [N,3] color values
    A = np.ones_like(pts) * 0.3
    A[:,0] = np.cos(3*pts[:,0])**2
    return A

# render from the current view
ps.render_implicit_surface("sphere sdf", sphere_sdf, 
                           mode='sphere_march', enabled=True)
ps.render_implicit_surface_color("sphere sdf", sphere_sdf, color_func, 
                                 mode='sphere_march', enabled=True)

ps.show()
```

#### Implicit Render Options

The most important option to set the `mode` for the renderer. There are two choices:

- `mode='sphere_march'` should be used if your implicit function is a Signed Distance Function (SDF). That is, its magnitude gives the distance to the surface, or at least a conservative bound on the distance. This allows the renderer to take large steps based on the SDF value.
- `mdoe='fixed_step` must be used if your implicit function is not necessarily an SDF. This forces to renderer to take many small steps, which is inefficient but always works for sufficiently small step size.

The following options can be set as additional keywords arguments to any render function

- `camera_view` a `CameraView` structure (or the string name of one). If given, the render will be performed from the viewpoint of that camera, and the resulting render image will be added to the camera
- `camera_parameters` a `CameraParameters` object defining the view to render from. If is not passed, then the current viewport will be used, unless the `camera_view` arg is set, in which case that camera will be used instead
- `dim` 2-tuple of ints giving the dimension to render at (if rendering from the current view, this may be omitted, and the viewport resolution will be used)
- `subsample_factor` int, if `dim` is being set automatically, downscale it by this factor (e.g. `subsample_factor=2` means use `dimX/2` and `dimY/2`)
- `miss_dist` float, an absolute value for how far a ray must go to be considered a miss
- `miss_dist_relative` float, a relative value for how far a ray must go to be considered a miss (default: 20.)
- `hit_dist` float, an absolute value for how close a ray must go to be considered a hit
- `hit_dist_relative` float, a relative value for how close a ray must go to be considered a hit (default: 1e-4)
- `step_factor` float, a small tolerance factor applied to step sizes (default: 0.99)
- `normal_sample_eps` float, a relative numerical parameter for finite differences normals (default: 1e-3)
- `step_size` float, the absolute step size to used for `fixed_step` marching
- `step_size_relative` float, the relative step size to used for `fixed_step` marching (default: 1e-2)
- `n_max_steps` int, the maximum number of steps to take (default: 1024)

For options which have an absolute and relative version, you may specify either but not both. [Relative values]([[url.prefix]]/basics/parameters/#scaled-values) are defined with respect to the scene length scale.

#### Render Depth Images
    
Render a depth [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. The resulting surface will be shaded with materials and lighting.

??? func "`#!python render_implicit_surface(name, func, mode, color=None, **kwargs)`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render
    - `mode` is the render mode, one of `'sphere_march', 'fixed_step'`
    - see the bulleted listing above for other arguments common to all render functions

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Batch Evaluation" popout at the top for a description of the expected signatures for function arguments.


#### Render Scalar Images

Render a scalar [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. The resulting surface will be shaded with materials and lighting. An additional implicit function defines a scalar value which will be shaded with colormapping on the isosurface.

??? func "`#!python render_implicit_surface_scalar(name, func, func_scalar, mode, **kwargs)`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render
    - `func_scalar` another batch callable defining a scalar function which will be evaluated on the isosurface and displayed with color mapping
    - `mode` is the render mode, one of `'sphere_march', 'fixed_step'`
    - see the bulleted listing above for other arguments common to all render functions

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Batch Evaluation" popout at the top for a description of the expected signatures for function arguments.



#### Render Color Images

Render a color [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. The resulting surface will be shaded with materials and lighting. An additional implicit function defines a color value which will be shaded with colormapping on the isosurface.


??? func "`#!python render_implicit_surface_color(name, func, func_color, mode, **kwargs)`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render
    - `func_color` another batch callable defining a color function which will be evaluated on the isosurface and displayed with color mapping
    - `mode` is the render mode, one of `'sphere_march', 'fixed_step'`
    - see the bulleted listing above for other arguments common to all render functions

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Batch Evaluation" popout at the top for a description of the expected signatures for function arguments.



#### Render Raw Color Images

Render a raw color [Render Image]([[url.prefix]]/structures/floating_quantities/render_images) of the 0 isosurface of a function. An additional implicit function defines a color value which will be used on the isosurface. The difference between _color_ and _raw color_ images is that plain `Color` rendered images apply lighting and material shading to the colors (like a `SurfaceMesh` would), whereas `RawColor` images really just directly display the given color as the pixel values.


??? func "`#!python render_implicit_surface_raw_color(name, func, func_color, mode, **kwargs)`"
    
    - `func` a batch callable defining the function whose 0-levelset we will render
    - `func_color` another batch callable defining a color function which will be evaluated on the isosurface
    - `mode` is the render mode, one of `'sphere_march', 'fixed_step'`
    - see the bulleted listing above for other arguments common to all render functions

    The 0 isolevel is always used. To render a different isolevel, add a constant offset shift to your function before passing it in.

    See the "Batch Evaluation" popout at the top for a description of the expected signatures for function arguments.



## Implicit Volumes

In addition rendering isosurfaces, Polyscope can automatically register the implicit function as a volumetric grid of values. See the [volume grid scalar quantity]([[url.prefix]]/structures/volume_grid/scalar_quantities/#add-implicit-scalars) for details.
