Polyscope supports headless rendering on linux machines which do not have displays, such as remote servers and clusters.

Polyscope's default interactive backend uses GLFW to create an OpenGL context, which essentially requires that a physical display be attached for any rendering to be performed. This would prevent workflows like running compute jobs on remote clusters and logging images or saving videos rendered via Polyscope---headless rendering offers a solution.


!!! warning "What is headless rendering not?"

    "Headless" just means that Polyscope can run its rendering engine even when no display is present, rendering images to buffers or files. You can save them, store them, or even log them to viewers like Tensorboard.

    Headless rendering is _not_ the same as running the UI in a browser tab or a cell of a Jupyter notebook.  There is currently no support for either of these uses (although local Jupyter notebooks work; the window will be opened outside of the notebook).

    Also, headless rendering is _not_ necessary if you are remotely connecting to a machine which has a physical display attached; for instance, when remotely connecting to macOS or Windows machines with displays.

!!! note "Unix only"

    Headless rendering is only supported on Unix/Linux, because EGL is only available there.

    

## Using headless rendering

Headless rendering requires compiling with and initializing a separate EGL backend. 

Your system must have EGL available. It is likely packaged with graphics drivers, or can be installed from a package manager. Another alternative is to fall back on (much slower!) rendering by installing `OSMesa` from your package manager.

At configuration time, the EGL backend must be enabled in CMake for headless support.  The default CMake settings enable it only if you are on Linux and EGL headers seem to be present on your system.  Set the CMake variable `POLYSCOPE_BACKEND_OPENGL3_EGL=ON` to force-enable building with EGL support. 

```cmake
cmake .. -DPOLYSCOPE_BACKEND_OPENGL3_EGL=ON
```

At runtime, you must tell Polyscope to initialize with the EGL engine. The simplest way to do this is to specify it explicitly when you call `init()`. Alternately, the default automatic initialization scheme will select the EGL headless backend if no others are available, but only if you enable the headless backends option first.

**Example:** headless usage
```cpp
// explicit initialization
polyscope::init("openGL3_egl");
// OR
polyscope::options::allowHeadlessBackends = true;  // enable headless backends
polyscope::init(); // automatic initialization will use the EGL backend
                   // if it is available and there is no display

// ... add structures and quantities to polyscope as usual ...

// save screenshots, render movies, etc
polyscope::screenshot(); 
std::vector<unsigned char> viz_img = polyscope::screenshotToBuffer();
```

Once you have initialized the backend and added your data as usual, you can preform rendering operations such as saving rendered screenshots to disk or to buffer.

Unless you really know what you are doing, you probably do not want to call `show()` -- by default this would initiate a render loop which spins endlessly with no effect. However it is still permitted to do so, e.g. if you set a user callback which has side effects.

!!! note "ImGui not rendered"

    In headless mode, the ImGui UI is not actually drawn to the screen. You can still issue ImGui calls in your code if you would like, but they will never have any effect.

## Options

??? func "`#!cpp bool isHeadless()`"
    
    ##### isHeadless()

    Returns `true` if polyscope is currently running in headless mode. May only be called after initialization.


??? func "`#!cpp bool options::allowHeadlessBackends`"
    
    ##### allowHeadlessBackends

    If `true` default automatic initialization is allowed to initialize with a headless backend, if that is the only option.

    Default: `false`

    This is set to `false` by default, because sometimes misconfigured or low-capability machines will have no display, and automatically creating headless backends on such machines would confuse new users.

??? func "`#!cpp int options::eglDeviceIndex`"
    
    ##### eglDeviceIndex

    Pass an index to manually specify which EGL device to use for headless EGL rendering. If set to `-1` (default), Polyscope will try all devices, with some heuristics to attempt to use hardware renderers before software renderers.

    Default: `-1`

    If you are trying to figure out which device index to use, set Polyscope's verbosity to a large value (`> 5`). At high verbosity, Polyscope will print the list of found EGL devices and their indices when attempting initialization.




